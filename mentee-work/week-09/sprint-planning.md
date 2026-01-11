# Sprint Planning

## Sprint Details

- **Sprint Duration:** 2 weeks (10 business days)
- **Team Capacity:** 40 hours (1 QA × 8 hours × 5 days)
- **Velocity:** 20 story points
- **Sprint:** Sprint 1

---

## Sprint 1 – Selected Stories

| Story ID | User Story | Story Points | Hours Estimate | Why Selected? |
|--------|------------|--------------|----------------|---------------|
| US-001 | User Login | 5 | 10 hours | High priority, no dependencies, foundational feature |
| US-002 | Add Items to Cart | 8 | 16 hours | High priority, core shopping functionality |
| US-003 | Product Sorting | 3 | 6 hours | Medium priority, simple functionality |
| US-005 | Remove from Cart | 5 | 10 hours | Medium priority, complements add-to-cart |

**Total:**  
- **Story Points:** 21  
- **Estimated Hours:** 42 hours (slightly above capacity, manageable risk)

---

## Testing Task Breakdown

### US-001: User Login (5 Story Points – 10 Hours)

**Testing Tasks:**
- [ ] Review acceptance criteria with team (30 min)
- [ ] Prepare test data (valid, invalid, locked users) (30 min)
- [ ] Write test cases (positive, negative, security) (2 hours)
- [ ] Execute smoke tests (happy path) (1 hour)
- [ ] Execute functional tests (all scenarios) (2 hours)
- [ ] Execute security tests (SQL injection, XSS) (1 hour)
- [ ] Cross-browser testing (Chrome, Firefox, Edge) (1.5 hours)
- [ ] Regression testing (verify no impact on other modules) (1 hour)
- [ ] Document test results and defects (30 min)

**Total:** 10 hours

---

### US-002: Add Items to Cart (8 Story Points – 16 Hours)

**Testing Tasks:**
- [ ] Review acceptance criteria (30 min)
- [ ] Prepare test data (products, cart states) (1 hour)
- [ ] Write test cases (add, badge update, persistence) (3 hours)
- [ ] Execute functional tests (4 hours)
- [ ] Execute boundary tests (0, 1, 6 items) (1 hour)
- [ ] Execute state transition tests (empty → items → checkout) (2 hours)
- [ ] Cross-browser testing (2 hours)
- [ ] Basic performance check (cart load time) (1 hour)
- [ ] Regression testing (2 hours)
- [ ] Document test results (30 min)

**Total:** 16 hours

---

### US-003: Product Sorting (3 Story Points – 6 Hours)

**Testing Tasks:**
- [ ] Review acceptance criteria (15 min)
- [ ] Write test cases for all sorting options (1.5 hours)
- [ ] Execute functional tests (A–Z, Z–A, Price low/high) (2 hours)
- [ ] Verify UI consistency after sorting (1 hour)
- [ ] Regression testing (1 hour)
- [ ] Document test results (15 min)

**Total:** 6 hours

---

### US-005: Remove from Cart (5 Story Points – 10 Hours)

**Testing Tasks:**
- [ ] Review acceptance criteria (30 min)
- [ ] Prepare test data (single and multiple items) (30 min)
- [ ] Write test cases (remove from cart, badge update) (2 hours)
- [ ] Execute functional tests (2.5 hours)
- [ ] Verify empty cart state behavior (1 hour)
- [ ] Cross-browser testing (1.5 hours)
- [ ] Regression testing (1.5 hours)
- [ ] Document test results (30 min)

**Total:** 10 hours

---

## Sprint Risks and Mitigation

| Risk ID | Risk Description | Probability | Impact | Mitigation Strategy |
|-------|------------------|------------|--------|---------------------|
| R-001 | US-002 depends on US-001 | High | High | Complete US-001 early in sprint |
| R-002 | Sprint over capacity (42h vs 40h) | High | Medium | De-scope US-005 if needed |
| R-003 | Test environment instability | Medium | High | Report early, use backup browser |
| R-004 | Late cross-browser issues | Low | Medium | Run cross-browser tests early |
| R-005 | Acceptance criteria unclear | Medium | Medium | Clarify with PO before testing |

---

## Sprint Goal

**Primary Goal:**  
Enable users to log in and manage their shopping cart (add and remove items).

---

## Sprint Success Criteria

- ✅ User login works for valid credentials
- ✅ Users can add products to cart
- ✅ Users can remove items from cart
- ✅ Cart badge shows correct item count
- ✅ Product sorting works correctly
- ✅ All acceptance criteria met
- ✅ Definition of Done met for all stories
- ✅ No open critical or high-severity defects

---

## Sprint Metrics

- **Planned Stories:** 4  
- **Planned Story Points:** 21  
- **Planned Testing Hours:** 42  
- **Target Velocity:** 20 story points

## Stories Deferred from Sprint 1

The following stories were intentionally not selected for this sprint:

- **US-004: Checkout Process (13 story points)**  
  Deferred because it is a large story and depends on successful completion of US-001 (Login) and US-002 (Add to Cart).

- **US-006: View Product Details (3 story points)**  
  Lower priority and does not impact core shopping flow.

- **US-007: Search Products (8 story points)**  
  Low business priority and outside current sprint goal.

This helps the team focus on foundational functionality and reduces delivery risk.


---

## Notes

This sprint focuses on core user flows and foundational functionality.  
Lower-priority features (checkout, search) are intentionally deferred to reduce risk.
