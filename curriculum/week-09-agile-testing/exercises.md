# Week 9: Agile Testing & BDD - Exercises

## Exercise Overview
This week focuses on applying Agile Testing & BDD concepts to SauceDemo, building on your Week 8 test cases.
Complete all exercises and document your work in `mentee-work/week-09/`

**Total Time:** ~7 hours (420 minutes)

---

## Exercise 1: Map Tests to Agile Testing Quadrants (60 min)

### Objective
Categorize your Week 8 test cases into the four Agile Testing Quadrants, understanding which tests serve which purpose.

### Background
**Agile Testing Quadrants** (from tutorial.md Section 1):
- **Q1:** Technology-facing, Supporting the Team (Unit, Integration, Component tests)
- **Q2:** Business-facing, Supporting the Team (Functional, BDD, Acceptance tests)
- **Q3:** Business-facing, Critiquing the Product (Exploratory, Usability, UAT)
- **Q4:** Technology-facing, Critiquing the Product (Performance, Security, Load tests)

### Instructions

**Step 1: Review Week 8 Test Cases (10 min)**
Open your `mentee-work/week-08/write-50+-test-cases.md` file.

**Step 2: Create Quadrant Mapping Table (40 min)**

For each of your 60 test cases, identify which quadrant it belongs to.

**Mapping Guide:**

| Test Type | Typical Quadrant | Example |
|-----------|-----------------|---------|
| **Smoke tests** | Q2 | TC-LOGIN-001 (verify core functionality) |
| **Functional tests** | Q2 | TC-CART-001 (add to cart works) |
| **Negative tests** | Q2 | TC-LOGIN-003 (invalid credentials) |
| **Security tests** | Q4 | TC-LOGIN-010 (SQL injection) |
| **UI tests** | Q3 | TC-LOGIN-011 (password masking) |
| **Boundary tests** | Q2 | TC-CART-014 (max items) |
| **E2E tests** | Q2 | TC-CHECKOUT-020 (full flow) |
| **Performance tests** | Q4 | (if you had any) |

**Create this table:**

```markdown
## Agile Testing Quadrants - SauceDemo Test Suite

### Quadrant 1: Technology-Facing, Supporting the Team
*Automated tests that help developers (unit, integration, component)*

**Count:** 0
**Tests:**
- (None - SauceDemo is UI testing focus, no unit tests created)

**Note:** In a real project, developers would create Q1 tests for backend logic, API endpoints, database queries.

---

### Quadrant 2: Business-Facing, Supporting the Team
*Automated functional tests that verify requirements (BDD, acceptance tests)*

**Count:** [Your count]
**Tests:**
- TC-LOGIN-001: Verify login with valid credentials (Smoke)
- TC-CART-001: Verify add to cart from inventory (Functional)
- TC-CHECKOUT-001: Verify checkout with valid info (Functional)
- [... list all Q2 tests ...]

**Automation Recommendation:** High priority - these validate business requirements

---

### Quadrant 3: Business-Facing, Critiquing the Product
*Manual exploratory tests that critique UX and usability*

**Count:** [Your count]
**Tests:**
- TC-LOGIN-011: Verify password masking (UI/UX)
- TC-LOGIN-012: Verify login button clickable (UI)
- TC-PRODUCTS-002: Verify product images displayed (UI)
- [... list all Q3 tests ...]

**Automation Recommendation:** Low priority - exploratory/UX tests often manual

---

### Quadrant 4: Technology-Facing, Critiquing the Product
*Non-functional tests that critique quality attributes (performance, security, load)*

**Count:** [Your count]
**Tests:**
- TC-LOGIN-010: SQL injection test (Security)
- TC-LOGIN-015: Unauthorized access prevention (Security)
- [... list all Q4 tests ...]

**Automation Recommendation:** High priority - security tests should run in CI/CD
```

**Step 3: Analysis (10 min)**

Answer these questions:

```markdown
## Quadrant Distribution Analysis

**Q1 (Unit/Integration):** [X] tests ([Y]%)
**Q2 (Functional/BDD):** [X] tests ([Y]%)
**Q3 (Exploratory/UI):** [X] tests ([Y]%)
**Q4 (Performance/Security):** [X] tests ([Y]%)

**Total:** 60 tests (100%)

### Observations:

1. **Which quadrant has the most tests?**
   [Your answer]

2. **Which quadrant has the fewest?**
   [Your answer]

3. **Is this distribution appropriate for UI testing?**
   [Your answer - Hint: Q2 should be largest for functional UI testing]

4. **What's missing?**
   [Example: "No unit tests (Q1) because we're testing UI, not backend code"]

5. **Automation priorities:**
   - High: Q2 (functional tests) + Q4 (security)
   - Medium: Q3 (some UI tests can be automated)
   - Low: Q3 (exploratory, usability - best done manually)
```

### Deliverable
Save as `mentee-work/week-09/agile-testing-quadrants.md`

Include:
- Quadrant 1-4 tables with test counts
- Complete list of tests per quadrant
- Distribution analysis with percentages
- Observations and automation recommendations

### Success Criteria
- ✅ All 60 test cases categorized into quadrants
- ✅ Percentages calculated correctly
- ✅ Q2 (functional) has the most tests (expected for UI testing)
- ✅ Q4 includes security tests (TC-LOGIN-010, TC-LOGIN-015)
- ✅ Q3 includes UI/UX tests (password masking, button clicks, images)
- ✅ Analysis shows understanding of quadrant purposes

---

## Exercise 2: Convert Test Cases to BDD Scenarios (90 min)

### Objective
Convert 15 traditional test cases from Week 8 into BDD (Behavior-Driven Development) scenarios using Given-When-Then format.

### Background
**BDD Syntax** (from tutorial.md Section 2):
- **Given:** Initial context/preconditions
- **When:** Action/event
- **Then:** Expected outcome
- **And:** Additional conditions/actions

### Instructions

**Step 1: Select 15 Test Cases to Convert (5 min)**

Choose these specific test cases from Week 8:

**Login Module (5 scenarios):**
- TC-LOGIN-001: Valid login
- TC-LOGIN-003: Invalid username
- TC-LOGIN-008: Locked user
- TC-LOGIN-010: SQL injection
- TC-LOGIN-014: Logout

**Products Module (3 scenarios):**
- TC-PRODUCTS-001: View all products
- TC-SORT-001: Sort by name A-Z
- TC-PRODUCTS-005: Product detail page

**Cart Module (4 scenarios):**
- TC-CART-001: Add item to cart
- TC-CART-005: Remove item from cart
- TC-CART-009: Cart retains items after navigation
- TC-CART-012: Checkout button navigation

**Checkout Module (3 scenarios):**
- TC-CHECKOUT-001: Checkout with valid info
- TC-CHECKOUT-002: Checkout with empty first name
- TC-CHECKOUT-020: End-to-end smoke test

**Step 2: Study BDD Conversion Example (10 min)**

**Traditional Test Case (TC-LOGIN-001):**
```markdown
### TC-LOGIN-001: Verify login with valid credentials

**Test Objective:** Verify user can log in with valid credentials

**Preconditions:**
- SauceDemo accessible
- User exists: standard_user / secret_sauce
- User logged out

**Test Steps:**
1. Navigate to https://www.saucedemo.com
2. Enter "standard_user" in Username
3. Enter "secret_sauce" in Password
4. Click LOGIN button

**Expected Result:** User redirected to inventory page with 6 products visible
```

**BDD Scenario (Converted):**
```gherkin
Feature: User Authentication

Scenario: Successful login with valid credentials
  Given I am on the SauceDemo login page
  And I am logged out
  When I enter "standard_user" in the username field
  And I enter "secret_sauce" in the password field
  And I click the LOGIN button
  Then I should be redirected to the inventory page
  And I should see 6 products displayed
```

**Key Differences:**
- BDD uses plain language (business-readable)
- No test case ID needed (scenario name is descriptive)
- Given/When/Then structure makes flow clear
- Focus on user behavior, not technical steps

**Step 3: Convert All 15 Test Cases (60 min, ~4 min each)**

For each test case, write a BDD scenario.

**Template:**
```gherkin
Feature: [Module Name - e.g., User Authentication, Shopping Cart]

Scenario: [Descriptive name in plain English]
  Given [initial context/preconditions]
  And [additional context if needed]
  When [action user takes]
  And [additional actions if needed]
  Then [expected outcome]
  And [additional outcomes if needed]
```

**Example Conversions:**

**TC-LOGIN-003 → BDD:**
```gherkin
Scenario: Login fails with invalid username
  Given I am on the SauceDemo login page
  When I enter "invalid_user" in the username field
  And I enter "secret_sauce" in the password field
  And I click the LOGIN button
  Then I should see an error message "Epic sadface: Username and password do not match any user in this service"
  And I should remain on the login page
```

**TC-CART-001 → BDD:**
```gherkin
Scenario: Add product to cart from inventory page
  Given I am logged in as "standard_user"
  And I am on the inventory page
  When I click the "Add to cart" button for "Sauce Labs Backpack"
  Then the cart badge should display "1"
  And the button text should change to "Remove"
```

**TC-CHECKOUT-020 (E2E) → BDD:**
```gherkin
Scenario: Complete end-to-end purchase flow
  Given I am on the SauceDemo login page
  When I login as "standard_user" with password "secret_sauce"
  And I add "Sauce Labs Backpack" to the cart
  And I navigate to the cart
  And I click the "Checkout" button
  And I enter checkout information:
    | First Name | Last Name | Zip Code |
    | John       | Doe       | 12345    |
  And I click "Continue"
  And I click "Finish"
  Then I should see the order confirmation page
  And I should see the message "Thank you for your order"
  And the cart should be empty
```

**Step 4: Add Scenario Outlines for Data-Driven Tests (15 min)**

For tests with multiple data variations, use **Scenario Outline**.

**Example: TC-LOGIN-003, TC-LOGIN-004, TC-LOGIN-005, TC-LOGIN-006 combined:**
```gherkin
Scenario Outline: Login fails with invalid credentials
  Given I am on the SauceDemo login page
  When I enter "<username>" in the username field
  And I enter "<password>" in the password field
  And I click the LOGIN button
  Then I should see an error message "<error_message>"
  And I should remain on the login page

  Examples:
    | username      | password      | error_message                                                   |
    | invalid_user  | secret_sauce  | Username and password do not match any user in this service    |
    | standard_user | wrong_pass    | Username and password do not match any user in this service    |
    |               | secret_sauce  | Epic sadface: Username is required                              |
    | standard_user |               | Epic sadface: Password is required                              |
```

**Create 2-3 Scenario Outlines** for tests that share structure but vary data.

### Deliverable
Save as `mentee-work/week-09/bdd-scenarios.md`

**Format:**
```markdown
# BDD Scenarios - SauceDemo

## Feature: User Authentication

### Scenario 1: Successful login with valid credentials
[BDD scenario in Gherkin format]

### Scenario 2: Login fails with invalid username
[BDD scenario in Gherkin format]

[... continue for all 15 scenarios ...]

## Feature: Shopping Cart

### Scenario 6: Add product to cart from inventory page
[BDD scenario in Gherkin format]

[... etc ...]

## Scenario Outlines (Data-Driven Tests)

### Scenario Outline 1: Login validation errors
[Scenario Outline with Examples table]

[... 2-3 more Scenario Outlines ...]
```

### Success Criteria
- ✅ 15 BDD scenarios converted from Week 8 test cases
- ✅ All scenarios use correct Given-When-Then format
- ✅ Scenarios grouped by Feature (Authentication, Cart, Checkout, Products)
- ✅ Plain language (business-readable, not technical)
- ✅ 2-3 Scenario Outlines with Examples tables
- ✅ Specific values in scenarios (not placeholders like "enter valid username")
- ✅ Expected results are clear and measurable

---

## Exercise 3: Write Acceptance Criteria for User Stories (45 min)

### Objective
Create 5 user stories with acceptance criteria for SauceDemo features, using INVEST principles and Given-When-Then format.

### Background
**User Story Format:**
```
As a [role]
I want [goal/feature]
So that [benefit/value]
```

**INVEST Criteria:**
- **I**ndependent
- **N**egotiable
- **V**aluable
- **E**stimable
- **S**mall
- **T**estable

### Instructions

**Step 1: Review User Story Template (5 min)**

**Example User Story:**
```markdown
## User Story 1: User Login

**As a** registered user
**I want** to log in with my username and password
**So that** I can access my shopping cart and purchase products

### Acceptance Criteria

**AC1: Successful login with valid credentials**
- **Given** I am on the login page
- **When** I enter valid username "standard_user" and password "secret_sauce"
- **And** I click the LOGIN button
- **Then** I should be redirected to the inventory page
- **And** I should see 6 products available

**AC2: Login fails with invalid username**
- **Given** I am on the login page
- **When** I enter invalid username "wrong_user" and valid password "secret_sauce"
- **Then** I should see error "Username and password do not match"
- **And** I should remain on the login page

**AC3: Login fails with invalid password**
- **Given** I am on the login page
- **When** I enter valid username "standard_user" and invalid password "wrong_pass"
- **Then** I should see error "Username and password do not match"
- **And** I should remain on the login page

**AC4: Locked user cannot login**
- **Given** I am on the login page
- **When** I enter locked username "locked_out_user" and password "secret_sauce"
- **Then** I should see error "Sorry, this user has been locked out"
- **And** I should remain on the login page
```

**Step 2: Create 5 User Stories (35 min, ~7 min each)**

Write user stories for these SauceDemo features:

**User Story 1: User Login** (provided above as example)

**User Story 2: Add Items to Cart**
```markdown
**As a** shopper
**I want** to add products to my shopping cart
**So that** I can purchase multiple items in a single order

### Acceptance Criteria
[Write 3-4 AC using Given-When-Then format]
- AC1: Add single item from inventory page
- AC2: Add multiple different items
- AC3: Cart badge updates with item count
- AC4: Remove button appears after adding item
```

**User Story 3: Product Sorting**
```markdown
**As a** shopper
**I want** to sort products by name and price
**So that** I can easily find products that meet my needs

### Acceptance Criteria
[Write 4 AC for sorting options]
- AC1: Sort by name A-Z
- AC2: Sort by name Z-A
- AC3: Sort by price low-to-high
- AC4: Sort by price high-to-low
```

**User Story 4: Checkout Process**
```markdown
**As a** shopper
**I want** to complete checkout with my information
**So that** I can finalize my purchase

### Acceptance Criteria
[Write 4-5 AC covering valid checkout, validation errors, order confirmation]
```

**User Story 5: Remove Items from Cart**
```markdown
**As a** shopper
**I want** to remove items from my cart
**So that** I can change my mind before purchasing

### Acceptance Criteria
[Write 3-4 AC covering removal, badge update, empty cart state]
```

**Step 3: INVEST Check (5 min)**

For each user story, verify:
```markdown
## INVEST Validation

| Story | Independent? | Negotiable? | Valuable? | Estimable? | Small? | Testable? |
|-------|-------------|-------------|-----------|-----------|--------|-----------|
| User Login | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Add to Cart | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [... etc ...] | | | | | | |
```

### Deliverable
Save as `mentee-work/week-09/acceptance-criteria.md`

Include:
- 5 user stories with As-Want-So That format
- 3-5 acceptance criteria per story in Given-When-Then format
- INVEST validation table

### Success Criteria
- ✅ 5 user stories created
- ✅ Each story uses As-Want-So That template
- ✅ Each story has 3-5 acceptance criteria
- ✅ All AC use Given-When-Then format
- ✅ AC are specific and measurable (not vague)
- ✅ Stories follow INVEST principles
- ✅ AC cover happy path + error scenarios

---

## Exercise 4: Create Definition of Done Checklist (30 min)

### Objective
Define a comprehensive "Definition of Done" checklist for SauceDemo testing that ensures quality beyond just acceptance criteria.

### Background
**Definition of Done (DoD)** = Checklist that must be complete before a story is considered "done."

**DoD vs Acceptance Criteria:**
- **AC:** Feature works as specified (functional completeness)
- **DoD:** Feature is production-ready (technical completeness)

### Instructions

**Step 1: Review DoD Template (5 min)**

**DoD Categories:**
1. Code Quality
2. Testing
3. Documentation
4. Non-Functional Requirements
5. Deployment Readiness

**Step 2: Create SauceDemo Definition of Done (20 min)**

```markdown
# Definition of Done - SauceDemo Testing

A user story is considered "DONE" when ALL items below are completed:

## ✅ Code Quality
- [ ] All code reviewed by at least one team member
- [ ] Code follows project coding standards
- [ ] No critical or high-severity linting errors
- [ ] Code committed to version control with clear commit messages
- [ ] No hardcoded credentials or sensitive data

## ✅ Testing
- [ ] All acceptance criteria met and verified
- [ ] Unit tests written and passing (if applicable)
- [ ] Integration tests written and passing
- [ ] Manual exploratory testing completed
- [ ] Regression tests executed (no new bugs introduced)
- [ ] Cross-browser testing completed (Chrome, Firefox, Safari, Edge)
- [ ] Mobile responsiveness tested (if applicable)
- [ ] Test results documented in test management tool

## ✅ Security & Performance
- [ ] Security testing completed (XSS, SQL injection, CSRF)
- [ ] No sensitive data exposed in logs or error messages
- [ ] Performance benchmarks met (page load < 3 seconds)
- [ ] No memory leaks detected
- [ ] Accessibility standards checked (WCAG AA)

## ✅ Documentation
- [ ] User-facing documentation updated (if needed)
- [ ] API documentation updated (if applicable)
- [ ] Release notes drafted
- [ ] Known issues documented
- [ ] Test cases updated in test management system

## ✅ Non-Functional Requirements
- [ ] Feature works in production-like environment
- [ ] Error handling implemented and tested
- [ ] Logging added for debugging
- [ ] Analytics/tracking implemented (if applicable)
- [ ] Feature flags configured (if applicable)

## ✅ Deployment Readiness
- [ ] Build succeeds in CI/CD pipeline
- [ ] All automated tests pass in CI/CD
- [ ] Database migrations tested (if applicable)
- [ ] Rollback plan documented
- [ ] Production deployment checklist reviewed
- [ ] Product Owner has approved the feature

## ✅ Team Communication
- [ ] Demo completed in Sprint Review
- [ ] Stakeholders notified of changes
- [ ] Support team briefed (if customer-facing)
- [ ] Handoff documentation provided to operations team

---

## Story-Specific DoD Example

**User Story:** As a shopper, I want to add items to cart

**Additional DoD for This Story:**
- [ ] Cart badge displays correct item count (1-6 items)
- [ ] Cart state persists across page navigation
- [ ] Cart state persists after logout/login
- [ ] Maximum 6 items enforced (all SauceDemo products)
- [ ] "Add to cart" button changes to "Remove" after adding
- [ ] No duplicate items in cart (same item can't be added twice)
- [ ] Cart total calculation accurate
- [ ] Empty cart state displays correctly
```

**Step 3: Identify Story-Specific DoD Items (5 min)**

For the "Checkout Process" user story, add 5-7 story-specific DoD items:
```markdown
## Story-Specific DoD: Checkout Process

- [ ] [Your item 1]
- [ ] [Your item 2]
- [ ] [Your item 3]
- [ ] [Your item 4]
- [ ] [Your item 5]
```

### Deliverable
Save as `mentee-work/week-09/definition-of-done.md`

Include:
- Complete DoD checklist (7 categories)
- 2 story-specific DoD examples

### Success Criteria
- ✅ DoD checklist covers Code, Testing, Security, Documentation, NFRs, Deployment, Communication
- ✅ At least 30 total checklist items
- ✅ 2 story-specific DoD examples with 5+ items each
- ✅ Items are measurable (can answer yes/no)
- ✅ Items go beyond acceptance criteria (technical completeness)

---

## Exercise 5: Sprint Planning for SauceDemo Testing (60 min)

### Objective
Plan a 2-week sprint for SauceDemo testing, including story selection, estimation, risk identification, and task breakdown.

### Background
**Sprint Planning** includes:
1. Review stories in backlog
2. Select stories for sprint
3. Estimate effort (story points or hours)
4. Break down into tasks
5. Identify risks and dependencies

### Instructions

**Step 1: Review Sprint Planning Template (10 min)**

**Sprint Details:**
- **Sprint Duration:** 2 weeks (10 business days)
- **Team Capacity:** 40 hours (5 days × 8 hours, assuming 1 QA)
- **Velocity:** 20 story points (based on past sprints)

**Step 2: Select Stories from Backlog (15 min)**

**Backlog (Prioritized):**

| Story ID | User Story | Story Points | Priority | Dependencies |
|----------|-----------|--------------|----------|--------------|
| US-001 | User Login | 5 | High | None |
| US-002 | Add Items to Cart | 8 | High | US-001 (login required) |
| US-003 | Product Sorting | 3 | Medium | US-001 |
| US-004 | Checkout Process | 13 | High | US-001, US-002 |
| US-005 | Remove from Cart | 5 | Medium | US-002 |
| US-006 | View Product Details | 3 | Low | US-001 |
| US-007 | Search Products | 8 | Low | US-001 |

**Select stories for Sprint 1 (target: 20 story points, 40 hours):**

Create this table:
```markdown
## Sprint 1 - Selected Stories

| Story ID | Story | Story Points | Hours Estimate | Why Selected? |
|----------|-------|--------------|----------------|---------------|
| US-001 | User Login | 5 | 10 hours | High priority, no dependencies, foundational |
| US-002 | Add to Cart | 8 | 16 hours | High priority, depends on US-001 |
| US-003 | Product Sorting | 3 | 6 hours | Medium priority, fills remaining capacity |
| US-005 | Remove from Cart | 5 | 10 hours | Medium priority, quick win |

**Total:** 21 story points, 42 hours (slightly over capacity - will adjust in sprint)
```

**Step 3: Break Down Stories into Testing Tasks (20 min)**

For each selected story, list testing tasks:

```markdown
## Testing Task Breakdown

### US-001: User Login (5 story points, 10 hours)

**Testing Tasks:**
- [ ] Review acceptance criteria with team (30 min)
- [ ] Create test data (users, credentials) (30 min)
- [ ] Write test cases (5 positive, 5 negative) (2 hours)
- [ ] Execute smoke tests (happy path) (1 hour)
- [ ] Execute functional tests (all scenarios) (2 hours)
- [ ] Execute security tests (SQL injection, XSS) (1 hour)
- [ ] Cross-browser testing (Chrome, Firefox, Safari) (1.5 hours)
- [ ] Regression testing (verify no impact on other features) (1 hour)
- [ ] Document test results (30 min)

**Total:** 10 hours

---

### US-002: Add Items to Cart (8 story points, 16 hours)

**Testing Tasks:**
- [ ] Review acceptance criteria (30 min)
- [ ] Create test data (products, cart states) (1 hour)
- [ ] Write test cases (10 scenarios: add, remove, badge, persist) (3 hours)
- [ ] Execute functional tests (4 hours)
- [ ] Execute boundary tests (0 items, 1 item, 6 items) (1 hour)
- [ ] Execute state transition tests (empty → items → checkout) (2 hours)
- [ ] Cross-browser testing (2 hours)
- [ ] Performance testing (cart load time) (1 hour)
- [ ] Regression testing (2 hours)
- [ ] Document test results (30 min)

**Total:** 16 hours

[... continue for US-003 and US-005 ...]
```

**Step 4: Identify Risks and Mitigation (10 min)**

```markdown
## Sprint Risks

| Risk ID | Risk Description | Probability | Impact | Mitigation Strategy |
|---------|-----------------|-------------|--------|---------------------|
| R-001 | US-002 depends on US-001 completion | High | High | Complete US-001 in first week, US-002 in second |
| R-002 | Test environment unstable | Medium | High | Setup backup test environment, report issues early |
| R-003 | Ambiguous acceptance criteria for US-004 | Medium | Medium | Clarify with PO in Sprint Planning, before dev starts |
| R-004 | Over-committed (42 hours vs 40 capacity) | High | Medium | Drop US-005 if needed, focus on US-001, US-002, US-003 |
| R-005 | Cross-browser bugs found late | Low | Medium | Run cross-browser tests early (day 3-4) |
```

**Step 5: Create Sprint Goal and Success Criteria (5 min)**

```markdown
## Sprint Goal

**Primary Goal:** Enable users to log in and manage shopping cart (add/remove items)

**Success Criteria:**
- ✅ Users can log in with valid credentials
- ✅ Users can add products to cart from inventory page
- ✅ Users can remove items from cart
- ✅ Cart badge displays accurate item count
- ✅ Product sorting works (bonus if time allows)
- ✅ All acceptance criteria met
- ✅ Definition of Done met for all stories
- ✅ Zero critical/high severity bugs in production

**Sprint Metrics:**
- Planned stories: 4
- Planned story points: 21
- Planned testing hours: 42
- Target velocity: 20 story points
```

### Deliverable
Save as `mentee-work/week-09/sprint-planning.md`

Include:
- Sprint details (duration, capacity, velocity)
- Selected stories table (4 stories, ~20 story points)
- Task breakdown for each story
- Risk identification table (5+ risks)
- Sprint goal and success criteria

### Success Criteria
- ✅ 4 user stories selected for sprint
- ✅ Total story points ≈ 20 (±3 points acceptable)
- ✅ Testing tasks broken down for each story
- ✅ Hours estimated per task
- ✅ 5+ risks identified with mitigation strategies
- ✅ Sprint goal clearly defined
- ✅ Success criteria measurable

---

## ✅ Exercise Completion Checklist
- [ ] Exercise 1: Agile Testing Quadrants - All 60 test cases categorized
- [ ] Exercise 2: BDD Scenarios - 15 test cases converted to Given-When-Then
- [ ] Exercise 3: Acceptance Criteria - 5 user stories with AC created
- [ ] Exercise 4: Definition of Done - Comprehensive DoD checklist created
- [ ] Exercise 5: Sprint Planning - 2-week sprint planned with tasks and risks

---

## Grading Rubric

| Category | Weight | Criteria |
|----------|--------|----------|
| **Completeness** | 20% | All 5 exercises completed, required counts met |
| **Quality** | 30% | BDD scenarios readable, AC specific, DoD comprehensive |
| **Accuracy** | 20% | Quadrant categorization correct, sprint math accurate |
| **Critical Thinking** | 15% | Risk identification thoughtful, task breakdown realistic |
| **Agile Understanding** | 10% | Demonstrates understanding of Agile principles and ceremonies |
| **Professionalism** | 5% | Clean formatting, clear writing, follows templates |
| **TOTAL** | **100%** | |

**FAANG-Level Standards:**
- BDD scenarios must be business-readable (no technical jargon)
- Acceptance criteria must be measurable (clear pass/fail)
- DoD must go beyond AC (technical + functional completeness)
- Sprint planning must consider dependencies and risks
- Quadrant distribution should reflect UI testing focus (Q2 dominant)

---

**Good luck! This week connects Week 8 test cases to Agile/BDD thinking. 🎯**
