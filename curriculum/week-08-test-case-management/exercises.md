# Week 8: Test Case Design & Management - Exercises

## Exercise Overview
This week focuses on applying Test Case Design & Management concepts to SauceDemo.
Complete all exercises and document your work in `mentee-work/week-08/`

## Exercise 1: Write 50+ Test Cases (180 min)

### Objective
Comprehensive test case creation

### Instructions
[Detailed steps to complete this exercise]

### Deliverable
Save as `mentee-work/week-08/write-50+-test-cases.md`

---

## Exercise 2: Organize by Module (60 min)

### Objective
Structure test cases logically

### Instructions
[Detailed steps to complete this exercise]

### Deliverable
Save as `mentee-work/week-08/organize-by-module.md`

---

## Exercise 3: Traceability Matrix (60 min)

### Objective
Map requirements to tests

### Instructions
[Detailed steps to complete this exercise]

### Deliverable
Save as `mentee-work/week-08/traceability-matrix.md`

---

## Exercise 4: Test Data Management (45 min)

### Objective
Design test data sets

### Instructions
[Detailed steps to complete this exercise]

### Deliverable
Save as `mentee-work/week-08/test-data-management.md`

---

## Exercise 5: Test Case Review (45 min)

### Objective
Review and improve quality

### Instructions
[Detailed steps to complete this exercise]

### Deliverable
Save as `mentee-work/week-08/test-case-review.md`

---

## Exercise 6: GitHub Projects Test Management (60 min)

### Objective
Convert your test cases into GitHub issues for tracking and management using GitHub Projects

### Instructions

**Part 1: Create Test Case Issues (40 min)**

1. Navigate to: https://github.com/aslavchev/qa-fundamentals-11weeks/issues/new/choose
2. Select **"Test Case"** template
3. Convert your test cases from Exercises 1-5 into GitHub issues:
   - Use test case template for each issue
   - Title format: `[TEST] Brief description`
   - Add appropriate labels:
     - Test type: `test:ui`, `test:api`, `test:e2e`, `test:regression`, `test:smoke`, `test:integration`, `test:performance`
     - Severity: `severity:s0-blocker`, `severity:s1-critical`, `severity:s2-major`, `severity:s3-minor`, `severity:s4-trivial`
   - Add to "SauceDemo Test Suite" project
4. Organize in GitHub Project:
   - Set custom fields: Test Type, Test Suite, Severity, Module, Automation Status
   - Set Last Run Status to "Not Run"

**Part 2: Explore Project Views (10 min)**

1. Open "SauceDemo Test Suite" GitHub Project
2. Explore views:
   - **Test Inventory:** See all test cases organized by module
   - **Regression Suite:** Board view of regression tests
   - **Automation Backlog:** Which tests need automation
   - **Test Execution Tracker:** Track test execution status
3. Practice filtering and sorting

**Part 3: Document Setup (10 min)**

Create documentation with:
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

---


## ✅ Exercise Completion Checklist
- [ ] Exercise 1: Write 50+ Test Cases completed
- [ ] Exercise 2: Organize by Module completed
- [ ] Exercise 3: Traceability Matrix completed
- [ ] Exercise 4: Test Data Management completed
- [ ] Exercise 5: Test Case Review completed
- [ ] Exercise 6: GitHub Projects Test Management completed
