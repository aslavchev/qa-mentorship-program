# Week 11 - Exercise 3: CSV/JSON File Handling

**Your Name:** Kamen Asenov  
**Date:** 2026-01-26  

---

## Files Created

- [x] checkout_test_data.csv (50 records)
- [x] checkout_test_data.json (50 records)
- [x] save_to_csv.py (working)
- [x] read_from_csv.py (working)
- [x] save_to_json.py (working)
- [x] read_from_json.py (working)

---

## CSV Output Sample

test_id,first_name,last_name,zip_code,expected_result
TC-CHECKOUT-001,Tammy,Anderson,10675,Order placed successfully
TC-CHECKOUT-002,Bryan,Harrison,94358,Order placed successfully
TC-CHECKOUT-003,Stephen,Davis,33780,Order placed successfully
TC-CHECKOUT-004,Riley,Martinez,46401,Order placed successfully
TC-CHECKOUT-005,Clarence,Ramsey,43330,Order placed successfully
TC-CHECKOUT-006,Douglas,Lee,78690,Order placed successfully
TC-CHECKOUT-007,Dalton,Salinas,06772,Order placed successfully
TC-CHECKOUT-008,Susan,Silva,94983,Order placed successfully
TC-CHECKOUT-009,Benjamin,Brown,26131,Order placed successfully

## JSON Output Sample

[
  {
    "testId": "TC-CHECKOUT-001",
    "firstName": "John",
    "lastName": "Smith",
    "zipCode": "90210",
    "expectedResult": "Order placed successfully",
    "priority": "P2",
    "module": "Checkout"
  },
  {
    "testId": "TC-CHECKOUT-002",
    "firstName": "Maria",
    "lastName": "Garcia",
    "zipCode": "10001",
    "expectedResult": "Order placed successfully",
    "priority": "P2",
    "module": "Checkout"
  }
]

## Read CSV Output

Reading test data from CSV...

Loaded 50 test cases:

Test ID              Name                           Zip       
------------------------------------------------------------
TC-CHECKOUT-001      Tammy Anderson                 10675     
TC-CHECKOUT-002      Bryan Harrison                 94358     
TC-CHECKOUT-003      Stephen Davis                  33780     
TC-CHECKOUT-004      Riley Martinez                 46401     
TC-CHECKOUT-005      Clarence Ramsey                43330     
TC-CHECKOUT-006      Douglas Lee                    78690     
TC-CHECKOUT-007      Dalton Salinas                 06772     
TC-CHECKOUT-008      Susan Silva                    94983     
TC-CHECKOUT-009      Benjamin Brown                 26131     
TC-CHECKOUT-010      Gregory Ruiz                   20456     
TC-CHECKOUT-011      Courtney Hardin                57926     
TC-CHECKOUT-012      Michael Byrd                   93664     
TC-CHECKOUT-013      Christian Lopez                85929     
TC-CHECKOUT-014      Katherine Allen                44012     
TC-CHECKOUT-015      Michael Day                    29472     
TC-CHECKOUT-016      Chase Decker                   85002     
TC-CHECKOUT-017      Jonathan Solis                 49251     
TC-CHECKOUT-018      Shannon Walker                 89504     
TC-CHECKOUT-019      Curtis Hughes                  03424     
TC-CHECKOUT-020      James Ingram                   69596     
TC-CHECKOUT-021      David Mccall                   66646     
TC-CHECKOUT-022      Trevor Mahoney                 80556     
TC-CHECKOUT-023      David Tyler                    74487     
TC-CHECKOUT-024      Latoya Nolan                   58458     
TC-CHECKOUT-025      Julie Williams                 19919     
TC-CHECKOUT-026      Suzanne Burke                  28071     
TC-CHECKOUT-027      Teresa Singh                   09342     
TC-CHECKOUT-028      Jenny Russell                  90064     
TC-CHECKOUT-029      Russell Gutierrez              17804     
TC-CHECKOUT-030      Robert Carpenter               88023     
TC-CHECKOUT-031      Cynthia Mcguire                92846     
TC-CHECKOUT-032      Holly Long                     21497     
TC-CHECKOUT-033      Patrick Barnes                 35587     
TC-CHECKOUT-034      Erin Sanders                   34856     
TC-CHECKOUT-035      Antonio Brooks                 00779     
TC-CHECKOUT-036      Jason Wells                    44398     
TC-CHECKOUT-037      Jessica Shields                54866     
TC-CHECKOUT-038      Thomas Huerta                  30627     
TC-CHECKOUT-039      Lindsay Barber                 36562     
TC-CHECKOUT-040      Gerald Chavez                  96138     
TC-CHECKOUT-041      Alexandra Dawson               43322     
TC-CHECKOUT-042      David Edwards                  74829     
TC-CHECKOUT-043      Nicole Chen                    30938     
TC-CHECKOUT-044      Beth Holland                   03778     
TC-CHECKOUT-045      Michelle Young                 44952     
TC-CHECKOUT-046      Daniel Martinez                91811     
TC-CHECKOUT-047      Laura Bradley                  34804     
TC-CHECKOUT-048      Christina Mitchell             73218     
TC-CHECKOUT-049      Keith Frye                     68588     
TC-CHECKOUT-050      Jeanne Farmer                  58678     

✅ Successfully read 50 records from CSV

## Read JSON Output

Reading test data from JSON...

Loaded 50 test cases:

Test ID: TC-CHECKOUT-001
  Name: Michelle Floyd
  Zip: 44114
  Priority: P2

Test ID: TC-CHECKOUT-002
  Name: Danielle Garrett
  Zip: 59664
  Priority: P2

Test ID: TC-CHECKOUT-003
  Name: Cynthia Ward
  Zip: 49927
  Priority: P2

Test ID: TC-CHECKOUT-004
  Name: Albert Nguyen
  Zip: 23420
  Priority: P2

Test ID: TC-CHECKOUT-005
  Name: Christopher Chavez
  Zip: 11228
  Priority: P2

✅ Successfully read 50 records from JSON

Real QA Use Case
CSV vs JSON - When to use which?

CSV:
Use CSV when I want data that is easy to view/edit by humans (Excel/Google Sheets), or when sharing test datasets with non-technical teammates.

JSON:
Use JSON when I want structured data for automation, API payloads, configuration files, or when tests need nested/typed fields.

How I would use these files in real testing:
I would generate a dataset once, save it to CSV for easy review, and use JSON in scripts (or automation frameworks) to feed test runs with consistent test data.

Code Explanation

What does csv.DictWriter(csvfile, fieldnames=fieldnames) do?
It creates a CSV writer that takes dictionaries and writes them into columns matching fieldnames.

What does json.dump(data, jsonfile, indent=2) do?
It writes Python objects (list/dict) into a JSON file. indent=2 formats it to be readable.

Why use with open(filename, 'w') as csvfile:?
Because it automatically closes the file after writing (prevents file locks/leaks and is safer).