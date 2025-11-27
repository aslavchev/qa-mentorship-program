# Week 2: Test Levels - Exercises

## Exercise 1: Test Level Identification (30 minutes)

### Objective
Practice categorizing test scenarios into appropriate test levels.

### Instructions

For each test scenario below, identify the test level (Unit, Integration, System, or Acceptance) and justify your answer.

| # | Test Scenario | Level | Justification |
|---|---------------|-------|---------------|
| 1 | Verify `calculateTotal()` function returns correct sum | | |
| 2 | User can log in and see products page | | |
| 3 | Shopping cart updates when product is added via API | | |
| 4 | Password encryption function works correctly | | |
| 5 | Complete purchase flow from login to confirmation | | |
| 6 | Database stores user credentials correctly | | |
| 7 | Frontend displays data from backend API | | |
| 8 | New user can complete first purchase without help | | |
| 9 | Sorting function arranges products alphabetically | | |
| 10 | Payment gateway integrates with checkout system | | |

Continue for scenarios 11-20...

---

## Exercise 2: SauceDemo Test Level Mapping (45 minutes)

### Objective
Map all SauceDemo features to appropriate test levels.

### Instructions

Create a comprehensive matrix showing which test levels apply to each SauceDemo feature.

**Template:**

| Feature/Module | Unit | Integration | System | Acceptance | Notes |
|----------------|------|-------------|--------|------------|-------|
| **Authentication** | | | | | |
| - Login validation | ❌ (no access to code) | ✅ | ✅ | ✅ | |
| - Session management | ❌ | ✅ | ✅ | ✅ | |
| - Logout | ❌ | ✅ | ✅ | ✅ | |
| **Product Catalog** | | | | | |
| - Display products | | | | | |
| - Product details | | | | | |
| - Sorting | | | | | |
| - Filtering | | | | | |
| **Shopping Cart** | | | | | |
| - Add to cart | | | | | |
| - Remove from cart | | | | | |
| - Update quantity | | | | | |
| - Calculate total | | | | | |
| **Checkout** | | | | | |
| - Form validation | | | | | |
| - Information step | | | | | |
| - Overview step | | | | | |
| - Complete purchase | | | | | |

**Questions to Answer:**
1. Which features require testing at all levels?
2. Which features can skip certain levels? Why?
3. Where would you focus most effort if time is limited?

### Deliverable
Save as `mentee-work/week-02/saucedemo-test-matrix.md`

---

## Exercise 3: Entry/Exit Criteria (45 minutes)

### Objective
Define clear entry and exit criteria for each test level.

### Instructions

Complete the following tables for SauceDemo testing:

### Unit Testing (if you had access to code)

**Entry Criteria:**
- [ ] Code written and compiles
- [ ] Unit test framework set up
- [ ] ___________________
- [ ] ___________________

**Exit Criteria:**
- [ ] All unit tests pass
- [ ] Code coverage > 80%
- [ ] ___________________
- [ ] ___________________

### Integration Testing

**Entry Criteria:**
- [ ] Unit testing complete
- [ ] Modules ready for integration
- [ ] Integration test environment available
- [ ] ___________________
- [ ] ___________________

**Exit Criteria:**
- [ ] All integration tests pass
- [ ] API contracts validated
- [ ] ___________________
- [ ] ___________________

### System Testing

**Entry Criteria:**
- [ ] Integration testing complete (>90% pass)
- [ ] QA test environment stable
- [ ] All features development complete
- [ ] Test cases reviewed and approved
- [ ] ___________________

**Exit Criteria:**
- [ ] All system tests executed (>95%)
- [ ] Pass rate > 90%
- [ ] No critical/high defects open
- [ ] ___________________
- [ ] ___________________

### Acceptance Testing

**Entry Criteria:**
- [ ] System testing complete
- [ ] All P0/P1 defects resolved
- [ ] Staging environment ready
- [ ] UAT participants available
- [ ] ___________________

**Exit Criteria:**
- [ ] All UAT scenarios passed
- [ ] Business sign-off received
- [ ] No showstopper issues
- [ ] ___________________
- [ ] ___________________

### Deliverable
Save as `mentee-work/week-02/entry-exit-criteria.md`

---

## Exercise 4: Integration Test Scenarios (45 minutes)

### Objective
Write integration test scenarios for SauceDemo component interactions.

### Instructions

Write 5 detailed integration test scenarios testing interactions between SauceDemo components.

**Template for each scenario:**

```markdown
### Integration Test Scenario #X

**Test ID:** INT-XXX
**Test Title:** [Clear title]
**Components Under Test:** Component A ↔ Component B

**Objective:**
What integration are you validating?

**Preconditions:**
- Precondition 1
- Precondition 2

**Test Steps:**
1. Step 1
2. Step 2
3. Step 3

**Expected Result:**
What should happen when components interact correctly?

**Data Flow:**
Component A → [data] → Component B → [result]

**Pass Criteria:**
- Criteria 1
- Criteria 2
```

**Example Integration Scenarios to Write:**

1. **Login API ↔ Product Catalog**
   - Verify authenticated user can access product catalog
   - Verify session token is passed correctly

2. **Product Catalog ↔ Shopping Cart**
   - Verify adding product updates cart via API
   - Verify cart count updates in UI

3. **Shopping Cart ↔ Checkout**
   - Verify cart items are passed to checkout
   - Verify totals match between cart and checkout

4. **Checkout Form ↔ Payment System**
   - Verify form data is sent to payment processing
   - Verify payment confirmation returns to app

5. **Order Completion ↔ Confirmation**
   - Verify order details are saved
   - Verify confirmation page displays correct information

### Deliverable
Save as `mentee-work/week-02/integration-scenarios.md`

---

## Exercise 5: System Test Scenarios (60 minutes)

### Objective
Write end-to-end system test scenarios for SauceDemo.

### Instructions

Write 10 comprehensive system test scenarios covering major SauceDemo workflows.

**Template:**

```markdown
### System Test Scenario #X

**Test ID:** SYS-XXX
**Test Title:** [User-focused title]
**Test Type:** End-to-End / Workflow / Functional

**User Story:**
As a [user type], I want to [action], so that [benefit].

**Preconditions:**
- Application is accessible
- Test data is prepared

**Test Steps:**
1. Navigate to...
2. Enter...
3. Click...
[Detailed step-by-step]

**Expected Results:**
- Result 1
- Result 2
- Overall outcome

**Test Data:**
- Username: standard_user
- Password: secret_sauce
- Product: [specific product]

**Verification Points:**
- [ ] Checkpoint 1
- [ ] Checkpoint 2
- [ ] Final verification
```

**10 System Scenarios to Write:**

1. **Happy Path - Complete Purchase**
   - Login → Browse → Add to Cart → Checkout → Confirm

2. **Product Browsing and Sorting**
   - Login → Sort products (all options) → Verify order

3. **Cart Management**
   - Login → Add multiple items → Update quantities → Remove items → Verify total

4. **Checkout Form Validation**
   - Login → Add item → Go to checkout → Test form validation

5. **Multi-item Purchase**
   - Login → Add 3 different products → Complete checkout

6. **Cancel and Resume Shopping**
   - Login → Add to cart → Start checkout → Cancel → Continue shopping

7. **Invalid Login Handling**
   - Try invalid credentials → Verify error → Successful login

8. **Product Detail Navigation**
   - Login → View product details → Add to cart → Verify in cart

9. **Logout and Session Management**
   - Login → Add to cart → Logout → Login again → Verify cart state

10. **Complete Flow with Different User Types**
    - Test with standard_user, problem_user, performance_glitch_user

### Deliverable
Save as `mentee-work/week-02/system-scenarios.md`

---

## 🎯 Bonus Exercise (Optional)

### Create a Test Level Strategy Document

Write a 2-3 page document answering:

1. **If you were the QA lead for SauceDemo, how would you allocate testing effort across levels?**
   - X% Unit (developers)
   - X% Integration (dev + QA)
   - X% System (QA)
   - X% Acceptance (users + QA)

2. **What would be your test pyramid for SauceDemo?**
   - Draw the pyramid
   - Justify the distribution

3. **What are the risks of skipping each level?**
   - Risk of no unit testing
   - Risk of no integration testing
   - Risk of no system testing
   - Risk of no acceptance testing

### Deliverable
Save as `mentee-work/week-02/test-level-strategy.md`

---

## ✅ Exercise Completion Checklist

- [ ] Exercise 1: Test level identification completed
- [ ] Exercise 2: SauceDemo test matrix created
- [ ] Exercise 3: Entry/Exit criteria defined
- [ ] Exercise 4: 5 integration scenarios written
- [ ] Exercise 5: 10 system scenarios written
- [ ] All deliverables saved in week-02 folder
- [ ] All files committed to GitHub
- [ ] Ready for mentor session

---

## 📤 Submission

1. Create folder: `mentee-work/week-02/`
2. Save all deliverables
3. Commit with message:
   ```
   Week 2 complete: Test levels analysis and scenarios
   ```
4. Prepare to discuss in mentor session

---

**Time Estimate:** 3-4 hours total for all exercises
