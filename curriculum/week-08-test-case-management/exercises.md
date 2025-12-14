# Week 8: Test Case Design & Management - Exercises

## Exercise Overview
This week focuses on applying Test Case Design & Management concepts to SauceDemo.
Complete all exercises and document your work in `mentee-work/week-08/`

**Total Time:** ~7 hours (420 minutes)

---

## Exercise 1: Write 50+ Test Cases (180 min)

### Objective
Create comprehensive, professional test cases for SauceDemo covering all major modules using systematic test design techniques.

### Target Breakdown

Write **at least 50 test cases** distributed across modules:

| Module | Minimum Test Cases | Test Design Focus |
|--------|-------------------|-------------------|
| **Login (Authentication)** | 15 | EP, BVA, Security (SQL injection) |
| **Product Browsing & Sorting** | 10 | EP, Decision Tables (filter combinations) |
| **Shopping Cart** | 15 | State Transitions, BVA (quantity) |
| **Checkout Flow** | 20 | Decision Tables (form validation), E2E |
| **TOTAL** | **60+** | **Mixed techniques** |

### Instructions

**Step 1: Review Tutorial Examples (15 min)**

Re-read tutorial.md sections:
- Section 1: Anatomy of a Good Test Case (lines 27-262)
- Section 2: Test Design Techniques Applied (lines 266-370)
- Section 8: SauceDemo Complete Test Case Examples (lines 928-1066)

**Step 2: Review Test Case Template (10 min)**

Open `curriculum/templates/test-case-template.md` - you'll use this format for each test case.

**Step 3: Create Test Cases by Module (150 min)**

For each module, create test cases in this order:

#### Module 1: Login/Authentication (15 test cases, 35 min)

**Required Test Cases:**
1. TC-LOGIN-001: Verify login with valid credentials (standard_user)
2. TC-LOGIN-002: Verify login with another valid user (problem_user)
3. TC-LOGIN-003: Verify login fails with invalid username
4. TC-LOGIN-004: Verify login fails with invalid password
5. TC-LOGIN-005: Verify login fails with empty username
6. TC-LOGIN-006: Verify login fails with empty password
7. TC-LOGIN-007: Verify login fails with empty both fields
8. TC-LOGIN-008: Verify locked user cannot login (locked_out_user)
9. TC-LOGIN-009: Verify login with special characters in username
10. TC-LOGIN-010: Verify login fails with SQL injection attempt (' OR '1'='1)
11. TC-LOGIN-011: Verify password is masked (dots/asterisks)
12. TC-LOGIN-012: Verify login button is clickable
13. TC-LOGIN-013: Verify error message for invalid credentials
14. TC-LOGIN-014: Verify successful logout
15. TC-LOGIN-015: Verify user cannot access inventory without login

**Techniques Used:**
- Equivalence Partitioning (valid users, invalid users, locked users, empty inputs)
- Boundary Value Analysis (empty strings, special chars)
- Security testing (SQL injection)
- State testing (logged in vs logged out)

#### Module 2: Products/Inventory (10 test cases, 25 min)

**Required Test Cases:**
1. TC-PRODUCTS-001: Verify all 6 products display on inventory page
2. TC-PRODUCTS-002: Verify product images load correctly
3. TC-PRODUCTS-003: Verify product names are visible
4. TC-PRODUCTS-004: Verify product prices are displayed
5. TC-SORT-001: Verify sort by Name (A to Z)
6. TC-SORT-002: Verify sort by Name (Z to A)
7. TC-SORT-003: Verify sort by Price (low to high)
8. TC-SORT-004: Verify sort by Price (high to low)
9. TC-PRODUCTS-005: Verify product detail page opens
10. TC-PRODUCTS-006: Verify back button returns to inventory

**Techniques Used:**
- Positive testing (happy path)
- Boundary testing (sorting edge cases)

#### Module 3: Shopping Cart (15 test cases, 40 min)

**Required Test Cases:**
1. TC-CART-001: Verify add item to cart from inventory page
2. TC-CART-002: Verify add item to cart from product detail page
3. TC-CART-003: Verify cart badge updates when item added
4. TC-CART-004: Verify cart displays added item
5. TC-CART-005: Verify remove item from cart
6. TC-CART-006: Verify cart badge updates when item removed
7. TC-CART-007: Verify add multiple different items
8. TC-CART-008: Verify add same item twice (if allowed)
9. TC-CART-009: Verify cart total calculation is correct
10. TC-CART-010: Verify cart persists across page navigation
11. TC-CART-011: Verify empty cart displays correctly
12. TC-CART-012: Verify Continue Shopping button returns to inventory
13. TC-CART-013: Verify Checkout button navigates to checkout
14. TC-CART-014: Verify cart with 1 item (boundary: minimum)
15. TC-CART-015: Verify cart with all 6 items (boundary: maximum)

**Techniques Used:**
- State Transition (empty → has items → checkout)
- Boundary Value Analysis (0 items, 1 item, 6 items)
- Positive/Negative testing

#### Module 4: Checkout (20 test cases, 50 min)

**Required Test Cases:**
1. TC-CHECKOUT-001: Verify checkout with all valid information
2. TC-CHECKOUT-002: Verify checkout fails with empty first name
3. TC-CHECKOUT-003: Verify checkout fails with empty last name
4. TC-CHECKOUT-004: Verify checkout fails with empty zip code
5. TC-CHECKOUT-005: Verify checkout fails with all fields empty
6. TC-CHECKOUT-006: Verify checkout with maximum length first name (50 chars)
7. TC-CHECKOUT-007: Verify checkout with maximum length last name (50 chars)
8. TC-CHECKOUT-008: Verify checkout with maximum length zip code (10 chars)
9. TC-CHECKOUT-009: Verify checkout with special characters in name (O'Brien)
10. TC-CHECKOUT-010: Verify Continue button navigates to overview page
11. TC-CHECKOUT-011: Verify Cancel button returns to cart
12. TC-CHECKOUT-012: Verify overview page displays correct item
13. TC-CHECKOUT-013: Verify overview page displays correct total
14. TC-CHECKOUT-014: Verify overview page displays tax calculation
15. TC-CHECKOUT-015: Verify Finish button completes order
16. TC-CHECKOUT-016: Verify order confirmation page displays
17. TC-CHECKOUT-017: Verify order confirmation message appears
18. TC-CHECKOUT-018: Verify Back Home button returns to inventory
19. TC-CHECKOUT-019: Verify cart is empty after order completion
20. TC-CHECKOUT-020: Verify End-to-End smoke test (login→add→checkout→finish)

**Techniques Used:**
- Decision Tables (form validation combinations)
- Boundary Value Analysis (field lengths)
- End-to-End testing (full user journey)

**Step 4: Format Test Cases (5 min)**

For each test case, include these **required fields** (from template):
- ✅ Test Case ID (TC-MODULE-###)
- ✅ Test Case Title
- ✅ Module
- ✅ Test Type (UI, Smoke, Regression, E2E, etc.)
- ✅ Severity (S0-S4)
- ✅ Test Objective (1-2 sentences)
- ✅ Preconditions
- ✅ Test Steps (numbered, specific actions)
- ✅ Expected Results (for each step or overall)
- ✅ Test Data (if applicable)

### Deliverable

Save as `mentee-work/week-08/write-50+-test-cases.md`

**Format:**
```markdown
# SauceDemo Test Cases

## Module: Login/Authentication

### TC-LOGIN-001: Verify login with valid credentials

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-LOGIN-001 |
| **Module** | Login |
| **Test Type** | Smoke |
| **Severity** | S1-Critical |

**Test Objective:**
Verify that a user with valid credentials can successfully log in and is redirected to the inventory page.

**Preconditions:**
- SauceDemo application is accessible
- User account exists: standard_user / secret_sauce
- No active session (clear cookies)

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to https://www.saucedemo.com | Login page displays |
| 2 | Enter "standard_user" in Username | Text appears |
| 3 | Enter "secret_sauce" in Password | Password masked |
| 4 | Click LOGIN button | Redirect to /inventory.html, 6 products visible |

---

[... Continue for all 50+ test cases ...]
```

### Success Criteria
- ✅ Minimum 50 test cases created
- ✅ All modules covered (Login: 15+, Products: 10+, Cart: 15+, Checkout: 20+)
- ✅ All required fields present in each test case
- ✅ Test case IDs use TC-[MODULE]-[###] format
- ✅ Specific, measurable steps and expected results
- ✅ Mix of positive and negative test cases
- ✅ Test design techniques applied (EP, BVA, Decision Tables, State Transition)

---

## Exercise 2: Organize by Module (60 min)

### Objective
Structure your 50+ test cases into a logical, maintainable organization using modules, priorities, and test suites.

### Instructions

**Step 1: Create Module Organization (20 min)**

Reorganize your test cases into this folder structure within your markdown file:

```markdown
# SauceDemo Test Suite Organization

## 📁 Test Suite Structure

### Module 1: Login/Authentication (15 tests)
- **Priority:** S0-S1 (5 tests) - Critical path
- **Priority:** S2-S3 (10 tests) - Standard coverage

### Module 2: Product Browsing (10 tests)
- **Priority:** S1-S2 (6 tests) - Core functionality
- **Priority:** S3-S4 (4 tests) - Secondary features

### Module 3: Shopping Cart (15 tests)
- **Priority:** S0-S1 (7 tests) - Critical cart operations
- **Priority:** S2-S3 (8 tests) - Edge cases

### Module 4: Checkout (20 tests)
- **Priority:** S0-S1 (10 tests) - Payment-critical
- **Priority:** S2-S3 (10 tests) - Validation edge cases
```

**Step 2: Create Priority Matrix (15 min)**

Create a table showing test distribution by priority:

| Priority | Count | % of Total | Examples |
|----------|-------|------------|----------|
| **S0-Blocker** | X | X% | TC-LOGIN-001, TC-CHECKOUT-020 |
| **S1-Critical** | X | X% | TC-CART-001, TC-CHECKOUT-001 |
| **S2-Major** | X | X% | TC-SORT-001, TC-CART-010 |
| **S3-Minor** | X | X% | TC-PRODUCTS-005, TC-LOGIN-011 |
| **S4-Trivial** | X | X% | TC-PRODUCTS-002 (if any) |
| **TOTAL** | 50+ | 100% | |

**Step 3: Create Test Suite Assignments (15 min)**

Assign your test cases to test suites:

**Smoke Suite (10-15 tests):**
- Critical path must-pass tests
- Examples: TC-LOGIN-001, TC-CART-001, TC-CHECKOUT-001, TC-CHECKOUT-020

**Regression Suite (30-40 tests):**
- All S0-S2 tests
- Re-run after any code changes

**Full Suite (All 50+ tests):**
- Complete test coverage
- Run before major releases

Create a table:

| Suite | Test Count | Test IDs | Execution Time Estimate |
|-------|------------|----------|-------------------------|
| **Smoke** | 10-15 | TC-LOGIN-001, TC-CART-001, ... | ~30 minutes |
| **Regression** | 30-40 | All S0-S2 tests | ~2 hours |
| **Full** | 50+ | All tests | ~3 hours |

**Step 4: Create Test Execution Order (10 min)**

Define recommended execution order:

```markdown
## Recommended Execution Order

### Phase 1: Smoke Testing (Run First)
1. Authentication tests (TC-LOGIN-001 to TC-LOGIN-003)
2. Critical cart test (TC-CART-001)
3. Critical checkout test (TC-CHECKOUT-001)
4. End-to-end smoke (TC-CHECKOUT-020)

### Phase 2: Module Testing
1. Complete Login module (TC-LOGIN-001 to TC-LOGIN-015)
2. Complete Products module (TC-PRODUCTS-001 to TC-SORT-004)
3. Complete Cart module (TC-CART-001 to TC-CART-015)
4. Complete Checkout module (TC-CHECKOUT-001 to TC-CHECKOUT-020)

### Phase 3: Regression Suite
- Re-run all S0-S2 tests after any code change
```

### Deliverable

Save as `mentee-work/week-08/organize-by-module.md`

Include:
- Module breakdown with counts
- Priority matrix
- Test suite assignments
- Execution order recommendations

### Success Criteria
- ✅ Test cases organized by module
- ✅ Priority distribution calculated
- ✅ Test suites defined (Smoke, Regression, Full)
- ✅ Execution order documented
- ✅ Clear navigation structure

---

## Exercise 3: Traceability Matrix (60 min)

### Objective
Create a Requirements Traceability Matrix (RTM) mapping Week 7 Test Plan requirements to your Week 8 test cases, proving 100% coverage.

### Instructions

**Step 1: Extract Requirements from Week 7 Test Plan (15 min)**

Review your `mentee-work/week-07/test-plan-creation.md` and list all functional requirements.

If your Test Plan doesn't have explicit requirements, create them now based on SauceDemo functionality:

**Minimum 13 Requirements:**
1. REQ-AUTH-001: User can login with valid credentials
2. REQ-AUTH-002: User cannot login with invalid credentials
3. REQ-AUTH-003: Locked user cannot login
4. REQ-AUTH-004: User can logout successfully
5. REQ-PROD-001: User can view all products
6. REQ-PROD-002: User can sort products by name
7. REQ-PROD-003: User can sort products by price
8. REQ-CART-001: User can add items to cart
9. REQ-CART-002: User can remove items from cart
10. REQ-CART-003: Cart displays correct total
11. REQ-CHKT-001: User can enter checkout information
12. REQ-CHKT-002: Checkout validates required fields
13. REQ-CHKT-003: User can complete order

**Step 2: Create RTM Table (30 min)**

Use the template from `curriculum/templates/traceability-matrix-template.md`

Create main RTM table:

| Req ID | Requirement Description | Priority | Test Case IDs | Test Count | Coverage |
|--------|------------------------|----------|---------------|------------|----------|
| REQ-AUTH-001 | User can login with valid credentials | Critical | TC-LOGIN-001, TC-LOGIN-002 | 2 | ✅ 100% |
| REQ-AUTH-002 | User cannot login with invalid credentials | Critical | TC-LOGIN-003, TC-LOGIN-004, TC-LOGIN-005, TC-LOGIN-006, TC-LOGIN-007 | 5 | ✅ 100% |
| REQ-AUTH-003 | Locked user cannot login | High | TC-LOGIN-008 | 1 | ✅ 100% |
| ... | ... | ... | ... | ... | ... |

**Step 3: Calculate Coverage Metrics (10 min)**

**Requirements Coverage:**
```
Total Requirements: 13
Requirements with Tests: X
Requirements Coverage = (X / 13) × 100% = ?%
```

**Test Case Distribution:**
```
Total Test Cases: 50+
Mapped to Requirements: X
Orphaned Tests (no requirement): X
```

**Module Coverage:**
| Module | Requirements | Tests Covering | Coverage % |
|--------|--------------|----------------|------------|
| Authentication | 4 | 15 | 375% (multiple tests per req) |
| Products | 3 | 10 | 333% |
| Cart | 3 | 15 | 500% |
| Checkout | 3 | 20 | 667% |

**Step 4: Gap Analysis (5 min)**

Identify gaps:

```markdown
## Coverage Gaps

### Requirements Without Tests
- None - All requirements have test cases ✅

### Test Cases Without Requirements
- [List any orphaned tests, if any]

### Under-Tested Requirements (< 2 tests)
- [List requirements with only 1 test case]

### Recommendations
- [Suggest additional tests for under-covered requirements]
```

### Deliverable

Save as `mentee-work/week-08/traceability-matrix.md`

Use template structure from `curriculum/templates/traceability-matrix-template.md`:
- Document Control section
- Purpose statement
- Main RTM table
- Summary Statistics
- Module-by-module breakdown
- Forward traceability (Requirements → Tests)
- Backward traceability (Tests → Requirements)
- Gap Analysis

### Success Criteria
- ✅ All 13+ requirements listed
- ✅ Every requirement has at least 1 test case
- ✅ All 50+ test cases mapped to requirements
- ✅ Coverage % calculated
- ✅ Gap analysis completed
- ✅ No orphaned tests or untested requirements

---

## Exercise 4: Test Data Management (45 min)

### Objective
Design and document test data strategy for SauceDemo, including valid, invalid, boundary, and security test data.

### Instructions

**Step 1: Document Valid Test Data (10 min)**

Create tables for valid happy-path data:

```markdown
# SauceDemo Test Data Management

## Valid Test Data

### Users (Valid Login Credentials)

| Username | Password | User Type | Notes |
|----------|----------|-----------|-------|
| standard_user | secret_sauce | Standard | Default happy-path user |
| problem_user | secret_sauce | Problem | Has issues (for negative testing) |
| performance_glitch_user | secret_sauce | Performance | Slow responses |

### Products (Available Items)

| Product ID | Product Name | Price | Notes |
|------------|--------------|-------|-------|
| 1 | Sauce Labs Backpack | $29.99 | Most common test item |
| 2 | Sauce Labs Bike Light | $9.99 | Lowest price |
| 3 | Sauce Labs Bolt T-Shirt | $15.99 | Mid-range |
| 4 | Sauce Labs Fleece Jacket | $49.99 | Highest price |
| 5 | Sauce Labs Onesie | $7.99 | Boundary test |
| 6 | Test.allTheThings() T-Shirt (Red) | $15.99 | Special chars in name |

### Checkout Information (Valid Data)

| Field | Valid Examples |
|-------|---------------|
| First Name | John, Jane, Alex, Maria, José, François |
| Last Name | Doe, Smith, Johnson, Garcia, O'Brien, Müller |
| Zip Code | 12345, 90210, 10001, 75001, 94105 |
```

**Step 2: Document Invalid Test Data (10 min)**

```markdown
## Invalid Test Data

### Invalid Login Credentials

| Test Scenario | Username | Password | Expected Error |
|---------------|----------|----------|----------------|
| Wrong username | wrong_user | secret_sauce | "Username and password do not match" |
| Wrong password | standard_user | wrong_pass | "Username and password do not match" |
| Empty username | [empty] | secret_sauce | "Username is required" |
| Empty password | standard_user | [empty] | "Password is required" |
| Both empty | [empty] | [empty] | "Username is required" |
| Locked user | locked_out_user | secret_sauce | "Sorry, this user has been locked out" |

### Invalid Checkout Data

| Field | Invalid Values | Purpose |
|-------|---------------|---------|
| First Name | [empty], `<script>`, `123456`, `!@#$%` | Required field, XSS, numbers, special chars |
| Last Name | [empty], `--`, `"OR 1=1`, `😀🎉` | Required field, SQL injection, emojis |
| Zip Code | [empty], `ABC123`, `-12345`, `9999999999` | Required field, alpha, negative, too long |
```

**Step 3: Document Boundary Test Data (10 min)**

```markdown
## Boundary Value Test Data

### Cart Quantity Boundaries

| Boundary | Value | Expected Behavior |
|----------|-------|-------------------|
| Minimum - 1 | 0 items | Invalid (cart is empty) |
| Minimum | 1 item | Valid (minimum cart) |
| Minimum + 1 | 2 items | Valid |
| Maximum | 6 items | Valid (all products) |

### Field Length Boundaries

| Field | Min Valid | Max Valid | Test Values |
|-------|-----------|-----------|-------------|
| First Name | 1 char | 50 chars | "A", "AAAA...A" (50 chars) |
| Last Name | 1 char | 50 chars | "B", "BBBB...B" (50 chars) |
| Zip Code | 1 char | 10 chars | "1", "1234567890" |
```

**Step 4: Document Security Test Data (10 min)**

```markdown
## Security Test Data (For Negative Testing)

### SQL Injection Payloads

| Payload | Purpose |
|---------|---------|
| `' OR '1'='1` | Basic SQL injection attempt |
| `admin'--` | Comment-based injection |
| `1' UNION SELECT NULL--` | Union-based injection |

### XSS (Cross-Site Scripting) Payloads

| Payload | Purpose |
|---------|---------|
| `<script>alert('XSS')</script>` | Basic XSS |
| `<img src=x onerror=alert('XSS')>` | Image-based XSS |
| `javascript:alert('XSS')` | JavaScript protocol |

**Note:** These should all be **rejected** by the application. Include in test cases to verify input sanitization.
```

**Step 5: Create Test Data Files (5 min)**

Document how test data would be stored:

```markdown
## Test Data File Organization

Recommended structure (for future automation):

```
test-data/
├── users.csv               (valid users)
├── users-invalid.csv       (invalid users)
├── products.json           (product catalog)
├── checkout-valid.csv      (valid checkout data)
├── checkout-invalid.csv    (invalid checkout data)
├── boundary-values.csv     (boundary test values)
├── security-payloads.txt   (SQL injection, XSS)
```

**Example: users.csv**
```csv
username,password,expected_result,user_type
standard_user,secret_sauce,success,standard
problem_user,secret_sauce,success,problem
locked_out_user,secret_sauce,locked,locked
wrong_user,secret_sauce,invalid,invalid
standard_user,wrong_pass,invalid,invalid
```
```

### Deliverable

Save as `mentee-work/week-08/test-data-management.md`

Include:
- Valid test data tables
- Invalid test data tables
- Boundary value data
- Security test data (SQL injection, XSS)
- Test data file organization plan

### Success Criteria
- ✅ All SauceDemo users documented
- ✅ All 6 products documented
- ✅ Valid and invalid checkout data listed
- ✅ Boundary values identified
- ✅ Security payloads documented
- ✅ Test data organization proposed

---

## Exercise 5: Test Case Review (45 min)

### Objective
Peer-review your own test cases against quality checklist, identify improvements, and document learnings.

### Instructions

**Step 1: Select 10 Test Cases for Review (5 min)**

Choose a diverse sample:
- 3 Login tests (including 1 positive, 1 negative, 1 security)
- 2 Product tests
- 3 Cart tests
- 2 Checkout tests

**Step 2: Apply Review Checklist (30 min)**

For each of the 10 test cases, use this checklist from tutorial.md Section 6:

```markdown
## Test Case Review - TC-LOGIN-001

### Completeness
- [x] All required fields filled (ID, title, steps, expected results)
- [x] Preconditions clearly stated
- [x] Test data specified
- [x] Expected result for each step
- [x] Linked to requirement ID

### Clarity
- [x] Title is clear and specific
- [ ] Steps are unambiguous (no "etc.", "and so on")  ← NEEDS FIX
- [x] One action per step
- [x] Uses exact field names, button names
- [ ] Expected results are specific (not "should work")  ← NEEDS FIX

### Correctness
- [x] Steps are in logical order
- [x] Expected results are accurate
- [x] Test data is valid for the scenario
- [x] No typos or grammatical errors

### Testability
- [x] Can be executed without additional information
- [x] Repeatable (same result each time)
- [x] Independent (doesn't depend on other tests)
- [x] Executable in reasonable time (< 10 min)

### Coverage
- [x] Positive scenario covered
- [ ] Negative scenario covered  ← ADD TC-LOGIN-003
- [x] Boundary values tested (if applicable)
- [x] No duplicate tests

**Issues Found:** 2
**Severity:** Minor

**Improvements Needed:**
1. Step 3 says "Enter password" - should say "Enter 'secret_sauce' in Password field"
2. Expected result says "Login works" - should say "User redirected to /inventory.html, 6 products visible"

**Action:** Update TC-LOGIN-001 with specific language
```

Repeat for all 10 selected test cases.

**Step 3: Summarize Findings (10 min)**

Create summary report:

```markdown
# Test Case Review Summary

## Test Cases Reviewed
10 test cases reviewed across all modules

## Issues Found by Category

| Category | Issues | % of Reviews | Examples |
|----------|--------|--------------|----------|
| Completeness | 2 | 20% | Missing preconditions in TC-CART-005 |
| Clarity | 5 | 50% | Vague steps in TC-LOGIN-003, TC-CHECKOUT-002 |
| Correctness | 1 | 10% | Wrong expected result in TC-SORT-001 |
| Testability | 0 | 0% | All tests are executable |
| Coverage | 2 | 20% | Missing negative case for TC-CART-001 |
| **TOTAL** | **10** | | |

## Common Patterns

**Good Practices Used:**
- ✅ Consistent TC-[MODULE]-[###] naming
- ✅ All tests have preconditions
- ✅ Test data specified for all tests

**Improvement Areas:**
- ❌ Some expected results are vague ("should work", "displays correctly")
- ❌ Occasional multi-action steps ("Login and navigate to cart")
- ❌ Missing specific error messages in negative tests

## Action Items

1. Update 5 test cases with more specific expected results
2. Split multi-action steps in TC-CART-007 and TC-CHECKOUT-010
3. Add exact error message text to all negative tests
4. Consider adding 3 more boundary tests for cart quantity

## Learnings

**What I Learned:**
- Specific expected results prevent ambiguity during execution
- One action per step makes debugging failures easier
- Test independence is critical for parallel execution
- Boundary values often expose edge case bugs

**Will Apply Going Forward:**
- Always use exact button/field names
- Always specify exact error messages
- Review checklist before submitting test cases
- Ask: "Could someone else execute this without asking me questions?"
```

### Deliverable

Save as `mentee-work/week-08/test-case-review.md`

Include:
- Review checklist results for 10 test cases
- Issues found and severity
- Summary of findings
- Common patterns (good and bad)
- Action items
- Personal learnings

### Success Criteria
- ✅ 10 test cases reviewed
- ✅ Review checklist applied to each
- ✅ Issues documented with severity
- ✅ Improvements identified
- ✅ Summary report completed
- ✅ Learnings documented

---

## Exercise 6: GitHub Projects Test Management (60 min)

### Objective
Convert your test cases into GitHub issues for tracking and management using GitHub Projects

### Instructions

> **📋 Workflow:** Manually create 5-10 test cases to learn the process, then contact mentor to create automation script for remaining tests.

**Part 1: Manual Practice - Create 5-10 Test Case Issues (20 min)**

1. Navigate to: https://github.com/aslavchev/qa-fundamentals-11weeks/issues/new/choose
2. Select **"Test Case"** template
3. **Manually convert 5-10 diverse test cases** (select from different modules):
   - 2 Login tests (1 positive, 1 negative)
   - 2 Cart tests
   - 2 Checkout tests (including the E2E smoke test)
   - 3-4 additional tests of your choice
4. For each issue:
   - Use test case template
   - Title format: `[TEST] Brief description`
   - Add appropriate labels:
     - Test type: `test:ui`, `test:api`, `test:e2e`, `test:regression`, `test:smoke`, `test:integration`, `test:performance`
     - Severity: `severity:s0-blocker`, `severity:s1-critical`, `severity:s2-major`, `severity:s3-minor`, `severity:s4-trivial`
   - Add to "SauceDemo Test Suite" project
   - Set custom fields: Test Type, Test Suite, Severity, Module, Automation Status
   - Set Last Run Status to "Not Run"

**Part 2: Automate Remaining Tests - Contact Mentor (20 min)**

5. **📞 Contact your mentor** - you'll pair program to create a Python/Bash script that:
   - Parses your markdown test cases (from Exercise 1)
   - Bulk-creates remaining 40+ GitHub Issues using `gh` CLI
   - Automatically sets labels and custom fields
   - **Learning goal:** Test automation + API scripting (preview of Week 11 Python)

**Part 3: Explore Project Views (10 min)**

6. Open "SauceDemo Test Suite" GitHub Project
7. Explore views:
   - **Test Inventory:** See all test cases organized by module
   - **Regression Suite:** Board view of regression tests
   - **Automation Backlog:** Which tests need automation
   - **Test Execution Tracker:** Track test execution status
8. Practice filtering and sorting

**Part 4: Document Setup (10 min)**

9. Create documentation with:
- Total test cases created
- Breakdown by module (Login: X, Checkout: Y, etc.)
- Breakdown by severity (S0-S4)
- Screenshots of:
  - Test Inventory view
  - Regression Suite board
  - One example test case issue

### Deliverable

Save as `mentee-work/week-08/test-management-organization.md` including:
- Summary statistics
- Screenshots of project views
- One sample test case issue link
- Reflection: Benefits of using GitHub Projects for test management

### Tips

**Batch Creation:**
- Open multiple browser tabs with issue template
- Copy/paste test steps from your markdown test cases
- Save time by using consistent formatting

**Label Strategy:**
- Every test should have: 1 test type + 1 severity
- Example: `test:ui`, `test:regression`, `severity:s2-major`

**Custom Fields:**
- Test Type: UI, API, E2E, Regression, Smoke, Integration, Performance
- Test Suite: Regression, Smoke, Full, Sanity, Exploratory
- Severity: S0-Blocker, S1-Critical, S2-Major, S3-Minor, S4-Trivial
- Module: Login, Inventory, Cart, Checkout, User Account, Navigation
- Automation Status: Not Automated, In Progress, Automated
- Last Run Status: Not Run, Pass, Fail, Blocked, Skipped

**Reference:**
- Curriculum template: `curriculum/templates/test-case-template.md`
- GitHub Projects: Built-in test management, free alternative to TestRail

### Success Criteria
- ✅ 5-10 test cases manually created as GitHub issues (practice)
- ✅ Automation script created with mentor to import remaining 40+ tests
- ✅ All 50+ test cases in GitHub Issues with proper labels
- ✅ All issues added to "SauceDemo Test Suite" GitHub Project
- ✅ Custom fields set for all issues
- ✅ Screenshots captured
- ✅ Reflection on benefits of automation + test management tools written

---

## ✅ Exercise Completion Checklist
- [ ] Exercise 1: 50+ Test Cases written (Login: 15+, Products: 10+, Cart: 15+, Checkout: 20+)
- [ ] Exercise 2: Test cases organized by module with priority matrix and suite assignments
- [ ] Exercise 3: Traceability Matrix created with 100% requirements coverage
- [ ] Exercise 4: Test Data Management strategy documented
- [ ] Exercise 5: 10 test cases peer-reviewed with improvements identified
- [ ] Exercise 6: GitHub Projects configured with test case issues and screenshots

---

## Grading Rubric

| Category | Weight | Criteria |
|----------|--------|----------|
| **Completeness** | 20% | All 6 exercises completed, 50+ test cases written |
| **Quality** | 30% | Test cases follow template, specific steps/results, no ambiguity |
| **Organization** | 15% | Clear module structure, priority distribution, suite assignments |
| **Traceability** | 20% | RTM complete, 100% coverage, gap analysis thorough |
| **Critical Thinking** | 10% | Test design techniques applied, security tests included, review insights |
| **Professionalism** | 5% | Clean formatting, consistent naming, GitHub integration |
| **TOTAL** | **100%** | |

**FAANG-Level Standards:**
- Test cases must be **independent** (no dependencies)
- Expected results must be **specific and measurable**
- Traceability matrix must show **100% requirements coverage**
- GitHub Projects integration demonstrates **tool proficiency**

---

**Good luck! This week builds portfolio-ready test artifacts. 🎯**
