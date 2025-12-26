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
