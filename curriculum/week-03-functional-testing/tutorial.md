# Week 3: Functional Testing Types

## 🎯 Learning Objectives

By the end of this week, you will be able to:
- Differentiate between Smoke, Sanity, and Regression testing
- Perform effective Exploratory testing
- Write both Positive and Negative test cases
- Apply Re-testing strategies
- Choose the right testing type for different scenarios

---

## 📚 What is Functional Testing?

**Functional Testing** validates that the software functions according to specified requirements. It answers the question: "Does the feature work as expected?"

Functional testing focuses on:
- ✅ Inputs and outputs
- ✅ User interactions
- ✅ Business logic
- ✅ Data processing
- ✅ Feature completeness

---

## 🔥 Smoke Testing

### Definition
**Smoke Testing** is a quick, shallow test of critical functionality to verify the build is stable enough for further testing. Think of it as a "sanity check" before investing time in detailed testing.

**Origin:** The term comes from hardware testing - if you plug in a device and it doesn't smoke, it passes the basic test!

### Characteristics
- **Scope:** Critical paths only
- **Depth:** Surface-level, not exhaustive
- **Duration:** 15-30 minutes
- **Frequency:** Every build
- **Automation:** Highly recommended (95-100%)

### When to Use
- ✅ New build received
- ✅ Before starting detailed testing
- ✅ After deployment to test environment
- ✅ As first-level gate

### SauceDemo Smoke Test Suite (10 tests)

1. **Application loads successfully**
2. **Login with valid credentials succeeds**
3. **Products page displays**
4. **At least one product is visible**
5. **Can view product details**
6. **Can add product to cart**
7. **Cart icon updates with count**
8. **Can access cart page**
9. **Can access checkout page**
10. **Can logout successfully**

**Pass Criteria:** ALL tests must pass. If any fail, build is rejected.

### Example Smoke Test

```
Test ID: SMOKE-001
Title: Verify critical user journey

Steps:
1. Navigate to https://www.saucedemo.com/
2. Login with standard_user / secret_sauce
3. Verify Products page loads
4. Add "Backpack" to cart
5. Click cart icon
6. Click Checkout
7. Verify checkout page loads
8. Logout

Expected: All steps complete without errors

Time: 2-3 minutes
```

---

## 🧹 Sanity Testing

### Definition
**Sanity Testing** is a narrow, deep test of specific functionality after a minor change or bug fix. It verifies that a particular function or bug fix works correctly without testing the entire application.

### Characteristics
- **Scope:** Specific feature or bug fix
- **Depth:** Thorough for that specific area
- **Duration:** 30 minutes - 2 hours
- **Frequency:** After bug fixes or minor changes
- **Automation:** Partial (50%)

### Smoke vs Sanity

| Aspect | Smoke Testing | Sanity Testing |
|--------|---------------|----------------|
| **Scope** | Broad (entire app) | Narrow (specific feature) |
| **Depth** | Shallow | Deep |
| **When** | Every build | After bug fix/minor change |
| **Goal** | Is build stable? | Does fix work? |
| **Example** | Test all major features | Test login after fixing login bug |

### SauceDemo Sanity Test Example

**Scenario:** Bug fixed - "Cart counter not updating"

**Sanity Tests:**
1. Add single item → verify count = 1
2. Add second item → verify count = 2
3. Remove item → verify count = 1
4. Remove all items → verify count disappears/shows 0
5. Add item, navigate away, return → verify count persists
6. Add from product page → verify count updates
7. Add from catalog page → verify count updates

**Scope:** ONLY cart counter functionality, not entire app

---

## 🔄 Regression Testing

### Definition
**Regression Testing** ensures that existing functionality still works after changes (bug fixes, new features, refactoring). It verifies that new code didn't break old code.

### Characteristics
- **Scope:** Entire application or affected areas
- **Depth:** Comprehensive
- **Duration:** Hours to days
- **Frequency:** Before every release
- **Automation:** Highly recommended (70-80%)

### When to Perform Regression Testing
- ✅ Before every release
- ✅ After major bug fixes
- ✅ After new feature addition
- ✅ After code refactoring
- ✅ After configuration changes

### Types of Regression Testing

#### 1. Full Regression
- Test entire application
- All test cases executed
- Time-consuming but thorough
- **When:** Major releases

#### 2. Partial Regression
- Test affected areas + related functionality
- Subset of test cases
- More efficient
- **When:** Minor changes, bug fixes

#### 3. Unit Regression
- Re-run unit tests after code changes
- Automated via CI/CD
- **When:** Every code commit

### Regression Test Selection Strategies

**1. Test All:** Run entire regression suite
- **Pro:** Complete coverage
- **Con:** Time-consuming

**2. Test Selection:** Run only affected tests
- **Pro:** Faster
- **Con:** Requires impact analysis

**3. Test Prioritization:** Run high-priority tests first
- **Pro:** Early detection of critical issues
- **Con:** May miss lower-priority defects

### SauceDemo Regression Checklist

After adding a new feature (e.g., "Save for Later" button), test:

**Core Workflows:**
- [ ] Login still works
- [ ] Product catalog displays
- [ ] Add to cart works
- [ ] Checkout process works
- [ ] Logout works

**Related Features:**
- [ ] Shopping cart functionality
- [ ] Product details page
- [ ] Cart calculations

**Edge Cases:**
- [ ] Multiple items in cart
- [ ] Empty cart scenarios
- [ ] Session management

---

## 🔍 Exploratory Testing

### Definition
**Exploratory Testing** is simultaneous learning, test design, and test execution. Testers actively explore the application, learn its behavior, design tests on-the-fly, and execute them.

**James Bach:** "Exploratory testing is simultaneous test design and test execution."

### Characteristics
- **Scripted:** No (designed during testing)
- **Structure:** Charter-based or session-based
- **Duration:** Time-boxed sessions (60-120 minutes)
- **Documentation:** Notes, mind maps, bugs found
- **Automation:** Cannot be automated (requires human creativity)

### When to Use Exploratory Testing
- ✅ Understanding new application
- ✅ Finding unexpected issues
- ✅ After scripted tests are complete
- ✅ When requirements are unclear
- ✅ Time-constrained testing

### Session-Based Exploratory Testing

**Structure:**
1. **Charter:** What to explore and why
2. **Time-box:** 60-90 minute uninterrupted session
3. **Exploration:** Active testing with note-taking
4. **Debrief:** Document findings, bugs, questions

**Example Charter:**

```
Charter: Explore shopping cart functionality to discover edge cases

Focus Areas:
- Multiple items of same product
- Maximum quantity limits
- Cart persistence across sessions
- Removing items behavior
- Price calculations

Time: 90 minutes
```

### Exploratory Testing Techniques

**1. Tours (Guided Exploration)**
- **Money Tour:** Test most important features
- **Landmark Tour:** Visit all major features
- **Feature Tour:** Deep dive into one feature
- **Bad-Neighborhood Tour:** Test error-prone areas
- **Tourist Tour:** Random exploration

**2. Personas**
- Test as different user types
- Beginner, expert, malicious user

**3. Scenarios**
- Real-world usage scenarios
- "What would happen if...?"

**4. Heuristics**
- Boundary values
- Null/empty inputs
- Special characters
- Very long inputs

### SauceDemo Exploratory Session Example

**Charter:** Explore checkout process for usability and edge cases

**Notes:**
- Checkout requires first/last name, zip code
- What happens with special characters in name?
- What if zip code is invalid format?
- Can I go back and change cart after starting checkout?
- Does checkout save progress if I navigate away?
- What's maximum character limit for fields?

**Bugs Found:**
- [Document any issues discovered]

**Questions:**
- [Note unclear behaviors]

**Test Ideas:**
- [Ideas for future test cases]

---

## ✅ Positive Testing

### Definition
**Positive Testing** validates that the application behaves correctly when given valid inputs and under normal conditions.

### Goal
Verify the application does what it's supposed to do.

### Examples for SauceDemo

| Feature | Positive Test |
|---------|---------------|
| **Login** | Valid username + valid password → Success |
| **Add to Cart** | Click "Add to Cart" → Item added, count updates |
| **Checkout** | Valid form data → Order processes |
| **Sorting** | Select "Price (low to high)" → Products sorted correctly |
| **Product Details** | Click product → Details page displays |

### Positive Test Case Template

```
Test ID: POS-001
Title: User can successfully login with valid credentials

Preconditions: User exists in system

Test Data:
- Username: standard_user
- Password: secret_sauce

Steps:
1. Navigate to login page
2. Enter valid username
3. Enter valid password
4. Click Login button

Expected Result:
- Login successful
- Redirected to Products page
- No error messages
- Products are visible

Actual Result: [Pass/Fail]
```

---

## ❌ Negative Testing

### Definition
**Negative Testing** validates that the application handles invalid inputs, error conditions, and unexpected user behavior gracefully.

### Goal
Verify the application fails safely and provides helpful error messages.

### Why Negative Testing Matters
- Real users make mistakes
- Malicious users may try to break the system
- Systems should fail gracefully
- Good error messages improve UX

### Examples for SauceDemo

| Feature | Negative Test |
|---------|---------------|
| **Login** | Invalid username → Error message displayed |
| **Login** | Empty password → Validation error |
| **Login** | SQL injection attempt → Handled safely |
| **Checkout** | Missing required field → Form validation |
| **Checkout** | Special characters in name → Handled correctly |

### Negative Test Case Template

```
Test ID: NEG-001
Title: Login fails with invalid credentials

Preconditions: None

Test Data:
- Username: invalid_user
- Password: wrong_password

Steps:
1. Navigate to login page
2. Enter invalid username
3. Enter invalid password
4. Click Login button

Expected Result:
- Login fails
- Error message displayed: "Username and password do not match"
- User remains on login page
- Password field cleared for security

Actual Result: [Pass/Fail]
```

### Categories of Negative Tests

**1. Invalid Input Data**
- Wrong data type (text in number field)
- Out of range values
- Null/empty values
- Special characters

**2. Boundary Conditions**
- Below minimum
- Above maximum
- Exactly at boundary

**3. Security Testing**
- SQL injection
- XSS attempts
- Authentication bypass attempts

**4. State/Sequence Errors**
- Accessing pages out of order
- Skipping required steps
- Going back after completing action

**5. Environmental Issues**
- Network interruption
- Browser back button
- Session timeout

### Positive vs Negative Testing Balance

**Rule of Thumb:**
- 60-70% Positive tests (happy paths)
- 30-40% Negative tests (error handling)

**Why:** Positive tests verify core functionality. Negative tests ensure robustness.

---

## 🔁 Re-testing (Confirmation Testing)

### Definition
**Re-testing** is testing the same scenario that previously failed after a bug fix to verify the fix works.

### Characteristics
- **Purpose:** Verify bug is fixed
- **Scope:** Exact same test that failed
- **When:** After developer marks bug as "Fixed"
- **Automation:** Can be automated

### Re-testing Process

1. **Bug Reported:** QA finds and logs bug
2. **Bug Fixed:** Developer fixes and marks "Fixed"
3. **Re-test:** QA runs exact same test
4. **Verify:** If passes → Close bug; If fails → Reopen bug

### Re-testing vs Regression Testing

| Aspect | Re-testing | Regression Testing |
|--------|------------|-------------------|
| **Purpose** | Verify bug fix works | Ensure nothing else broke |
| **Scope** | Specific test that failed | Broader application testing |
| **When** | After bug fix | Before release |
| **Test Cases** | Same test as original failure | Suite of regression tests |

---

## 🎯 Choosing the Right Test Type

### Decision Matrix

| Situation | Recommended Test Type |
|-----------|----------------------|
| New build received | Smoke Testing |
| Bug marked as fixed | Re-testing + Sanity |
| New feature added | Sanity (feature) + Regression (impact) |
| Before release | Full Regression |
| Exploring new app | Exploratory Testing |
| Validating requirements | Positive + Negative Testing |
| Time is very limited | Smoke + Risk-based Selection |

---

## 💡 Best Practices

### 1. Automate Smoke Tests
- Run on every build automatically
- Fast feedback (< 10 minutes)
- Gate for detailed testing

### 2. Document Exploratory Sessions
- Use session sheets
- Capture bugs, questions, test ideas
- Review in team meetings

### 3. Balance Positive and Negative
- Don't only test happy paths
- Users will make mistakes
- Systems will receive invalid data

### 4. Prioritize Regression Tests
- Not everything needs regression testing every time
- Use risk-based prioritization
- Automate high-priority tests

### 5. Make Regression Repeatable
- Document test cases clearly
- Automate where possible
- Maintain regression suite

---

## 📝 Key Takeaways

1. **Smoke Testing:** Quick check of critical paths (build stability)
2. **Sanity Testing:** Deep check of specific area (after bug fix)
3. **Regression Testing:** Ensure old features still work (before release)
4. **Exploratory Testing:** Unscripted discovery (find unexpected issues)
5. **Positive Testing:** Valid inputs work correctly (happy paths)
6. **Negative Testing:** Invalid inputs handled gracefully (error handling)
7. **Re-testing:** Verify bug fix works (confirmation)

---

## 📖 Terminology

| Term | Definition |
|------|------------|
| **Smoke Test** | Quick test of critical functionality |
| **Sanity Test** | Focused test of specific area |
| **Regression** | Re-testing after changes |
| **Exploratory** | Simultaneous learning and testing |
| **Positive Test** | Valid input scenarios |
| **Negative Test** | Invalid input scenarios |
| **Re-test** | Verify bug fix |
| **Charter** | Guiding mission for exploratory session |

---

## 🎓 Further Reading

- "Exploratory Software Testing" by James Whittaker
- "Lessons Learned in Software Testing" by Kaner, Bach, Pettichord
- ISTQB Foundation Syllabus - Chapter 2.3 (Test Types)
- Ministry of Testing - Exploratory Testing resources

---

## 📝 Self-Assessment

1. What's the difference between Smoke and Sanity testing?
2. When would you perform Regression testing?
3. Why is Negative testing important?
4. What is a "charter" in Exploratory testing?
5. Name 3 scenarios for Positive and Negative tests
6. How is Re-testing different from Regression?
7. How long should an Exploratory testing session be?

---

**Next:** Complete Week 3 exercises to apply these testing types to SauceDemo!
