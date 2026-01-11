# Agile Testing Quadrants

## Purpose

This document maps the Week 8 SauceDemo test cases to the Agile Testing Quadrants in order to understand:
- What type of value each test provides
- Which tests support the team vs critique the product
- Automation priorities in an Agile context

---

## Quadrant 1: Technology-Facing, Supporting the Team
*Unit, integration, component tests*

**Count:** 0  
**Percentage:** 0%

**Tests:**
- None

**Explanation:**
SauceDemo testing in this program focuses on UI and system-level testing.  
Unit and integration tests (Q1) are typically created by developers for backend logic, APIs, and database interactions, which are out of scope for this QA-focused UI project.

---

## Quadrant 2: Business-Facing, Supporting the Team
*Functional, acceptance, BDD-style tests*

**Count:** 42  
**Percentage:** 70%

**Tests:**

### Login / Authentication
- TC-LOGIN-001 – Verify login with valid credentials
- TC-LOGIN-002 – Verify login with another valid user
- TC-LOGIN-003 – Invalid username
- TC-LOGIN-004 – Invalid password
- TC-LOGIN-005 – Empty username
- TC-LOGIN-006 – Empty password
- TC-LOGIN-007 – Empty username and password
- TC-LOGIN-008 – Locked user cannot login
- TC-LOGIN-013 – Error message for invalid login
- TC-LOGIN-014 – Logout functionality
- TC-LOGIN-015 – Access inventory without login

### Product Browsing / Inventory
- TC-PRODUCTS-001 – View all products
- TC-PRODUCTS-003 – Product names visible
- TC-PRODUCTS-004 – Product prices visible
- TC-SORT-001 – Sort by name (A–Z)
- TC-SORT-002 – Sort by name (Z–A)
- TC-SORT-003 – Sort by price (low to high)
- TC-SORT-004 – Sort by price (high to low)
- TC-PRODUCTS-005 – Open product details
- TC-PRODUCTS-006 – Back to inventory

### Shopping Cart
- TC-CART-001 – Add item to cart
- TC-CART-002 – Add item from product page
- TC-CART-003 – Cart badge updates
- TC-CART-004 – Item visible in cart
- TC-CART-005 – Remove item
- TC-CART-006 – Cart badge updates after removal
- TC-CART-007 – Add multiple items
- TC-CART-009 – Cart total calculation
- TC-CART-010 – Cart persists across pages
- TC-CART-011 – Empty cart state
- TC-CART-012 – Continue shopping
- TC-CART-013 – Checkout navigation
- TC-CART-014 – Cart with 1 item
- TC-CART-015 – Cart with all items

### Checkout
- TC-CHECKOUT-001 – Checkout with valid information
- TC-CHECKOUT-002 – Empty first name
- TC-CHECKOUT-003 – Empty last name
- TC-CHECKOUT-004 – Empty ZIP code
- TC-CHECKOUT-005 – All fields empty
- TC-CHECKOUT-010 – Continue to overview
- TC-CHECKOUT-015 – Finish order
- TC-CHECKOUT-020 – End-to-end checkout flow

**Automation Recommendation:**  
High priority – these tests validate core business requirements and are strong candidates for automation.

---

## Quadrant 3: Business-Facing, Critiquing the Product
*UI, usability, exploratory tests*

**Count:** 12  
**Percentage:** 20%

**Tests:**
- TC-LOGIN-011 – Password masking
- TC-LOGIN-012 – Login button clickable
- TC-PRODUCTS-002 – Product images load correctly
- TC-PRODUCTS-006 – Back button navigation
- TC-CART-008 – Add same item twice
- TC-CART-011 – Empty cart display
- TC-CHECKOUT-011 – Cancel checkout
- TC-CHECKOUT-016 – Order confirmation page
- TC-CHECKOUT-017 – Confirmation message
- TC-CHECKOUT-018 – Back home button
- TC-CHECKOUT-019 – Cart empty after order
- Exploratory checks during cart and checkout flows

**Automation Recommendation:**  
Low to medium priority – many of these are better suited for manual or exploratory testing.

---

## Quadrant 4: Technology-Facing, Critiquing the Product
*Security and non-functional tests*

**Count:** 6  
**Percentage:** 10%

**Tests:**
- TC-LOGIN-010 – SQL injection attempt
- TC-LOGIN-016 – XSS attempt in username
- TC-CHECKOUT-021 – XSS in first name
- TC-CHECKOUT-022 – XSS in last name
- TC-LOGIN-015 – Unauthorized access prevention
- TC-CART-009 – Data consistency (cart totals)

**Automation Recommendation:**  
High priority – security tests should be included in CI/CD pipelines where possible.

---

## Quadrant Distribution Analysis

| Quadrant | Test Count | Percentage |
|--------|-----------|------------|
| Q1 – Unit / Integration | 0 | 0% |
| Q2 – Functional / Acceptance | 42 | 70% |
| Q3 – UI / Exploratory | 12 | 20% |
| Q4 – Security / Non-functional | 6 | 10% |
| **Total** | **60** | **100%** |

---

## Observations

1. **Which quadrant has the most tests?**  
Quadrant 2 – Functional tests, which is expected for UI-heavy testing.

2. **Which quadrant has the fewest tests?**  
Quadrant 1 – No unit or integration tests, as backend testing is out of scope.

3. **Is this distribution appropriate for UI testing?**  
Yes. UI testing focuses primarily on business-facing functionality (Q2), supported by UI critique (Q3) and security checks (Q4).

4. **What's missing?**  
Developer-owned unit and integration tests (Q1).

5. **Automation priorities:**  
- **High:** Q2 and Q4  
- **Medium:** Some Q3 UI checks  
- **Low:** Exploratory and usability tests

---

## Conclusion

The SauceDemo test suite demonstrates a strong focus on business value through functional testing (Q2), supported by security validation (Q4) and usability checks (Q3).  
This aligns well with Agile testing principles for UI-driven applications.
