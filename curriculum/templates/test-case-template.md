# Test Case Template

## Test Case Information

| Field | Details |
|-------|---------|
| **Test Case ID** | TC-[Module]-[Number] (e.g., TC-LOGIN-001) |
| **Test Case Title** | Clear, concise title describing what is being tested |
| **Module/Feature** | The feature or module under test |
| **Priority** | Critical / High / Medium / Low |
| **Test Type** | Functional / Integration / Regression / Smoke / etc. |
| **Created By** | Your name |
| **Created Date** | YYYY-MM-DD |
| **Last Updated** | YYYY-MM-DD |

---

## Test Objective

Brief description of what this test case validates (1-2 sentences).

---

## Preconditions

List all conditions that must be met before executing this test:
- Condition 1
- Condition 2
- Condition 3

---

## Test Data

| Data Field | Value | Notes |
|------------|-------|-------|
| Username | standard_user | Valid user |
| Password | secret_sauce | Valid password |
| Product | Backpack | First item in list |

---

## Test Steps

| Step # | Action | Expected Result | Actual Result | Status |
|--------|--------|-----------------|---------------|--------|
| 1 | Navigate to https://www.saucedemo.com/ | Application loads successfully | | |
| 2 | Enter username "standard_user" | Username field populated | | |
| 3 | Enter password "secret_sauce" | Password field shows dots/asterisks | | |
| 4 | Click "Login" button | User redirected to Products page | | |
| 5 | Verify page title is "Products" | Title "Products" visible | | |

---

## Expected Results

Overall expected outcome when all steps pass:
- User successfully logged in
- Products page displayed
- No error messages shown

---

## Actual Results

_To be filled during test execution_

---

## Pass/Fail Criteria

**Pass:** All steps execute successfully and expected results match actual results
**Fail:** Any step fails or expected results don't match actual results

---

## Status

- [ ] Not Executed
- [ ] Pass
- [ ] Fail
- [ ] Blocked
- [ ] Skipped

---

## Test Environment

| Component | Details |
|-----------|---------|
| OS | Windows 11 / macOS / Linux |
| Browser | Chrome 118.x |
| Application URL | https://www.saucedemo.com/ |
| Test Environment | Production / Staging / QA |

---

## Dependencies

List any dependencies on other test cases, data, or features:
- Depends on: TC-LOGIN-001
- Requires: Valid user credentials

---

## Notes / Comments

Any additional information, observations, or special considerations:
-
-

---

## Linked Defects

If test fails, link to bug reports:
- Bug ID: BUG-XXX
- Bug Title: Brief description

---

## Traceability

| Requirement ID | Requirement Description |
|----------------|-------------------------|
| REQ-001 | User must be able to log in with valid credentials |

---

**Template Version:** 1.0
**Last Updated:** October 2025
