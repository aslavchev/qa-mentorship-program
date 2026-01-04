## Module: Login / Authentication

## TC-LOGIN-001: Verify login with valid credentials (standard_user)

| Field | Value |
|------|------|
| **Test Case ID** | TC-LOGIN-001 |
| **Module** | Login |
| **Test Type** | Smoke |
| **Severity** | S1 – Critical |

**Test Objective:**  
Verify that a user can successfully log in with valid credentials and is redirected to the inventory page.

**Preconditions:**
- SauceDemo application is accessible
- User is logged out
- Browser cache and cookies are cleared

**Test Data:**
- Username: `standard_user`
- Password: `secret_sauce`
- Expected URL: `/inventory.html`

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Navigate to https://www.saucedemo.com | Login page is displayed |
| 2 | Enter `standard_user` in Username field | Username text appears |
| 3 | Enter `secret_sauce` in Password field | Password is masked |
| 4 | Click Login button | User is redirected to inventory page, 6 products are visible |


---

## TC-LOGIN-002: Verify login with another valid user (problem_user)

| Field | Value |
|------|------|
| **Test Case ID** | TC-LOGIN-002 |
| **Module** | Login |
| **Test Type** | Functional |
| **Severity** | S1 – Critical |

**Test Objective:**  
Verify that user can log in using another valid account.

**Preconditions:**
- SauceDemo application is accessible
- User is logged out

**Test Data:**
- Username: `problem_user`
- Password: `secret_sauce`

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Navigate to login page | Login page loads |
| 2 | Enter `problem_user` in Username field | Username text appears |
| 3 | Enter `secret_sauce` in Password field | Password is masked |
| 4 | Click Login button | Inventory page is displayed |


---

## TC-LOGIN-003: Verify login fails with invalid username

| Field | Value |
|------|------|
| **Test Case ID** | TC-LOGIN-003 |
| **Module** | Login |
| **Test Type** | Negative |
| **Severity** | S2 – Major |

**Test Objective:**  
Verify that login fails when an invalid username is provided.

**Preconditions:**
- SauceDemo application is accessible
- User is logged out

**Test Data:**
- Username: `invalid_user`
- Password: `secret_sauce`

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Enter invalid username | Username text appears |
| 2 | Enter valid password | Password is masked |
| 3 | Click Login button | Error message is displayed |
| 4 | Observe error text | **"Epic sadface: Username and password do not match any user"** |


---

## TC-LOGIN-004: Verify login fails with invalid password

| Field | Value |
|------|------|
| **Test Case ID** | TC-LOGIN-004 |
| **Module** | Login |
| **Test Type** | Negative |
| **Severity** | S2 – Major |

**Test Objective:**  
Verify that login fails when an invalid password is used.

**Preconditions:**
- SauceDemo application is accessible
- User is logged out

**Test Data:**
- Username: `standard_user`
- Password: `wrong_password`

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Enter valid username | Username text appears |
| 2 | Enter invalid password | Password is masked |
| 3 | Click Login button | Error message is displayed |
| 4 | Observe error text | **"Epic sadface: Username and password do not match any user"** |


---

## TC-LOGIN-005: Verify login fails with empty username

| Field | Value |
|------|------|
| **Test Case ID** | TC-LOGIN-005 |
| **Module** | Login |
| **Test Type** | Negative |
| **Severity** | S2 – Major |

**Test Objective:**  
Verify that login fails when username field is empty.

**Preconditions:**
- SauceDemo application is accessible
- User is logged out

**Test Data:**
- Password: `secret_sauce`

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Leave Username field empty | Username field is empty |
| 2 | Enter password | Password is masked |
| 3 | Click Login button | Error message is displayed |
| 4 | Observe error text | **"Epic sadface: Username is required"** |


---

## TC-LOGIN-006: Verify login fails with empty password

| Field | Value |
|------|------|
| **Test Case ID** | TC-LOGIN-006 |
| **Module** | Login |
| **Test Type** | Negative |
| **Severity** | S2 – Major |

**Test Objective:**  
Verify that login fails when password field is empty.

**Preconditions:**
- SauceDemo application is accessible
- User is logged out

**Test Data:**
- Username: `standard_user`

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Enter valid username | Username text appears |
| 2 | Leave Password field empty | Password field is empty |
| 3 | Click Login button | Error message is displayed |
| 4 | Observe error text | **"Epic sadface: Password is required"** |


---

## TC-LOGIN-007: Verify login fails with empty username and password

| Field | Value |
|------|------|
| **Test Case ID** | TC-LOGIN-007 |
| **Module** | Login |
| **Test Type** | Negative |
| **Severity** | S2 – Major |

**Test Objective:**  
Verify that login fails when both username and password fields are empty.

**Preconditions:**
- SauceDemo application is accessible
- User is logged out

**Test Data:**  
N/A

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Leave Username field empty | Username field is empty |
| 2 | Leave Password field empty | Password field is empty |
| 3 | Click Login button | Error message is displayed |
| 4 | Observe error text | **"Epic sadface: Username is required"** |


---

## TC-LOGIN-008: Verify locked user cannot login

| Field | Value |
|------|------|
| **Test Case ID** | TC-LOGIN-008 |
| **Module** | Login |
| **Test Type** | Security |
| **Severity** | S1 – Critical |

**Test Objective:**  
Verify that a locked user cannot log in to the application.

**Preconditions:**
- SauceDemo application is accessible
- User is logged out

**Test Data:**
- Username: `locked_out_user`
- Password: `secret_sauce`

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Enter locked user username | Username text appears |
| 2 | Enter password | Password is masked |
| 3 | Click Login button | Error message is displayed |
| 4 | Observe error text | **"Epic sadface: Sorry, this user has been locked out."** |


---

## TC-LOGIN-009: Verify login with special characters in username

| Field | Value |
|------|------|
| **Test Case ID** | TC-LOGIN-009 |
| **Module** | Login |
| **Test Type** | Negative |
| **Severity** | S2 – Major |

**Test Objective:**  
Verify that login fails when special characters are used in username.

**Preconditions:**
- SauceDemo application is accessible
- User is logged out

**Test Data:**
- Username: `!@#$%^`
- Password: `secret_sauce`

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Enter special characters in Username field | Username text appears |
| 2 | Enter valid password | Password is masked |
| 3 | Click Login button | Error message is displayed |
| 4 | Observe error text | **"Epic sadface: Username and password do not match any user"** |


---

## TC-LOGIN-010: Verify login fails with SQL injection attempt

| Field | Value |
|------|------|
| **Test Case ID** | TC-LOGIN-010 |
| **Module** | Login |
| **Test Type** | Security |
| **Severity** | S0 – Blocker |

**Test Objective:**  
Verify that the login form is protected against SQL injection attacks.

**Preconditions:**
- SauceDemo application is accessible
- User is logged out

**Test Data:**
- Username: `' OR '1'='1`
- Password: `' OR '1'='1`

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Enter SQL injection payload in Username | Payload text appears |
| 2 | Enter SQL injection payload in Password | Password field accepts input |
| 3 | Click Login button | Login fails |
| 4 | Observe application behavior | Error message displayed, no login occurs |


---

## TC-LOGIN-011: Verify password field is masked

| Field | Value |
|------|------|
| **Test Case ID** | TC-LOGIN-011 |
| **Module** | Login |
| **Test Type** | UI |
| **Severity** | S3 – Minor |

**Test Objective:**  
Verify that the password field masks entered characters for security reasons.

**Preconditions:**
- SauceDemo application is accessible
- User is on login page
- User is logged out

**Test Data:**
- Password: `secret_sauce`

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Navigate to https://www.saucedemo.com | Login page is displayed |
| 2 | Click on Password field | Cursor is visible in password field |
| 3 | Enter `secret_sauce` | Characters are displayed as dots/asterisks |
| 4 | Observe the field | Actual password text is not visible |


---

## TC-LOGIN-012: Verify login button is clickable

| Field | Value |
|------|------|
| **Test Case ID** | TC-LOGIN-012 |
| **Module** | Login |
| **Test Type** | UI |
| **Severity** | S3 – Minor |

**Test Objective:**  
Verify that the Login button is enabled and clickable on the login page.

**Preconditions:**
- SauceDemo application is accessible
- User is on login page

**Test Data:**  
N/A

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Navigate to https://www.saucedemo.com | Login page loads successfully |
| 2 | Observe Login button | Login button is visible |
| 3 | Click Login button without entering credentials | Error message appears: **"Epic sadface: Username is required"** |


---

## TC-LOGIN-013: Verify error message for invalid credentials

| Field | Value |
|------|------|
| **Test Case ID** | TC-LOGIN-013 |
| **Module** | Login |
| **Test Type** | Negative |
| **Severity** | S2 – Major |

**Test Objective:**  
Verify that an appropriate error message is displayed when invalid credentials are used.

**Preconditions:**
- SauceDemo application is accessible
- User is logged out

**Test Data:**
- Username: `invalid_user`
- Password: `invalid_pass`

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Enter `invalid_user` in Username field | Username text appears |
| 2 | Enter `invalid_pass` in Password field | Password is masked |
| 3 | Click Login button | Error message is displayed |
| 4 | Observe error message | **"Epic sadface: Username and password do not match any user"** is shown |

---

## TC-LOGIN-014: Verify successful logout

| Field | Value |
|------|------|
| **Test Case ID** | TC-LOGIN-014 |
| **Module** | Login |
| **Test Type** | Functional |
| **Severity** | S1 – Critical |

**Test Objective:**  
Verify that a logged-in user can successfully log out from the application.

**Preconditions:**
- SauceDemo application is accessible
- User is logged in as `standard_user`

**Test Data:**  
N/A

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Click the menu (☰) button | Side menu opens |
| 2 | Click **Logout** | User is logged out |
| 3 | Observe current page | Login page is displayed |


---

## TC-LOGIN-015: Verify user cannot access inventory page without login

| Field | Value |
|------|------|
| **Test Case ID** | TC-LOGIN-015 |
| **Module** | Login |
| **Test Type** | Security |
| **Severity** | S1 – Critical |

**Test Objective:**  
Verify that unauthenticated users cannot access the inventory page directly via URL.

**Preconditions:**
- SauceDemo application is accessible
- User is logged out
- Browser cache and cookies are cleared

**Test Data:**
- URL: https://www.saucedemo.com/inventory.html

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Open browser | Browser opens successfully |
| 2 | Navigate directly to inventory URL | Access is denied |
| 3 | Observe current page | User is redirected to login page |

## TC-LOGIN-016: Verify login fails with XSS attempt in username field

| Field | Value |
|------|------|
| **Test Case ID** | TC-LOGIN-016 |
| **Module** | Login / Authentication |
| **Test Type** | Security |
| **Severity** | S1 – Critical |

**Test Objective:**  
Verify that the application prevents execution of XSS payload entered in the username field and displays a proper validation error.

**Preconditions:**
- SauceDemo application is accessible
- User is logged out
- Browser cache and cookies are cleared

**Test Data:**  
Username: `<script>alert('XSS')</script>`  
Password: `secret_sauce`

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Navigate to https://www.saucedemo.com | Login page is displayed |
| 2 | Enter `<script>alert('XSS')</script>` in Username field | Text is displayed as plain text |
| 3 | Enter `secret_sauce` in Password field | Password is masked |
| 4 | Click **Login** | Login fails |
| 5 | Observe application behavior | No alert popup appears |
| 6 | Observe error message | Error message displayed: **"Epic sadface: Username and password do not match any user"** |

**Security Validation:**  
- No JavaScript execution  
- No DOM manipulation  
- Input is sanitized and treated as text



## Module: Product Browsing / Inventory

## TC-PRODUCTS-001: Verify all products are displayed on inventory page

| Field | Value |
|------|------|
| **Test Case ID** | TC-PRODUCTS-001 |
| **Module** | Products |
| **Test Type** | Functional |
| **Severity** | S1 – Critical |

**Test Objective:**  
Verify that all available products are displayed on the inventory page after successful login.

**Preconditions:**
- SauceDemo application is accessible
- User is logged in as `standard_user`

**Test Data:**  
N/A

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Login with valid credentials | Inventory page is displayed |
| 2 | Observe product list | Exactly 6 products are displayed |


---

## TC-PRODUCTS-002: Verify product images are displayed

| Field | Value |
|------|------|
| **Test Case ID** | TC-PRODUCTS-002 |
| **Module** | Products |
| **Test Type** | UI |
| **Severity** | S3 – Minor |

**Test Objective:**  
Verify that each product has an associated image displayed on the inventory page.

**Preconditions:**
- User is logged in
- Inventory page is open

**Test Data:**  
N/A

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Observe product list | Each product has an image |
| 2 | Check image loading | No broken image icons are displayed |


---

## TC-PRODUCTS-003: Verify product names are visible

| Field | Value |
|------|------|
| **Test Case ID** | TC-PRODUCTS-003 |
| **Module** | Products |
| **Test Type** | UI |
| **Severity** | S2 – Major |

**Test Objective:**  
Verify that product names are clearly visible for each product.

**Preconditions:**
- User is logged in
- Inventory page is displayed

**Test Data:**  
N/A

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Observe product list | Each product has a visible name |


---

## TC-PRODUCTS-004: Verify product prices are displayed

| Field | Value |
|------|------|
| **Test Case ID** | TC-PRODUCTS-004 |
| **Module** | Products |
| **Test Type** | Functional |
| **Severity** | S1 – Critical |

**Test Objective:**  
Verify that each product displays a price on the inventory page.

**Preconditions:**
- User is logged in
- Inventory page is open

**Test Data:**  
N/A

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Observe product prices | Each product displays a price value |


---

## TC-SORT-001: Verify sorting by Name (A to Z)

| Field | Value |
|------|------|
| **Test Case ID** | TC-SORT-001 |
| **Module** | Products |
| **Test Type** | Functional |
| **Severity** | S2 – Major |

**Test Objective:**  
Verify that products can be sorted alphabetically from A to Z.

**Preconditions:**
- User is logged in
- Inventory page is displayed

**Test Data:**  
Sort option: Name (A to Z)

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Select "Name (A to Z)" from sort dropdown | Products reorder alphabetically |
| 2 | Observe first and last product | Names follow ascending order |


---

## TC-SORT-002: Verify sorting by Name (Z to A)

| Field | Value |
|------|------|
| **Test Case ID** | TC-SORT-002 |
| **Module** | Products |
| **Test Type** | Functional |
| **Severity** | S2 – Major |

**Test Objective:**  
Verify that products can be sorted alphabetically from Z to A.

**Preconditions:**
- User is logged in
- Inventory page is displayed

**Test Data:**  
Sort option: Name (Z to A)

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Select "Name (Z to A)" from sort dropdown | Products reorder in reverse alphabetical order |


---

## TC-SORT-003: Verify sorting by Price (low to high)

| Field | Value |
|------|------|
| **Test Case ID** | TC-SORT-003 |
| **Module** | Products |
| **Test Type** | Functional |
| **Severity** | S2 – Major |

**Test Objective:**  
Verify that products can be sorted by price from lowest to highest.

**Preconditions:**
- User is logged in
- Inventory page is displayed

**Test Data:**  
Sort option: Price (low to high)

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Select "Price (low to high)" | Cheapest product appears first |


---

## TC-SORT-004: Verify sorting by Price (high to low)

| Field | Value |
|------|------|
| **Test Case ID** | TC-SORT-004 |
| **Module** | Products |
| **Test Type** | Functional |
| **Severity** | S2 – Major |

**Test Objective:**  
Verify that products can be sorted by price from highest to lowest.

**Preconditions:**
- User is logged in
- Inventory page is displayed

**Test Data:**  
Sort option: Price (high to low)

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Select "Price (high to low)" | Most expensive product appears first |


---

## TC-PRODUCTS-005: Verify product detail page opens

| Field | Value |
|------|------|
| **Test Case ID** | TC-PRODUCTS-005 |
| **Module** | Products |
| **Test Type** | Functional |
| **Severity** | S2 – Major |

**Test Objective:**  
Verify that clicking on a product opens its detail page.

**Preconditions:**
- User is logged in
- Inventory page is displayed

**Test Data:**  
N/A

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Click on a product name | Product detail page opens |
| 2 | Observe product info | Name, image, description, price displayed |


---

## TC-PRODUCTS-006: Verify back button returns to inventory page

| Field | Value |
|------|------|
| **Test Case ID** | TC-PRODUCTS-006 |
| **Module** | Products |
| **Test Type** | Navigation |
| **Severity** | S3 – Minor |

**Test Objective:**  
Verify that the Back button on product detail page returns user to inventory page.

**Preconditions:**
- User is on product detail page

**Test Data:**  
N/A

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Click Back button | User is redirected to inventory page |


## Module: Shopping Cart

## TC-CART-001: Verify add item to cart from inventory page

| Field | Value |
|------|------|
| **Test Case ID** | TC-CART-001 |
| **Module** | Cart |
| **Test Type** | Functional |
| **Severity** | S1 – Critical |

**Test Objective:**  
Verify that a user can add a product to the shopping cart from the inventory page.

**Preconditions:**
- SauceDemo application is accessible
- User is logged in as `standard_user`
- Inventory page is displayed

**Test Data:**  
Product: Sauce Labs Backpack

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Click **Add to cart** for Sauce Labs Backpack | Button changes to **Remove** |
| 2 | Observe cart icon badge | Cart badge shows value **1** |


---

## TC-CART-002: Verify add item to cart from product detail page

| Field | Value |
|------|------|
| **Test Case ID** | TC-CART-002 |
| **Module** | Cart |
| **Test Type** | Functional |
| **Severity** | S1 – Critical |

**Test Objective:**  
Verify that a user can add a product to the cart from the product detail page.

**Preconditions:**
- User is logged in
- Inventory page is displayed

**Test Data:**  
Product: Sauce Labs Bike Light

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Click product name | Product detail page opens |
| 2 | Click **Add to cart** | Button changes to **Remove** |
| 3 | Observe cart badge | Cart badge shows **1** |

---

## TC-CART-003: Verify cart badge updates when item added

| Field | Value |
|------|------|
| **Test Case ID** | TC-CART-003 |
| **Module** | Cart |
| **Test Type** | UI |
| **Severity** | S2 – Major |

**Test Objective:**  
Verify that the cart icon badge updates correctly when items are added.

**Preconditions:**
- User is logged in
- Inventory page is displayed

**Test Data:**  
N/A

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Add one product to cart | Cart badge shows **1** |
| 2 | Add second product | Cart badge updates to **2** |


---

## TC-CART-004: Verify cart displays added items

| Field | Value |
|------|------|
| **Test Case ID** | TC-CART-004 |
| **Module** | Cart |
| **Test Type** | Functional |
| **Severity** | S1 – Critical |

**Test Objective:**  
Verify that items added to the cart are displayed correctly in the cart page.

**Preconditions:**
- User is logged in
- At least one item is added to cart

**Test Data:**  
N/A

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Click cart icon | Cart page opens |
| 2 | Observe cart contents | Added items are listed with name and price |


---

## TC-CART-005: Verify remove item from cart

| Field | Value |
|------|------|
| **Test Case ID** | TC-CART-005 |
| **Module** | Cart |
| **Test Type** | Functional |
| **Severity** | S1 – Critical |

**Test Objective:**  
Verify that a user can remove an item from the cart.

**Preconditions:**
- User is logged in
- Cart contains at least one item

**Test Data:**  
N/A

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Click **Remove** button for an item | Item is removed from cart |
| 2 | Observe cart badge | Badge value decreases |


---

## TC-CART-006: Verify cart badge updates when item removed

| Field | Value |
|------|------|
| **Test Case ID** | TC-CART-006 |
| **Module** | Cart |
| **Test Type** | UI |
| **Severity** | S2 – Major |

**Test Objective:**  
Verify that the cart badge updates correctly when an item is removed.

**Preconditions:**
- User is logged in
- Cart contains two items

**Test Data:**  
N/A

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Remove one item | Cart badge updates from **2** to **1** |


---

## TC-CART-007: Verify add multiple different items to cart

| Field | Value |
|------|------|
| **Test Case ID** | TC-CART-007 |
| **Module** | Cart |
| **Test Type** | Functional |
| **Severity** | S1 – Critical |

**Test Objective:**  
Verify that multiple different products can be added to the cart.

**Preconditions:**
- User is logged in
- Inventory page is displayed

**Test Data:**  
Products: Backpack, Bike Light, Bolt T-Shirt

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Add three different products | Cart badge shows **3** |
| 2 | Open cart | All three products are listed |


---

## TC-CART-008: Verify add same item twice is not allowed

| Field | Value |
|------|------|
| **Test Case ID** | TC-CART-008 |
| **Module** | Cart |
| **Test Type** | Negative |
| **Severity** | S2 – Major |

**Test Objective:**  
Verify that the same product cannot be added twice to the cart.

**Preconditions:**
- User is logged in
- Inventory page is displayed

**Test Data:**  
Product: Sauce Labs Backpack

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Add product to cart | Button changes to **Remove** |
| 2 | Attempt to add again | Quantity does not increase |


---

## TC-CART-009: Verify cart total calculation is correct

| Field | Value |
|------|------|
| **Test Case ID** | TC-CART-009 |
| **Module** | Cart |
| **Test Type** | Functional |
| **Severity** | S1 – Critical |

**Test Objective:**  
Verify that cart displays correct total price for added items.

**Preconditions:**
- User is logged in
- Multiple items added to cart

**Test Data:**  
Known product prices

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Open cart | All item prices are visible |
| 2 | Calculate sum manually | Sum matches displayed total |


---

## TC-CART-010: Verify cart persists across page navigation

| Field | Value |
|------|------|
| **Test Case ID** | TC-CART-010 |
| **Module** | Cart |
| **Test Type** | Regression |
| **Severity** | S2 – Major |

**Test Objective:**  
Verify that cart contents persist when navigating between pages.

**Preconditions:**
- User is logged in
- Item added to cart

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Navigate to another page | Cart badge remains unchanged |
| 2 | Return to cart | Item is still present |


---

## TC-CART-011: Verify empty cart displays correctly

| Field | Value |
|------|------|
| **Test Case ID** | TC-CART-011 |
| **Module** | Cart |
| **Test Type** | UI |
| **Severity** | S3 – Minor |

**Test Objective:**  
Verify that empty cart page displays correctly.

**Preconditions:**
- User is logged in
- Cart is empty

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Open cart | No items displayed, page loads correctly |


---

## TC-CART-012: Verify Continue Shopping button returns to inventory

| Field | Value |
|------|------|
| **Test Case ID** | TC-CART-012 |
| **Module** | Cart |
| **Test Type** | Navigation |
| **Severity** | S3 – Minor |

**Test Objective:**  
Verify Continue Shopping button navigates back to inventory page.

**Preconditions:**
- User is logged in
- Cart page is open

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Click **Continue Shopping** | Inventory page is displayed |


---

## TC-CART-013: Verify Checkout button navigates to checkout page

| Field | Value |
|------|------|
| **Test Case ID** | TC-CART-013 |
| **Module** | Cart |
| **Test Type** | Functional |
| **Severity** | S1 – Critical |

**Test Objective:**  
Verify Checkout button navigates user to checkout information page.

**Preconditions:**
- User is logged in
- Cart contains at least one item

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Click **Checkout** | Checkout information page opens |


---

## TC-CART-014: Verify cart with single item (minimum boundary)

| Field | Value |
|------|------|
| **Test Case ID** | TC-CART-014 |
| **Module** | Cart |
| **Test Type** | Boundary |
| **Severity** | S2 – Major |

**Test Objective:**  
Verify cart behavior with minimum number of items (1).

**Preconditions:**
- User is logged in
- One item added to cart

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Open cart | One item is displayed |


---

## TC-CART-015: Verify cart with all products added (maximum boundary)

| Field | Value |
|------|------|
| **Test Case ID** | TC-CART-015 |
| **Module** | Cart |
| **Test Type** | Boundary |
| **Severity** | S2 – Major |

**Test Objective:**  
Verify cart behavior when all available products are added.

**Preconditions:**
- User is logged in
- Inventory page is displayed

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Add all 6 products to cart | Cart badge shows **6** |
| 2 | Open cart | All products are listed |


## Module: Checkout

## TC-CHECKOUT-001: Verify checkout with valid information

| Field | Value |
|------|------|
| **Test Case ID** | TC-CHECKOUT-001 |
| **Module** | Checkout |
| **Test Type** | Functional |
| **Severity** | S0 – Blocker |

**Test Objective:**  
Verify that a user can successfully complete checkout when all required information is valid.

**Preconditions:**
- User is logged in as `standard_user`
- At least one item is added to the cart
- Cart page is open

**Test Data:**  
First Name: John  
Last Name: Doe  
ZIP Code: 12345

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Click **Checkout** | Checkout: Your Information page opens |
| 2 | Enter First Name | Text appears in field |
| 3 | Enter Last Name | Text appears in field |
| 4 | Enter ZIP Code | Text appears in field |
| 5 | Click **Continue** | Checkout Overview page opens |


---

## TC-CHECKOUT-002: Verify checkout fails with empty first name

| Field | Value |
|------|------|
| **Test Case ID** | TC-CHECKOUT-002 |
| **Module** | Checkout |
| **Test Type** | Negative |
| **Severity** | S1 – Critical |

**Test Objective:**  
Verify error message appears when first name is empty.

**Preconditions:**
- User is logged in
- Checkout information page is open

**Test Data:**  
First Name: (empty)  
Last Name: Doe  
ZIP Code: 12345

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Leave First Name empty | Field remains empty |
| 2 | Click **Continue** | Error message: **"Error: First Name is required"** |


---

## TC-CHECKOUT-003: Verify checkout fails with empty last name

| Field | Value |
|------|------|
| **Test Case ID** | TC-CHECKOUT-003 |
| **Module** | Checkout |
| **Test Type** | Negative |
| **Severity** | S1 – Critical |

**Test Objective:**  
Verify error message appears when last name is empty.

**Test Data:**  
First Name: John  
Last Name: (empty)  
ZIP Code: 12345

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Leave Last Name empty | Field remains empty |
| 2 | Click **Continue** | Error message: **"Error: Last Name is required"** |


---

## TC-CHECKOUT-004: Verify checkout fails with empty ZIP code

| Field | Value |
|------|------|
| **Test Case ID** | TC-CHECKOUT-004 |
| **Module** | Checkout |
| **Test Type** | Negative |
| **Severity** | S1 – Critical |

**Test Objective:**  
Verify error message appears when ZIP code is empty.

**Test Data:**  
First Name: John  
Last Name: Doe  
ZIP Code: (empty)

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Leave ZIP Code empty | Field remains empty |
| 2 | Click **Continue** | Error message: **"Error: Postal Code is required"** |


---

## TC-CHECKOUT-005: Verify checkout fails when all fields are empty

| Field | Value |
|------|------|
| **Test Case ID** | TC-CHECKOUT-005 |
| **Module** | Checkout |
| **Test Type** | Negative |
| **Severity** | S1 – Critical |

**Test Objective:**  
Verify that checkout validation prevents continuing when all required fields are empty.

**Preconditions:**
- User is logged in as `standard_user`
- At least one item is added to the cart
- Checkout: Your Information page is open

**Test Data:**  
First Name: (empty)  
Last Name: (empty)  
ZIP Code: (empty)

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Leave all input fields empty | Fields remain empty |
| 2 | Click **Continue** | Error message displayed: **"Error: First Name is required"** |


---

## TC-CHECKOUT-006: Verify checkout with maximum length first name

| Field | Value |
|------|------|
| **Test Case ID** | TC-CHECKOUT-006 |
| **Module** | Checkout |
| **Test Type** | Boundary |
| **Severity** | S2 – Major |

**Test Objective:**  
Verify that checkout accepts a first name with maximum allowed length.

**Preconditions:**
- User is logged in
- Checkout information page is open

**Test Data:**  
First Name: 50 characters (e.g. `AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA`)  
Last Name: Doe  
ZIP Code: 12345

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Enter 50-character first name | Text accepted in field |
| 2 | Enter valid last name and ZIP code | Text accepted |
| 3 | Click **Continue** | Checkout Overview page opens successfully |


---

## TC-CHECKOUT-007: Verify checkout with maximum length last name

| Field | Value |
|------|------|
| **Test Case ID** | TC-CHECKOUT-007 |
| **Module** | Checkout |
| **Test Type** | Boundary |
| **Severity** | S2 – Major |

**Test Objective:**  
Verify checkout works when last name is at maximum allowed length.

**Test Data:**  
First Name: John  
Last Name: 50 characters  
ZIP Code: 12345

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Enter valid first name | Text accepted |
| 2 | Enter 50-character last name | Text accepted |
| 3 | Click **Continue** | User navigates to Checkout Overview page |


---

## TC-CHECKOUT-008: Verify checkout with maximum length ZIP code

| Field | Value |
|------|------|
| **Test Case ID** | TC-CHECKOUT-008 |
| **Module** | Checkout |
| **Test Type** | Boundary |
| **Severity** | S2 – Major |

**Test Objective:**  
Verify checkout accepts ZIP code with maximum allowed length.

**Test Data:**  
First Name: John  
Last Name: Doe  
ZIP Code: 1234567890

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Enter ZIP code with 10 digits | ZIP code accepted |
| 2 | Click **Continue** | Checkout Overview page opens |


---

## TC-CHECKOUT-009: Verify checkout with special characters in name

| Field | Value |
|------|------|
| **Test Case ID** | TC-CHECKOUT-009 |
| **Module** | Checkout |
| **Test Type** | Functional |
| **Severity** | S2 – Major |

**Test Objective:**  
Verify checkout allows valid special characters in name fields.

**Test Data:**  
First Name: O'Brien  
Last Name: Smith  
ZIP Code: 12345

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Enter special characters in First Name | Text accepted |
| 2 | Complete remaining fields | Accepted |
| 3 | Click **Continue** | Checkout Overview page opens |


---

## TC-CHECKOUT-010: Verify Continue button navigates to overview page

| Field | Value |
|------|------|
| **Test Case ID** | TC-CHECKOUT-010 |
| **Module** | Checkout |
| **Test Type** | Navigation |
| **Severity** | S1 – Critical |

**Test Objective:**  
Verify Continue button correctly navigates user to checkout overview.

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Fill all required fields | Fields accepted |
| 2 | Click **Continue** | Checkout Overview page displayed |


---

## TC-CHECKOUT-011: Verify Cancel button returns to cart

| Field | Value |
|------|------|
| **Test Case ID** | TC-CHECKOUT-011 |
| **Module** | Checkout |
| **Test Type** | Navigation |
| **Severity** | S2 – Major |

**Test Objective:**  
Verify Cancel button returns user to cart page.

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Click **Cancel** | User redirected to Cart page |


---

## TC-CHECKOUT-012: Verify overview page displays correct items

| Field | Value |
|------|------|
| **Test Case ID** | TC-CHECKOUT-012 |
| **Module** | Checkout |
| **Test Type** | Functional |
| **Severity** | S1 – Critical |

**Test Objective:**  
Verify items in overview match items added to cart.

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Reach Checkout Overview page | Correct item names displayed |


---

## TC-CHECKOUT-013: Verify overview page displays correct total price

| Field | Value |
|------|------|
| **Test Case ID** | TC-CHECKOUT-013 |
| **Module** | Checkout |
| **Test Type** | Functional |
| **Severity** | S1 – Critical |

**Test Objective:**  
Verify item total equals sum of item prices.

**Expected Result:**  
Displayed total equals sum of product prices.


---

## TC-CHECKOUT-014: Verify tax calculation is displayed correctly

| Field | Value |
|------|------|
| **Test Case ID** | TC-CHECKOUT-014 |
| **Module** | Checkout |
| **Test Type** | Functional |
| **Severity** | S2 – Major |

**Test Objective:**  
Verify tax value is displayed and calculated correctly.

**Expected Result:**  
Tax is displayed and added to total price.


---

## TC-CHECKOUT-015: Verify Finish button completes the order

| Field | Value |
|------|------|
| **Test Case ID** | TC-CHECKOUT-015 |
| **Module** | Checkout |
| **Test Type** | Functional |
| **Severity** | S0 – Blocker |

**Test Objective:**  
Verify clicking Finish completes the order.

**Expected Result:**  
Order completion page displayed.


---

## TC-CHECKOUT-016: Verify order confirmation page is displayed

| Field | Value |
|------|------|
| **Test Case ID** | TC-CHECKOUT-016 |
| **Module** | Checkout |
| **Test Type** | UI |
| **Severity** | S1 – Critical |

**Expected Result:**  
Confirmation page with success message is visible.


---

## TC-CHECKOUT-017: Verify order confirmation message appears

| Field | Value |
|------|------|
| **Test Case ID** | TC-CHECKOUT-017 |
| **Module** | Checkout |
| **Test Type** | UI |
| **Severity** | S2 – Major |

**Expected Result:**  
Message **"THANK YOU FOR YOUR ORDER"** is displayed.


---

## TC-CHECKOUT-018: Verify Back Home button returns to inventory

| Field | Value |
|------|------|
| **Test Case ID** | TC-CHECKOUT-018 |
| **Module** | Checkout |
| **Test Type** | Navigation |
| **Severity** | S2 – Major |

**Expected Result:**  
User redirected to inventory page.


---

## TC-CHECKOUT-019: Verify cart is empty after order completion

| Field | Value |
|------|------|
| **Test Case ID** | TC-CHECKOUT-019 |
| **Module** | Checkout |
| **Test Type** | Functional |
| **Severity** | S1 – Critical |

**Test Objective:**  
Verify cart is cleared after successful order.

**Expected Result:**  
Cart badge shows 0 items.


---

## TC-CHECKOUT-020: Verify end-to-end checkout flow (E2E Smoke Test)

| Field | Value |
|------|------|
| **Test Case ID** | TC-CHECKOUT-020 |
| **Module** | Checkout |
| **Test Type** | E2E / Smoke |
| **Severity** | S0 – Blocker |

**Test Objective:**  
Verify full user journey from login to successful order completion.

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Login | Inventory page opens |
| 2 | Add product to cart | Cart badge updates |
| 3 | Complete checkout | Order confirmation displayed |

## TC-CHECKOUT-021: Verify checkout prevents XSS attempt in First Name field

| Field | Value |
|------|------|
| **Test Case ID** | TC-CHECKOUT-021 |
| **Module** | Checkout |
| **Test Type** | Security |
| **Severity** | S1 – Critical |

**Test Objective:**  
Verify that XSS payload entered in the First Name field is not executed and checkout validation blocks malicious input.

**Preconditions:**
- User is logged in as `standard_user`
- At least one item is added to the cart
- Checkout: Your Information page is open

**Test Data:**  
First Name: `<img src=x onerror=alert('XSS')>`  
Last Name: Doe  
ZIP Code: 12345

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Enter XSS payload in First Name field | Text appears as plain text |
| 2 | Enter valid Last Name and ZIP Code | Text accepted |
| 3 | Click **Continue** | Checkout does not proceed |
| 4 | Observe application behavior | No alert popup appears |
| 5 | Observe error message | Validation error displayed or input sanitized |

**Security Validation:**  
- No JavaScript execution  
- No page break or redirect  
- Input is safely handled

## TC-CHECKOUT-022: Verify checkout prevents XSS attempt in Last Name field

| Field | Value |
|------|------|
| **Test Case ID** | TC-CHECKOUT-022 |
| **Module** | Checkout |
| **Test Type** | Security |
| **Severity** | S1 – Critical |

**Test Objective:**  
Verify that XSS payload in Last Name field is not executed and application remains secure.

**Preconditions:**
- User is logged in
- Checkout information page is open

**Test Data:**  
First Name: John  
Last Name: `<script>alert('XSS')</script>`  
ZIP Code: 12345

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|-----|--------|----------------|
| 1 | Enter XSS payload in Last Name field | Text displayed as plain text |
| 2 | Enter valid First Name and ZIP Code | Accepted |
| 3 | Click **Continue** | Checkout blocked or input sanitized |
| 4 | Observe application behavior | No JavaScript execution |
| 5 | Observe UI | Page remains stable, no alert |

**Security Validation:**  
- Script tags not executed  
- Application state unchanged  
- User data protected
