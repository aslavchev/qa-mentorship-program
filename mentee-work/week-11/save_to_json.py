# save_to_json.py
# Save SauceDemo checkout test data to JSON

import json
from faker import Faker

fake = Faker()


def generate_test_data(count: int = 50):
    """Generate checkout test data as list of dictionaries."""
    data = []
    for i in range(count):
        data.append({
            "testId": f"TC-CHECKOUT-{i+1:03d}",
            "firstName": fake.first_name(),
            "lastName": fake.last_name(),
            "zipCode": fake.zipcode(),
            "expectedResult": "Order placed successfully",
            "priority": "P2",
            "module": "Checkout"
        })
    return data


def save_to_json(data, filename: str = "checkout_test_data.json"):
    """Save list of dicts to JSON file."""
    with open(filename, "w", encoding="utf-8") as jsonfile:
        json.dump(data, jsonfile, indent=2, ensure_ascii=False)

    print(f"✅ Saved {len(data)} records to {filename}")


if __name__ == "__main__":
    print("Generating test data...")
    test_data = generate_test_data(50)

    print("Saving to JSON...")
    save_to_json(test_data)

    print("\n✅ JSON file created successfully!")
    print("📂 Open 'checkout_test_data.json' in a text editor.")
