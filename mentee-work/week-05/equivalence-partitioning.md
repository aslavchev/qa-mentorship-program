# Week 5 — Exercise 1: Equivalence Partitioning

## Objective  
Apply Equivalence Partitioning (EP) to input fields in SauceDemo.

## Scope
- Login form (username & password)
- Checkout form (first name, last name, postal code)

---

# Login Form — Username

## Partitions
| Partition Type | Example Value | Expected Result |
|----------------|---------------|-----------------|
| Valid user | `standard_user` | Login success |
| Locked user | `locked_out_user` | Error: User locked |
| Invalid user | `wrong_user` | Error: Invalid credentials |
| Empty | `""` | Error: Username required |

## Test Cases
- EP-1: `standard_user` → success  
- EP-2: `locked_out_user` → locked error  
- EP-3: `wrong_user` → invalid credentials  
- EP-4: `""` → username required  

---

# Login Form — Password

## Partitions
| Partition Type | Example | Expected |
|----------------|---------|----------|
| Valid password | `secret_sauce` | Success (if username valid) |
| Invalid | `abc123` | Invalid credentials |
| Empty | `""` | Error: Password required |

---

# Checkout Form

Fields:  
✔ First Name  
✔ Last Name  
✔ Zip Code  

## Partitions
| Field | Valid | Invalid | Empty |
|-------|--------|---------|-------|
| First Name | `"Kamen"` | `"123"` | `""` |
| Last Name | `"Asenov"` | `"!@#"` | `""` |
| Zip Code | `"11111"` | `"abc"` | `""` |

## Representative Tests
- EP-10: All valid → Proceed to overview  
- EP-11: First name empty → Error  
- EP-12: Last name empty → Error  
- EP-13: Zip empty → Error  

---

## Summary
EP identifies logical input groups and reduces test cases while ensuring coverage.
