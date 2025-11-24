# NHTSA HIC Data Workflow

## Prereqs
- Node.js (for `fetch_hic.js`)
- Python 3 (for the filter/annotate scripts)
- R with `tidyverse` and `rmarkdown` (for the analysis notebook)

## Steps (run from repo root)

1. Fetch all crash test data and occupant info:
   ```bash
   node fetch_hic.js
   ```
   Generates `hic_latest.csv`.

2. Filter to head-on, zero-offset, front-seat records with valid HIC duration (adds `HIC_duration`):
   ```bash
   python3 filter-results.py --input hic_latest.csv --output hic_filtered.csv
   ```

3. Find repeated tests (same vehicle/occupant details, matching HIC duration bucket):
   ```bash
   python3 find-variable-speed.py --input hic_filtered.csv --output variable-speed.csv
   ```

4. Annotate and normalize HIC (speed^3.625, 35 mph baseline; 4400 lb weight baseline). Produces combined and dummy-specific outputs:
   ```bash
   python3 annotate-results.py \
     --input hic_filtered.csv \
     --output annotated_results.csv \
     --output-m50-15 annotated_results_m50_bucket15.csv \
     --output-m50-36 annotated_results_m50_bucket36.csv \
     --output-f5-15 annotated_results_f5_bucket15.csv \
     --output-f5-36 annotated_results_f5_bucket36.csv \
     --output-ratios hic_ratio_by_make.csv
   ```
   - `annotated_results.csv`: bucket 15 only, combined M50/F5 pairs.
   - `annotated_results_m50_bucket15.csv` / `annotated_results_m50_bucket36.csv`: M50 left-front only.
   - `annotated_results_f5_bucket15.csv` / `annotated_results_f5_bucket36.csv`: F5 left-front only.
   - `hic_ratio_by_make.csv`: average `HIC_ratio_f5_to_m50` per make, sorted by closeness to 1.0.

5. (Optional) Render the R analysis notebook using `variable-speed.csv`:
   ```bash
   Rscript -e "rmarkdown::render('variable-speed-analysis.Rmd')"
   ```
   If you re-enable the plotting chunk, images are written under `plots/`.
