# Test Case Review

## Document Control

| Field | Details |
|------|--------|
| Project Name | SauceDemo |
| Document Title | Test Case Review |
| Author | Kamen Asenov |
| Created Date | 2025-26-12 |
| Version | 1.0 |
| Status | Draft |

---

## Purpose

This document contains a self-review of selected SauceDemo test cases.
The goal is to evaluate test case quality using a review checklist,
identify issues, and document improvements and learnings.

---

## Selected Test Cases for Review

| Module | Test Case ID | Scenario Type |
|------|--------------|---------------|
| Login | TC-LOGIN-001 | Positive |
| Login | TC-LOGIN-003 | Negative |
| Login | TC-LOGIN-010 | Security |
| Products | TC-PRODUCTS-001 | Positive |
| Products | TC-SORT-001 | Functional |
| Cart | TC-CART-001 | Positive |
| Cart | TC-CART-005 | Negative |
| Cart | TC-CART-010 | State |
| Checkout | TC-CHECKOUT-001 | Positive |
| Checkout | TC-CHECKOUT-002 | Negative |

---

## Test Case Review Details

### Test Case Review – TC-LOGIN-001

#### Completeness
- [x] All required fields filled
- [x] Preconditions stated
- [x] Test data specified
- [x] Expected results defined
- [x] Linked to requirement

#### Clarity
- [x] Clear title
- [ ] Steps fully specific  
- [x] One action per step
- [x] Exact field and button names used
- [ ] Expected results fully specific  

#### Correctness
- [x] Logical order
- [x] Accurate expected results
- [x] Valid test data
- [x] No typos

#### Testability
- [x] Executable without extra info
- [x] Repeatable
- [x] Independent
- [x] < 10 min execution

#### Coverage
- [x] Positive scenario
- [ ] Negative scenario missing
- [x] Boundary not applicable
- [x] No duplicates

**Issues Found:** 2  
**Severity:** Minor  

**Improvements Needed:**
1. Replace “Enter password” with exact value.
2. Replace “Login works” with expected URL and page elements.

---

### Test Case Review – TC-LOGIN-003

**Issues Found:**  
- Error message not explicitly stated  
**Severity:** Minor  

**Action:** Add exact error message text.

---

### Test Case Review – TC-LOGIN-010

**Issues Found:**  
- Security expectation not explicit  
**Severity:** Minor  

**Action:** Specify that input is sanitized and no script executes.

---

### Test Case Review – TC-PRODUCTS-001

**Issues Found:**  
- None  
**Severity:** None  

---

### Test Case Review – TC-SORT-001

**Issues Found:**  
- Expected sorting order not fully listed  
**Severity:** Minor  

**Action:** List exact expected product order.

---

### Test Case Review – TC-CART-001

**Issues Found:**  
- Missing negative coverage reference  
**Severity:** Minor  

**Action:** Reference related negative test TC-CART-005.

---

### Test Case Review – TC-CART-005

**Issues Found:**  
- Preconditions missing cart state  
**Severity:** Minor  

**Action:** Explicitly state “Cart contains at least one item”.

---

### Test Case Review – TC-CART-010

**Issues Found:**  
- Multi-action step detected  
**Severity:** Minor  

**Action:** Split navigation and verification into separate steps.

---

### Test Case Review – TC-CHECKOUT-001

**Issues Found:**  
- None  
**Severity:** None  

---

### Test Case Review – TC-CHECKOUT-002

**Issues Found:**  
- Error message not exact  
**Severity:** Minor  

**Action:** Add full validation message text.

---

## Test Case Review Summary

### Test Cases Reviewed
10 test cases reviewed across all modules

---

### Issues Found by Category

| Category | Issues | % of Reviews | Examples |
|--------|--------|--------------|----------|
| Completeness | 2 | 20% | Missing preconditions in TC-CART-005 |
| Clarity | 5 | 50% | Vague steps in TC-LOGIN-003 |
| Correctness | 1 | 10% | Sorting order in TC-SORT-001 |
| Testability | 0 | 0% | All tests executable |
| Coverage | 2 | 20% | Missing negative references |
| **TOTAL** | **10** | | |

---

## Common Patterns

### Good Practices
- Consistent TC-[MODULE]-[###] naming
- Clear preconditions in most tests
- Test data specified consistently

### Improvement Areas
- Vague expected results (“should work”)
- Occasional multi-action steps
- Missing exact error messages

---

## Action Items

1. Update expected results in 5 test cases
2. Split multi-action steps in 2 test cases
3. Add exact validation messages
4. Add 3 more boundary tests for cart quantity

---

## Learnings

### What I Learned
- Specific expected results reduce ambiguity
- One action per step improves readability
- Independent tests are easier to maintain
- Boundary testing improves coverage

### Will Apply Going Forward
- Always use exact UI text
- Always specify error messages
- Self-review before submitting
- Write tests assuming another tester will execute them

