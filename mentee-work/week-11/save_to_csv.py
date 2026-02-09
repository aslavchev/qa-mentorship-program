# save_to_csv.py
# Save SauceDemo checkout test data to CSV

import csv
from faker import Faker

fake = Faker()


def generate_test_data(count: int = 50):
    """Generate checkout test data as list of dictionaries."""
    data = []
    for i in range(count):
        data.append({
            "test_id": f"TC-CHECKOUT-{i+1:03d}",
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "zip_code": fake.zipcode(),
            "expected_result": "Order placed successfully"
        })
    return data


def save_to_csv(data, filename: str = "checkout_test_data.csv"):
    """Save list of dicts to CSV file."""
    fieldnames = ["test_id", "first_name", "last_name", "zip_code", "expected_result"]

    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f"✅ Saved {len(data)} records to {filename}")


if __name__ == "__main__":
    print("Generating test data...")
    test_data = generate_test_data(50)

    print("Saving to CSV...")
    save_to_csv(test_data)

    print("\n✅ CSV file created successfully!")
    print("📂 Open 'checkout_test_data.csv' in Excel or a text editor.")
