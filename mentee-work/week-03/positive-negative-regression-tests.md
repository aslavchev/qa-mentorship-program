**Week 3 – Exercises 3, 4, 5**  
(Combined, because they are related)

**Exercise 3: Positive Test Cases (15 total)**

**Login – Positive Tests (3)**

| ID | Test Case | Steps | Expected Result |
|----|-----------|--------|------------------|
| POS-LOGIN-01 | Login with valid standard user | 1. Open site 2. Enter `standard_user` 3. Enter valid password 4. Click Login | User is logged in and redirected to Products page |
| POS-LOGIN-02 | Login with valid locked-out scenario (visual check) | Enter `locked_out_user` and valid password | User receives correct locked-out message |
| POS-LOGIN-03 | Login page loads properly | Open login page | Username, password fields and login button are visible |


**Product Catalog – Positive Tests (4)**

| ID | Test Case | Steps | Expected Result |
|----|-----------|--------|------------------|
| POS-PROD-01 | Products page loads after login | Login → Products | Product list and sort dropdown are visible |
| POS-PROD-02 | Add item to cart from list | Click “Add to cart” | Button becomes “Remove”, badge = 1 |
| POS-PROD-03 | Open product details | Click product title/image | Product details page opens |
| POS-PROD-04 | Sort products A→Z | Select “Name (A to Z)” | Products sorted alphabetically |


**Shopping Cart – Positive Tests (4)**

| ID | Test Case | Steps | Expected Result |
|----|-----------|--------|------------------|
| POS-CART-01 | Open cart page | Click cart icon | Cart page loads |
| POS-CART-02 | Remove item from cart | Add item to cart then Remove | Item disappears from cart |
| POS-CART-03 | Cart badge updates | Add 2 items | Badge shows 2 |
| POS-CART-04 | Continue shopping | Cart → Continue Shopping | User returns to Products |


**Checkout – Positive Tests (4)**

| ID | Test Case | Steps | Expected Result |
|----|-----------|--------|------------------|
| POS-CHK-01 | Start checkout | Add item → cart → Checkout | Information form loads |
| POS-CHK-02 | Complete order | Fill info → Continue → Finish | Order completes, thank-you page displayed |
| POS-CHK-03 | Price calculation | Add item → checkout | Total = item price + tax |
| POS-CHK-04 | Cancel checkout | Checkout → Cancel | User returns to cart |


**Exercise 4: Negative Test Cases (15 total)**

**Invalid Login Attempts (5)**

| ID | Test Case | Expected Result |
|----|-----------|------------------|
| NEG-LOGIN-01 | Empty username & password | Error: “Username is required” |
| NEG-LOGIN-02 | Valid username + empty password | Error: “Password is required” |
| NEG-LOGIN-03 | Empty username + valid password | Error: “Username is required” |
| NEG-LOGIN-04 | Wrong username + password | Error message shown |
| NEG-LOGIN-05 | Special characters in username | Error message shown |


**Checkout Form Validation (4)**

| ID | Test Case | Expected Result |
|----|-----------|------------------|
| NEG-CHK-01 | Empty First Name | Error: “First Name is required” |
| NEG-CHK-02 | Empty Last Name | Error: “Last Name is required” |
| NEG-CHK-03 | Empty Postal Code | Error: “Postal Code is required” |
| NEG-CHK-04 | Spaces only in fields | Field treated as empty → error |

**Boundary / Cart Conditions (3)**

| ID | Test Case | Expected Result |
|----|-----------|------------------|
| NEG-CART-01 | Remove item not in cart | No action, no errors |
| NEG-CART-02 | Add same item twice | Quantity stays 1 |
| NEG-CART-03 | Empty cart view | Cart shows empty state |


**Special Characters / Inputs (3)**

| ID | Test Case | Expected Result |
|----|-----------|------------------|
| NEG-SPEC-01 | First name only special characters | Validation error |
| NEG-SPEC-02 | Postal code contains letters | Validation error |
| NEG-SPEC-03 | Extremely long text (>100 chars) | Error or field prevents input |

**Exercise 5: Regression Checklist**

**SauceDemo Regression Checklist**

**General**
- [ ] App loads without errors  
- [ ] Navigation works between all pages  

**Login**
- [ ] Valid login works  
- [ ] Error messages for invalid data  
- [ ] Logout works  

**Products Page**
- [ ] Product list loads  
- [ ] Add/remove cart from list works  
- [ ] Product details open  
- [ ] Sorting works  

**Shopping Cart**
- [ ] Cart badge updates  
- [ ] Remove works  
- [ ] Cart loads normally  
- [ ] Continue Shopping works  

**Checkout**
- [ ] Required field validation  
- [ ] Total price is correct  
- [ ] Successful order flow works  
- [ ] Cancel works correctly  

**Post-Order**
- [ ] Thank you page loads  
- [ ] Back Home returns to products  
