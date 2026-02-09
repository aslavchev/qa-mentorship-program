# read_from_csv.py
# Read SauceDemo checkout test data from CSV

import csv


def read_csv(filename: str = "checkout_test_data.csv"):
    """Read CSV into list of dictionaries."""
    data = []
    with open(filename, "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data


if __name__ == "__main__":
    print("Reading test data from CSV...\n")
    test_data = read_csv()

    print(f"Loaded {len(test_data)} test cases:\n")
    print(f"{'Test ID':<20} {'Name':<30} {'Zip':<10}")
    print("-" * 60)

    for record in test_data:
        full_name = f"{record['first_name']} {record['last_name']}"
        print(f"{record['test_id']:<20} {full_name:<30} {record['zip_code']:<10}")

    print(f"\n✅ Successfully read {len(test_data)} records from CSV")
