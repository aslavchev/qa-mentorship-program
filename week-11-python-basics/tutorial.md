# Week 11: Python for Test Data & APIs

## 🎯 Learning Objectives
- Set up Python development environment
- Generate test data programmatically
- Read and write CSV/JSON files
- Perform basic API testing with requests library
- Automate repetitive test data tasks
- Understand when automation adds value

## 📚 Why Python for QA?

**Problem:** Manual test data creation is time-consuming, error-prone, and tedious.

**Solution:** Python can automate test data generation, file handling, and simple API testing.

### Benefits
- ✅ Generate hundreds of test data records in seconds
- ✅ Randomize data for variety
- ✅ Read/write test data files (CSV, JSON)
- ✅ Simple API testing without UI
- ✅ Repeatable, consistent data
- ✅ Save hours of manual work

### What This Week is NOT
❌ This is NOT a comprehensive Python course
❌ This is NOT Selenium automation training
❌ This is NOT about replacing manual testing

### What This Week IS
✅ Light introduction to Python for QA tasks
✅ Focus on test data and simple API testing
✅ Practical scripts you can use immediately
✅ Foundation for future automation learning

---

## 1️⃣ Python Setup

### Install Python

#### Windows
1. Go to https://www.python.org/downloads/
2. Download Python 3.11+ (latest stable version)
3. Run installer
   - ✅ Check "Add Python to PATH"
   - Click "Install Now"
4. Verify installation:
   ```bash
   python --version
   # Should show: Python 3.11.x
   ```

#### macOS
**Option 1: Official Installer**
1. Go to https://www.python.org/downloads/
2. Download macOS installer
3. Run and follow prompts

**Option 2: Homebrew (recommended)**
```bash
brew install python3
```

Verify:
```bash
python3 --version
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip
```

Verify:
```bash
python3 --version
pip3 --version
```

### Install IDE/Editor

**Option 1: VS Code (Recommended)**
1. Download: https://code.visualstudio.com/
2. Install Python extension:
   - Open VS Code
   - Click Extensions (left sidebar)
   - Search "Python"
   - Install "Python" by Microsoft

**Option 2: PyCharm Community (Full IDE)**
- Download: https://www.jetbrains.com/pycharm/download/
- Free community edition available

**Option 3: Sublime Text / Atom**
- Lightweight editors, good for beginners

### Create Your First Python Script

**test_hello.py:**
```python
# My first Python script
print("Hello, QA World!")
print("Python version:")
import sys
print(sys.version)
```

**Run it:**
```bash
python test_hello.py
```

**Output:**
```
Hello, QA World!
Python version:
3.11.5 (main, ...)
```

---

## 2️⃣ Python Basics for QA

### Variables & Data Types

```python
# String (text)
username = "standard_user"
password = "secret_sauce"
error_message = "Username and password do not match"

# Integer (whole numbers)
item_count = 5
test_case_count = 150

# Float (decimal numbers)
product_price = 29.99
tax_rate = 0.08

# Boolean (True/False)
is_logged_in = True
test_passed = False

# List (ordered collection)
users = ["standard_user", "problem_user", "locked_out_user"]
test_data = [("John", "Doe", "12345"), ("Jane", "Smith", "90210")]

# Dictionary (key-value pairs)
user_credentials = {
    "username": "standard_user",
    "password": "secret_sauce"
}
```

### Print Output

```python
# Basic print
print("Test started")

# Print variables
username = "standard_user"
print("Testing with user:", username)

# F-strings (formatted strings)
result = "PASS"
print(f"Test result: {result}")

# Multiple values
print("Username:", username, "Password:", password)
```

### String Operations

```python
# Concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # John Doe

# Length
username = "standard_user"
print(len(username))  # 13

# Upper/Lower case
print(username.upper())  # STANDARD_USER
print(username.lower())  # standard_user

# Check if substring exists
if "user" in username:
    print("Contains 'user'")

# Replace
new_username = username.replace("standard", "test")
print(new_username)  # test_user

# Split
full_name = "John Doe"
parts = full_name.split(" ")
print(parts)  # ['John', 'Doe']
print(parts[0])  # John
print(parts[1])  # Doe
```

### Lists (Arrays)

```python
# Create list
products = ["Backpack", "Bike Light", "T-Shirt", "Jacket"]

# Access elements
print(products[0])  # Backpack
print(products[1])  # Bike Light

# Add elements
products.append("Onesie")
print(products)  # ['Backpack', ..., 'Onesie']

# Remove elements
products.remove("T-Shirt")
print(products)  # ['Backpack', 'Bike Light', 'Jacket', 'Onesie']

# Length
print(len(products))  # 4

# Loop through list
for product in products:
    print(f"Testing product: {product}")

# Check if element exists
if "Backpack" in products:
    print("Backpack is available")
```

### Dictionaries (Key-Value)

```python
# Create dictionary
user = {
    "username": "standard_user",
    "password": "secret_sauce",
    "firstName": "John",
    "lastName": "Doe"
}

# Access values
print(user["username"])  # standard_user
print(user.get("firstName"))  # John

# Add/update values
user["zipCode"] = "12345"
user["firstName"] = "Jane"

# Loop through dictionary
for key, value in user.items():
    print(f"{key}: {value}")

# Check if key exists
if "password" in user:
    print("Password is set")
```

### Conditional Statements

```python
# If statement
test_result = "PASS"

if test_result == "PASS":
    print("Test succeeded!")
elif test_result == "FAIL":
    print("Test failed!")
else:
    print("Unknown result")

# Comparison operators
defect_count = 5

if defect_count == 0:
    print("No defects")
elif defect_count > 10:
    print("Too many defects!")
elif defect_count >= 1 and defect_count <= 10:
    print("Acceptable defect count")
```

### Loops

```python
# For loop (iterate over list)
users = ["standard_user", "problem_user", "locked_out_user"]

for user in users:
    print(f"Testing with {user}")

# For loop with range (0-4)
for i in range(5):
    print(f"Test iteration {i}")

# While loop
test_count = 0
while test_count < 3:
    print(f"Running test {test_count}")
    test_count += 1
```

### Functions

```python
# Define function
def generate_username(first_name, last_name):
    username = first_name.lower() + "_" + last_name.lower()
    return username

# Call function
username = generate_username("John", "Doe")
print(username)  # john_doe

# Function with default parameters
def generate_zip_code(length=5):
    import random
    return ''.join([str(random.randint(0, 9)) for _ in range(length)])

print(generate_zip_code())      # 12345 (5 digits, default)
print(generate_zip_code(9))     # 123456789 (9 digits)
```

---

## 3️⃣ Generating Test Data

### Random Data Generation

```python
import random
import string

# Random integer
random_age = random.randint(18, 100)
print(f"Age: {random_age}")  # e.g., 42

# Random choice from list
users = ["standard_user", "problem_user", "performance_glitch_user"]
random_user = random.choice(users)
print(f"Selected user: {random_user}")

# Random string (for first name)
def generate_random_string(length=6):
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for _ in range(length))

first_name = generate_random_string(6)
print(f"First name: {first_name}")  # e.g., JXKMPQ

# Random email
def generate_random_email():
    username = generate_random_string(8).lower()
    domains = ["gmail.com", "yahoo.com", "test.com"]
    domain = random.choice(domains)
    return f"{username}@{domain}"

email = generate_random_email()
print(f"Email: {email}")  # e.g., abcdefgh@gmail.com

# Random phone number
def generate_phone_number():
    return f"({random.randint(200, 999)}) {random.randint(200, 999)}-{random.randint(1000, 9999)}"

phone = generate_phone_number()
print(f"Phone: {phone}")  # e.g., (555) 123-4567
```

### Realistic Test Data

```python
import random

# Lists of realistic data
first_names = ["John", "Jane", "Michael", "Emily", "David", "Sarah",
               "James", "Mary", "Robert", "Patricia"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones",
              "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
states = ["NY", "CA", "IL", "TX", "AZ"]

# Generate realistic person
def generate_person():
    return {
        "firstName": random.choice(first_names),
        "lastName": random.choice(last_names),
        "zipCode": str(random.randint(10000, 99999)),
        "city": random.choice(cities),
        "state": random.choice(states)
    }

# Generate 5 people
for i in range(5):
    person = generate_person()
    print(f"Person {i+1}: {person['firstName']} {person['lastName']}, "
          f"{person['city']}, {person['state']} {person['zipCode']}")
```

**Output:**
```
Person 1: John Smith, New York, NY 12345
Person 2: Emily Garcia, Chicago, IL 60601
Person 3: David Williams, Phoenix, AZ 85001
Person 4: Sarah Johnson, Los Angeles, CA 90001
Person 5: James Martinez, Houston, TX 77001
```

### SauceDemo Test Data Generator

```python
import random

# Generate checkout test data for SauceDemo
def generate_checkout_data(count=10):
    first_names = ["John", "Jane", "Michael", "Emily", "David"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones"]

    test_data = []

    for i in range(count):
        data = {
            "test_id": f"TC-CHECKOUT-{i+1:03d}",
            "firstName": random.choice(first_names),
            "lastName": random.choice(last_names),
            "zipCode": str(random.randint(10000, 99999)),
            "expected_result": "SUCCESS"
        }
        test_data.append(data)

    return test_data

# Generate and display
checkout_data = generate_checkout_data(5)
for data in checkout_data:
    print(f"{data['test_id']}: {data['firstName']} {data['lastName']}, Zip: {data['zipCode']}")
```

**Output:**
```
TC-CHECKOUT-001: John Smith, Zip: 12345
TC-CHECKOUT-002: Emily Johnson, Zip: 67890
TC-CHECKOUT-003: Michael Williams, Zip: 45678
TC-CHECKOUT-004: Jane Brown, Zip: 98765
TC-CHECKOUT-005: David Jones, Zip: 34567
```

---

## 4️⃣ Working with CSV Files

### Writing CSV Files

```python
import csv

# Test data
checkout_data = [
    ["Test ID", "First Name", "Last Name", "Zip Code", "Expected Result"],
    ["TC-001", "John", "Doe", "12345", "SUCCESS"],
    ["TC-002", "Jane", "Smith", "90210", "SUCCESS"],
    ["TC-003", "Bob", "Johnson", "60601", "SUCCESS"],
]

# Write to CSV
with open("checkout_test_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(checkout_data)

print("CSV file created: checkout_test_data.csv")
```

**Result:** `checkout_test_data.csv`
```csv
Test ID,First Name,Last Name,Zip Code,Expected Result
TC-001,John,Doe,12345,SUCCESS
TC-002,Jane,Smith,90210,SUCCESS
TC-003,Bob,Johnson,60601,SUCCESS
```

### Reading CSV Files

```python
import csv

# Read CSV
with open("checkout_test_data.csv", "r") as file:
    reader = csv.reader(file)

    # Skip header
    next(reader)

    # Read each row
    for row in reader:
        test_id = row[0]
        first_name = row[1]
        last_name = row[2]
        zip_code = row[3]

        print(f"{test_id}: Testing checkout with {first_name} {last_name}, Zip: {zip_code}")
```

**Output:**
```
TC-001: Testing checkout with John Doe, Zip: 12345
TC-002: Testing checkout with Jane Smith, Zip: 90210
TC-003: Testing checkout with Bob Johnson, Zip: 60601
```

### CSV DictReader (Better)

```python
import csv

# Read CSV as dictionaries
with open("checkout_test_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(f"{row['Test ID']}: {row['First Name']} {row['Last Name']}")
        print(f"  Zip: {row['Zip Code']}, Expected: {row['Expected Result']}")
```

### Generate and Save CSV

```python
import csv
import random

def generate_csv_test_data(filename, count=10):
    first_names = ["John", "Jane", "Michael", "Emily", "David"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones"]

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        # Write header
        writer.writerow(["Test ID", "First Name", "Last Name", "Zip Code", "Expected"])

        # Write data rows
        for i in range(count):
            test_id = f"TC-CHECKOUT-{i+1:03d}"
            first = random.choice(first_names)
            last = random.choice(last_names)
            zip_code = str(random.randint(10000, 99999))
            expected = "SUCCESS"

            writer.writerow([test_id, first, last, zip_code, expected])

    print(f"Generated {count} test records in {filename}")

# Generate 20 test cases
generate_csv_test_data("saucedemo_checkout_tests.csv", 20)
```

---

## 5️⃣ Working with JSON Files

### Writing JSON Files

```python
import json

# Test data (dictionary/list)
test_users = [
    {
        "username": "standard_user",
        "password": "secret_sauce",
        "type": "valid"
    },
    {
        "username": "locked_out_user",
        "password": "secret_sauce",
        "type": "locked"
    },
    {
        "username": "problem_user",
        "password": "secret_sauce",
        "type": "problem"
    }
]

# Write to JSON file
with open("test_users.json", "w") as file:
    json.dump(test_users, file, indent=2)

print("JSON file created: test_users.json")
```

**Result:** `test_users.json`
```json
[
  {
    "username": "standard_user",
    "password": "secret_sauce",
    "type": "valid"
  },
  {
    "username": "locked_out_user",
    "password": "secret_sauce",
    "type": "locked"
  },
  {
    "username": "problem_user",
    "password": "secret_sauce",
    "type": "problem"
  }
]
```

### Reading JSON Files

```python
import json

# Read JSON file
with open("test_users.json", "r") as file:
    users = json.load(file)

# Loop through users
for user in users:
    print(f"Username: {user['username']}, Type: {user['type']}")
```

**Output:**
```
Username: standard_user, Type: valid
Username: locked_out_user, Type: locked
Username: problem_user, Type: problem
```

### Complex JSON Test Data

```python
import json

# Comprehensive test data structure
test_data = {
    "users": [
        {"username": "standard_user", "password": "secret_sauce", "type": "valid"},
        {"username": "locked_out_user", "password": "secret_sauce", "type": "locked"}
    ],
    "products": [
        {"name": "Sauce Labs Backpack", "price": 29.99, "id": 4},
        {"name": "Sauce Labs Bike Light", "price": 9.99, "id": 0}
    ],
    "checkout_data": [
        {"firstName": "John", "lastName": "Doe", "zipCode": "12345"},
        {"firstName": "Jane", "lastName": "Smith", "zipCode": "90210"}
    ]
}

# Save to JSON
with open("saucedemo_test_data.json", "w") as file:
    json.dump(test_data, file, indent=2)

print("Complete test data saved!")
```

---

## 6️⃣ Basic API Testing with Python

### Install Requests Library

```bash
pip install requests
```

or

```bash
pip3 install requests
```

### Simple GET Request

```python
import requests

# Make GET request
response = requests.get("https://jsonplaceholder.typicode.com/users/1")

# Print status code
print(f"Status Code: {response.status_code}")  # 200

# Print response body (JSON)
print(f"Response: {response.json()}")

# Access specific fields
data = response.json()
print(f"Name: {data['name']}")
print(f"Email: {data['email']}")
```

### API Test: Verify Response

```python
import requests

def test_get_user():
    # Arrange
    url = "https://jsonplaceholder.typicode.com/users/1"

    # Act
    response = requests.get(url)

    # Assert
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    data = response.json()
    assert "name" in data, "Response missing 'name' field"
    assert "email" in data, "Response missing 'email' field"

    print("✅ Test passed: GET user API works correctly")

# Run test
test_get_user()
```

### POST Request (Create Data)

```python
import requests
import json

# Data to send
new_user = {
    "name": "John Doe",
    "email": "john.doe@test.com",
    "phone": "555-1234"
}

# Make POST request
response = requests.post(
    "https://jsonplaceholder.typicode.com/users",
    json=new_user
)

print(f"Status Code: {response.status_code}")  # 201 (Created)
print(f"Response: {response.json()}")
```

### API Test Suite Example

```python
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_all_users():
    """Test GET /users returns list of users"""
    response = requests.get(f"{BASE_URL}/users")

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    users = response.json()
    assert len(users) > 0, "Expected at least 1 user"
    assert isinstance(users, list), "Expected list of users"

    print("✅ Test passed: GET all users")

def test_get_single_user():
    """Test GET /users/{id} returns specific user"""
    response = requests.get(f"{BASE_URL}/users/1")

    assert response.status_code == 200

    user = response.json()
    assert user["id"] == 1
    assert "name" in user
    assert "email" in user

    print("✅ Test passed: GET single user")

def test_get_invalid_user():
    """Test GET /users/9999 returns 404"""
    response = requests.get(f"{BASE_URL}/users/9999")

    # This API returns 404 for invalid IDs
    assert response.status_code == 404, f"Expected 404, got {response.status_code}"

    print("✅ Test passed: GET invalid user returns 404")

def test_create_user():
    """Test POST /users creates new user"""
    new_user = {
        "name": "Test User",
        "email": "test@example.com"
    }

    response = requests.post(f"{BASE_URL}/users", json=new_user)

    assert response.status_code == 201, f"Expected 201, got {response.status_code}"

    created_user = response.json()
    assert "id" in created_user, "Response missing 'id'"

    print("✅ Test passed: POST create user")

# Run all tests
if __name__ == "__main__":
    print("Running API Tests...\n")
    test_get_all_users()
    test_get_single_user()
    test_get_invalid_user()
    test_create_user()
    print("\n✅ All tests passed!")
```

**Output:**
```
Running API Tests...

✅ Test passed: GET all users
✅ Test passed: GET single user
✅ Test passed: GET invalid user returns 404
✅ Test passed: POST create user

✅ All tests passed!
```

---

## 7️⃣ Complete Test Data Script for SauceDemo

### All-in-One Test Data Generator

```python
import random
import csv
import json

# --- Configuration ---
FIRST_NAMES = ["John", "Jane", "Michael", "Emily", "David", "Sarah", "James", "Mary"]
LAST_NAMES = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis"]

# --- Functions ---

def generate_checkout_data(count=10):
    """Generate checkout form test data"""
    data = []
    for i in range(count):
        data.append({
            "test_id": f"TC-CHECKOUT-{i+1:03d}",
            "firstName": random.choice(FIRST_NAMES),
            "lastName": random.choice(LAST_NAMES),
            "zipCode": str(random.randint(10000, 99999)),
            "expected": "SUCCESS"
        })
    return data

def generate_invalid_data(count=5):
    """Generate invalid test data for negative testing"""
    invalid_data = []

    # Empty fields
    invalid_data.append({
        "test_id": "TC-INVALID-001",
        "firstName": "",
        "lastName": "Doe",
        "zipCode": "12345",
        "expected": "ERROR: First Name is required"
    })

    # Special characters
    invalid_data.append({
        "test_id": "TC-INVALID-002",
        "firstName": "<script>alert(1)</script>",
        "lastName": "Hacker",
        "zipCode": "12345",
        "expected": "ERROR or sanitized input"
    })

    # Too long
    invalid_data.append({
        "test_id": "TC-INVALID-003",
        "firstName": "A" * 100,
        "lastName": "B" * 100,
        "zipCode": "999999999",
        "expected": "ERROR or truncated"
    })

    # Numbers in name
    invalid_data.append({
        "test_id": "TC-INVALID-004",
        "firstName": "John123",
        "lastName": "Doe456",
        "zipCode": "12345",
        "expected": "ERROR or accepted"
    })

    # SQL injection
    invalid_data.append({
        "test_id": "TC-INVALID-005",
        "firstName": "' OR '1'='1",
        "lastName": "'; DROP TABLE users--",
        "zipCode": "12345",
        "expected": "ERROR or sanitized"
    })

    return invalid_data

def save_to_csv(data, filename):
    """Save data to CSV file"""
    if not data:
        print("No data to save")
        return

    with open(filename, "w", newline="") as file:
        # Get headers from first item
        headers = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=headers)

        writer.writeheader()
        writer.writerows(data)

    print(f"✅ Saved {len(data)} records to {filename}")

def save_to_json(data, filename):
    """Save data to JSON file"""
    with open(filename, "w") as file:
        json.dump(data, file, indent=2)

    print(f"✅ Saved {len(data)} records to {filename}")

# --- Main Program ---

def main():
    print("SauceDemo Test Data Generator")
    print("=" * 40)

    # Generate valid checkout data
    print("\n1. Generating valid checkout data...")
    valid_data = generate_checkout_data(20)
    save_to_csv(valid_data, "valid_checkout_data.csv")
    save_to_json(valid_data, "valid_checkout_data.json")

    # Generate invalid data
    print("\n2. Generating invalid test data...")
    invalid_data = generate_invalid_data()
    save_to_csv(invalid_data, "invalid_checkout_data.csv")
    save_to_json(invalid_data, "invalid_checkout_data.json")

    # Generate combined dataset
    print("\n3. Generating combined dataset...")
    all_data = valid_data + invalid_data
    save_to_json({"valid": valid_data, "invalid": invalid_data}, "all_test_data.json")

    print("\n" + "=" * 40)
    print(f"✅ Complete! Generated {len(valid_data)} valid + {len(invalid_data)} invalid test cases")
    print(f"📁 Files created:")
    print("   - valid_checkout_data.csv")
    print("   - valid_checkout_data.json")
    print("   - invalid_checkout_data.csv")
    print("   - invalid_checkout_data.json")
    print("   - all_test_data.json")

if __name__ == "__main__":
    main()
```

**Run it:**
```bash
python generate_test_data.py
```

**Output:**
```
SauceDemo Test Data Generator
========================================

1. Generating valid checkout data...
✅ Saved 20 records to valid_checkout_data.csv
✅ Saved 20 records to valid_checkout_data.json

2. Generating invalid test data...
✅ Saved 5 records to invalid_checkout_data.csv
✅ Saved 5 records to invalid_checkout_data.json

3. Generating combined dataset...
✅ Saved 25 records to all_test_data.json

========================================
✅ Complete! Generated 20 valid + 5 invalid test cases
📁 Files created:
   - valid_checkout_data.csv
   - valid_checkout_data.json
   - invalid_checkout_data.csv
   - invalid_checkout_data.json
   - all_test_data.json
```

---

## 8️⃣ When to Use Python for QA

### Good Use Cases ✅

1. **Test Data Generation**
   - Need 100+ test records
   - Randomized data for variety
   - Avoid manual data entry

2. **File Operations**
   - Read test data from CSV/JSON
   - Batch process test results
   - Convert between formats

3. **Simple API Testing**
   - Test REST APIs without UI
   - Faster than UI testing
   - Easier to automate

4. **Data Validation**
   - Verify file contents
   - Compare expected vs actual data
   - Check data integrity

5. **Reporting**
   - Generate test reports
   - Aggregate test results
   - Create metrics dashboards

### Poor Use Cases ❌

1. **Replacing Manual Testing**
   - Exploratory testing needs human creativity
   - Usability testing requires human judgment

2. **Premature Automation**
   - Automating unstable features
   - UI changes frequently (maintenance burden)

3. **Complex UI Automation (for beginners)**
   - Selenium requires significant learning
   - Start with test data and APIs first

4. **Everything**
   - Not every task needs automation
   - Manual testing is faster for one-time tests

---

## 📝 Summary

### Key Takeaways

1. **Python Setup:**
   - Install Python 3.11+
   - Use VS Code or PyCharm
   - Verify with `python --version`

2. **Test Data Generation:**
   - Use `random` module for randomization
   - Create realistic data (first/last names, zip codes)
   - Save to CSV or JSON files

3. **CSV Files:**
   - Use `csv.writer()` to write
   - Use `csv.DictReader()` to read (easiest)
   - Great for tabular test data

4. **JSON Files:**
   - Use `json.dump()` to write
   - Use `json.load()` to read
   - Great for structured, nested data

5. **API Testing:**
   - Install `requests` library
   - `requests.get()`, `requests.post()`
   - Verify status codes and response data

6. **When to Automate:**
   - Repetitive tasks (test data generation)
   - API testing (faster than UI)
   - Data validation
   - NOT exploratory or usability testing

### This Week's Challenge

**Create a complete test data generator for SauceDemo:**
- Valid checkout data (20 records)
- Invalid checkout data (10 records)
- Save to both CSV and JSON
- Test a public API with 5 test cases

---

## 🤔 Self-Assessment Questions

1. How do you install Python on your OS?
2. What's the difference between a list and a dictionary in Python?
3. How do you generate a random integer between 1 and 100?
4. What library is used to read/write CSV files?
5. What library is used to read/write JSON files?
6. What library is used for API testing in Python?
7. How do you check if an API returns status code 200?
8. When should you use Python for QA tasks?
9. When should you NOT use Python for QA tasks?
10. What's the difference between CSV and JSON for test data?

### Answers to Check
1. Download from python.org, run installer, check "Add to PATH"; or use Homebrew (macOS) or apt (Linux)
2. List = ordered collection with index [0, 1, 2]; Dictionary = key-value pairs {"name": "John"}
3. `import random; num = random.randint(1, 100)`
4. `csv` module (built-in)
5. `json` module (built-in)
6. `requests` library (install with `pip install requests`)
7. `response = requests.get(url); assert response.status_code == 200`
8. Test data generation, file operations, simple API testing, data validation, reporting
9. Manual exploratory testing, usability testing, complex UI automation (as beginner), premature automation
10. CSV = tabular data (rows/columns, simple); JSON = nested structured data (objects/arrays, more flexible)

---

## 🎉 Congratulations!

You've completed the 11-Week QA Fundamentals Program!

### What You've Learned:
- ✅ Week 1: QA Foundations & SDLC
- ✅ Week 2: Test Levels (Unit, Integration, System, Acceptance)
- ✅ Week 3: Functional Testing Types
- ✅ Week 4: Non-Functional Testing
- ✅ Week 5: Test Design Techniques (Basic)
- ✅ Week 6: Test Design Techniques (Advanced)
- ✅ Week 7: Test Planning & Strategy
- ✅ Week 8: Test Case Design & Management
- ✅ Week 9: Agile Testing & BDD
- ✅ Week 10: Defect Management
- ✅ Week 11: Python for Test Data & APIs

### Next Steps:

**Continue Learning:**
- Practice on real projects (contribute to open source)
- Learn test automation (Selenium, Cypress, Playwright)
- Explore API testing deeply (Postman, REST Assured)
- Study performance testing (JMeter, K6)
- Learn CI/CD integration (Jenkins, GitHub Actions)

**Build Portfolio:**
- Document your SauceDemo testing project on GitHub
- Write blog posts about what you learned
- Create test plans and test cases to showcase
- Contribute test documentation to open source projects

**Get Certified:**
- ISTQB Foundation Level (optional, but recognized)
- ISTQB Agile Tester

**Join Communities:**
- Ministry of Testing (ministryoftesting.com)
- Reddit: r/QualityAssurance, r/softwaretesting
- LinkedIn QA groups
- Local meetups (Test Automation, Agile Testing)

**Apply for Jobs:**
- Junior QA Engineer
- QA Analyst
- Software Tester
- Test Engineer

**You're Ready!** 🚀

You now have the foundational knowledge and practical skills to start your QA career. Keep practicing, stay curious, and never stop learning.

**Good luck on your QA journey!** 🎯
