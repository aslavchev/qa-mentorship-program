## Module: Login / Authentication

### TC-LOGIN-001: Verify login with valid credentials (standard_user)

| Field | Value |
|------|-------|
| **Test Case ID** | TC-LOGIN-001 |
| **Module** | Login |
| **Test Type** | Smoke |
| **Severity** | S1-Critical |

**Test Objective:**  
Verify that a user with valid credentials can successfully log in and access the inventory page.

**Preconditions:**  
- SauceDemo application is accessible  
- User exists: standard_user / secret_sauce  
- User is logged out  

**Test Data:**  
- Username: standard_user  
- Password: secret_sauce  

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|----|--------|----------------|
| 1 | Navigate to https://www.saucedemo.com | Login page is displayed |
| 2 | Enter "standard_user" in Username field | Username is entered |
| 3 | Enter "secret_sauce" in Password field | Password is masked |
| 4 | Click LOGIN button | User is redirected to inventory page |

---

### TC-LOGIN-002: Verify login with valid credentials (problem_user)

| Field | Value |
|------|-------|
| **Test Case ID** | TC-LOGIN-002 |
| **Module** | Login |
| **Test Type** | Functional |
| **Severity** | S2-Major |

**Test Objective:**  
Verify that another valid user can log in successfully.

**Preconditions:**  
- SauceDemo application is accessible  
- User exists: problem_user / secret_sauce  

**Test Data:**  
- Username: problem_user  
- Password: secret_sauce  

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|----|--------|----------------|
| 1 | Navigate to login page | Login page is displayed |
| 2 | Enter valid credentials | Data is entered |
| 3 | Click LOGIN | Inventory page is displayed |

---

### TC-LOGIN-003: Verify login fails with invalid username

| Field | Value |
|------|-------|
| **Test Case ID** | TC-LOGIN-003 |
| **Module** | Login |
| **Test Type** | Negative |
| **Severity** | S1-Critical |

**Test Objective:**  
Verify that login fails when an invalid username is used.

**Test Data:**  
- Username: invalid_user  
- Password: secret_sauce  

**Expected Result:**  
Error message is displayed and user is not logged in.

---

### TC-LOGIN-004: Verify login fails with invalid password

| Field | Value |
|------|-------|
| **Test Case ID** | TC-LOGIN-004 |
| **Module** | Login |
| **Test Type** | Negative |
| **Severity** | S1-Critical |

**Test Data:**  
- Username: standard_user  
- Password: wrong_pass  

**Expected Result:**  
Login fails with error message.

---

### TC-LOGIN-005: Verify login fails with empty username

| Field | Value |
|------|-------|
| **Test Case ID** | TC-LOGIN-005 |
| **Module** | Login |
| **Test Type** | Negative |
| **Severity** | S2-Major |

**Expected Result:**  
Validation error for missing username is shown.

---

### TC-LOGIN-006: Verify login fails with empty password

| Field | Value |
|------|-------|
| **Test Case ID** | TC-LOGIN-006 |
| **Module** | Login |
| **Test Type** | Negative |
| **Severity** | S2-Major |

**Expected Result:**  
Validation error for missing password is shown.

---

### TC-LOGIN-007: Verify login fails with empty username and password

| Field | Value |
|------|-------|
| **Test Case ID** | TC-LOGIN-007 |
| **Module** | Login |
| **Test Type** | Negative |
| **Severity** | S2-Major |

**Expected Result:**  
User is not logged in and error message is displayed.

---

### TC-LOGIN-008: Verify locked user cannot login

| Field | Value |
|------|-------|
| **Test Case ID** | TC-LOGIN-008 |
| **Module** | Login |
| **Test Type** | Security |
| **Severity** | S1-Critical |

**Test Data:**  
- Username: locked_out_user  
- Password: secret_sauce  

**Expected Result:**  
Error message indicates user is locked out.

---

### TC-LOGIN-009: Verify login with special characters in username

| Field | Value |
|------|-------|
| **Test Case ID** | TC-LOGIN-009 |
| **Module** | Login |
| **Test Type** | Negative |
| **Severity** | S3-Minor |

**Test Data:**  
- Username: !@#$  
- Password: secret_sauce  

**Expected Result:**  
Login fails with validation error.

---

### TC-LOGIN-010: Verify login fails with SQL injection attempt

| Field | Value |
|------|-------|
| **Test Case ID** | TC-LOGIN-010 |
| **Module** | Login |
| **Test Type** | Security |
| **Severity** | S1-Critical |

**Test Data:**  
- Username: ' OR '1'='1  
- Password: anything  

**Expected Result:**  
Login fails and input is handled securely.

---

### TC-LOGIN-011: Verify password field is masked

| Field | Value |
|------|-------|
| **Test Case ID** | TC-LOGIN-011 |
| **Module** | Login |
| **Test Type** | UI |
| **Severity** | S3-Minor |

**Expected Result:**  
Password characters are hidden.

---

### TC-LOGIN-012: Verify login button is clickable

| Field | Value |
|------|-------|
| **Test Case ID** | TC-LOGIN-012 |
| **Module** | Login |
| **Test Type** | UI |
| **Severity** | S4-Trivial |

**Expected Result:**  
Login button can be clicked.

---

### TC-LOGIN-013: Verify error message for invalid credentials

| Field | Value |
|------|-------|
| **Test Case ID** | TC-LOGIN-013 |
| **Module** | Login |
| **Test Type** | Negative |
| **Severity** | S2-Major |

**Expected Result:**  
Correct error message is displayed.

---

### TC-LOGIN-014: Verify successful logout

| Field | Value |
|------|-------|
| **Test Case ID** | TC-LOGIN-014 |
| **Module** | Login |
| **Test Type** | Functional |
| **Severity** | S1-Critical |

**Expected Result:**  
User is logged out and redirected to login page.

---

### TC-LOGIN-015: Verify user cannot access inventory without login

| Field | Value |
|------|-------|
| **Test Case ID** | TC-LOGIN-015 |
| **Module** | Login |
| **Test Type** | Security |
| **Severity** | S1-Critical |

**Expected Result:**  
Unauthorized access is blocked and login page is shown.

## Module: Product Browsing / Inventory

### TC-PRODUCTS-001: Verify all products are displayed on inventory page

| Field | Value |
|------|-------|
| **Test Case ID** | TC-PRODUCTS-001 |
| **Module** | Products |
| **Test Type** | Smoke |
| **Severity** | S1-Critical |

**Test Objective:**  
Verify that all products are visible after successful login.

**Preconditions:**  
- User is logged in  
- Inventory page is opened  

**Expected Result:**  
All 6 products are displayed on the inventory page.

---

### TC-PRODUCTS-002: Verify product images are displayed

| Field | Value |
|------|-------|
| **Test Case ID** | TC-PRODUCTS-002 |
| **Module** | Products |
| **Test Type** | UI |
| **Severity** | S3-Minor |

**Expected Result:**  
Each product has a visible image.

---

### TC-PRODUCTS-003: Verify product names are displayed

| Field | Value |
|------|-------|
| **Test Case ID** | TC-PRODUCTS-003 |
| **Module** | Products |
| **Test Type** | UI |
| **Severity** | S3-Minor |

**Expected Result:**  
Each product displays a name.

---

### TC-PRODUCTS-004: Verify product prices are displayed

| Field | Value |
|------|-------|
| **Test Case ID** | TC-PRODUCTS-004 |
| **Module** | Products |
| **Test Type** | UI |
| **Severity** | S2-Major |

**Expected Result:**  
Each product displays a price.

---

### TC-SORT-001: Verify products can be sorted by name (A to Z)

| Field | Value |
|------|-------|
| **Test Case ID** | TC-SORT-001 |
| **Module** | Products |
| **Test Type** | Functional |
| **Severity** | S2-Major |

**Test Steps:**  
1. Open sort dropdown  
2. Select "Name (A to Z)"

**Expected Result:**  
Products are sorted alphabetically from A to Z.

---

### TC-SORT-002: Verify products can be sorted by name (Z to A)

| Field | Value |
|------|-------|
| **Test Case ID** | TC-SORT-002 |
| **Module** | Products |
| **Test Type** | Functional |
| **Severity** | S2-Major |

**Expected Result:**  
Products are sorted alphabetically from Z to A.

---

### TC-SORT-003: Verify products can be sorted by price (low to high)

| Field | Value |
|------|-------|
| **Test Case ID** | TC-SORT-003 |
| **Module** | Products |
| **Test Type** | Functional |
| **Severity** | S2-Major |

**Expected Result:**  
Products are sorted from lowest to highest price.

---

### TC-SORT-004: Verify products can be sorted by price (high to low)

| Field | Value |
|------|-------|
| **Test Case ID** | TC-SORT-004 |
| **Module** | Products |
| **Test Type** | Functional |
| **Severity** | S2-Major |

**Expected Result:**  
Products are sorted from highest to lowest price.

---

### TC-PRODUCTS-005: Verify product details page opens

| Field | Value |
|------|-------|
| **Test Case ID** | TC-PRODUCTS-005 |
| **Module** | Products |
| **Test Type** | Functional |
| **Severity** | S2-Major |

**Test Steps:**  
1. Click on a product name  

**Expected Result:**  
Product details page is displayed.

---

### TC-PRODUCTS-006: Verify back button returns to inventory page

| Field | Value |
|------|-------|
| **Test Case ID** | TC-PRODUCTS-006 |
| **Module** | Products |
| **Test Type** | Functional |
| **Severity** | S3-Minor |

**Expected Result:**  
User is returned to the inventory page.

## Module: Shopping Cart

### TC-CART-001: Verify item can be added to cart from inventory page

| Field | Value |
|------|-------|
| **Test Case ID** | TC-CART-001 |
| **Module** | Cart |
| **Test Type** | Smoke |
| **Severity** | S1-Critical |

**Test Objective:**  
Verify that a user can add a product to the cart from the inventory page.

**Preconditions:**  
- User is logged in  
- Inventory page is opened  

**Test Steps:**  
1. Click "Add to cart" button for a product  

**Expected Result:**  
- Product is added to cart  
- Cart badge shows quantity "1"

---

### TC-CART-002: Verify item can be added to cart from product details page

| Field | Value |
|------|-------|
| **Test Case ID** | TC-CART-002 |
| **Module** | Cart |
| **Test Type** | Functional |
| **Severity** | S2-Major |

**Expected Result:**  
Product is added to cart from product details page.

---

### TC-CART-003: Verify cart badge updates when item is added

| Field | Value |
|------|-------|
| **Test Case ID** | TC-CART-003 |
| **Module** | Cart |
| **Test Type** | UI |
| **Severity** | S2-Major |

**Expected Result:**  
Cart badge displays correct number of added items.

---

### TC-CART-004: Verify cart displays added item

| Field | Value |
|------|-------|
| **Test Case ID** | TC-CART-004 |
| **Module** | Cart |
| **Test Type** | Functional |
| **Severity** | S2-Major |

**Test Steps:**  
1. Navigate to cart page  

**Expected Result:**  
Added item is listed in the cart.

---

### TC-CART-005: Verify item can be removed from cart

| Field | Value |
|------|-------|
| **Test Case ID** | TC-CART-005 |
| **Module** | Cart |
| **Test Type** | Functional |
| **Severity** | S2-Major |

**Test Steps:**  
1. Click "Remove" button for an item  

**Expected Result:**  
Item is removed from the cart.

---

### TC-CART-006: Verify cart badge updates when item is removed

| Field | Value |
|------|-------|
| **Test Case ID** | TC-CART-006 |
| **Module** | Cart |
| **Test Type** | UI |
| **Severity** | S3-Minor |

**Expected Result:**  
Cart badge decreases or disappears when item is removed.

---

### TC-CART-007: Verify multiple different items can be added to cart

| Field | Value |
|------|-------|
| **Test Case ID** | TC-CART-007 |
| **Module** | Cart |
| **Test Type** | Functional |
| **Severity** | S2-Major |

**Expected Result:**  
Multiple different items are displayed in the cart.

---

### TC-CART-008: Verify same item cannot be added twice

| Field | Value |
|------|-------|
| **Test Case ID** | TC-CART-008 |
| **Module** | Cart |
| **Test Type** | Negative |
| **Severity** | S3-Minor |

**Expected Result:**  
Same item cannot be added twice to the cart.

---

### TC-CART-009: Verify cart retains items after page navigation

| Field | Value |
|------|-------|
| **Test Case ID** | TC-CART-009 |
| **Module** | Cart |
| **Test Type** | Regression |
| **Severity** | S2-Major |

**Expected Result:**  
Items remain in the cart after navigating between pages.

---

### TC-CART-010: Verify empty cart is displayed correctly

| Field | Value |
|------|-------|
| **Test Case ID** | TC-CART-010 |
| **Module** | Cart |
| **Test Type** | UI |
| **Severity** | S3-Minor |

**Expected Result:**  
Cart page shows no items when cart is empty.

---

### TC-CART-011: Verify Continue Shopping button returns to inventory page

| Field | Value |
|------|-------|
| **Test Case ID** | TC-CART-011 |
| **Module** | Cart |
| **Test Type** | Functional |
| **Severity** | S3-Minor |

**Expected Result:**  
User is redirected to inventory page.

---

### TC-CART-012: Verify Checkout button navigates to checkout page

| Field | Value |
|------|-------|
| **Test Case ID** | TC-CART-012 |
| **Module** | Cart |
| **Test Type** | Smoke |
| **Severity** | S1-Critical |

**Expected Result:**  
User is redirected to checkout information page.

---

### TC-CART-013: Verify cart with minimum items (1 item)

| Field | Value |
|------|-------|
| **Test Case ID** | TC-CART-013 |
| **Module** | Cart |
| **Test Type** | Boundary |
| **Severity** | S2-Major |

**Expected Result:**  
Cart displays correctly with one item.

---

### TC-CART-014: Verify cart with maximum items (6 items)

| Field | Value |
|------|-------|
| **Test Case ID** | TC-CART-014 |
| **Module** | Cart |
| **Test Type** | Boundary |
| **Severity** | S2-Major |

**Expected Result:**  
Cart displays correctly with all available items.

---

### TC-CART-015: Verify cart state transitions correctly

| Field | Value |
|------|-------|
| **Test Case ID** | TC-CART-015 |
| **Module** | Cart |
| **Test Type** | State Transition |
| **Severity** | S2-Major |

**Expected Result:**  
Cart transitions correctly from empty → items added → checkout.

## Module: Checkout

### TC-CHECKOUT-001: Verify checkout with valid information

| Field | Value |
|------|-------|
| **Test Case ID** | TC-CHECKOUT-001 |
| **Module** | Checkout |
| **Test Type** | Smoke |
| **Severity** | S1-Critical |

**Test Objective:**  
Verify that user can complete checkout with valid information.

**Preconditions:**  
- User is logged in  
- At least one item is added to cart  
- Cart page is opened  

**Test Steps:**  
1. Click "Checkout" button  
2. Enter valid First Name  
3. Enter valid Last Name  
4. Enter valid Zip Code  
5. Click "Continue"  

**Expected Result:**  
User is navigated to checkout overview page.

---

### TC-CHECKOUT-002: Verify checkout fails with empty first name

| Field | Value |
|------|-------|
| **Test Case ID** | TC-CHECKOUT-002 |
| **Module** | Checkout |
| **Test Type** | Negative |
| **Severity** | S2-Major |

**Expected Result:**  
Error message is displayed for missing first name.

---

### TC-CHECKOUT-003: Verify checkout fails with empty last name

| Field | Value |
|------|-------|
| **Test Case ID** | TC-CHECKOUT-003 |
| **Module** | Checkout |
| **Test Type** | Negative |
| **Severity** | S2-Major |

**Expected Result:**  
Error message is displayed for missing last name.

---

### TC-CHECKOUT-004: Verify checkout fails with empty zip code

| Field | Value |
|------|-------|
| **Test Case ID** | TC-CHECKOUT-004 |
| **Module** | Checkout |
| **Test Type** | Negative |
| **Severity** | S2-Major |

**Expected Result:**  
Error message is displayed for missing zip code.

---

### TC-CHECKOUT-005: Verify checkout fails with all fields empty

| Field | Value |
|------|-------|
| **Test Case ID** | TC-CHECKOUT-005 |
| **Module** | Checkout |
| **Test Type** | Negative |
| **Severity** | S2-Major |

**Expected Result:**  
Validation error message is displayed.

---

### TC-CHECKOUT-006: Verify checkout with maximum length first name

| Field | Value |
|------|-------|
| **Test Case ID** | TC-CHECKOUT-006 |
| **Module** | Checkout |
| **Test Type** | Boundary |
| **Severity** | S3-Minor |

**Expected Result:**  
First name field accepts maximum allowed characters.

---

### TC-CHECKOUT-007: Verify checkout with maximum length last name

| Field | Value |
|------|-------|
| **Test Case ID** | TC-CHECKOUT-007 |
| **Module** | Checkout |
| **Test Type** | Boundary |
| **Severity** | S3-Minor |

**Expected Result:**  
Last name field accepts maximum allowed characters.

---

### TC-CHECKOUT-008: Verify checkout with maximum length zip code

| Field | Value |
|------|-------|
| **Test Case ID** | TC-CHECKOUT-008 |
| **Module** | Checkout |
| **Test Type** | Boundary |
| **Severity** | S3-Minor |

**Expected Result:**  
Zip code field accepts maximum allowed characters.

---

### TC-CHECKOUT-009: Verify checkout accepts special characters in name

| Field | Value |
|------|-------|
| **Test Case ID** | TC-CHECKOUT-009 |
| **Module** | Checkout |
| **Test Type** | Validation |
| **Severity** | S3-Minor |

**Expected Result:**  
Name with special characters is accepted.

---

### TC-CHECKOUT-010: Verify Cancel button returns to cart page

| Field | Value |
|------|-------|
| **Test Case ID** | TC-CHECKOUT-010 |
| **Module** | Checkout |
| **Test Type** | Functional |
| **Severity** | S3-Minor |

**Expected Result:**  
User is redirected back to cart page.

---

### TC-CHECKOUT-011: Verify overview page displays selected items

| Field | Value |
|------|-------|
| **Test Case ID** | TC-CHECKOUT-011 |
| **Module** | Checkout |
| **Test Type** | Functional |
| **Severity** | S2-Major |

**Expected Result:**  
All selected items are displayed on overview page.

---

### TC-CHECKOUT-012: Verify overview page displays correct total price

| Field | Value |
|------|-------|
| **Test Case ID** | TC-CHECKOUT-012 |
| **Module** | Checkout |
| **Test Type** | Functional |
| **Severity** | S2-Major |

**Expected Result:**  
Total price equals sum of item prices.

---

### TC-CHECKOUT-013: Verify tax is calculated correctly

| Field | Value |
|------|-------|
| **Test Case ID** | TC-CHECKOUT-013 |
| **Module** | Checkout |
| **Test Type** | Calculation |
| **Severity** | S2-Major |

**Expected Result:**  
Tax amount is calculated and displayed correctly.

---

### TC-CHECKOUT-014: Verify Finish button completes the order

| Field | Value |
|------|-------|
| **Test Case ID** | TC-CHECKOUT-014 |
| **Module** | Checkout |
| **Test Type** | Smoke |
| **Severity** | S1-Critical |

**Expected Result:**  
Order is completed successfully.

---

### TC-CHECKOUT-015: Verify order confirmation page is displayed

| Field | Value |
|------|-------|
| **Test Case ID** | TC-CHECKOUT-015 |
| **Module** | Checkout |
| **Test Type** | UI |
| **Severity** | S2-Major |

**Expected Result:**  
Confirmation page is displayed after order completion.

---

### TC-CHECKOUT-016: Verify confirmation message is shown

| Field | Value |
|------|-------|
| **Test Case ID** | TC-CHECKOUT-016 |
| **Module** | Checkout |
| **Test Type** | UI |
| **Severity** | S3-Minor |

**Expected Result:**  
Success message is visible to the user.

---

### TC-CHECKOUT-017: Verify Back Home button returns to inventory page

| Field | Value |
|------|-------|
| **Test Case ID** | TC-CHECKOUT-017 |
| **Module** | Checkout |
| **Test Type** | Functional |
| **Severity** | S3-Minor |

**Expected Result:**  
User is redirected to inventory page.

---

### TC-CHECKOUT-018: Verify cart is empty after order completion

| Field | Value |
|------|-------|
| **Test Case ID** | TC-CHECKOUT-018 |
| **Module** | Checkout |
| **Test Type** | Regression |
| **Severity** | S2-Major |

**Expected Result:**  
Cart is empty after order is completed.

---

### TC-CHECKOUT-019: Verify user cannot access checkout without items

| Field | Value |
|------|-------|
| **Test Case ID** | TC-CHECKOUT-019 |
| **Module** | Checkout |
| **Test Type** | Negative |
| **Severity** | S2-Major |

**Expected Result:**  
Checkout cannot be started with empty cart.

---

### TC-CHECKOUT-020: Verify end-to-end checkout flow

| Field | Value |
|------|-------|
| **Test Case ID** | TC-CHECKOUT-020 |
| **Module** | Checkout |
| **Test Type** | E2E |
| **Severity** | S0-Blocker |

**Expected Result:**  
User can complete full flow: login → add item → checkout → order confirmation.
