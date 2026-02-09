# test_data_master.py
# Complete test data generation solution for SauceDemo checkout

import csv
import json
from datetime import datetime
from faker import Faker

fake = Faker()


def generate_random_data(count: int = 50) -> list[dict]:
    """Generate random checkout test data records."""
    data: list[dict] = []
    for i in range(count):
        data.append({
            "test_id": f"TC-CHECKOUT-{i+1:03d}",
            "category": "Random",
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "zip_code": fake.zipcode(),
            "expected_result": "Order placed successfully",
            "priority": "P2",
            "status": "Not Executed",
        })
    return data


def generate_edge_cases() -> list[dict]:
    """Generate edge case checkout test data records."""
    return [
        {
            "test_id": "TC-CHECKOUT-EDGE-001",
            "category": "Edge Case",
            "first_name": "A",
            "last_name": "B",
            "zip_code": "12345",
            "expected_result": "Order placed successfully",
            "priority": "P1",
            "status": "Not Executed",
        },
        {
            "test_id": "TC-CHECKOUT-EDGE-002",
            "category": "Edge Case",
            "first_name": "A" * 100,
            "last_name": "B" * 100,
            "zip_code": "99999",
            "expected_result": "Order placed successfully",
            "priority": "P1",
            "status": "Not Executed",
        },
        {
            "test_id": "TC-CHECKOUT-EDGE-003",
            "category": "Edge Case",
            "first_name": "John-Paul",
            "last_name": "O'Brien",
            "zip_code": "12345",
            "expected_result": "Order placed successfully",
            "priority": "P2",
            "status": "Not Executed",
        },
        {
            "test_id": "TC-CHECKOUT-EDGE-004",
            "category": "Edge Case",
            "first_name": "María",
            "last_name": "José",
            "zip_code": "90210",
            "expected_result": "Order placed successfully",
            "priority": "P2",
            "status": "Not Executed",
        },
        {
            "test_id": "TC-CHECKOUT-EDGE-005",
            "category": "Edge Case",
            "first_name": "John Paul",
            "last_name": "Van Der Berg",
            "zip_code": "12345",
            "expected_result": "Order placed successfully",
            "priority": "P2",
            "status": "Not Executed",
        },
        {
            "test_id": "TC-CHECKOUT-EDGE-006",
            "category": "Edge Case",
            "first_name": "François",
            "last_name": "Müller",
            "zip_code": "12345",
            "expected_result": "Order placed successfully",
            "priority": "P2",
            "status": "Not Executed",
        },
        {
            "test_id": "TC-CHECKOUT-EDGE-007",
            "category": "Edge Case",
            "first_name": "北京",
            "last_name": "东京",
            "zip_code": "12345",
            "expected_result": "Error (expected): Invalid characters",
            "priority": "P2",
            "status": "Not Executed",
        },
        {
            "test_id": "TC-CHECKOUT-EDGE-008",
            "category": "Edge Case",
            "first_name": "John123",
            "last_name": "Doe456",
            "zip_code": "12345",
            "expected_result": "Error (expected): Numbers not allowed",
            "priority": "P2",
            "status": "Not Executed",
        },
        {
            "test_id": "TC-CHECKOUT-EDGE-009",
            "category": "Edge Case",
            "first_name": "",
            "last_name": "Doe",
            "zip_code": "12345",
            "expected_result": "Error: First Name is required",
            "priority": "P1",
            "status": "Not Executed",
        },
        {
            "test_id": "TC-CHECKOUT-EDGE-010",
            "category": "Edge Case",
            "first_name": "John",
            "last_name": "",
            "zip_code": "12345",
            "expected_result": "Error: Last Name is required",
            "priority": "P1",
            "status": "Not Executed",
        },
    ]


def save_to_csv(data: list[dict], filename: str = "saucedemo_checkout_tests.csv") -> None:
    """Save test data to CSV file."""
    fieldnames = [
        "test_id",
        "category",
        "first_name",
        "last_name",
        "zip_code",
        "expected_result",
        "priority",
        "status",
    ]

    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f"✅ CSV: Saved {len(data)} records to {filename}")


def save_to_json(data: list[dict], filename: str = "saucedemo_checkout_tests.json") -> None:
    """Save test data to JSON file with metadata."""
    output = {
        "metadata": {
            "generated_at": datetime.now().isoformat(timespec="seconds"),
            "total_tests": len(data),
            "generator": "test_data_master.py",
            "application": "SauceDemo",
            "module": "Checkout",
        },
        "tests": data,
    }

    with open(filename, "w", encoding="utf-8") as jsonfile:
        json.dump(output, jsonfile, indent=2, ensure_ascii=False)

    print(f"✅ JSON: Saved {len(data)} records to {filename}")


def print_summary(random_data: list[dict], edge_data: list[dict]) -> None:
    total = len(random_data) + len(edge_data)
    p1_count = sum(1 for d in (random_data + edge_data) if d["priority"] == "P1")
    p2_count = total - p1_count

    print("\n" + "=" * 70)
    print("SAUCEDEMO CHECKOUT TEST DATA - GENERATION SUMMARY")
    print("=" * 70)
    print("\n📊 Statistics:")
    print(f"   Random Test Cases: {len(random_data)}")
    print(f"   Edge Cases: {len(edge_data)}")
    print(f"   Total Records: {total}")

    print("\n📌 Priority Distribution:")
    print(f"   P1 (High): {p1_count}")
    print(f"   P2 (Medium): {p2_count}")

    print("\n💾 Files Created:")
    print("   saucedemo_checkout_tests.csv")
    print("   saucedemo_checkout_tests.json")

    print("\n✅ Ready for testing!")
    print("=" * 70)


if __name__ == "__main__":
    print("Generating SauceDemo checkout test data...\n")

    random_data = generate_random_data(50)
    edge_data = generate_edge_cases()
    all_data = random_data + edge_data

    save_to_csv(all_data)
    save_to_json(all_data)
    print_summary(random_data, edge_data)
