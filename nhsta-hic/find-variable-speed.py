#!/usr/bin/env python3
"""
Identify vehicles (make/model/year + occupant details) that were tested multiple times
(different testNo), regardless of whether the speeds match, while requiring the same
occupant location/type/sex/size.

Usage:
  python3 find-variable-speed.py --input hic_filtered.csv --output variable-speed.csv
"""

import argparse
import csv
from collections import defaultdict
from pathlib import Path


def parse_speed(value):
  """Return float speed if possible, else None."""
  if value is None:
    return None
  s = str(value).strip()
  if not s:
    return None
  try:
    return float(s)
  except ValueError:
    return None


def parse_duration(value):
  """Return float duration if possible, else None."""
  if value is None:
    return None
  s = str(value).strip()
  if not s:
    return None
  try:
    return float(s)
  except ValueError:
    return None


def norm_text(value):
  """Uppercased, stripped text for grouping; empty -> ''."""
  if value is None:
    return ""
  return str(value).strip().upper()


def main():
  parser = argparse.ArgumentParser(description="Find vehicles tested at multiple speeds.")
  parser.add_argument("--input", "-i", default="hic_filtered.csv", help="Path to input CSV (default: hic_filtered.csv)")
  parser.add_argument("--output", "-o", default="variable-speed.csv", help="Path to output CSV (default: variable-speed.csv)")
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

  groups = defaultdict(list)
  for row in rows:
    duration = parse_duration(row.get("HIC_duration"))
    if duration is None:
      continue
    if not (abs(duration - 15) <= 1 or abs(duration - 36) <= 1):
      continue
    # bucket durations so grouping tolerates +/-1 within target windows
    if abs(duration - 15) <= 1:
      duration_bucket = "15"
    else:
      duration_bucket = "36"

    key = (
      row.get("make"),
      row.get("model"),
      row.get("year"),
      norm_text(row.get("occupantLocation")),
      norm_text(row.get("occupantType")),
      norm_text(row.get("occupantSex")),
      norm_text(row.get("dummySizePercentile")),
      duration_bucket,
    )
    row_speed = parse_speed(row.get("closingSpeed_kph"))
    row["_closingSpeedParsed"] = row_speed  # stash parsed numeric for later checks
    row["_durationBucket"] = duration_bucket
    groups[key].append(row)

  matched_rows = []
  for key, grouped_rows in groups.items():
    test_nos = {r.get("testNo") for r in grouped_rows}
    # Speeds can be same or different; require multiple distinct testNos.
    if len(test_nos) > 1:
      matched_rows.extend(grouped_rows)

  if not matched_rows:
    print("No vehicles found with multiple tests for the same make/model/year and occupant details.")
    return

  with output_path.open("w", newline="") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in matched_rows:
      # drop helper key
      row.pop("_closingSpeedParsed", None)
      row.pop("_durationBucket", None)
      writer.writerow(row)

  combos = {(r.get("make"), r.get("model"), r.get("year")) for r in matched_rows}
  print(f"Wrote {len(matched_rows)} rows to {output_path} for {len(combos)} make/model/year combos with multiple tests (same occupant characteristics).")


if __name__ == "__main__":
  main()
