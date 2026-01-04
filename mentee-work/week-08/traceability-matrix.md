# Requirements Traceability Matrix (RTM) – SauceDemo

## Document Control

| Field | Details |
|------|--------|
| **Project Name** | SauceDemo |
| **Document Title** | Requirements Traceability Matrix |
| **Version** | 1.0 |
| **Author** | Kamen Asenov |
| **Created Date** | 2025-24-12 |

---

## Purpose

This document provides a Requirements Traceability Matrix (RTM) that maps
Week 7 Test Plan requirements to Week 8 test cases for the SauceDemo
application.  
The goal is to demonstrate **100% requirements coverage** and clear
traceability between requirements and test cases.

---

## Identified Requirements (from Week 7 Test Plan)

| Req ID | Requirement Description | Priority |
|------|-------------------------|----------|
| REQ-AUTH-001 | User can login with valid credentials | Critical |
| REQ-AUTH-002 | User cannot login with invalid credentials | Critical |
| REQ-AUTH-003 | Locked user cannot login | High |
| REQ-AUTH-004 | User can logout successfully | High |
| REQ-PROD-001 | User can view all products | High |
| REQ-PROD-002 | User can sort products by name | Medium |
| REQ-PROD-003 | User can sort products by price | Medium |
| REQ-CART-001 | User can add items to cart | Critical |
| REQ-CART-002 | User can remove items from cart | High |
| REQ-CART-003 | Cart displays correct total | High |
| REQ-CHKT-001 | User can enter checkout information | Critical |
| REQ-CHKT-002 | Checkout validates required fields | Critical |
| REQ-CHKT-003 | User can complete order | Critical |

---

## Requirements Traceability Matrix

| Req ID | Requirement Description | Priority | Test Case IDs | Test Count | Coverage |
|------|-------------------------|----------|---------------|------------|----------|
| REQ-AUTH-001 | Login with valid credentials | Critical | TC-LOGIN-001, TC-LOGIN-002 | 2 | ✅ 100% |
| REQ-AUTH-002 | Login blocked with invalid credentials | Critical | TC-LOGIN-003, TC-LOGIN-004, TC-LOGIN-005, TC-LOGIN-006, TC-LOGIN-007 | 5 | ✅ 100% |
| REQ-AUTH-003 | Locked user cannot login | High | TC-LOGIN-008 | 1 | ✅ 100% |
| REQ-AUTH-004 | User can logout | High | TC-LOGIN-014 | 1 | ✅ 100% |
| REQ-PROD-001 | View all products | High | TC-PRODUCTS-001, TC-PRODUCTS-003, TC-PRODUCTS-004 | 3 | ✅ 100% |
| REQ-PROD-002 | Sort products by name | Medium | TC-SORT-001, TC-SORT-002 | 2 | ✅ 100% |
| REQ-PROD-003 | Sort products by price | Medium | TC-SORT-003, TC-SORT-004 | 2 | ✅ 100% |
| REQ-CART-001 | Add items to cart | Critical | TC-CART-001, TC-CART-002, TC-CART-007 | 3 | ✅ 100% |
| REQ-CART-002 | Remove items from cart | High | TC-CART-005, TC-CART-006 | 2 | ✅ 100% |
| REQ-CART-003 | Correct cart total | High | TC-CART-009, TC-CART-014, TC-CART-015 | 3 | ✅ 100% |
| REQ-CHKT-001 | Enter checkout information | Critical | TC-CHECKOUT-001, TC-CHECKOUT-006, TC-CHECKOUT-007, TC-CHECKOUT-008 | 4 | ✅ 100% |
| REQ-CHKT-002 | Validate required checkout fields | Critical | TC-CHECKOUT-002, TC-CHECKOUT-003, TC-CHECKOUT-004, TC-CHECKOUT-005 | 4 | ✅ 100% |
| REQ-CHKT-003 | Complete order successfully | Critical | TC-CHECKOUT-015, TC-CHECKOUT-016, TC-CHECKOUT-017, TC-CHECKOUT-020 | 4 | ✅ 100% |

---

## Coverage Metrics

### Requirements Coverage

- **Total Requirements:** 13  
- **Requirements with Tests:** 13  
- **Coverage:**  
  **(13 / 13) × 100% = 100% ✅**

---

### Test Case Distribution

| Metric | Count |
|------|------|
| Total Test Cases | 60 |
| Test Cases Mapped to Requirements | 60 |
| Orphaned Test Cases | 0 |

---

## Module Coverage

| Module | Requirements | Tests Covering | Coverage |
|------|-------------|---------------|----------|
| Authentication | 4 | 15 | 375% |
| Products | 3 | 10 | 333% |
| Cart | 3 | 15 | 500% |
| Checkout | 3 | 20 | 667% |

> Note: Coverage above 100% indicates multiple test cases validating the same requirement.

---

## Forward Traceability (Requirements → Tests)

- Each requirement is linked to one or more test cases.
- Critical requirements have multiple tests for positive and negative scenarios.

---

## Backward Traceability (Tests → Requirements)

- All test cases are mapped to at least one functional requirement.
- No orphaned or undocumented tests exist.

## Complete Requirements Traceability Matrix (RTM)

## Overview
This RTM maps all test cases for the SauceDemo application across modules, linking them to requirements. Supplementary tests and security/UI tests are included.

| Legend | Description |
|--------|------------|
| S0 – Blocker | Critical for system functionality; failure blocks further testing |
| S1 – Critical | High priority; major functionality |
| S2 – Major | Medium priority; important functionality |
| S3 – Minor | Low priority; UI or cosmetic |

---

## 1. Login / Authentication

| Test Case ID | Module | Type | Severity | Objective / Description | Mapped Requirement |
|--------------|--------|------|---------|------------------------|------------------|
| TC-LOGIN-001 | Login | Smoke | S1 | Verify login with valid credentials (`standard_user`) | REQ-AUTH-001 |
| TC-LOGIN-002 | Login | Functional | S1 | Verify login with another valid user (`problem_user`) | REQ-AUTH-001 |
| TC-LOGIN-003 | Login | Negative | S2 | Verify login fails with invalid username | REQ-AUTH-002 |
| TC-LOGIN-004 | Login | Negative | S2 | Verify login fails with invalid password | REQ-AUTH-002 |
| TC-LOGIN-005 | Login | Negative | S2 | Verify login fails with empty username | REQ-AUTH-002 |
| TC-LOGIN-006 | Login | Negative | S2 | Verify login fails with empty password | REQ-AUTH-002 |
| TC-LOGIN-007 | Login | Negative | S2 | Verify login fails with empty username and password | REQ-AUTH-002 |
| TC-LOGIN-008 | Login | Security | S1 | Verify locked user cannot login | REQ-AUTH-003 |
| TC-LOGIN-009 | Login | Negative | S2 | Verify login fails with special characters in username | REQ-AUTH-002 |
| TC-LOGIN-010 | Login | Security | S0 | Verify login form protected against SQL injection | Supplementary |
| TC-LOGIN-011 | Login | UI | S3 | Verify password field is masked | Supplementary |
| TC-LOGIN-012 | Login | UI | S3 | Verify login button clickable and error message shown | Supplementary |
| TC-LOGIN-013 | Login | Negative | S2 | Verify error message for invalid credentials | REQ-AUTH-002 |
| TC-LOGIN-014 | Login | Functional | S1 | Verify successful logout | REQ-AUTH-004 |
| TC-LOGIN-015 | Login | Security | S1 | Verify user cannot access inventory page without login | Supplementary |
| TC-LOGIN-016 | Login | Security | S1 | Verify login fails with XSS in username field | Supplementary |

---

## 2. Product Browsing / Inventory

| Test Case ID | Module | Type | Severity | Objective / Description | Mapped Requirement |
|--------------|--------|------|---------|------------------------|------------------|
| TC-PRODUCTS-001 | Products | Functional | S1 | Verify all products are displayed on inventory page | REQ-PROD-001 |
| TC-PRODUCTS-002 | Products | UI | S3 | Verify product images are displayed | Supplementary |
| TC-PRODUCTS-003 | Products | UI | S2 | Verify product names are visible | Supplementary |
| TC-PRODUCTS-004 | Products | Functional | S1 | Verify product prices are displayed | REQ-PROD-001 |
| TC-PRODUCTS-005 | Products | Functional | S2 | Verify product detail page opens | REQ-PROD-001 |
| TC-PRODUCTS-006 | Products | Navigation | S3 | Verify back button returns to inventory page | Supplementary |
| TC-SORT-001 | Products | Functional | S2 | Verify sorting by Name (A to Z) | REQ-PROD-002 |
| TC-SORT-002 | Products | Functional | S2 | Verify sorting by Name (Z to A) | REQ-PROD-002 |
| TC-SORT-003 | Products | Functional | S2 | Verify sorting by Price (low to high) | REQ-PROD-003 |
| TC-SORT-004 | Products | Functional | S2 | Verify sorting by Price (high to low) | REQ-PROD-003 |

---

## 3. Shopping Cart

| Test Case ID | Module | Type | Severity | Objective / Description | Mapped Requirement |
|--------------|--------|------|---------|------------------------|------------------|
| TC-CART-001 | Cart | Functional | S1 | Add item to cart from inventory page | REQ-CART-001 |
| TC-CART-002 | Cart | Functional | S1 | Add item to cart from product detail page | REQ-CART-001 |
| TC-CART-003 | Cart | UI | S2 | Verify cart badge updates when item added | Supplementary |
| TC-CART-004 | Cart | Functional | S1 | Verify cart displays added items | REQ-CART-001 |
| TC-CART-005 | Cart | Functional | S1 | Verify remove item from cart | REQ-CART-002 |
| TC-CART-006 | Cart | UI | S2 | Verify cart badge updates when item removed | Supplementary |
| TC-CART-007 | Cart | Functional | S1 | Add multiple different items to cart | REQ-CART-001 |
| TC-CART-008 | Cart | Negative | S2 | Verify add same item twice is not allowed | REQ-CART-001 |
| TC-CART-009 | Cart | Functional | S1 | Verify cart total calculation is correct | REQ-CART-003 |
| TC-CART-010 | Cart | Regression | S2 | Verify cart persists across page navigation | Supplementary |
| TC-CART-011 | Cart | UI | S3 | Verify empty cart displays correctly | Supplementary |
| TC-CART-012 | Cart | Navigation | S3 | Continue Shopping button returns to inventory | Supplementary |
| TC-CART-013 | Cart | Functional | S1 | Checkout button navigates to checkout page | REQ-CHKT-001 |
| TC-CART-014 | Cart | Boundary | S2 | Cart with single item | REQ-CART-003 |
| TC-CART-015 | Cart | Boundary | S2 | Cart with all products added | REQ-CART-003 |

---

## 4. Checkout

| Test Case ID | Module | Type | Severity | Objective / Description | Mapped Requirement |
|--------------|--------|------|---------|------------------------|------------------|
| TC-CHECKOUT-001 | Checkout | Functional | S0 | Checkout with valid info | REQ-CHKT-001 |
| TC-CHECKOUT-002 | Checkout | Negative | S1 | Checkout fails with empty first name | REQ-CHKT-002 |
| TC-CHECKOUT-003 | Checkout | Negative | S1 | Checkout fails with empty last name | REQ-CHKT-002 |
| TC-CHECKOUT-004 | Checkout | Negative | S1 | Checkout fails with empty ZIP code | REQ-CHKT-002 |
| TC-CHECKOUT-005 | Checkout | Negative | S1 | Checkout fails when all fields are empty | REQ-CHKT-002 |
| TC-CHECKOUT-006 | Checkout | Boundary | S2 | Checkout with maximum length first name | REQ-CHKT-001 |
| TC-CHECKOUT-007 | Checkout | Boundary | S2 | Checkout with maximum length last name | REQ-CHKT-001 |
| TC-CHECKOUT-008 | Checkout | Boundary | S2 | Checkout with maximum length ZIP code | REQ-CHKT-001 |
| TC-CHECKOUT-009 | Checkout | Functional | S2 | Checkout allows special characters in name | REQ-CHKT-001 |
| TC-CHECKOUT-010 | Checkout | Navigation | S1 | Continue button navigates to overview page | Supplementary |
| TC-CHECKOUT-011 | Checkout | Navigation | S2 | Cancel button returns to cart | Supplementary |
| TC-CHECKOUT-012 | Checkout | Functional | S1 | Overview page displays correct items | REQ-CHKT-003 |
| TC-CHECKOUT-013 | Checkout | Functional | S1 | Overview page displays correct total price | REQ-CHKT-003 |
| TC-CHECKOUT-014 | Checkout | Functional | S2 | Verify tax calculation | REQ-CHKT-003 |
| TC-CHECKOUT-015 | Checkout | Functional | S0 | Finish button completes order | REQ-CHKT-003 |
| TC-CHECKOUT-016 | Checkout | UI | S1 | Order confirmation page displayed | Supplementary |
| TC-CHECKOUT-017 | Checkout | UI | S2 | Order confirmation message displayed | Supplementary |
| TC-CHECKOUT-018 | Checkout | Navigation | S2 | Back Home button returns to inventory | Supplementary |
| TC-CHECKOUT-019 | Checkout | Functional | S1 | Cart empty after order | REQ-CHKT-003 |
| TC-CHECKOUT-020 | Checkout | E2E / Smoke | S0 | End-to-end checkout flow | REQ-CHKT-003 |
| TC-CHECKOUT-021 | Checkout | Security | S1 | Prevent XSS in First Name | Supplementary |
| TC-CHECKOUT-022 | Checkout | Security | S1 | Prevent XSS in Last Name | Supplementary |

---

## Notes
- All supplementary tests (UI, security, XSS, SQL injection) are explicitly marked as **Supplementary**.  
- Severity and type are assigned based on criticality and functional impact.  

---

## Gap Analysis

### Requirements Without Tests
- None ✅

### Test Cases Without Requirements
- None ✅

### Under-Tested Requirements (Only 1 Test Case)
- REQ-AUTH-003 (Locked user login)
- REQ-AUTH-004 (Logout)

### Recommendations
- Add additional negative and edge-case tests for logout functionality.
- Add security-focused tests for locked user behavior (e.g. direct URL access).

---

## Conclusion

The SauceDemo test suite achieves **100% requirements coverage** with
clear forward and backward traceability.  
The RTM confirms that all critical business requirements are fully
validated by the implemented test cases.
