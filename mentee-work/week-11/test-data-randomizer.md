# Week 11 - Exercise 5: Complete Test Data Script

**Your Name:** Kamen Asenov  
**Date:** 2026-01-26  

---

## Script Output

Generating SauceDemo checkout test data...

✅ CSV: Saved 60 records to saucedemo_checkout_tests.csv
✅ JSON: Saved 60 records to saucedemo_checkout_tests.json

======================================================================
SAUCEDEMO CHECKOUT TEST DATA - GENERATION SUMMARY
======================================================================

📊 Statistics:
   Random Test Cases: 50
   Edge Cases: 10
   Total Records: 60

📌 Priority Distribution:
   P1 (High): 4
   P2 (Medium): 56

💾 Files Created:
   saucedemo_checkout_tests.csv
   saucedemo_checkout_tests.json

✅ Ready for testing!

Generated Files

saucedemo_checkout_tests.csv (60 records)

saucedemo_checkout_tests.json (60 records)

## CSV Sample (First 10 rows)

test_id,category,first_name,last_name,zip_code,expected_result,priority,status
TC-CHECKOUT-001,Random,Steven,Taylor,60097,Order placed successfully,P2,Not Executed
TC-CHECKOUT-002,Random,Matthew,Thomas,52997,Order placed successfully,P2,Not Executed
TC-CHECKOUT-003,Random,Ashley,Casey,33866,Order placed successfully,P2,Not Executed
TC-CHECKOUT-004,Random,Veronica,Glass,32928,Order placed successfully,P2,Not Executed
TC-CHECKOUT-005,Random,Kelly,Simmons,63958,Order placed successfully,P2,Not Executed
TC-CHECKOUT-006,Random,Valerie,Rivera,78304,Order placed successfully,P2,Not Executed
TC-CHECKOUT-007,Random,Kelly,Nguyen,90768,Order placed successfully,P2,Not Executed
TC-CHECKOUT-008,Random,James,Cunningham,72132,Order placed successfully,P2,Not Executed
TC-CHECKOUT-009,Random,John,Zamora,20900,Order placed successfully,P2,Not Executed
TC-CHECKOUT-010,Random,Catherine,Short,02601,Order placed successfully,P2,Not Executed

## JSON Metadata

"metadata": {
    "generated_at": "2026-02-08T15:59:32",
    "total_tests": 60,
    "generator": "test_data_master.py",
    "application": "SauceDemo",
    "module": "Checkout"
  },

## Verification

CSV: 60 records loaded
JSON: 60 records loaded
Generated at: 2026-02-08T15:59:32

✅ Both files verified successfully!

Production-Ready Features

What makes this script production-ready?

Generates both Random + Edge Case datasets to increase coverage.

Saves output to both CSV (Excel-friendly) and JSON (automation/API-friendly).

JSON includes metadata (timestamp, counts, generator) for traceability.

Uses UTF-8 + ensure_ascii=False to safely store international characters.

Clear, readable summary output (quick “QA report” after generation).

How would you improve this script further?

Add CLI arguments (count, output filenames).

Add schema validation (e.g., ensure zip not empty for “success” expected results).

Add deterministic mode via seed for reproducible runs.

Add automated unit tests for generator functions.

Real-World Usage

Scenario: You need to test SauceDemo checkout 100 times with different data.

Without this script:

Manually create data sets, copy/paste into form.

High risk of duplicated data and human errors.

Time cost: ~1–2 hours for 50+ records.

With this script:

Generate 60 records instantly (or adjust for 100).

Reuse the same dataset across sessions or share with team.

Time cost: seconds.

Time saved:

Manual: ~120 minutes

Script: ~10 seconds

Savings: ~119+ minutes

Portfolio Piece

Could you show this in a FAANG interview?
Yes — it demonstrates solving a real QA pain point (test data generation), producing reusable artifacts (CSV/JSON), and adding traceability (metadata).

What would you explain to an interviewer?

“I built a small generator that creates realistic + edge-case checkout datasets, exports them to CSV and JSON, and prints a summary. This reduces manual data creation and improves coverage for validation and localization scenarios.”

