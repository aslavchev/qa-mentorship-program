## Exercise 4: Integration Test Scenarios 

### Objective
Write integration test scenarios for SauceDemo component interactions.

### Instructions

Write 5 detailed integration test scenarios testing interactions between SauceDemo components.

### Integration Test Scenario #1

**Test ID:** INT-1
**Test Title:** Test link between login and product catalog
**Components Under Test:** Login API ↔ Product catalog

**Objective:**
Validating when user logs in they go to the product catalog instantly

**Preconditions:**
- Valid username and password
- Working product catalog

**Test Steps:**
1. Enter standard_user username and secret_sauce password
2. Press on the login button
3. The page goes to product catalog

**Expected Result:**
From login the user should be able to instantly be redirected to the product catalog and see the products

**Data Flow:**
Login API → [session token] → Product Catalog → [authorized product list display]

**Pass Criteria:**
- Login is successful with valid credentials
- The product catalog opens 
### Integration Test Scenario #2

**Test ID:** INT-2
**Test Title:** Verify the products in catalog work as intended and can be added to cart
**Components Under Test:** Product Catalog ↔ Shopping Cart

**Objective:**
What integration are you validating? Validating that products when selected to to the cart and are displayed there as they should

**Preconditions:**
- Inside the product catalog with successfull login
- Working Shopping cart

**Test Steps:**
1. Add a product to the cart from the catalog menu
2. See in the top left cart button that the right amount of products are added 
3. Go in the cart and see that the right amount of products are there

**Expected Result:**
User should be able to add products to the cart and then see them there

**Data Flow:**
Product Catalog → [product ID via API] → Shopping Cart → [cart item + count update] 

**Pass Criteria:**
- Cart API receives correct product ID  
- UI updates cart item count instantly  
### Integration Test Scenario #3

**Test ID:** INT-3
**Test Title:** Proceed from shopping cart to checkout page
**Components Under Test:** Shopping Cart ↔ Checkout

**Objective:**
Validating that user can successfully proceed to checkout from the shopping cart with their products selected there

**Preconditions:**
- Products in Cart and Cart API working 
- User proceeds to checkout 

**Test Steps:**
1. Open cart page  
2. Click “Checkout” and enter needed names and post code
3. Go to checkout overview page

**Expected Result:**
What should happen when components interact correctly? The products from the cart should match in the checkout page with the correct price

**Data Flow:**
Shopping Cart → [cart data: items, quantity, total] → Checkout → [display summary]  

**Pass Criteria:**  
- Product details and totals match between cart and checkout  
- No missing or duplicate items 

### Integration Test Scenario #4

**Test ID:** INT-4
**Test Title:** Verify checkout form data is sent correctly to payment system  
**Components Under Test:** Checkout Form ↔ Payment System

**Objective:**
What integration are you validating? Validating that the form data is processed correctly in the payment system

**Preconditions:**
- Verify form data is sent to payment processing
- Verify payment confirmation returns to app

**Test Steps:**
1. Fill out checkout form (name, postal code, etc.)  
2. Click “Continue”  
3. Confirm payment submission  

**Expected Result:**  
Payment system processes transaction and returns success confirmation to application. 


**Data Flow:**
Checkout Form → [user & order data] → Payment System → [confirmation response]  

**Pass Criteria:**
- Verify form data is sent to payment processing
- Verify payment confirmation returns to app
### Integration Test Scenario #5

**Test ID:** INT-5
**Test Title:** [Clear title]
**Components Under Test:** Order Completion ↔ Confirmation

**Objective:**  
Validate that completed orders are stored in backend and confirmation details are displayed correctly to the user.  

**Preconditions:**  
- User has completed checkout and payment successfully  

**Test Steps:**  
1. Complete checkout process  
2. Wait for order confirmation page to load  
3. Review confirmation details (order number, items, total)  

**Expected Result:**  
Confirmation page displays correct order info retrieved from database, matching submitted data.  

**Data Flow:**  
Order Completion → [order data stored in DB] → Confirmation Page → [display order summary]  

**Pass Criteria:**  
- Order ID and item details match stored record  
- Confirmation message visible to user 

