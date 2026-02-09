# verify_data.py
# Verify that generated CSV and JSON files can be read correctly

import csv
import json


def verify_csv(filename: str = "saucedemo_checkout_tests.csv") -> int:
    with open(filename, "r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    return len(rows)


def verify_json(filename: str = "saucedemo_checkout_tests.json") -> tuple[int, str]:
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    total = int(data["metadata"]["total_tests"])
    generated_at = str(data["metadata"]["generated_at"])
    return total, generated_at


if __name__ == "__main__":
    csv_count = verify_csv()
    json_total, generated_at = verify_json()

    print(f"CSV: {csv_count} records loaded")
    print(f"JSON: {json_total} records loaded")
    print(f"Generated at: {generated_at}")
    print("\n✅ Both files verified successfully!")
