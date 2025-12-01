# Decision Tables – SauceDemo  

## 1. Objective
Create decision tables for SauceDemo to understand how different input combinations affect system behavior.

## 2. Scenario Chosen  
**Checkout Form Validation (First Name, Last Name, Zip Code)**  

## 3. Conditions and Actions

### Conditions
1. **C1: First Name provided?** (Yes / No)  
2. **C2: Last Name provided?** (Yes / No)  
3. **C3: Zip Code provided?** (Yes / No)

### Actions
1. **A1: Checkout continues successfully**
2. **A2: Error message shown**

## 4. Full Decision Table

| Rule | First Name | Last Name | Zip Code | Expected Result |
|------|------------|-----------|----------|-----------------|
| R1 | Yes | Yes | Yes | Success – user proceeds to next page |
| R2 | No | Yes | Yes | Error: First Name is required |
| R3 | Yes | No | Yes | Error: Last Name is required |
| R4 | Yes | Yes | No | Error: Zip Code is required |
| R5 | No | No | No | Error: All fields are required |

## 5. Reduced/Optimized Decision Table
(no duplicate outcomes — each rule unique)

| Test Case | C1 First Name | C2 Last Name | C3 Zip Code | Result |
|-----------|----------------|---------------|---------------|--------|
| TC1 | Valid | Valid | Valid | Success |
| TC2 | Empty | Valid | Valid | Error: First Name required |
| TC3 | Valid | Empty | Valid | Error: Last Name required |
| TC4 | Valid | Valid | Empty | Error: Zip Code required |
| TC5 | Empty | Empty | Empty | Error: All fields required |

## 6. Test Cases Derived from Decision Table

### **TC1 – All Valid**
- First Name: "Kamen"
- Last Name: "Asenov"
- Zip: "12345"  
**Expected:** User moves to "Checkout Overview" page.

### **TC2 – Missing First Name**
- First Name: ""  
- Last Name: "Asenov"
- Zip: "12345"  
**Expected:** Error message: *"Error: First Name is required"*

### **TC3 – Missing Last Name**
- First Name: "Kamen"  
- Last Name: ""  
- Zip: "12345"  
**Expected:** Error message: *"Error: Last Name is required"*

### **TC4 – Missing Zip Code**
- First Name: "Kamen"  
- Last Name: "Asenov"  
- Zip: ""  
**Expected:** Error message: *"Error: Postal Code is required"*

### **TC5 – All Fields Empty**
- First Name: ""  
- Last Name: ""  
- Zip: ""  
**Expected:** Error message: *"Error: First Name is required"* (this is the first missing field)

## 7. Summary
- Created a decision table with 3 input conditions and 5 rules.
- Converted rules into clear test cases.
- Used real behavior from SauceDemo checkout validation.
- Followed the Week 5 structured method.