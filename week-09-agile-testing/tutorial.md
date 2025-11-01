# Week 9: Agile Testing & Methodologies

## 🎯 Learning Objectives
- Understand Agile Testing Quadrants
- Write BDD scenarios using Gherkin syntax (Given-When-Then)
- Create effective acceptance criteria
- Define "Definition of Done" for quality
- Participate in Agile ceremonies (sprint planning, daily standup, retrospectives)
- Adapt traditional testing practices to Agile/Scrum

## 📚 Why Agile Testing?

**Problem:** Traditional waterfall testing happens at the end, finding bugs late when they're expensive to fix.

**Solution:** Agile testing is continuous, collaborative, and integrated throughout development.

### Agile vs Waterfall Testing

| Aspect | Waterfall Testing | Agile Testing |
|--------|-------------------|---------------|
| **When** | After development completes | Throughout development (continuous) |
| **Documentation** | Heavy (100-page test plans) | Lightweight (user stories + acceptance criteria) |
| **Test Planning** | Upfront, comprehensive | Iterative, sprint-by-sprint |
| **Scope** | Fixed (all requirements defined) | Flexible (evolving requirements) |
| **Team** | Separate QA team | Cross-functional team (dev + QA + PO) |
| **Goal** | Find all bugs | Prevent bugs + rapid feedback |
| **Automation** | Optional | Essential (enables continuous testing) |

### Benefits of Agile Testing
- ✅ Bugs found earlier (cheaper to fix)
- ✅ Continuous feedback to developers
- ✅ Higher quality (quality built in, not tested in)
- ✅ Faster releases (2-week sprints vs 6-month releases)
- ✅ Better collaboration (whole team owns quality)
- ✅ Adaptability (respond to changing requirements)

---

## 1️⃣ Agile Testing Quadrants

### What Are Testing Quadrants?

**Created by:** Brian Marick, popularized by Lisa Crispin & Janet Gregory

**Purpose:** Classify tests by their purpose and audience

### The Four Quadrants

```
                Technology-Facing
                       |
                       |
        Q2             |              Q1
   Automated          |          Automated
   Functional Tests   |          Unit Tests
   (Business-facing)  |          Integration Tests
                      |          Component Tests
                      |
Supporting the Team --|-- Critiquing the Product
                      |
        Q3            |              Q4
   Manual            |          Manual
   Exploratory       |          Non-Functional
   Usability         |          Performance
   User Acceptance   |          Security
                     |
                     |
              Business-Facing
```

### Quadrant 1 (Q1): Technology-Facing, Supporting the Team

**Purpose:** Support development with automated tests

**Who:** Developers (with QA input)

**Types:**
- Unit tests (95%+ coverage target)
- Component tests
- Integration tests (API tests)

**Tools:** JUnit, PyTest, Jest, NUnit

**Examples for SauceDemo:**
```
- Unit test: Validate price calculation function
- Integration test: Verify API endpoint returns correct product list
- Component test: Test login authentication module
```

**Goal:** Catch bugs immediately, enable refactoring

**Automation:** 95-100%

### Quadrant 2 (Q2): Business-Facing, Supporting the Team

**Purpose:** Verify business requirements are met

**Who:** QA + Developers + Product Owner

**Types:**
- Functional tests (BDD scenarios)
- Story tests (acceptance tests)
- Prototypes/simulations
- Examples to guide development

**Tools:** Cucumber, SpecFlow, Behave, Selenium

**Examples for SauceDemo:**
```
Scenario: User adds item to cart
  Given user is logged in
  When user clicks "Add to cart" for Backpack
  Then cart badge shows "1"
  And Backpack appears in cart
```

**Goal:** Ensure features work as expected

**Automation:** 60-80%

### Quadrant 3 (Q3): Business-Facing, Critiquing the Product

**Purpose:** Explore and evaluate the product

**Who:** QA + Product Owner + Users

**Types:**
- Exploratory testing
- Usability testing
- User acceptance testing (UAT)
- A/B testing
- Alpha/Beta testing

**Tools:** Human intelligence, session-based testing

**Examples for SauceDemo:**
```
- Exploratory session: "Try to break the checkout flow"
- Usability: "Is the cart icon intuitive?"
- UAT: "Does this meet your needs?" (real users)
```

**Goal:** Find unexpected issues, validate user experience

**Automation:** 0-10%

### Quadrant 4 (Q4): Technology-Facing, Critiquing the Product

**Purpose:** Validate non-functional requirements

**Who:** QA + Performance/Security specialists

**Types:**
- Performance testing (load, stress, endurance)
- Security testing (penetration, vulnerability scans)
- Scalability testing
- Reliability testing
- Infrastructure testing

**Tools:** JMeter, K6, Gatling, OWASP ZAP, Burp Suite

**Examples for SauceDemo:**
```
- Performance: Can app handle 1000 concurrent users?
- Security: Is app vulnerable to SQL injection?
- Scalability: Does response time degrade under load?
```

**Goal:** Ensure system is production-ready

**Automation:** 70-90%

### Mapping SauceDemo Tests to Quadrants

| Test | Quadrant | Why |
|------|----------|-----|
| Unit test: calculateTotal() function | Q1 | Technology-facing, supports development |
| BDD: User can login with valid credentials | Q2 | Business-facing, verifies requirement |
| Exploratory: Cart edge cases | Q3 | Business-facing, critiques UX |
| Performance: 100 concurrent logins | Q4 | Technology-facing, critiques system |
| Integration: API returns product JSON | Q1 | Technology-facing, supports development |
| Functional: Checkout form validation | Q2 | Business-facing, verifies requirement |
| Usability: Is sort dropdown intuitive? | Q3 | Business-facing, critiques UX |
| Security: XSS protection | Q4 | Technology-facing, critiques system |

### Quadrants and Automation

```
Q1: 95-100% automated (unit, integration)
Q2: 60-80% automated (functional regression)
Q3: 0-10% automated (exploratory, manual)
Q4: 70-90% automated (performance, security)
```

**Key Insight:** Not all tests should be automated. Exploratory and usability tests require human judgment.

---

## 2️⃣ Behavior-Driven Development (BDD)

### What is BDD?

**Definition:** BDD uses natural language to describe application behavior from the user's perspective. Tests are written before or alongside code.

**Created by:** Dan North (2003)

**Key Concept:** "Specification by Example" - Use concrete examples to define requirements

### Why BDD?

**Problem:** Requirements are ambiguous. "User can login" means what exactly?

**Solution:** Use specific examples in Given-When-Then format

**Benefits:**
- ✅ Shared understanding (dev, QA, PO speak same language)
- ✅ Living documentation (tests ARE the spec)
- ✅ Better requirements (concrete examples reveal gaps)
- ✅ Collaboration (whole team writes scenarios together)
- ✅ Automation-ready (Gherkin → automated tests)

### Gherkin Syntax

**Language:** Gherkin (domain-specific language for BDD)

**Keywords:**
- `Feature:` High-level description
- `Scenario:` Specific example/test case
- `Given:` Preconditions (setup)
- `When:` Action (trigger)
- `Then:` Expected outcome (verification)
- `And:` Additional steps
- `But:` Negative assertion

### BDD Template: Given-When-Then

```gherkin
Scenario: [Brief description of scenario]
  Given [Precondition/setup]
  When [Action/trigger]
  Then [Expected result]
```

### SauceDemo BDD Examples

#### Example 1: Login Success

```gherkin
Feature: User Authentication
  As a registered user
  I want to log in to SauceDemo
  So that I can shop for products

Scenario: Successful login with valid credentials
  Given I am on the SauceDemo login page
  And I have valid credentials (standard_user / secret_sauce)
  When I enter "standard_user" in the username field
  And I enter "secret_sauce" in the password field
  And I click the LOGIN button
  Then I should be redirected to the inventory page
  And I should see 6 products displayed
  And the URL should be "/inventory.html"
```

#### Example 2: Login Failure

```gherkin
Scenario: Failed login with invalid password
  Given I am on the SauceDemo login page
  When I enter "standard_user" in the username field
  And I enter "wrong_password" in the password field
  And I click the LOGIN button
  Then I should remain on the login page
  And I should see an error message "Username and password do not match"
  And the error message should be displayed in red
```

#### Example 3: Add to Cart

```gherkin
Feature: Shopping Cart Management
  As a shopper
  I want to add items to my cart
  So that I can purchase them later

Scenario: Add single item to empty cart
  Given I am logged in as "standard_user"
  And I am on the inventory page
  And my cart is empty (badge shows no count)
  When I click "Add to cart" for "Sauce Labs Backpack"
  Then the button should change to "Remove"
  And the cart badge should show "1"
  And the cart should contain "Sauce Labs Backpack"
  And the cart total should be "$29.99"
```

#### Example 4: Checkout Validation

```gherkin
Scenario: Checkout fails when required field is empty
  Given I am logged in as "standard_user"
  And I have 1 item in my cart
  And I am on the checkout information page
  When I leave the "First Name" field empty
  And I enter "Doe" in the "Last Name" field
  And I enter "12345" in the "Postal Code" field
  And I click the CONTINUE button
  Then I should remain on the checkout information page
  And I should see an error message "Error: First Name is required"
  And the error message should be displayed in red
```

### BDD Best Practices

#### ✅ DO:
- **Use business language** (not technical)
  ```
  ✅ Given I am on the login page
  ❌ Given the URL is "https://www.saucedemo.com"
  ```

- **One scenario per test case**
  ```
  ✅ Scenario: Login with valid credentials
  ✅ Scenario: Login with invalid password
  ❌ Scenario: Login with valid and invalid credentials (two scenarios)
  ```

- **Be specific with data**
  ```
  ✅ When I enter "standard_user" in the username field
  ❌ When I enter a username
  ```

- **Focus on behavior, not implementation**
  ```
  ✅ Then I should see the inventory page
  ❌ Then the Angular controller should load the inventory component
  ```

- **Keep scenarios independent**
  - Each scenario should work standalone
  - No dependencies on other scenarios

#### ❌ DON'T:
- **Don't use technical jargon**
  ```
  ❌ Given the DOM is loaded
  ❌ When I POST to /api/login
  ```

- **Don't write scripts (too detailed)**
  ```
  ❌ When I move mouse to coordinates 450, 230
  ❌ Then the CSS class should be "logged-in"
  ```

- **Don't combine multiple scenarios**
  ```
  ❌ Scenario: Login and add item and checkout (3 scenarios)
  ```

### Scenario Outline (Data-Driven BDD)

**Purpose:** Test multiple data sets with one scenario template

**Example:**

```gherkin
Scenario Outline: Login with different invalid credentials
  Given I am on the SauceDemo login page
  When I enter "<username>" in the username field
  And I enter "<password>" in the password field
  And I click the LOGIN button
  Then I should see error message "<error>"

  Examples:
    | username       | password      | error                                    |
    | standard_user  | wrong_pass    | Username and password do not match       |
    | wrong_user     | secret_sauce  | Username and password do not match       |
    | locked_out_user| secret_sauce  | Sorry, this user has been locked out     |
    |                | secret_sauce  | Username is required                     |
    | standard_user  |               | Password is required                     |
```

**Result:** 5 test cases executed from one scenario template

---

## 3️⃣ User Stories & Acceptance Criteria

### User Story Format

**Template:**
```
As a [user role]
I want to [goal/desire]
So that [benefit/value]
```

**Example:**
```
As a shopper
I want to add items to my cart
So that I can purchase multiple products in one order
```

### Acceptance Criteria (AC)

**Purpose:** Defines when a user story is "done" from a functional perspective

**Format:** Given-When-Then (same as BDD scenarios)

**Example:**

```
User Story: Add item to cart

Acceptance Criteria:
1. Given I am on the inventory page
   When I click "Add to cart" for a product
   Then the product should appear in my cart
   And the cart badge count should increase by 1
   And the button should change to "Remove"

2. Given I am on the inventory page
   When I click "Add to cart" for the same product twice
   Then the product should appear once in the cart
   And the quantity should not increase (or should increase, per requirements)

3. Given I am on the product detail page
   When I click "Add to cart"
   Then the product should be added to cart
   And I should be able to continue shopping
```

### INVEST Criteria for User Stories

Good user stories are **INVEST:**

- **I**ndependent: Can be developed in any order
- **N**egotiable: Details can be discussed
- **V**aluable: Provides value to user/business
- **E**stimable: Team can estimate effort
- **S**mall: Can be completed in one sprint
- **T**estable: Clear acceptance criteria

### SauceDemo User Stories

#### Story 1: User Login

```
As a registered user
I want to log in to the application
So that I can access my personalized shopping experience

Acceptance Criteria:
1. Login succeeds with valid credentials
   Given I have a valid account (standard_user / secret_sauce)
   When I enter my credentials and click LOGIN
   Then I should be redirected to the inventory page

2. Login fails with invalid password
   Given I enter valid username but wrong password
   When I click LOGIN
   Then I should see error "Username and password do not match"

3. Locked user cannot login
   Given I am a locked user (locked_out_user)
   When I attempt to login
   Then I should see error "Sorry, this user has been locked out"
```

#### Story 2: Cart Persistence

```
As a shopper
I want my cart to persist across sessions
So that I don't lose my selections if I close the browser

Acceptance Criteria:
1. Cart persists after logout/login
   Given I add 2 items to cart
   When I logout and login again
   Then my cart should still contain those 2 items

2. Cart persists after browser close
   Given I add 1 item to cart
   When I close the browser and reopen
   Then my cart should still contain that 1 item

3. Cart clears after order completion
   Given I complete an order
   When I return to the inventory page
   Then my cart should be empty
```

### Definition of Done (DoD)

**Purpose:** Checklist that defines when work is complete (beyond just acceptance criteria)

**Applies to:** User stories, sprints, releases

**Example DoD for User Stories:**

```
Definition of Done: User Story

✅ Code:
- [ ] Code written and reviewed
- [ ] Unit tests written (80%+ coverage)
- [ ] Code merged to main branch
- [ ] No critical code analysis warnings

✅ Testing:
- [ ] All acceptance criteria met
- [ ] Functional tests executed and passing
- [ ] Regression tests passing
- [ ] Exploratory testing completed (1 session)
- [ ] No Severity 1 or 2 defects

✅ Documentation:
- [ ] Code documented (comments, docstrings)
- [ ] User-facing documentation updated
- [ ] Test cases updated in TestRail

✅ Automation:
- [ ] Automated tests created (where applicable)
- [ ] Automated tests passing in CI/CD

✅ Review:
- [ ] Code review completed
- [ ] QA review completed
- [ ] Product Owner acceptance

✅ Deployment:
- [ ] Deployed to staging environment
- [ ] Smoke tests pass in staging
- [ ] Ready for production deployment
```

---

## 4️⃣ Agile Ceremonies & QA Role

### Sprint Planning

**What:** Plan work for upcoming sprint (usually 2 weeks)

**Duration:** 2-4 hours (for 2-week sprint)

**QA Role:**
- Review user stories and acceptance criteria
- Ask clarifying questions ("What if...?", "How should it behave when...?")
- Estimate testing effort
- Identify risks early
- Ensure testability (can we test this in 2 weeks?)

**QA Questions to Ask:**
```
- What are the acceptance criteria?
- What's the expected behavior for edge cases?
- Are there any dependencies (APIs, test data)?
- What's the test environment?
- Do we need test data setup?
- Are there any security/performance concerns?
- What's NOT in scope? (define boundaries)
```

**Output:** Committed user stories for sprint, with clear acceptance criteria

### Daily Standup

**What:** Daily 15-minute sync

**QA Updates:**
```
Yesterday: Completed functional testing for Story A, found 2 bugs
Today: Will test Story B, retest fixes from yesterday
Blockers: Waiting for test environment access
```

**Keep it brief:** What (tasks), not How (details)

### Backlog Refinement (Grooming)

**What:** Review and clarify upcoming user stories

**Duration:** 1-2 hours per week

**QA Role:**
- Review acceptance criteria (are they testable?)
- Suggest additional scenarios
- Identify missing requirements
- Estimate testing effort

**Example:**
```
Story: User can filter products by price range

QA Input:
- AC missing: What if min > max? (e.g., min=$100, max=$10)
- AC missing: What if user enters negative price?
- AC missing: What's the maximum price range allowed?
- Testability: Need test data with products at various price points
```

### Sprint Review (Demo)

**What:** Demonstrate completed work to stakeholders

**Duration:** 1-2 hours

**QA Role:**
- Confirm all acceptance criteria met
- Highlight testing completed
- Demo new features (sometimes)
- Provide quality metrics (pass rate, defects found/fixed)

### Sprint Retrospective

**What:** Reflect on what went well, what didn't, how to improve

**Duration:** 1-2 hours

**QA Input:**
```
What went well:
- Early involvement in story refinement helped catch issues
- Automation saved 6 hours in regression testing

What didn't go well:
- Test environment was unstable (3 days downtime)
- Requirements changed mid-sprint (scope creep)

Action items:
- Set up dedicated test environment (not shared)
- Implement change control process
```

---

## 5️⃣ Agile Testing Best Practices

### 1. Shift-Left Testing

**Concept:** Test early and often, don't wait until the end

**How:**
- QA reviews requirements before development starts
- QA creates test cases from acceptance criteria upfront
- QA pairs with developers during coding
- Automated tests run on every commit (CI/CD)

**Benefits:**
- Bugs found early (cheaper to fix)
- Faster feedback loop
- Higher quality

### 2. Whole Team Approach

**Concept:** Quality is everyone's responsibility, not just QA

**How:**
- Developers write unit tests
- Product Owner defines clear acceptance criteria
- QA facilitates quality conversations
- Everyone participates in exploratory testing

**Mindset Shift:**
```
❌ "I'm done coding, QA can test it now"
✅ "I've completed development AND testing, it's ready for QA review"
```

### 3. Test Automation Pyramid

**Concept:** More unit tests, fewer UI tests

```
           /\
          /  \  E2E (UI) Tests (10%)
         /    \  Slow, brittle, expensive
        /------\
       /        \  Integration/API Tests (30%)
      /          \  Moderate speed/cost
     /------------\
    /              \  Unit Tests (60%)
   /________________\  Fast, stable, cheap
```

**Goal:**
- 60-70% unit tests (fast, isolated)
- 20-30% integration tests (API, component)
- 10-20% E2E tests (UI, critical paths)

### 4. Continuous Testing

**Concept:** Tests run automatically on every code change

**Implementation:**
- CI/CD pipeline (Jenkins, GitHub Actions, GitLab CI)
- Automated tests triggered on commit/PR
- Fast feedback (within 10-15 minutes)

**Example Pipeline:**
```
1. Developer commits code
2. Unit tests run (2 min)
3. Integration tests run (5 min)
4. Smoke tests run (3 min)
5. Build succeeds or fails → notify team
```

### 5. Risk-Based Testing in Sprints

**Concept:** Limited time, so prioritize high-risk areas

**How:**
- Identify high-risk stories early (sprint planning)
- Allocate more testing effort to high-risk
- Low-risk stories get basic smoke testing

**Example:**
```
Story A: New payment integration (HIGH RISK)
- 15 test cases, exploratory session, security review

Story B: Change button color (LOW RISK)
- Visual verification only, 2 test cases
```

---

## 6️⃣ Agile Testing Challenges & Solutions

### Challenge 1: Time Pressure

**Problem:** 2-week sprints, not enough time to test everything

**Solution:**
- Risk-based prioritization (test what matters most)
- Test automation (regression testing)
- Exploratory testing (time-boxed sessions)
- Clear Definition of Done (prevent incomplete work)

### Challenge 2: Changing Requirements

**Problem:** Requirements change mid-sprint, tests become obsolete

**Solution:**
- Limit scope changes mid-sprint (defer to next sprint)
- Involve QA early in change discussions
- Update test cases incrementally
- Focus on acceptance criteria, not detailed scripts

### Challenge 3: Incomplete Acceptance Criteria

**Problem:** Stories don't have clear testable acceptance criteria

**Solution:**
- QA reviews stories in backlog refinement
- Use BDD Given-When-Then format
- Ask "What if...?" questions
- Reject stories without clear AC

### Challenge 4: Technical Debt

**Problem:** Pressure to deliver fast, skip testing, accumulate bugs

**Solution:**
- Make technical debt visible (track in backlog)
- Allocate 10-20% sprint capacity for debt reduction
- "Boy Scout Rule" - always leave code better than you found it
- Include quality metrics in sprint review

### Challenge 5: Automation Maintenance

**Problem:** Automated tests break frequently, consuming time

**Solution:**
- Design stable, maintainable tests (Page Object Model)
- Don't automate everything (exploratory stays manual)
- Refactor tests when application changes
- Monitor test flakiness (fix or remove flaky tests)

---

## 7️⃣ SauceDemo Agile Testing Example

### Sprint Goal
"Enable users to add items to cart and persist cart across sessions"

### User Stories for Sprint

#### Story 1: Add to Cart
```
As a shopper
I want to add items to my cart
So that I can purchase multiple products

Acceptance Criteria:
1. User can add item from inventory page
2. Cart badge updates with item count
3. Button changes from "Add to cart" to "Remove"
4. Item appears in cart with correct price

Estimate: 5 story points
```

#### Story 2: Cart Persistence
```
As a shopper
I want my cart to persist across sessions
So that I don't lose my selections

Acceptance Criteria:
1. Cart persists after logout/login
2. Cart persists after browser close/reopen
3. Cart uses local storage (technical requirement)

Estimate: 8 story points (higher complexity)
```

### QA Sprint Plan

**Week 1:**
- Day 1-2: Review acceptance criteria, create BDD scenarios
- Day 3-4: Story 1 testing (functional + exploratory)
- Day 5: Automation for Story 1 critical paths

**Week 2:**
- Day 1-2: Story 2 testing (functional + edge cases)
- Day 3: Exploratory session (cart persistence scenarios)
- Day 4: Regression testing (automated suite)
- Day 5: Bug fixes retest, sprint summary

### BDD Scenarios Created

```gherkin
Feature: Shopping Cart

Scenario: Add item to cart from inventory
  Given I am logged in as "standard_user"
  And I am on the inventory page
  When I click "Add to cart" for "Sauce Labs Backpack"
  Then cart badge should show "1"
  And button should change to "Remove"

Scenario: Cart persists after logout
  Given I am logged in as "standard_user"
  And I have added "Sauce Labs Backpack" to cart
  When I logout
  And I login again as "standard_user"
  Then cart should still contain "Sauce Labs Backpack"
  And cart badge should show "1"
```

### Testing Summary

**Tests Executed:** 25
**Passed:** 22
**Failed:** 3
**Defects Found:** 3 (2 fixed, 1 deferred)

**Sprint Outcome:** ✅ Stories completed, Definition of Done met

---

## 📝 Summary

### Key Takeaways

1. **Agile Testing Quadrants:**
   - Q1: Unit/Integration (automated, tech-facing, support dev)
   - Q2: Functional/BDD (automated, business-facing, support dev)
   - Q3: Exploratory/Usability (manual, business-facing, critique product)
   - Q4: Performance/Security (automated, tech-facing, critique product)

2. **BDD (Behavior-Driven Development):**
   - Use Given-When-Then format
   - Write in business language, not technical
   - Scenarios are living documentation
   - Enables collaboration (dev, QA, PO)

3. **User Stories & Acceptance Criteria:**
   - Template: As a [role] I want [goal] So that [benefit]
   - Acceptance Criteria define "done"
   - Use Given-When-Then format for clarity

4. **Definition of Done:**
   - Checklist beyond acceptance criteria
   - Includes code, tests, documentation, deployment
   - Prevents incomplete work

5. **Agile Ceremonies:**
   - Sprint Planning: Review AC, identify risks, estimate
   - Daily Standup: Brief status update
   - Backlog Refinement: Clarify upcoming stories
   - Sprint Review: Demo completed work
   - Retrospective: Continuous improvement

### This Week's Challenge

**Convert 15 traditional test cases to BDD scenarios** using Given-When-Then format

**Map SauceDemo tests to Agile Testing Quadrants**

**Create acceptance criteria for 3 user stories**

---

## 🤔 Self-Assessment Questions

1. What are the four Agile Testing Quadrants?
2. What's the difference between Q1 and Q2 tests?
3. What does Given-When-Then represent in BDD?
4. How do you write a user story?
5. What's the difference between Acceptance Criteria and Definition of Done?
6. What's QA's role in Sprint Planning?
7. Why is shift-left testing important?
8. What's the Test Automation Pyramid?
9. How does Agile testing differ from Waterfall testing?
10. What's a Scenario Outline in BDD?

### Answers to Check
1. Q1 (Unit/Integration), Q2 (Functional/BDD), Q3 (Exploratory/Usability), Q4 (Performance/Security)
2. Q1 = Technology-facing (unit tests, for developers); Q2 = Business-facing (functional tests, for requirements)
3. Given = preconditions/setup, When = action/trigger, Then = expected result
4. As a [role] I want [goal] So that [benefit]
5. AC = when feature is functionally complete; DoD = when feature is truly done (tested, documented, deployed)
6. Review stories, ask questions, clarify AC, estimate testing effort, identify risks
7. Find bugs earlier (cheaper to fix), prevent bugs through early involvement
8. More unit tests (60%), fewer integration (30%), fewest UI/E2E (10%)
9. Agile = continuous, lightweight docs, flexible; Waterfall = end-phase, heavy docs, fixed scope
10. Data-driven BDD - one scenario template with multiple data examples

---

**📚 Continue to: exercises.md → Write 15+ BDD scenarios for SauceDemo**

**⏭️ Next Week:** Defect Management - Bug lifecycle, severity vs priority, effective bug reporting
