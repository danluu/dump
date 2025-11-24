#!/usr/bin/env python3
"""
Annotate hic_filtered.csv with normalized HIC values and average normalized HIC per vehicle,
after filtering to well-formed records and requiring both front-seat dummy types.

Rules:
- Drop rows missing speed, weight, HIC, occupant sex, or dummy percentile.
- Drop vehicles (make, model, year) that do not include BOTH:
  * LEFT FRONT SEAT, sex M, dummySizePercentile ~ 50
  * RIGHT FRONT SEAT, sex F, dummySizePercentile ~ 5
- Normalized HIC: adjust to baseline speed and weight.
  * Speed baseline: 35 mph (converted to kph), exponent 3.625; higher speed => higher raw HIC,
    so normalized = HIC / ( (v / v_baseline)^3.625 ).
  * Weight baseline: 4400 lbs (converted to kg); normalized = previous / (weight / weight_baseline).
- Average normalized HIC: mean of normalized HIC across all rows for a vehicle that passes the dummy test.
- Output is sorted by average normalized HIC ascending.

Usage:
  python3 annotate-results.py --input hic_filtered.csv --output annotated_results.csv
"""

import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path

BASE_SPEED_MPH = 35.0
MPH_TO_KPH = 1.60934
BASE_SPEED_KPH = BASE_SPEED_MPH * MPH_TO_KPH
SPEED_EXP = 4.0

BASE_WEIGHT_LB = 4400.0
LB_TO_KG = 0.45359237
BASE_WEIGHT_KG = BASE_WEIGHT_LB * LB_TO_KG


def parse_float(val):
    if val is None:
        return None
    s = str(val).strip()
    if not s:
        return None
    try:
        return float(s)
    except ValueError:
        return None


def norm_text(val):
    return str(val).strip().upper() if val is not None else ""


def main():
    parser = argparse.ArgumentParser(description="Annotate HIC results with normalized metrics.")
    parser.add_argument("--input", "-i", default="hic_filtered.csv", help="Input CSV (default: hic_filtered.csv)")
    parser.add_argument("--output", "-o", default="annotated_results.csv", help="Output CSV (bucket 15 only; default: annotated_results.csv)")
    parser.add_argument("--output-m50-15", default="annotated_results_m50_bucket15.csv", help="Output for M50 left-front, HIC bucket 15 (default: annotated_results_m50_bucket15.csv)")
    parser.add_argument("--output-m50-36", default="annotated_results_m50_bucket36.csv", help="Output for M50 left-front, HIC bucket 36 (default: annotated_results_m50_bucket36.csv)")
    parser.add_argument("--output-f5-15", default="annotated_results_f5_bucket15.csv", help="Output for F5 left-front, HIC bucket 15 (default: annotated_results_f5_bucket15.csv)")
    parser.add_argument("--output-f5-36", default="annotated_results_f5_bucket36.csv", help="Output for F5 left-front, HIC bucket 36 (default: annotated_results_f5_bucket36.csv)")
    parser.add_argument("--output-ratios", default="hic_ratio_by_make.csv", help="Output CSV for average HIC_ratio_f5_to_m50 per make (default: hic_ratio_by_make.csv)")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        raise SystemExit(f"Input file not found: {input_path}")

    with input_path.open(newline="") as f:
        reader = csv.DictReader(f)
        raw_rows = list(reader)
        fieldnames = reader.fieldnames or []

    # Filter rows with required numeric/dummy fields
    rows = []
    for r in raw_rows:
        speed = parse_float(r.get("closingSpeed_kph"))
        weight = parse_float(r.get("vehicleTestWeight"))
        hic = parse_float(r.get("HIC"))
        hic_dur = parse_float(r.get("HIC_duration"))
        sex = norm_text(r.get("occupantSex"))
        percentile = parse_float(r.get("dummySizePercentile"))
        occ_loc = norm_text(r.get("occupantLocation"))
        if None in (speed, weight, hic, hic_dur, percentile) or not sex or not occ_loc:
            continue
        if speed == 0 or weight == 0:
            continue
        if speed < 54 or speed > 58:
            continue
        if abs(hic_dur - 15) <= 1:
            hic_bucket = "15"
        elif abs(hic_dur - 36) <= 1:
            hic_bucket = "36"
        else:
            continue
        r["_speed_kph"] = speed
        r["_weight_kg"] = weight  # assume provided weight is kg
        r["_hic"] = hic
        r["_hic_dur"] = hic_dur
        r["_hic_bucket"] = hic_bucket
        if r.get("make") and norm_text(r.get("make")) == "OTHER":
            continue
        r["_sex"] = sex
        r["_percentile"] = percentile
        r["_occ_loc"] = occ_loc
        rows.append(r)

    # Group by vehicle and HIC duration bucket (15±1 or 36±1)
    groups = defaultdict(list)
    for r in rows:
        key = (r.get("make"), r.get("model"), r.get("year"), r["_hic_bucket"])
        groups[key].append(r)

    def has_required_dummies(group_rows):
        has_left_m50 = False
        has_right_f5 = False
        for r in group_rows:
            if r["_occ_loc"] == "LEFT FRONT SEAT" and r["_sex"] == "M" and abs(r["_percentile"] - 50) < 1e-6:
                has_left_m50 = True
            if r["_occ_loc"] == "RIGHT FRONT SEAT" and r["_sex"] == "F" and abs(r["_percentile"] - 5) < 1e-6:
                has_right_f5 = True
        return has_left_m50 and has_right_f5

    def avg(vals):
        return sum(vals) / len(vals) if vals else None

    output_rows = []
    m50_only_rows = []
    f5_left_only_rows = []
    for key, group_rows in groups.items():
        m50_rows = []
        f5_rows = []
        f5_left_rows = []
        for r in group_rows:
            speed_factor = (r["_speed_kph"] / BASE_SPEED_KPH) ** SPEED_EXP
            weight_factor = (r["_weight_kg"] / BASE_WEIGHT_KG)
            combined = speed_factor * weight_factor
            if combined == 0:
                print(
                    f"Skipping row with zero speed/weight factor: "
                    f"{r.get('make')} {r.get('model')} {r.get('year')} "
                    f"testNo={r.get('testNo')} speed={r['_speed_kph']} weight={r['_weight_kg']} "
                    f"speed_factor={speed_factor} weight_factor={weight_factor}",
                    file=sys.stderr,
                )
                continue
            r["normalizedHIC"] = r["_hic"] / combined
            if r["_occ_loc"] == "LEFT FRONT SEAT" and r["_sex"] == "M" and abs(r["_percentile"] - 50) < 1e-6:
                m50_rows.append(r)
            if r["_occ_loc"] == "RIGHT FRONT SEAT" and r["_sex"] == "F" and abs(r["_percentile"] - 5) < 1e-6:
                f5_rows.append(r)
            if r["_occ_loc"] == "LEFT FRONT SEAT" and r["_sex"] == "F" and abs(r["_percentile"] - 5) < 1e-6:
                f5_left_rows.append(r)

        def summarize(rows_list):
            return {
                "speed": avg([r["_speed_kph"] for r in rows_list]),
                "weight": avg([r["_weight_kg"] for r in rows_list]),
                "hic": avg([r["_hic"] for r in rows_list]),
                "norm_hic": avg([r["normalizedHIC"] for r in rows_list]),
                "hic_dur": avg([r["_hic_dur"] for r in rows_list]),
                "testNos": ";".join(sorted({str(r.get("testNo")) for r in rows_list})),
            }

        if m50_rows:
            m50 = summarize(m50_rows)
            m50_only_rows.append({
                "make": m50_rows[0].get("make"),
                "model": m50_rows[0].get("model"),
                "year": m50_rows[0].get("year"),
                "hic_bucket": m50_rows[0]["_hic_bucket"],
                "testNos_m50": m50["testNos"],
                "closingSpeed_kph_m50": m50["speed"],
                "vehicleTestWeight_m50": m50["weight"],
                "HIC_m50": m50["hic"],
                "normalizedHIC_m50": m50["norm_hic"],
                "HIC_duration_m50": m50["hic_dur"],
            })

        if f5_left_rows:
            f5l = summarize(f5_left_rows)
            f5_left_only_rows.append({
                "make": f5_left_rows[0].get("make"),
                "model": f5_left_rows[0].get("model"),
                "year": f5_left_rows[0].get("year"),
                "hic_bucket": f5_left_rows[0]["_hic_bucket"],
                "testNos_f5": f5l["testNos"],
                "closingSpeed_kph_f5": f5l["speed"],
                "vehicleTestWeight_f5": f5l["weight"],
                "HIC_f5": f5l["hic"],
                "normalizedHIC_f5": f5l["norm_hic"],
                "HIC_duration_f5": f5l["hic_dur"],
            })

        if not m50_rows or not f5_rows:
            continue

        m50 = summarize(m50_rows)
        f5 = summarize(f5_rows)
        combined_norm = avg([m50["norm_hic"], f5["norm_hic"]])

        ratio = f5["hic"] / m50["hic"] if m50["hic"] not in (None, 0) and f5["hic"] is not None else ""

        output_rows.append({
            "make": m50_rows[0].get("make"),
            "model": m50_rows[0].get("model"),
            "year": m50_rows[0].get("year"),
            "hic_bucket": m50_rows[0]["_hic_bucket"],
            "testNos_m50": m50["testNos"],
            "testNos_f5": f5["testNos"],
            "closingSpeed_kph_m50": m50["speed"],
            "closingSpeed_kph_f5": f5["speed"],
            "vehicleTestWeight_m50": m50["weight"],
            "vehicleTestWeight_f5": f5["weight"],
            "HIC_m50": m50["hic"],
            "HIC_f5": f5["hic"],
            "normalizedHIC_m50": m50["norm_hic"],
            "normalizedHIC_f5": f5["norm_hic"],
            "normalizedHIC": combined_norm,
            "HIC_ratio_f5_to_m50": ratio,
            "HIC_duration_m50": m50["hic_dur"],
            "HIC_duration_f5": f5["hic_dur"],
        })

    if not output_rows:
        raise SystemExit("No rows remained after filtering and dummy requirements.")

    # Sort by combined normalized HIC ascending
    output_rows.sort(key=lambda r: r["normalizedHIC"])

    out_fields = [
        "make", "model", "year", "hic_bucket",
        "testNos_m50", "testNos_f5",
        "closingSpeed_kph_m50", "closingSpeed_kph_f5",
        "vehicleTestWeight_m50", "vehicleTestWeight_f5",
        "HIC_m50", "HIC_f5",
        "normalizedHIC_m50", "normalizedHIC_f5",
        "normalizedHIC",
        "HIC_ratio_f5_to_m50",
        "HIC_duration_m50", "HIC_duration_f5",
    ]

    # Main output: only bucket 15
    bucket15_rows = [r for r in output_rows if r["hic_bucket"] == "15"]
    with output_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=out_fields)
        writer.writeheader()
        for r in bucket15_rows:
            writer.writerow({fn: r.get(fn, "") for fn in out_fields})
    # Write per-make average ratio across all combined rows, sorted by |ratio - 1|
    ratios_by_make = defaultdict(list)
    for r in output_rows:
        if r.get("HIC_ratio_f5_to_m50") not in ("", None):
            ratios_by_make[r["make"]].append(r["HIC_ratio_f5_to_m50"])
    ratio_rows = []
    for make, vals in ratios_by_make.items():
        avg_ratio = sum(vals) / len(vals)
        ratio_rows.append({
            "make": make,
            "avg_ratio": avg_ratio,
            "abs_diff_from_1": abs(avg_ratio - 1.0),
            "count": len(vals),
        })
    ratio_rows.sort(key=lambda r: r["abs_diff_from_1"])
    with Path(args.output_ratios).open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["make", "avg_ratio", "abs_diff_from_1", "count"])
        writer.writeheader()
        writer.writerows(ratio_rows)

    # M50-only outputs
    m50_fields = [
        "make", "model", "year", "hic_bucket",
        "testNos_m50", "closingSpeed_kph_m50", "vehicleTestWeight_m50",
        "HIC_m50", "normalizedHIC_m50", "HIC_duration_m50",
    ]

    m50_bucket15 = sorted(
        (r for r in m50_only_rows if r["hic_bucket"] == "15"),
        key=lambda r: r["normalizedHIC_m50"],
    )
    with Path(args.output_m50_15).open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=m50_fields)
        writer.writeheader()
        for r in m50_bucket15:
            writer.writerow({fn: r.get(fn, "") for fn in m50_fields})

    m50_bucket36 = sorted(
        (r for r in m50_only_rows if r["hic_bucket"] == "36"),
        key=lambda r: r["normalizedHIC_m50"],
    )
    with Path(args.output_m50_36).open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=m50_fields)
        writer.writeheader()
        for r in m50_bucket36:
            writer.writerow({fn: r.get(fn, "") for fn in m50_fields})

    f5_fields = [
        "make", "model", "year", "hic_bucket",
        "testNos_f5", "closingSpeed_kph_f5", "vehicleTestWeight_f5",
        "HIC_f5", "normalizedHIC_f5", "HIC_duration_f5",
    ]

    f5_bucket15 = sorted(
        (r for r in f5_left_only_rows if r["hic_bucket"] == "15"),
        key=lambda r: r["normalizedHIC_f5"],
    )
    with Path(args.output_f5_15).open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=f5_fields)
        writer.writeheader()
        for r in f5_bucket15:
            writer.writerow({fn: r.get(fn, "") for fn in f5_fields})

    f5_bucket36 = sorted(
        (r for r in f5_left_only_rows if r["hic_bucket"] == "36"),
        key=lambda r: r["normalizedHIC_f5"],
    )
    with Path(args.output_f5_36).open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=f5_fields)
        writer.writeheader()
        for r in f5_bucket36:
            writer.writerow({fn: r.get(fn, "") for fn in f5_fields})

    print(f"Wrote {len(bucket15_rows)} rows to {output_path}")
    print(f"Wrote {len(m50_bucket15)} rows to {args.output_m50_15}")
    print(f"Wrote {len(m50_bucket36)} rows to {args.output_m50_36}")
    print(f"Wrote {len(f5_bucket15)} rows to {args.output_f5_15}")
    print(f"Wrote {len(f5_bucket36)} rows to {args.output_f5_36}")


if __name__ == "__main__":
    main()
