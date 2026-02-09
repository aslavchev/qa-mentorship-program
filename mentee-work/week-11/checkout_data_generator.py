# checkout_data_generator.py
# Generates test data for SauceDemo checkout form (random + edge cases)

from faker import Faker

fake = Faker()

def generate_checkout_data(count: int = 50):
    """
    Generate random test data for SauceDemo checkout form.

    Args:
        count: Number of records to generate

    Returns:
        List of tuples (first_name, last_name, zip_code)
    """
    test_data = []
    for _ in range(count):
        first_name = fake.first_name()
        last_name = fake.last_name()
        zip_code = fake.zipcode()
        test_data.append((first_name, last_name, zip_code))
    return test_data


def generate_edge_cases():
    """
    Generate edge-case test data records for checkout fields.

    Notes:
    - Some cases are intentionally questionable (numbers in names, unicode, etc.)
      to help QA explore validation/sanitization expectations.
    """
    edge_cases = [
        # Minimum length
        ("A", "B", "12345"),

        # Very long strings (100 chars)
        ("A" * 100, "B" * 100, "99999"),

        # Special characters
        ("John-Paul", "O'Brien", "12345"),
        ("María", "José", "90210"),

        # Numbers in names (validation question)
        ("John123", "Doe456", "12345"),

        # Spaces / multi-part names
        ("John Paul", "Van Der Berg", "12345"),

        # Unicode / accents
        ("François", "Müller", "12345"),

        # Non-latin characters
        ("北京", "东京", "12345"),
    ]
    return edge_cases


def print_table(title: str, data):
    print("\n" + title)
    print("-" * 70)
    print(f"{'#':<5} {'First Name':<25} {'Last Name':<25} {'Zip Code':<10}")
    print("-" * 70)
    for i, (first, last, zip_code) in enumerate(data, 1):
        print(f"{i:<5} {first:<25} {last:<25} {zip_code:<10}")


if __name__ == "__main__":
    print("=" * 70)
    print("SAUCEDEMO CHECKOUT TEST DATA GENERATOR")
    print("=" * 70)

    random_data = generate_checkout_data(50)
    print(f"\nGenerated {len(random_data)} random records.")
    print_table("RANDOM DATA (50 records)", random_data)

    edge_data = generate_edge_cases()
    print(f"\nGenerated {len(edge_data)} edge-case records.")
    print_table("EDGE CASES", edge_data)

    print("\n✅ Test data generation complete!")
    print("💾 Copy values from the output and use them in checkout tests.")
