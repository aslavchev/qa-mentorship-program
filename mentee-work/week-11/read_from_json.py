# read_from_json.py
# Read SauceDemo checkout test data from JSON

import json


def read_json(filename: str = "checkout_test_data.json"):
    """Read JSON file into Python object (list of dicts)."""
    with open(filename, "r", encoding="utf-8") as jsonfile:
        return json.load(jsonfile)


if __name__ == "__main__":
    print("Reading test data from JSON...\n")
    test_data = read_json()

    print(f"Loaded {len(test_data)} test cases:\n")

    # Show first 5 records
    for record in test_data[:5]:
        print(f"Test ID: {record['testId']}")
        print(f"  Name: {record['firstName']} {record['lastName']}")
        print(f"  Zip: {record['zipCode']}")
        print(f"  Priority: {record['priority']}")
        print()

    print(f"✅ Successfully read {len(test_data)} records from JSON")
