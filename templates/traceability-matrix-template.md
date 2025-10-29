# Requirements Traceability Matrix (RTM) Template

## Document Control

| Field | Details |
|-------|---------|
| **Project Name** | [Application/Project Name] |
| **Document Title** | Requirements Traceability Matrix |
| **Version** | 1.0 |
| **Author** | [Your Name] |
| **Created Date** | YYYY-MM-DD |
| **Last Updated** | YYYY-MM-DD |

---

## Purpose

The Requirements Traceability Matrix (RTM) is a document that maps and traces:
- **Requirements** → **Test Cases** → **Test Results** → **Defects**

This ensures:
- ✅ All requirements are tested
- ✅ No functionality is missed
- ✅ Test coverage is complete
- ✅ Defects are linked to requirements

---

## Traceability Matrix

| Req ID | Requirement Description | Priority | Test Case ID(s) | Test Status | Execution Date | Defect ID | Defect Status | Comments |
|--------|------------------------|----------|-----------------|-------------|----------------|-----------|---------------|----------|
| REQ-001 | User can login with valid credentials | High | TC-LOGIN-001, TC-LOGIN-002 | Pass | 2025-10-29 | - | - | All login scenarios covered |
| REQ-002 | User receives error for invalid credentials | High | TC-LOGIN-003, TC-LOGIN-004 | Pass | 2025-10-29 | - | - | Negative test cases |
| REQ-003 | User can view product catalog | High | TC-CATALOG-001 | Pass | 2025-10-29 | - | - | Product grid displays correctly |
| REQ-004 | User can search for products | Medium | TC-SEARCH-001, TC-SEARCH-002 | Fail | 2025-10-29 | BUG-012 | Open | Search not returning results |
| REQ-005 | User can add items to cart | High | TC-CART-001, TC-CART-002 | Fail | 2025-10-29 | BUG-015 | Open | Cart counter not updating |
| REQ-006 | User can remove items from cart | Medium | TC-CART-003 | Pass | 2025-10-29 | - | - | Remove works correctly |
| REQ-007 | User can proceed to checkout | High | TC-CHECKOUT-001 | Not Run | - | - | - | Blocked by BUG-015 |
| REQ-008 | User can complete payment | Critical | TC-PAYMENT-001, TC-PAYMENT-002 | Not Run | - | - | - | Awaiting test environment |
| REQ-009 | User receives order confirmation | High | TC-CONFIRM-001 | Not Run | - | - | - | Awaiting payment test |
| REQ-010 | System validates payment details | Critical | TC-PAYMENT-003 | Not Run | - | - | - | Security testing required |

---

## Summary Statistics

### Overall Coverage

| Metric | Count | Percentage |
|--------|-------|------------|
| **Total Requirements** | 10 | 100% |
| **Requirements with Test Cases** | 10 | 100% |
| **Requirements Tested** | 6 | 60% |
| **Requirements Not Tested** | 4 | 40% |

### Test Execution Status

| Status | Count | Percentage |
|--------|-------|------------|
| **Pass** | 5 | 50% |
| **Fail** | 2 | 20% |
| **Not Run** | 3 | 30% |
| **Blocked** | 1 | 10% |

### Defect Summary

| Priority | Open | Closed | Total |
|----------|------|--------|-------|
| **Critical** | 0 | 0 | 0 |
| **High** | 1 | 0 | 1 |
| **Medium** | 1 | 0 | 1 |
| **Low** | 0 | 0 | 0 |
| **Total** | 2 | 0 | 2 |

---

## Detailed Traceability by Module

### Module: Authentication

| Req ID | Requirement | Test Cases | Status | Coverage |
|--------|-------------|------------|--------|----------|
| REQ-001 | Valid login | TC-LOGIN-001, TC-LOGIN-002 | ✅ Pass | 100% |
| REQ-002 | Invalid login error | TC-LOGIN-003, TC-LOGIN-004 | ✅ Pass | 100% |

**Module Coverage:** 100% (2/2 requirements tested)

---

### Module: Product Catalog

| Req ID | Requirement | Test Cases | Status | Coverage |
|--------|-------------|------------|--------|----------|
| REQ-003 | View product catalog | TC-CATALOG-001 | ✅ Pass | 100% |
| REQ-004 | Search products | TC-SEARCH-001, TC-SEARCH-002 | ❌ Fail | 100% |

**Module Coverage:** 100% (2/2 requirements tested)
**Defects Found:** BUG-012 (Search not working)

---

### Module: Shopping Cart

| Req ID | Requirement | Test Cases | Status | Coverage |
|--------|-------------|------------|--------|----------|
| REQ-005 | Add items to cart | TC-CART-001, TC-CART-002 | ❌ Fail | 100% |
| REQ-006 | Remove items from cart | TC-CART-003 | ✅ Pass | 100% |

**Module Coverage:** 100% (2/2 requirements tested)
**Defects Found:** BUG-015 (Cart counter not updating)

---

### Module: Checkout & Payment

| Req ID | Requirement | Test Cases | Status | Coverage |
|--------|-------------|------------|--------|----------|
| REQ-007 | Proceed to checkout | TC-CHECKOUT-001 | ⏸️ Blocked | 0% |
| REQ-008 | Complete payment | TC-PAYMENT-001, TC-PAYMENT-002 | ⏸️ Not Run | 0% |
| REQ-009 | Order confirmation | TC-CONFIRM-001 | ⏸️ Not Run | 0% |
| REQ-010 | Validate payment details | TC-PAYMENT-003 | ⏸️ Not Run | 0% |

**Module Coverage:** 0% (0/4 requirements tested)
**Blockers:** BUG-015 must be fixed first

---

## Forward Traceability

**Requirements → Test Cases**

| Requirement | Test Cases | Count |
|-------------|------------|-------|
| REQ-001 | TC-LOGIN-001, TC-LOGIN-002 | 2 |
| REQ-002 | TC-LOGIN-003, TC-LOGIN-004 | 2 |
| REQ-003 | TC-CATALOG-001 | 1 |
| REQ-004 | TC-SEARCH-001, TC-SEARCH-002 | 2 |
| REQ-005 | TC-CART-001, TC-CART-002 | 2 |
| REQ-006 | TC-CART-003 | 1 |
| REQ-007 | TC-CHECKOUT-001 | 1 |
| REQ-008 | TC-PAYMENT-001, TC-PAYMENT-002 | 2 |
| REQ-009 | TC-CONFIRM-001 | 1 |
| REQ-010 | TC-PAYMENT-003 | 1 |

**Total Test Cases:** 15

---

## Backward Traceability

**Test Cases → Requirements**

| Test Case | Requirement | Module |
|-----------|-------------|--------|
| TC-LOGIN-001 | REQ-001 | Authentication |
| TC-LOGIN-002 | REQ-001 | Authentication |
| TC-LOGIN-003 | REQ-002 | Authentication |
| TC-LOGIN-004 | REQ-002 | Authentication |
| TC-CATALOG-001 | REQ-003 | Product Catalog |
| TC-SEARCH-001 | REQ-004 | Product Catalog |
| TC-SEARCH-002 | REQ-004 | Product Catalog |
| TC-CART-001 | REQ-005 | Shopping Cart |
| TC-CART-002 | REQ-005 | Shopping Cart |
| TC-CART-003 | REQ-006 | Shopping Cart |
| TC-CHECKOUT-001 | REQ-007 | Checkout |
| TC-PAYMENT-001 | REQ-008 | Payment |
| TC-PAYMENT-002 | REQ-008 | Payment |
| TC-CONFIRM-001 | REQ-009 | Confirmation |
| TC-PAYMENT-003 | REQ-010 | Payment |

**Orphaned Test Cases (no requirement):** 0 ✅

---

## Defect-to-Requirement Traceability

| Defect ID | Defect Summary | Requirement | Severity | Status |
|-----------|----------------|-------------|----------|--------|
| BUG-012 | Search returns no results | REQ-004 | Medium | Open |
| BUG-015 | Cart counter not updating | REQ-005 | High | Open |

---

## Coverage Gaps

### Requirements Without Test Cases
None - All requirements have test cases ✅

### Test Cases Without Requirements
None - All test cases are linked ✅

### Untested Requirements (Not Run)
- REQ-007 (Blocked by BUG-015)
- REQ-008 (Environment not ready)
- REQ-009 (Depends on REQ-008)
- REQ-010 (Security testing pending)

---

## Risk Assessment

| Module | Coverage | Defects | Risk Level | Mitigation |
|--------|----------|---------|------------|------------|
| Authentication | 100% | 0 | ✅ Low | Fully tested, all pass |
| Product Catalog | 100% | 1 | ⚠️ Medium | BUG-012 needs fix |
| Shopping Cart | 100% | 1 | ⚠️ Medium | BUG-015 needs fix |
| Checkout & Payment | 0% | 0 | 🔴 High | Not tested yet, critical functionality |

---

## Recommendations

1. **Immediate Actions:**
   - Fix BUG-015 (cart counter) to unblock checkout testing
   - Fix BUG-012 (search) to complete catalog module
   - Prepare payment test environment

2. **Testing Priorities:**
   - Test REQ-007 through REQ-010 as soon as blockers resolved
   - Focus on high-priority requirements first
   - Conduct regression testing after defect fixes

3. **Process Improvements:**
   - Ensure all future requirements have test cases before development
   - Update RTM daily during active testing
   - Include RTM in code review checklist

---

## Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **QA Lead** | [Name] | | YYYY-MM-DD |
| **Test Manager** | [Name] | | YYYY-MM-DD |
| **Project Manager** | [Name] | | YYYY-MM-DD |

---

## Appendix: RTM Best Practices

### Why RTM is Important
- ✅ Ensures 100% requirement coverage
- ✅ Identifies gaps in testing
- ✅ Provides clear audit trail
- ✅ Supports compliance requirements
- ✅ Facilitates impact analysis for changes
- ✅ Helps with test prioritization

### How to Maintain RTM
1. **Create early:** During test planning phase
2. **Update regularly:** Daily during test execution
3. **Review weekly:** With team and stakeholders
4. **Include in reports:** Show coverage in status updates
5. **Use tools:** Excel, Jira, TestRail, or similar
6. **Automate:** Use test management tools for auto-linking

---

**Template Version:** 1.0
**Last Updated:** October 2025
