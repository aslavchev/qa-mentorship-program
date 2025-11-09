# SauceDemo Application Analysis

## Part A: Application Exploration

- Explored https://www.saucedemo.com/ using credentials: `standard_user / secret_sauce`
- Application is an e-commerce demo site with login, product catalog, cart, and checkout flow.
- Features include login/logout, sorting products, viewing product details, adding/removing items from cart, and completing checkout.

## Part B: Feature Map

```
SauceDemo E-Commerce Application
├── Authentication
│   ├── Login
│   ├── Logout
│   └── Error Messages for invalid credentials
├── Product Catalog
│   ├── Product Grid (6 products displayed)
│   ├── Product Details page
│   ├── Sorting (Name A-Z, Z-A, Price Low-High, High-Low)
│   └── Product Images and Descriptions
├── Shopping Cart
│   ├── Add Items
│   ├── Remove Items
│   ├── View Cart (item list, quantity, price)
│   └── Continue Shopping / Checkout buttons
├── Checkout Process
│   ├── Checkout Information (first name, last name, postal code)
│   ├── Checkout Overview (order summary, item total, tax, total)
│   └── Checkout Complete (confirmation message)
├── Navigation
│   ├── Menu (All Items, About, Logout, Reset App State)
│   └── Shopping Cart Icon (with item count badge)
└── User Roles
    ├── Standard User
    ├── Locked Out User
    ├── Problem User
    └── Performance Glitch User
```

## Part C: User Workflows

### 1. Happy Path – Complete Purchase
1. Go to https://www.saucedemo.com/
2. Login with `standard_user` / `secret_sauce`
3. Browse products
4. Choose products
5. Add to Cart
6. Go to Checkout
7. Enter First name/Last name/Zip code
8. Press Finish
9. See "Thank you for your order" displayed
10. Go back to home

### 2. Browse Products
1. Login successfully
2. Press on a product heading or picture
3. Press on "Back to products" button
4. Go to the sorting button
5. Change the sorting to "Z to A"
6. Change the sorting to "Price low to high"
7. Change the sorting to "Price high to low"
### 3. Manage Cart
1. Login successfully
2. Add products to the cart
3. Press the cart button on the top right
4. Remove an item 
5. Change the quantity of a product
6. Press the Continue shopping/Checkout button
 

## Part D: Functional Requirements

1. **REQ-001:** User shall be able to login with valid credentials.
2. **REQ-002:** User shall not be able to login with invalid credentials
3. **REQ-003:** User shall be able to add a product to the cart by pressing the "Add to cart" button
4. **REQ-004:** User shall be able to see the description of a product on a separate page by pressing on the heading of the product
5. **REQ-005:** User shall be able to add product to cart also from the separate page of the product
6. **REQ-006:** User shall be able to remove products from cart
7. **REQ-007:** User shall be able to proceed to checkout by typing their First name/Last name/Zip/postal code
8. **REQ-008:** User shall not be able to proceed to checkout with invalid First name/Last name/Zip/postal code
9. **REQ-009:** User shall be able to cancel their order from the button "Cancel" at any point
10. **REQ-010:** After checkout and pressing the Finish button, the user shall see "Thank you for your order" and a button to go back to the home page

## Part E: Non-Functional Requirements (NFRs)

1. **Performance:** The website shall be consistent at any time and not take more than 2-3 secs to load a page
2. **Usability:** The website shall be clean and easy to move around, not confusing
3. **Security:** The website shall be secured by encrypting the passwords of users
4. **Compatibility:** The website shall be mobile friendly
5. **Accessibility:** The website should be able to navigate with keyboard or screen readers also

## Part F: Initial Observations

**Strengths:**
- Clean, good-looking website
- Easy to use and navigate around
- Every key element is present (login, products, sorting, cart, verification, checkout, purchasing)

**Potential Issues:**
- No option to change the quantity of products
- Able to proceed to checkout and purchase without products in cart
- Able to proceed to checkout with invalid format of First name/last name/Zip/postal code

**User Experience Notes:**
- The site is easy to use, but does not appear secure enough. 
- It sometimes breaks
- No option to filter, only sort

