# Week 10 - Exercise 3: Severity & Priority Classification

**Name:** Kamen Asenov  
**Date:** 2026-01-18  
**Bugs Classified:** 10

---

## Classification Summary

### Severity Distribution

| Severity | Count | % of Total |
|----------|-------|------------|
| S1 (Critical) | 0 | 0% |
| S2 (High) | 1 | 10% |
| S3 (Medium) | 5 | 50% |
| S4 (Low) | 4 | 40% |
| **Total** | **10** | **100%** |

### Priority Distribution

| Priority | Count | % of Total |
|----------|-------|------------|
| P0 (Immediate) | 0 | 0% |
| P1 (High) | 1 | 10% |
| P2 (Medium) | 5 | 50% |
| P3 (Low) | 4 | 40% |
| **Total** | **10** | **100%** |

---

## Bug Classifications

---

### BUG-001: Checkout step pages accessible directly (empty-cart checkout possible)

**Severity:** S2 (High)  
**Priority:** P1 (High)

**Justification:**  
Severity is High because this is a state management and security-related issue that allows users to bypass required preconditions (non-empty cart) and enter the checkout flow directly. While it does not crash the application, it could lead to invalid orders in a real system. Priority is High because checkout integrity is a core business flow and this issue should be fixed within the current sprint.

---

### BUG-002: Zip/Postal Code accepts letters (no format validation)

**Severity:** S3 (Medium)  
**Priority:** P2 (Medium)

**Justification:**  
Severity is Medium because the checkout process still completes successfully, but invalid postal data is accepted, reducing data quality. There is a clear workaround (enter numeric zip), and no core flow is blocked. Priority is Medium as this should be addressed, but it is not urgent enough to block a release.

---

### BUG-003: Remove item has no confirmation/undo

**Severity:** S4 (Low)  
**Priority:** P3 (Low)

**Justification:**  
Severity is Low because the cart functionality works as expected and users can re-add removed items. The issue is purely a usability improvement. Priority is Low because this does not impact core business flows and can be addressed later if UX improvements are planned.

---

### BUG-004: Sort dropdown label does not match initial product order

**Severity:** S3 (Medium)  
**Priority:** P2 (Medium)

**Justification:**  
Severity is Medium because there is a mismatch between UI state and actual product order, which can confuse users. Sorting still works correctly once reselected, so a workaround exists. Priority is Medium as this affects user trust and clarity but does not block shopping.

---

### BUG-005: Cart badge overlaps icon on mobile viewport

**Severity:** S3 (Medium)  
**Priority:** P2 (Medium)

**Justification:**  
Severity is Medium because usability is reduced on mobile devices, but the cart remains functional. Priority is Medium since mobile usability is important, but desktop users are unaffected and there is no functional blocker.

---

### BUG-006: problem_user shows incorrect/mismatched product images

**Severity:** S3 (Medium)  
**Priority:** P2 (Medium)

**Justification:**  
Severity is Medium because incorrect product images mislead users and affect the shopping experience, but ordering is still possible. Priority is Medium as this impacts user confidence but is limited to a specific test user.

---

### BUG-007: Browser Back after completion may allow re-triggering finish flow

**Severity:** S3 (Medium)  
**Priority:** P2 (Medium)

**Justification:**  
Severity is Medium because this is a state/idempotency risk that could cause duplicate actions in a real system. Priority is Medium since the issue occurs only through specific navigation behavior and does not block the standard flow.

---

### BUG-008: Login error message persists while user edits inputs

**Severity:** S4 (Low)  
**Priority:** P3 (Low)

**Justification:**  
Severity is Low because login functionality works correctly and the issue is limited to user experience. Priority is Low since it does not affect successful login and has a clear workaround (retry login).

---

### BUG-009: performance_glitch_user login is very slow with no loading feedback

**Severity:** S3 (Medium)  
**Priority:** P2 (Medium)

**Justification:**  
Severity is Medium because the system eventually works, but lack of loading feedback may cause confusion or repeated actions. Priority is Medium as performance perception affects user experience but does not completely block access.

---

### BUG-010: Keyboard accessibility – focus indication is unclear

**Severity:** S4 (Low)  
**Priority:** P3 (Low)

**Justification:**  
Severity is Low because the application remains usable with mouse input, and this mainly affects accessibility. Priority is Low since it is an enhancement rather than a functional blocker, though still important for inclusivity.

---

## Severity / Priority Matrix

| Bug ID | Summary | Severity | Priority | Fix Timeline |
|------|--------|---------|----------|--------------|
| BUG-001 | Direct checkout access | S2 | P1 | This sprint |
| BUG-002 | Zip validation missing | S3 | P2 | Next sprint |
| BUG-003 | No undo on remove | S4 | P3 | Backlog |
| BUG-004 | Sort label mismatch | S3 | P2 | Next sprint |
| BUG-005 | Mobile badge overlap | S3 | P2 | Next sprint |
| BUG-006 | Mismatched images | S3 | P2 | Next sprint |
| BUG-007 | Back button state issue | S3 | P2 | Next sprint |
| BUG-008 | Persistent error message | S4 | P3 | Backlog |
| BUG-009 | Slow login feedback | S3 | P2 | Next sprint |
| BUG-010 | Weak focus indicator | S4 | P3 | Backlog |

---

## Analysis

**Most critical bug:** BUG-001 (S2 / P1)  
- Affects checkout integrity and security-related state validation.

**Most common severity:** S3 (Medium) – 5 bugs  
**Most common priority:** P2 (Medium) – 5 bugs  

**Interesting cases:**
- **Low Severity + High Visibility:** BUG-005 (mobile UI issue)
- **State-related risks:** BUG-001, BUG-007

**Recommended Fix Order:**
1. BUG-001
2. BUG-002
3. BUG-004
4. BUG-005
5. BUG-007

---

## Reflection

**What was challenging about classification?**  
Balancing technical impact versus business urgency, especially for UX and state-related issues.

**Did any bugs surprise you?**  
BUG-001 stood out as more serious than it initially appeared due to its security/state implications.

**How would you explain severity vs priority to a non-technical stakeholder?**  
Severity describes how broken something is, while priority describes how urgently the business needs it fixed. A bug can be severe but not urgent, or urgent even if technically minor.
