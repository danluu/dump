#!/usr/bin/env python3
"""
Filter hic_latest.csv to keep only records where:
  - configuration is VEHICLE INTO BARRIER (case-insensitive match)
  - impactAngle_deg == 0
  - offsetDistance_mm == 0
  - occupantLocation is a front seat (LEFT FRONT SEAT or RIGHT FRONT SEAT)
  - HIC is present (non-empty)

Usage:
  python3 filter-results.py --input hic_latest.csv --output hic_filtered.csv
"""

import argparse
import csv
from pathlib import Path


def parse_number(value):
    """Convert numeric-looking strings to float; blank/None -> None."""
    if value is None:
        return None
    s = str(value).strip()
    if not s:
        return None
    try:
        return float(s)
    except ValueError:
        return None


def main():
    parser = argparse.ArgumentParser(description="Filter HIC CSV results for head-on, zero-offset barrier tests (by configuration).")
    parser.add_argument("--input", "-i", default="hic_latest.csv", help="Path to input CSV (default: hic_latest.csv)")
    parser.add_argument("--output", "-o", default="hic_filtered.csv", help="Path to write filtered CSV (default: hic_filtered.csv)")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        raise SystemExit(f"Input file not found: {input_path}")

    with input_path.open(newline="") as infile:
        reader = csv.DictReader(infile)
        rows = list(reader)
        fieldnames = reader.fieldnames

    if fieldnames is None:
        raise SystemExit("Input CSV has no header.")

    def matches(row):
        configuration = (row.get("configuration") or "").strip().upper()
        impact_angle = parse_number(row.get("impactAngle_deg"))
        offset_distance = parse_number(row.get("offsetDistance_mm"))
        occupant_location = (row.get("occupantLocation") or "").strip().upper()
        hic_value = (row.get("HIC") or "").strip()
        front_seats = {"LEFT FRONT SEAT", "RIGHT FRONT SEAT"}
        return (
            configuration == "VEHICLE INTO BARRIER"
            and (impact_angle or 0) == 0
            and (offset_distance or 0) == 0
            and occupant_location in front_seats
            and hic_value != ""
        )

    filtered = [row for row in rows if matches(row)]

    with output_path.open("w", newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(filtered)

    print(f"Wrote {len(filtered)} rows to {output_path} (from {len(rows)} input rows)")


if __name__ == "__main__":
    main()
