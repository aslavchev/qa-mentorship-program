# Acceptance Criteria

## User Story 1: User Login

**As a** registered user  
**I want** to log in with my username and password  
**So that** I can access my shopping cart and purchase products  

### Acceptance Criteria

**AC1: Successful login with valid credentials**
- **Given** I am on the SauceDemo login page
- **When** I enter valid username "standard_user" and password "secret_sauce"
- **And** I click the LOGIN button
- **Then** I should be redirected to the inventory page
- **And** I should see 6 products displayed

**AC2: Login fails with invalid username**
- **Given** I am on the login page
- **When** I enter invalid username "wrong_user" and valid password "secret_sauce"
- **Then** I should see error message "Username and password do not match any user in this service"
- **And** I should remain on the login page

**AC3: Login fails with invalid password**
- **Given** I am on the login page
- **When** I enter valid username "standard_user" and invalid password "wrong_pass"
- **Then** I should see error message "Username and password do not match any user in this service"
- **And** I should remain on the login page

**AC4: Locked user cannot login**
- **Given** I am on the login page
- **When** I enter username "locked_out_user" and password "secret_sauce"
- **Then** I should see error message "Sorry, this user has been locked out."
- **And** I should remain on the login page

---

## User Story 2: Add Items to Cart

**As a** shopper  
**I want** to add products to my shopping cart  
**So that** I can purchase multiple items in a single order  

### Acceptance Criteria

**AC1: Add single item from inventory page**
- **Given** I am logged in and on the inventory page
- **When** I click "Add to cart" for a product
- **Then** the product should be added to the cart
- **And** the cart badge should display "1"

**AC2: Add multiple different items**
- **Given** I am on the inventory page
- **When** I add two different products to the cart
- **Then** both products should appear in the cart
- **And** the cart badge should display "2"

**AC3: Cart badge updates correctly**
- **Given** I add items to the cart
- **When** I add or remove a product
- **Then** the cart badge should update with the correct item count

**AC4: Remove button appears after adding item**
- **Given** I have added a product to the cart
- **Then** the "Add to cart" button should change to "Remove"

---

## User Story 3: Product Sorting

**As a** shopper  
**I want** to sort products by name and price  
**So that** I can easily find products that meet my needs  

### Acceptance Criteria

**AC1: Sort products by name A to Z**
- **Given** I am on the inventory page
- **When** I select "Name (A to Z)" from the sort dropdown
- **Then** products should be sorted alphabetically from A to Z

**AC2: Sort products by name Z to A**
- **Given** I am on the inventory page
- **When** I select "Name (Z to A)" from the sort dropdown
- **Then** products should be sorted alphabetically from Z to A

**AC3: Sort products by price low to high**
- **Given** I am on the inventory page
- **When** I select "Price (low to high)" from the sort dropdown
- **Then** products should be sorted from lowest to highest price

**AC4: Sort products by price high to low**
- **Given** I am on the inventory page
- **When** I select "Price (high to low)" from the sort dropdown
- **Then** products should be sorted from highest to lowest price

---

## User Story 4: Checkout Process

**As a** shopper  
**I want** to complete checkout with my information  
**So that** I can finalize my purchase  

### Acceptance Criteria

**AC1: Checkout with valid information**
- **Given** I have items in my cart
- **And** I am on the checkout information page
- **When** I enter valid first name, last name, and zip code
- **And** I click Continue
- **Then** I should be navigated to the checkout overview page

**AC2: First name is required**
- **Given** I am on the checkout information page
- **When** I leave the first name field empty
- **And** I click Continue
- **Then** I should see error message "Error: First Name is required"

**AC3: Last name is required**
- **Given** I am on the checkout information page
- **When** I leave the last name field empty
- **And** I click Continue
- **Then** I should see error message "Error: Last Name is required"

**AC4: Zip code is required**
- **Given** I am on the checkout information page
- **When** I leave the zip code field empty
- **And** I click Continue
- **Then** I should see error message "Error: Postal Code is required"

**AC5: Order confirmation after finishing checkout**
- **Given** I am on the checkout overview page
- **When** I click the Finish button
- **Then** I should see the order confirmation page
- **And** I should see message "Thank you for your order"

---

## User Story 5: Remove Items from Cart

**As a** shopper  
**I want** to remove items from my cart  
**So that** I can change my mind before purchasing  

### Acceptance Criteria

**AC1: Remove item from cart page**
- **Given** I have an item in my cart
- **And** I am on the cart page
- **When** I click the Remove button
- **Then** the item should be removed from the cart

**AC2: Cart badge updates after removal**
- **Given** I remove an item from the cart
- **Then** the cart badge should update to reflect the new item count

**AC3: Empty cart state**
- **Given** I remove all items from the cart
- **Then** the cart should be empty
- **And** no cart badge should be displayed

---

## INVEST Validation

| User Story | Independent | Negotiable | Valuable | Estimable | Small | Testable | Why |
|-----------|-------------|------------|----------|-----------|-------|----------|-----|
| User Login | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Login can be tested independently without Cart or Checkout functionality |
| Add Items to Cart | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Cart functionality depends only on login and delivers direct business value |
| Product Sorting | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Sorting is isolated UI behavior and easy to estimate and test |
| Checkout Process | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Checkout completes the purchase flow and has clear validation rules |
| Remove Items from Cart | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Removal logic is independent and testable without checkout |

