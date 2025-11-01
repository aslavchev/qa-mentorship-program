# Week 8: Test Case Design & Management

## 🎯 Learning Objectives
- Write clear, comprehensive test cases
- Structure and organize test suites
- Create requirements traceability matrices
- Manage test data effectively
- Review and maintain test case quality
- Use test management tools

## 📚 Why Good Test Case Design Matters

**Problem:** Poor test cases are ambiguous, incomplete, and hard to maintain. Different testers execute them differently, leading to inconsistent results.

**Solution:** Well-designed test cases are clear, repeatable, and maintainable. Anyone can execute them and get the same results.

### Benefits
- ✅ Consistent test execution (same results regardless of who runs them)
- ✅ Easy maintenance (update once, use many times)
- ✅ Clear requirements coverage (traceability)
- ✅ Knowledge transfer (new testers can execute)
- ✅ Reusability (regression testing, automation)
- ✅ Legal/compliance evidence (audit trail)

---

## 1️⃣ Anatomy of a Good Test Case

### Essential Components

#### 1. Test Case ID
**Purpose:** Unique identifier for tracking and reference

**Format:** `TC-[Module]-[Number]`

**Examples:**
```
TC-LOGIN-001
TC-LOGIN-002
TC-CART-015
TC-CHECKOUT-023
```

**Best Practices:**
- Use consistent naming convention
- Make it meaningful (includes module/feature)
- Sequential numbering
- Never reuse IDs (even for deleted tests)

#### 2. Test Case Title/Name
**Purpose:** Brief description of what's being tested

**Format:** `[Action] [Expected Result]`

**Good Examples:**
```
✅ Verify login with valid credentials succeeds
✅ Verify user cannot login with invalid password
✅ Verify cart total updates when item added
✅ Verify checkout fails with empty required fields
```

**Bad Examples:**
```
❌ Login test (too vague)
❌ Test the cart (what about the cart?)
❌ TC-001 (not descriptive)
❌ Check if login works or not (unclear)
```

**Best Practices:**
- Start with action verb (Verify, Validate, Confirm, Check)
- Be specific (which scenario?)
- Keep it concise (5-10 words)
- Make it searchable

#### 3. Test Objective/Description
**Purpose:** Detailed explanation of test purpose

**Example:**
```
Objective:
To verify that a user with valid credentials (standard_user) can
successfully log in to the SauceDemo application and is redirected
to the inventory page.
```

#### 4. Preconditions/Prerequisites
**Purpose:** Setup required before test execution

**Examples:**
```
Preconditions:
- SauceDemo application is accessible
- Test user account exists: standard_user / secret_sauce
- No active session (user logged out or cleared cookies)
- Browser: Chrome latest version
```

#### 5. Test Data
**Purpose:** Specific data values used in test

**Example:**
```
Test Data:
- Username: standard_user
- Password: secret_sauce
- Expected URL: https://www.saucedemo.com/inventory.html
```

#### 6. Test Steps
**Purpose:** Exact actions to perform (numbered, sequential)

**Format:**
```
Step # | Action
1. Navigate to https://www.saucedemo.com
2. Enter "standard_user" in Username field
3. Enter "secret_sauce" in Password field
4. Click LOGIN button
```

**Best Practices:**
- One action per step
- Be specific (exact values, exact button names)
- Use consistent language
- Number sequentially
- Assume tester knows nothing

#### 7. Expected Results
**Purpose:** What should happen after each step or overall

**Format Option 1: Step-by-step**
```
Step # | Action | Expected Result
1. Navigate to URL | Login page displays
2. Enter username | Text appears in field
3. Enter password | Text appears as dots (masked)
4. Click LOGIN | Redirected to inventory page, URL is /inventory.html
```

**Format Option 2: Overall expected result**
```
Expected Result:
- User is logged in successfully
- Redirected to inventory page
- URL changes to /inventory.html
- Shopping cart icon visible in top right
- 6 products displayed
```

#### 8. Test Environment
**Purpose:** Where the test should be executed

**Example:**
```
Environment:
- URL: https://www.saucedemo.com
- Browser: Chrome 120+
- OS: Windows 10/11 or macOS
- Screen Resolution: 1920×1080
```

#### 9. Test Type/Category
**Purpose:** Classify the test

**Examples:**
```
Type: Functional, Positive
Type: Functional, Negative
Type: Regression
Type: Integration
Type: Smoke
```

#### 10. Priority/Severity
**Purpose:** Importance ranking

**Levels:**
- **Critical/P0:** Core functionality, blocks everything
- **High/P1:** Important features, major workflows
- **Medium/P2:** Standard features
- **Low/P3:** Minor features, cosmetic

**Example:** `Priority: High (P1)`

#### 11. Author & Dates
**Purpose:** Ownership and tracking

**Example:**
```
Created by: Jane Doe
Created date: 2024-01-10
Last modified by: John Smith
Last modified date: 2024-01-15
```

#### 12. Status
**Purpose:** Track execution state

**Values:**
- Draft (being written)
- Ready for Review
- Approved
- Ready for Execution
- Executed - Pass
- Executed - Fail
- Blocked
- Deprecated/Obsolete

---

### Complete Test Case Example

```markdown
**Test Case ID:** TC-LOGIN-001

**Title:** Verify login with valid credentials succeeds

**Objective:**
To verify that a user with valid credentials (standard_user) can
successfully log in to the SauceDemo application and is redirected
to the inventory page.

**Preconditions:**
- SauceDemo application is accessible
- Test user account exists: standard_user / secret_sauce
- No active session (clear browser cookies/cache)
- Browser: Chrome latest version

**Test Data:**
- Username: standard_user
- Password: secret_sauce
- Expected URL: https://www.saucedemo.com/inventory.html

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to https://www.saucedemo.com | Login page displays with username, password fields, and LOGIN button |
| 2 | Enter "standard_user" in Username field | Text "standard_user" appears in field |
| 3 | Enter "secret_sauce" in Password field | Password appears masked (dots) |
| 4 | Click LOGIN button | User redirected to inventory page (URL: /inventory.html), 6 products visible, cart icon in header |

**Environment:**
- URL: https://www.saucedemo.com
- Browser: Chrome 120+
- OS: Windows 10 or macOS Ventura

**Test Type:** Functional, Positive, Smoke

**Priority:** Critical (P0)

**Created by:** QA Team
**Created date:** 2024-01-10
**Last modified:** 2024-01-10
**Status:** Approved

**Related Requirements:** REQ-AUTH-001 (User Authentication)

**Notes:** This is a smoke test - must pass before further testing
```

---

## 2️⃣ Test Case Design Techniques Applied

### Using Equivalence Partitioning

**Feature:** Login username field

**Partitions:**
1. Valid users (standard_user, problem_user, etc.)
2. Invalid users (wrong username)
3. Locked users (locked_out_user)
4. Empty username
5. Special characters in username

**Test Cases (one per partition):**
```
TC-LOGIN-001: Login with valid user (standard_user)
TC-LOGIN-002: Login with invalid user (wrong_user)
TC-LOGIN-003: Login with locked user (locked_out_user)
TC-LOGIN-004: Login with empty username
TC-LOGIN-005: Login with special chars username (<script>alert(1)</script>)
```

### Using Boundary Value Analysis

**Feature:** Product quantity in cart

**Boundaries:**
- Minimum: 0 (invalid), 1 (valid), 2 (valid)
- Maximum: Assume max 99 items → 98 (valid), 99 (valid), 100 (invalid)
- Special: Negative, decimal, very large number

**Test Cases:**
```
TC-CART-010: Add 1 item to cart (minimum valid)
TC-CART-011: Add 2 items to cart (minimum+1)
TC-CART-012: Add 99 items to cart (maximum valid)
TC-CART-013: Attempt to add 0 items (minimum-1, invalid)
TC-CART-014: Attempt to add -5 items (negative, invalid)
TC-CART-015: Attempt to add 1.5 items (decimal, invalid)
```

### Using Decision Tables

**Feature:** Checkout form validation

**Conditions:**
- First Name: Filled / Empty
- Last Name: Filled / Empty
- Zip Code: Filled / Empty

**Decision Table:**

| Rule | First Name | Last Name | Zip Code | Expected Result |
|------|-----------|-----------|----------|----------------|
| 1 | Filled | Filled | Filled | ✅ Success, proceed to review page |
| 2 | Empty | Filled | Filled | ❌ Error: "Error: First Name is required" |
| 3 | Filled | Empty | Filled | ❌ Error: "Error: Last Name is required" |
| 4 | Filled | Filled | Empty | ❌ Error: "Error: Postal Code is required" |
| 5 | Empty | Empty | Filled | ❌ Error: "Error: First Name is required" |
| 6 | Empty | Filled | Empty | ❌ Error: "Error: First Name is required" |
| 7 | Filled | Empty | Empty | ❌ Error: "Error: Last Name is required" |
| 8 | Empty | Empty | Empty | ❌ Error: "Error: First Name is required" |

**Test Cases (one per rule):**
```
TC-CHECKOUT-010: Checkout with all fields filled (rule 1)
TC-CHECKOUT-011: Checkout with empty first name (rule 2)
TC-CHECKOUT-012: Checkout with empty last name (rule 3)
TC-CHECKOUT-013: Checkout with empty zip code (rule 4)
... (continue for all 8 rules)
```

### Using State Transition

**Feature:** Shopping cart states

**States:**
1. Empty Cart
2. Cart with Items
3. Checkout Information Page
4. Checkout Review Page
5. Order Complete

**Transitions & Events:**
```
Empty Cart --[Add Item]--> Cart with Items
Cart with Items --[Remove All]--> Empty Cart
Cart with Items --[Checkout]--> Checkout Information Page
Checkout Info Page --[Cancel]--> Cart with Items
Checkout Info Page --[Continue]--> Checkout Review Page
Checkout Review Page --[Finish]--> Order Complete
Order Complete --[Back Home]--> Empty Cart
```

**Test Cases (one per transition):**
```
TC-CART-020: Add item to empty cart (Empty → Has Items)
TC-CART-021: Remove all items from cart (Has Items → Empty)
TC-CHECKOUT-020: Click checkout with items in cart (Has Items → Info Page)
TC-CHECKOUT-021: Cancel during checkout (Info Page → Cart)
TC-CHECKOUT-022: Continue from info to review (Info → Review)
TC-CHECKOUT-023: Complete order (Review → Complete)
TC-CHECKOUT-024: Return home after order (Complete → Empty)
```

---

## 3️⃣ Test Case Organization

### Organizing by Module/Feature

```
📁 SauceDemo Test Suite
├── 📁 01-Authentication
│   ├── TC-LOGIN-001 to TC-LOGIN-020 (20 tests)
│   └── TC-LOGOUT-001 to TC-LOGOUT-005 (5 tests)
├── 📁 02-Product-Browsing
│   ├── TC-PRODUCTS-001 to TC-PRODUCTS-010 (10 tests)
│   └── TC-SORT-001 to TC-SORT-008 (8 tests)
├── 📁 03-Shopping-Cart
│   ├── TC-CART-001 to TC-CART-025 (25 tests)
│   └── TC-CART-PERSISTENCE-001 to TC-CART-PERSISTENCE-010 (10 tests)
├── 📁 04-Checkout
│   ├── TC-CHECKOUT-001 to TC-CHECKOUT-030 (30 tests)
│   └── TC-CHECKOUT-REVIEW-001 to TC-CHECKOUT-REVIEW-010 (10 tests)
└── 📁 05-Regression-Suite
    └── Selected critical tests from all modules (50 tests)
```

**Total: ~168 test cases**

### Organizing by Test Type

```
📁 Test Suite by Type
├── 📁 Smoke Tests (10-15 critical path tests)
├── 📁 Functional Tests (100+ feature tests)
├── 📁 Regression Tests (50-80 reusable tests)
├── 📁 Exploratory Charters (8-10 session charters)
├── 📁 Integration Tests (API + UI integration, 20 tests)
├── 📁 Non-Functional Tests
│   ├── Performance (5 tests)
│   ├── Security (10 tests)
│   ├── Usability (5 checklists)
│   └── Compatibility (browser matrix, 15 tests)
```

### Organizing by Priority

```
📁 Test Suite by Priority
├── 📁 P0-Critical (Must execute every release) - 20 tests
├── 📁 P1-High (Execute for major releases) - 50 tests
├── 📁 P2-Medium (Execute when time allows) - 60 tests
└── 📁 P3-Low (Execute quarterly) - 38 tests
```

### Test Suite Naming Conventions

**Best Practices:**
- Use prefixes for grouping: `TC-[MODULE]-[NUMBER]`
- Keep naming consistent across team
- Make IDs sortable (alphabetically or numerically)
- Never reuse IDs

**Examples:**
```
✅ TC-LOGIN-001, TC-LOGIN-002, TC-LOGIN-003 (good)
❌ Login-test-1, Login_Test_2, LoginTest3 (inconsistent)

✅ TC-CART-010, TC-CART-011, TC-CART-012 (sortable)
❌ TC-CART-1, TC-CART-10, TC-CART-2 (TC-10 comes before TC-2 when sorted)
```

---

## 4️⃣ Requirements Traceability Matrix (RTM)

### What is RTM?

**Definition:** A document that maps requirements to test cases and defects, ensuring complete coverage.

**Purpose:**
- Verify all requirements have test cases
- Track which tests validate which requirements
- Ensure no requirement is untested
- Link defects back to requirements
- Support impact analysis (what to test when requirement changes)

### RTM Components

1. **Requirement ID:** Unique identifier
2. **Requirement Description:** What needs to be built
3. **Test Case IDs:** Which tests cover this requirement
4. **Test Status:** Pass/Fail/Blocked
5. **Defect IDs:** Bugs found related to this requirement
6. **Coverage Status:** Covered / Partially Covered / Not Covered

### SauceDemo RTM Example

| Req ID | Requirement | Priority | Test Cases | Test Status | Defects | Coverage |
|--------|-------------|----------|-----------|-------------|---------|----------|
| REQ-001 | User can login with valid credentials | Critical | TC-LOGIN-001, TC-LOGIN-002 | ✅ Pass | - | ✅ Covered |
| REQ-002 | User cannot login with invalid credentials | Critical | TC-LOGIN-003, TC-LOGIN-004, TC-LOGIN-005 | ✅ Pass | - | ✅ Covered |
| REQ-003 | Locked user cannot login | High | TC-LOGIN-006 | ✅ Pass | - | ✅ Covered |
| REQ-004 | User can view all products | Critical | TC-PRODUCTS-001 | ✅ Pass | - | ✅ Covered |
| REQ-005 | User can sort products by name | Medium | TC-SORT-001, TC-SORT-002 | ⚠️ Fail | DEF-045 | ⚠️ Partial |
| REQ-006 | User can sort products by price | Medium | TC-SORT-003, TC-SORT-004 | ✅ Pass | - | ✅ Covered |
| REQ-007 | User can add items to cart | Critical | TC-CART-001, TC-CART-002, TC-CART-003 | ✅ Pass | - | ✅ Covered |
| REQ-008 | User can remove items from cart | High | TC-CART-010, TC-CART-011 | ✅ Pass | DEF-047 | ✅ Covered |
| REQ-009 | Cart displays correct total | Critical | TC-CART-020, TC-CART-021 | ✅ Pass | - | ✅ Covered |
| REQ-010 | Cart persists across sessions | High | TC-CART-PERSISTENCE-001 to 005 | ⚠️ Fail | DEF-050 | ⚠️ Partial |
| REQ-011 | User can checkout with valid info | Critical | TC-CHECKOUT-001 to 010 | ✅ Pass | - | ✅ Covered |
| REQ-012 | Checkout validates required fields | Critical | TC-CHECKOUT-011 to 018 | ✅ Pass | - | ✅ Covered |
| REQ-013 | User can complete order | Critical | TC-CHECKOUT-025 | ✅ Pass | - | ✅ Covered |

**RTM Summary:**
- Total Requirements: 13
- Covered: 11 (85%)
- Partially Covered: 2 (15%)
- Not Covered: 0 (0%)
- Total Test Cases: 50+
- Pass Rate: 89% (47/53 tests passed)
- Defects: 3 open

### Forward Traceability
**Requirements → Test Cases → Defects**
```
REQ-005 (Sort by name)
  → TC-SORT-001 (Sort A-Z) - FAIL
  → TC-SORT-002 (Sort Z-A) - FAIL
    → DEF-045: Sort order not persisting after refresh
```

### Backward Traceability
**Defects → Test Cases → Requirements**
```
DEF-050 (Cart doesn't persist)
  → TC-CART-PERSISTENCE-003 (Logout and login, check cart)
    → REQ-010 (Cart persistence requirement)
```

### Coverage Analysis from RTM

**Formula:**
```
Requirements Coverage = (Requirements with tests / Total requirements) × 100%
= 13/13 = 100%

Pass Coverage = (Requirements with passing tests / Total requirements) × 100%
= 11/13 = 85%
```

**Gap Analysis:**
```
🔴 Gaps Found:
- REQ-005: Sorting issues (2 tests failing)
- REQ-010: Cart persistence issues (partial coverage, bugs)

✅ Action Items:
- Fix DEF-045 and retest
- Add 3 more cart persistence tests
- Retest after fixes
```

---

## 5️⃣ Test Data Management

### Why Test Data Matters

**Problem:** Tests fail due to bad/missing data, not bugs

**Solution:** Plan, create, and maintain quality test data

### Types of Test Data

#### 1. Valid Test Data
**Purpose:** Verify happy path scenarios

**Example: SauceDemo Login**
```
Valid Users:
- standard_user / secret_sauce
- problem_user / secret_sauce
- performance_glitch_user / secret_sauce

Valid Checkout Data:
- First Name: John, Jane, Alex, Maria
- Last Name: Doe, Smith, Johnson, Garcia
- Zip Code: 12345, 90210, 10001, 75001
```

#### 2. Invalid Test Data
**Purpose:** Verify error handling

**Example: SauceDemo Login**
```
Invalid Users:
- wrong_user / secret_sauce (wrong username)
- standard_user / wrong_password (wrong password)
- empty / secret_sauce (empty username)
- standard_user / empty (empty password)

Invalid Checkout Data:
- First Name: <blank>, <script>alert(1)</script>, 123456, !@#$%
- Zip Code: ABC123, -12345, 9999999999, <empty>
```

#### 3. Boundary Test Data
**Purpose:** Test limits

**Example: Cart Quantity**
```
Boundary Values:
- 0 (invalid, min-1)
- 1 (valid, min)
- 2 (valid, min+1)
- 99 (valid, max) [if limit exists]
- 100 (invalid, max+1)
```

#### 4. Special Characters / Unicode
**Purpose:** Test internationalization, security

**Example:**
```
Special Characters:
- Names: O'Brien, José, François, 李明, Müller
- Inputs: ' " < > & ; -- (SQL injection chars)
- Unicode: 😀 🎉 (emojis), العربية (Arabic), 中文 (Chinese)
```

### Test Data Strategies

#### Strategy 1: Hard-Coded Data
**What:** Data embedded in test cases

**Pros:**
- Simple, easy to understand
- No external dependencies

**Cons:**
- Hard to maintain (change in 100 test cases)
- Not reusable

**When to use:** Simple, one-off tests

**Example:**
```
Step 2: Enter "standard_user" in Username field
Step 3: Enter "secret_sauce" in Password field
```

#### Strategy 2: Test Data Files
**What:** Data stored in external files (CSV, JSON, Excel)

**Pros:**
- Easy to update (one place)
- Reusable across tests
- Can generate data programmatically

**Cons:**
- Extra file management
- Tests depend on file

**When to use:** Data-driven testing, many test variations

**Example: users.csv**
```csv
username,password,expected_result
standard_user,secret_sauce,success
problem_user,secret_sauce,success
locked_out_user,secret_sauce,locked
wrong_user,secret_sauce,invalid
standard_user,wrong_pass,invalid
```

**Example: checkout_data.json**
```json
{
  "valid_data": [
    {"firstName": "John", "lastName": "Doe", "zipCode": "12345"},
    {"firstName": "Jane", "lastName": "Smith", "zipCode": "90210"}
  ],
  "invalid_data": [
    {"firstName": "", "lastName": "Doe", "zipCode": "12345"},
    {"firstName": "John", "lastName": "", "zipCode": "12345"}
  ]
}
```

#### Strategy 3: Test Data Generation
**What:** Create data programmatically using scripts

**Pros:**
- Large volumes of data
- Randomized for variation
- Fresh data each run

**Cons:**
- Requires programming
- May be too random (hard to debug)

**When to use:** Performance testing, stress testing, fuzzing

**Example: Python script (Week 11 preview)**
```python
import random
import string

def generate_user_data(count=10):
    users = []
    for i in range(count):
        first = ''.join(random.choices(string.ascii_uppercase, k=6))
        last = ''.join(random.choices(string.ascii_uppercase, k=8))
        zip_code = ''.join(random.choices(string.digits, k=5))
        users.append({
            "firstName": first,
            "lastName": last,
            "zipCode": zip_code
        })
    return users
```

### Test Data Organization

**Directory Structure:**
```
test-data/
├── users.csv (login credentials)
├── products.json (product catalog)
├── checkout-valid.csv (valid checkout data)
├── checkout-invalid.csv (invalid checkout data)
├── boundary-values.csv (boundary test data)
└── sql-injection.txt (security test payloads)
```

### Test Data Best Practices

✅ **DO:**
- Keep test data separate from test code
- Use descriptive data (John Doe, not asdf)
- Document what each data set is for
- Version control test data files
- Reset data after tests (clean up)
- Use realistic data (masks production issues)

❌ **DON'T:**
- Use production data (privacy, security risk)
- Hard-code passwords (security risk)
- Share data across unrelated tests (dependencies)
- Forget to clean up (pollutes next run)
- Use overly complex data (hard to debug)

---

## 6️⃣ Test Case Review & Quality

### Why Review Test Cases?

- Catch errors before execution (saves time)
- Ensure clarity (different tester can execute)
- Improve coverage (find missing scenarios)
- Maintain consistency (standardize format)
- Knowledge sharing (team learns from each other)

### Test Case Review Checklist

#### Completeness
- [ ] All required fields filled (ID, title, steps, expected results)
- [ ] Preconditions clearly stated
- [ ] Test data specified
- [ ] Expected result for each step or overall
- [ ] Linked to requirement ID

#### Clarity
- [ ] Title is clear and specific
- [ ] Steps are unambiguous (no "etc.", "and so on")
- [ ] One action per step
- [ ] Uses exact field names, button names
- [ ] Expected results are specific (not "should work")

#### Correctness
- [ ] Steps are in logical order
- [ ] Expected results are accurate
- [ ] Test data is valid for the scenario
- [ ] No typos or grammatical errors

#### Testability
- [ ] Can be executed without additional information
- [ ] Repeatable (same result each time)
- [ ] Independent (doesn't depend on other tests)
- [ ] Executable in reasonable time (< 10 min)

#### Coverage
- [ ] Positive and negative scenarios covered
- [ ] Boundary values tested
- [ ] Error conditions tested
- [ ] No duplicate tests

### Test Case Quality Metrics

**Defect Detection Rate:**
```
Defects found / Test cases executed
High rate = Good test cases (finding bugs)
```

**Test Case Effectiveness:**
```
Valid defects found by test / Total defects
High % = Tests finding real issues
```

**Test Case Efficiency:**
```
Defects found / Execution time
High ratio = Finding bugs quickly
```

### Common Test Case Mistakes

#### ❌ Mistake 1: Vague Steps
**Bad:**
```
Step 1: Login to the application
Step 2: Go to cart
Step 3: Check that it works
```

**Good:**
```
Step 1: Navigate to https://www.saucedemo.com
Step 2: Enter "standard_user" in Username field
Step 3: Enter "secret_sauce" in Password field
Step 4: Click LOGIN button
Step 5: Click cart icon in top-right header
Step 6: Verify cart page displays with "Your Cart" heading
```

#### ❌ Mistake 2: Multiple Actions Per Step
**Bad:**
```
Step 1: Login and add item to cart
Step 2: Go to checkout and fill in details
```

**Good:**
```
Step 1: Navigate to login page
Step 2: Enter username
Step 3: Enter password
Step 4: Click LOGIN
Step 5: Click "Add to cart" for Backpack
Step 6: Click cart icon
Step 7: Click CHECKOUT button
Step 8: Enter first name
Step 9: Enter last name
Step 10: Enter zip code
Step 11: Click CONTINUE
```

#### ❌ Mistake 3: Unclear Expected Results
**Bad:**
```
Expected Result: Should work correctly
Expected Result: Page loads
Expected Result: No errors
```

**Good:**
```
Expected Result: User redirected to /inventory.html, 6 products visible
Expected Result: Cart page displays with heading "Your Cart" and CHECKOUT button
Expected Result: Error message "Error: Username is required" displayed in red
```

#### ❌ Mistake 4: Missing Preconditions
**Bad:**
```
Step 1: Click CHECKOUT button
```
*Where is the user? Are there items in cart? Is user logged in?*

**Good:**
```
Preconditions:
- User is logged in as standard_user
- Cart contains at least 1 item
- User is on cart page (/cart.html)

Step 1: Click CHECKOUT button
```

#### ❌ Mistake 5: Test Case Dependencies
**Bad:**
```
TC-CHECKOUT-002 depends on TC-CART-015 completing successfully
```
*If TC-CART-015 fails, TC-CHECKOUT-002 is blocked*

**Good:**
```
TC-CHECKOUT-002 is independent:
Preconditions: User logged in, cart contains 1 item
(Set up state in preconditions, don't depend on another test)
```

---

## 7️⃣ Test Management Tools

### Popular Test Management Tools

| Tool | Type | Best For | Pricing |
|------|------|----------|---------|
| **TestRail** | Commercial | Enterprise teams, detailed reporting | Paid |
| **Xray (Jira)** | Commercial | Teams using Jira, integration | Paid |
| **Zephyr** | Commercial | Jira integration, agile teams | Paid/Free |
| **qTest** | Commercial | Enterprise, compliance, regulated industries | Paid |
| **PractiTest** | Commercial | End-to-end test management | Paid |
| **TestLink** | Open Source | Small teams, budget-friendly | Free |
| **TestCollab** | Commercial | Collaboration, simple UI | Paid/Free |
| **Spreadsheets** | Manual | Very small teams, starting out | Free |

### Using Spreadsheets (Simple Approach)

**Pros:**
- Free
- Easy to start
- No learning curve
- Flexible

**Cons:**
- No version control (hard to track changes)
- No automatic reporting
- Manual effort
- Doesn't scale well
- No integrations

**Example: Excel/Google Sheets Test Case Template**

| TC ID | Title | Objective | Preconditions | Test Data | Steps | Expected Result | Priority | Status | Notes |
|-------|-------|-----------|--------------|-----------|-------|----------------|----------|--------|-------|
| TC-LOGIN-001 | Verify login with valid credentials | Validate authentication | App accessible, user logged out | user: standard_user, pass: secret_sauce | 1. Navigate to URL<br>2. Enter username<br>3. Enter password<br>4. Click LOGIN | Redirected to /inventory.html | Critical | Pass | - |
| TC-LOGIN-002 | Verify login with invalid password | Validate error handling | App accessible, user logged out | user: standard_user, pass: wrong | 1. Navigate to URL<br>2. Enter username<br>3. Enter wrong password<br>4. Click LOGIN | Error: "Username and password do not match" | High | Pass | - |

### Test Case Fields in Tools

**Minimum fields:**
- ID, Title, Steps, Expected Results, Status

**Recommended fields:**
- + Preconditions, Test Data, Priority, Type

**Advanced fields:**
- + Requirements link, Automation status, Execution time, Assigned to, Tags, Component

---

## 8️⃣ SauceDemo Complete Test Case Examples

### Example 1: Smoke Test

```markdown
**Test Case ID:** TC-SMOKE-001

**Title:** Verify critical user journey (Login → Add to Cart → Checkout → Complete Order)

**Objective:**
Validate the end-to-end critical path of SauceDemo application to ensure
basic functionality is working before detailed testing.

**Type:** Smoke Test, End-to-End

**Priority:** Critical (P0)

**Preconditions:**
- SauceDemo application is accessible
- Test user exists: standard_user / secret_sauce
- No active session (clear cookies)

**Test Data:**
- Username: standard_user
- Password: secret_sauce
- Product: Sauce Labs Backpack
- Checkout Data: John / Doe / 12345

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to https://www.saucedemo.com | Login page displays |
| 2 | Enter "standard_user" in Username field | Text appears in field |
| 3 | Enter "secret_sauce" in Password field | Password masked |
| 4 | Click LOGIN button | Redirected to inventory page, 6 products visible |
| 5 | Click "Add to cart" button for "Sauce Labs Backpack" | Button changes to "Remove", cart badge shows "1" |
| 6 | Click cart icon in header | Cart page displays, Backpack listed, total $29.99 |
| 7 | Click CHECKOUT button | Checkout info page displays (first/last/zip fields) |
| 8 | Enter "John" in First Name field | Text appears |
| 9 | Enter "Doe" in Last Name field | Text appears |
| 10 | Enter "12345" in Zip Code field | Text appears |
| 11 | Click CONTINUE button | Checkout overview page displays with Backpack, total $32.39 |
| 12 | Click FINISH button | Order complete page displays: "THANK YOU FOR YOUR ORDER" |
| 13 | Click BACK HOME button | Returned to inventory page, cart badge shows "0" |

**Environment:** https://www.saucedemo.com, Chrome 120+

**Status:** Ready for Execution

**Requirement:** REQ-CRITICAL-PATH-001
```

### Example 2: Negative Test

```markdown
**Test Case ID:** TC-LOGIN-010

**Title:** Verify login fails with SQL injection attempt

**Objective:**
To verify that the login form is protected against SQL injection attacks
and does not allow unauthorized access.

**Type:** Functional, Negative, Security

**Priority:** High (P1)

**Preconditions:**
- SauceDemo application is accessible
- No active session

**Test Data:**
- Username: ' OR '1'='1
- Password: ' OR '1'='1

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to https://www.saucedemo.com | Login page displays |
| 2 | Enter "' OR '1'='1" in Username field | Text appears (may be escaped) |
| 3 | Enter "' OR '1'='1" in Password field | Password masked |
| 4 | Click LOGIN button | Login FAILS with error message: "Username and password do not match any user in this service" |
| 5 | Verify user is NOT logged in | User remains on login page, inventory NOT accessible |

**Environment:** https://www.saucedemo.com, Chrome 120+

**Status:** Approved

**Requirement:** REQ-SEC-001 (SQL Injection Protection)

**Notes:** This is a security test. Application should sanitize inputs
and NOT allow SQL injection.
```

### Example 3: Boundary Value Test

```markdown
**Test Case ID:** TC-CHECKOUT-015

**Title:** Verify checkout with maximum length inputs (boundary test)

**Objective:**
To verify that the checkout form accepts maximum reasonable input lengths
without errors or truncation.

**Type:** Functional, Boundary Value Analysis

**Priority:** Medium (P2)

**Preconditions:**
- User logged in as standard_user
- At least 1 item in cart
- User on checkout information page (/checkout-step-one.html)

**Test Data:**
- First Name: 50 characters (A repeated 50 times)
- Last Name: 50 characters (B repeated 50 times)
- Zip Code: 10 characters (9 repeated 10 times)

**Test Steps & Expected Results:**

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Enter 50-character string in First Name | All characters accepted, no truncation |
| 2 | Enter 50-character string in Last Name | All characters accepted, no truncation |
| 3 | Enter 10-character string in Zip Code | All characters accepted, no truncation |
| 4 | Click CONTINUE button | Proceeds to checkout overview page, all data preserved |
| 5 | Verify data on review page | Names and zip displayed correctly (may be truncated in UI but data preserved) |

**Environment:** https://www.saucedemo.com, Chrome 120+

**Status:** Ready for Review

**Requirement:** REQ-CHECKOUT-VALIDATION-003

**Notes:** Verify application doesn't crash with long inputs. Some UI
truncation is acceptable as long as data is preserved.
```

---

## 📝 Summary

### Key Takeaways

1. **Good Test Cases Have:**
   - Clear, unique ID
   - Specific, descriptive title
   - Complete preconditions
   - Exact test data
   - Step-by-step actions
   - Specific expected results
   - Environment details
   - Priority/type classification

2. **Organization Strategies:**
   - By module/feature (Login, Cart, Checkout)
   - By test type (Smoke, Functional, Regression)
   - By priority (P0, P1, P2, P3)

3. **Requirements Traceability:**
   - Maps requirements → test cases → defects
   - Ensures complete coverage
   - Supports impact analysis
   - Provides audit trail

4. **Test Data Management:**
   - Valid, invalid, boundary data
   - Hard-coded, file-based, or generated
   - Keep separate from test cases
   - Never use production data

5. **Review for Quality:**
   - Completeness, clarity, correctness
   - Testability and independence
   - No ambiguity or vagueness
   - Peer review before execution

### This Week's Challenge

**Write 50+ test cases for SauceDemo** covering:
- Login (15 test cases)
- Product browsing & sorting (10 test cases)
- Cart operations (15 test cases)
- Checkout flow (20 test cases)

**Create RTM** linking all test cases to requirements

**Organize** test cases by module and priority

---

## 🤔 Self-Assessment Questions

1. What are the 5 essential components of a test case?
2. What's the difference between preconditions and test data?
3. Why should test steps be numbered and specific?
4. What is Requirements Traceability Matrix (RTM)?
5. How do you organize 100+ test cases effectively?
6. What's the difference between valid and invalid test data?
7. Why should test cases be independent (not depend on other tests)?
8. What makes a good test case title?
9. Name 3 common test case writing mistakes
10. How do you measure test case quality?

### Answers to Check
1. ID, title, steps, expected results, preconditions (+ test data, priority)
2. Preconditions = setup state before test; Test data = specific values used in test
3. Numbers provide sequence; Specificity ensures repeatability and clarity
4. Matrix mapping requirements to test cases and defects, ensuring coverage
5. By module/feature, by test type, by priority; use naming conventions
6. Valid = happy path, should work; Invalid = error conditions, should fail gracefully
7. If test A depends on test B, and B fails, A is blocked (cascade failure)
8. Starts with verb, specific scenario, concise, searchable (e.g., "Verify login with valid credentials succeeds")
9. Vague steps, multiple actions per step, unclear expected results, missing preconditions, test dependencies (any 3)
10. Defect detection rate, test effectiveness (valid bugs found), test efficiency (bugs per time)

---

**📚 Continue to: exercises.md → Write your 50+ test cases for SauceDemo**

**⏭️ Next Week:** Agile Testing & BDD - Behavior-Driven Development with Gherkin syntax
