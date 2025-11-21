// Fetch most-recent HIC values per make/model/year from the NHTSA Vehicle API.
// Writes hic_latest.csv in the current directory.

const fs = require('fs');

const BASE = 'https://nrd.api.nhtsa.dot.gov/nhtsa/vehicle/api/v1/'; // NHTSA Vehicle API root
const MAX_COUNT = 20000; // fetch all /vehicle-database-test-results/by-search records in one call
const CONCURRENCY = 50; // limit for simultaneous /get-occupant-info requests

function normalizeSex(sex) {
  if (sex === null || sex === undefined) return '';
  const s = String(sex).trim().toLowerCase();
  if (!s) return '';
  if (s === 'm' || s === 'male') return 'M';
  if (s === 'f' || s === 'female') return 'F';
  return s.toUpperCase(); // fallback: preserve info but standardize case
}

function normalizePercentile(value) {
  if (value === null || value === undefined) return '';
  const s = String(value).trim();
  if (!s) return '';
  const match = s.match(/([0-9]+(?:\.[0-9]+)?)/);
  if (match) {
    const num = Number(match[1]);
    if (!Number.isNaN(num)) {
      return Number.isInteger(num) ? `${num}` : `${num}`; // numeric percentile only
    }
  }
  return s; // fallback: return as-is if no numeric component
}

async function fetchJson(url) {
  const res = await fetch(url, { headers: { 'User-Agent': 'Mozilla/5.0' } });
  if (!res.ok) {
    const text = await res.text();
    throw new Error(`Request failed ${res.status} ${res.statusText} for ${url}: ${text.slice(0, 200)}`);
  }
  return res.json();
}

async function main() {
  const rows = [];

  const searchUrl = `${BASE}vehicle-database-test-results/by-search?count=${MAX_COUNT}` +
    `&orderBy=testNo&pageNumber=0&sortBy=DESC&excludeNhtsaVehicles=true`; // pulls master list of crash tests
  const data = await fetchJson(searchUrl);
  const results = data.results || []; // API response payload: array of vehicle test objects
  console.log(`Fetched ${results.length} test records`);

  // Fetch occupant info with limited concurrency
  let idx = 0;
  async function worker() {
    while (idx < results.length) {
      const myIdx = idx++;
      const r = results[myIdx];
      let occupants = [];
      try {
        const occ = await fetchJson(`${BASE}vehicle-database-test-results/get-occupant-info/${r.testNo}`); // occupant-level metrics for specific testNo
        occupants = (occ.results || []).map(o => ({
          location: o.occupantLocation, // occupantLocation from get-occupant-info
          type: o.occupantType, // occupantType field
          hic: o.headInjuryCriterion, // headInjuryCriterion (HIC)
          t1: o.lowerBoundaryofHICTimeInterval, // lowerBoundaryofHICTimeInterval
          t2: o.upperBoundaryofHICTimeInterval, // upperBoundaryofHICTimeInterval
          sex: normalizeSex(o.occupantSex), // standardized occupantSex
          percentile: normalizePercentile(o.dummySizePercentile), // standardized dummySizePercentile
        }));
      } catch (e) {
        occupants = [{ location: '', type: '', hic: '', t1: '', t2: '', sex: '', percentile: '', error: e.message }];
      }

      for (const occ of occupants) {
        rows.push({
          make: r.vehicleMake, // by-search -> vehicleMake
          model: r.vehicleModel, // by-search -> vehicleModel
          year: r.modelYear, // by-search -> modelYear
          testNo: r.testNo, // by-search -> testNo
          testType: r.testType, // by-search -> testType
          configuration: r.testConfiguration, // by-search -> testConfiguration
          performer: r.testPerformer, // by-search -> testPerformer
          closingSpeed: r.closingSpeed, // by-search -> closingSpeed
          impactAngle: r.impactAngle, // by-search -> impactAngle
          offsetDistance: r.offsetDistance, // by-search -> offsetDistance
          vehicleTestWeight: r.vehicleTestWeight, // by-search -> vehicleTestWeight
          occLocation: occ.location, // get-occupant-info -> occupantLocation
          occType: occ.type, // get-occupant-info -> occupantType
          hic: occ.hic, // get-occupant-info -> headInjuryCriterion
          t1: occ.t1, // get-occupant-info -> lowerBoundaryofHICTimeInterval
          t2: occ.t2, // get-occupant-info -> upperBoundaryofHICTimeInterval
          occSex: occ.sex, // get-occupant-info -> occupantSex (standardized)
          dummySizePercentile: occ.percentile, // get-occupant-info -> dummySizePercentile (standardized)
        });
      }

      if ((myIdx + 1) % 100 === 0) {
        console.log(`Processed ${myIdx + 1}/${results.length} vehicles`);
      }
    }
  }

  const workers = Array.from({ length: CONCURRENCY }, () => worker());
  await Promise.all(workers);

  // Write CSV
  const header = [
    'make', 'model', 'year', 'testNo', 'testType', 'configuration',
    'performer', 'closingSpeed_kph', 'impactAngle_deg', 'offsetDistance_mm',
    'vehicleTestWeight',
    'occupantLocation', 'occupantType', 'occupantSex', 'dummySizePercentile',
    'HIC', 'T1_ms', 'T2_ms',
    'sourceUrl', 'testSourceUrl'
  ];
  const lines = [header.join(',')];
  for (const row of rows) {
    const values = [
      row.make, row.model, row.year, row.testNo, row.testType, row.configuration,
      row.performer, row.closingSpeed, row.impactAngle, row.offsetDistance,
      row.vehicleTestWeight,
      row.occLocation, row.occType, row.occSex, row.dummySizePercentile,
      row.hic, row.t1, row.t2,
      `${BASE}vehicle-database-test-results/get-occupant-info/${row.testNo}`, // direct API source for occupant info
      searchUrl // endpoint used to obtain testNo per make/model/year
    ].map(v => {
      if (v === null || v === undefined) return '';
      const s = String(v);
      return s.includes(',') ? `"${s.replace(/"/g, '""')}"` : s;
    });
    lines.push(values.join(','));
  }
  fs.writeFileSync('hic_latest.csv', lines.join('\n'));
  console.log(`Wrote ${rows.length} rows for ${results.length} tests to hic_latest.csv`);
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
