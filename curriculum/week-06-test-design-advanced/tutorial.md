# Week 6: Test Design Techniques (Advanced)

## 🎯 Learning Objectives
- Apply Pairwise Testing to reduce test combinations
- Use Error Guessing to predict likely failures
- Perform Risk-Based Testing
- Execute Exploratory Testing sessions with charters
- Analyze and improve test coverage

## 📚 Why Advanced Test Design Techniques?

**Problem:** Complex applications have too many combinations to test exhaustively. How do we test smart, not hard?

**Solution:** Use advanced techniques to optimize testing while maintaining high defect detection rates.

### Benefits
- ✅ Reduce test execution time by 70-90%
- ✅ Focus effort on high-risk areas
- ✅ Find defects faster through structured exploration
- ✅ Achieve better coverage with fewer tests
- ✅ Leverage tester experience systematically

---

## 1️⃣ Pairwise Testing (All-Pairs Testing)

### Definition
Pairwise testing ensures every possible pair of input parameters is tested at least once. It's based on the empirical finding that most bugs are triggered by interactions between two parameters, not many parameters.

### Key Concept
**Research shows:** 70-95% of defects are caused by interactions between 1 or 2 parameters. Testing all pairs gives excellent coverage without testing all combinations.

### Why Pairwise?
**Example:** 5 parameters with 3 values each
- **All combinations:** 3^5 = 243 test cases
- **Pairwise:** ~15 test cases (94% reduction!)
- **Defect detection:** Catches 70-90% of bugs

### When to Use Pairwise
✅ Configuration testing (OS, browser, device combinations)
✅ Many input parameters with discrete values
✅ Time/resource constraints prevent exhaustive testing
✅ Integration testing with multiple systems

❌ Critical calculations requiring exhaustive testing
❌ Simple scenarios with few combinations

### How Pairwise Works

#### Example: Login Screen Configuration
**Parameters:**
- Browser: Chrome, Firefox, Safari
- OS: Windows, Mac, Linux
- Language: English, Spanish, French
- Resolution: 1920x1080, 1366x768, 2560x1440

**All combinations:** 3 × 3 × 3 × 3 = 81 test cases

**Pairwise approach:** ~12 test cases covering all pairs

| Test | Browser | OS | Language | Resolution |
|------|---------|----|---------|-----------  |
| 1 | Chrome | Windows | English | 1920x1080 |
| 2 | Chrome | Mac | Spanish | 1366x768 |
| 3 | Chrome | Linux | French | 2560x1440 |
| 4 | Firefox | Windows | Spanish | 2560x1440 |
| 5 | Firefox | Mac | French | 1920x1080 |
| 6 | Firefox | Linux | English | 1366x768 |
| 7 | Safari | Windows | French | 1366x768 |
| 8 | Safari | Mac | English | 2560x1440 |
| 9 | Safari | Linux | Spanish | 1920x1080 |

*Note: A full pairwise table would ensure ALL pairs appear at least once*

### SauceDemo Pairwise Example

**Scenario:** Testing product filtering and sorting

**Parameters:**
- User Type: standard_user, problem_user, performance_glitch_user
- Product Category: All items (6 products shown)
- Sort Order: Name (A-Z), Name (Z-A), Price (low-high), Price (high-low)
- Cart Status: Empty, Has items

**Pairwise Test Cases:**

| Test | User | Sort | Cart Status | Expected |
|------|------|------|-------------|----------|
| 1 | standard_user | Name (A-Z) | Empty | Backpack first |
| 2 | standard_user | Price (high-low) | Has items | Jacket first |
| 3 | problem_user | Name (Z-A) | Empty | T-Shirt (Red) first |
| 4 | problem_user | Price (low-high) | Has items | Onesie first |
| 5 | performance_glitch_user | Name (A-Z) | Has items | Backpack first (slow) |
| 6 | performance_glitch_user | Price (high-low) | Empty | Jacket first (slow) |

### Steps to Create Pairwise Tests

1. **List all parameters and their values**
   ```
   Parameter 1: [Value A, Value B, Value C]
   Parameter 2: [Value 1, Value 2]
   Parameter 3: [Value X, Value Y, Value Z]
   ```

2. **Use a pairwise tool** (manual is error-prone)
   - PICT (Microsoft's free tool)
   - ACTS (NIST tool)
   - AllPairs (Python script)
   - Online generators: PairwiseOnline.com

3. **Generate pairwise combinations**
   - Tool outputs minimum test set
   - All pairs covered at least once

4. **Add critical combinations manually**
   - Tool gives minimum coverage
   - Add high-risk or mandatory combos

5. **Create executable test cases**
   - Convert each row to a test case
   - Add steps, expected results

### Pairwise Best Practices
- ✅ Use tools - manual pairwise is error-prone
- ✅ Start with 3-4 most important parameters
- ✅ Add constraints (e.g., "Safari doesn't run on Linux")
- ✅ Document why you chose these parameters
- ✅ Supplement with risk-based additional tests

---

## 2️⃣ Error Guessing

### Definition
Error Guessing is an experience-based technique where testers predict likely failures based on:
- Past experience with similar applications
- Knowledge of common developer mistakes
- Understanding of technology weaknesses
- Intuition about where bugs hide

### Key Concept
**"Bugs cluster"** - Defects tend to cluster in certain modules. Experienced testers know where to look.

### When to Use Error Guessing
✅ Exploratory testing sessions
✅ Smoke/sanity testing
✅ Time-constrained testing
✅ After formal techniques (supplement)
✅ New feature testing

### Categories of Common Errors

#### 1. Boundary Issues
- Off-by-one errors
- Buffer overflows
- Min/max values ignored
- Empty collections

**Example:** Array index from 0 but loop starts at 1

#### 2. Input Validation Issues
- Special characters not handled: `' " < > & ; --`
- Unicode characters: emoji, non-Latin scripts
- Very long inputs (thousands of characters)
- Leading/trailing spaces
- Case sensitivity issues

#### 3. Calculation Errors
- Divide by zero
- Integer overflow
- Rounding errors
- Floating point precision
- Negative numbers where unexpected

#### 4. State & Timing Issues
- Race conditions
- Session timeout
- Concurrent users
- Fast clicking (double submit)
- Back button after submit

#### 5. Integration Issues
- Network failures
- Database connection loss
- API timeouts
- Third-party service down
- Invalid responses from dependencies

#### 6. User Experience Issues
- Missing error messages
- Confusing navigation
- Inconsistent UI elements
- Accessibility problems
- Mobile responsiveness

### SauceDemo Error Guessing Examples

#### Login Issues to Guess
```
❌ Empty username + empty password
❌ Valid username + empty password
❌ Spaces before/after username
❌ Copy-paste username with hidden characters
❌ Password with special chars: secret_sauce!@#
❌ SQL injection: ' OR '1'='1
❌ XSS attempt: <script>alert('test')</script>
❌ Very long username (1000+ chars)
❌ Username in different case: STANDARD_USER
❌ Multiple failed logins (account lockout?)
```

#### Cart Issues to Guess
```
❌ Add same item 100 times
❌ Add item, remove browser cookie, refresh
❌ Add to cart from multiple tabs
❌ Remove item that doesn't exist (manipulate URL)
❌ Checkout with empty cart (bypass validation)
❌ Negative quantity in cart (inspect element hack)
❌ Cart session timeout during checkout
```

#### Checkout Issues to Guess
```
❌ First name: <script>alert('xss')</script>
❌ Zip code: 9999999999999999999
❌ Zip code: -12345
❌ Last name: O'Brien (apostrophe)
❌ Missing required fields (disable JS)
❌ Back button after order placement
❌ Submit form twice rapidly (double order?)
```

### Building Your Error Guessing Library

**Create personal checklist:**

1. **Past bugs you found** → Document patterns
2. **Production incidents** → Learn from failures
3. **Code reviews** → Common developer mistakes
4. **Security vulnerabilities** → OWASP Top 10
5. **Technology-specific issues** → Framework weaknesses

### Steps to Apply Error Guessing

1. **Study the application**
   - Understand functionality
   - Identify risky areas

2. **Brainstorm potential failures**
   - What could go wrong?
   - What do users typically break?

3. **Prioritize guesses**
   - High impact + likely = test first
   - Low impact + unlikely = skip

4. **Create targeted tests**
   - One guess per test case
   - Document reasoning

5. **Track success rate**
   - Which guesses found bugs?
   - Refine technique over time

### Error Guessing Best Practices
- ✅ Document your guesses (build institutional knowledge)
- ✅ Share findings with team (collective wisdom)
- ✅ Start with high-risk areas
- ✅ Combine with formal techniques
- ❌ Don't rely solely on error guessing
- ❌ Don't skip planned tests to chase guesses

---

## 3️⃣ Risk-Based Testing (RBT)

### Definition
Risk-Based Testing prioritizes testing efforts based on risk assessment. Test high-risk areas more thoroughly, low-risk areas less.

### Key Concept
**Risk = Likelihood of failure × Impact of failure**

Limited time? Test what matters most.

### Why Risk-Based Testing?
- Never enough time to test everything
- Some features more critical than others
- Some code more complex/fragile than others
- Some failures more costly than others

### Types of Risk

#### Product Risks (Quality Risks)
Risks that the product might not work correctly:
- Complex business logic
- New technology/framework
- Frequently changed code
- Many dependencies
- Poor code quality
- Inadequate documentation

#### Project Risks
Risks that affect delivery:
- Time constraints
- Resource shortages
- Skill gaps
- Requirement changes
- Tool failures

**Focus:** We focus on PRODUCT risks in testing

### Risk Assessment Process

#### Step 1: Identify Risks
**Techniques:**
- Brainstorming sessions
- Review requirements
- Analyze architecture
- Study past defects
- Talk to developers
- User feedback/complaints

#### Step 2: Analyze Risk Level

**Likelihood (Probability of failure)**
- **High:** Complex, new, changed recently, many dependencies
- **Medium:** Moderate complexity, stable code, some dependencies
- **Low:** Simple, well-tested, unchanged, independent

**Impact (Consequence of failure)**
- **High:** Financial loss, safety hazard, legal issues, reputation damage
- **Medium:** Workaround available, affects some users, moderate impact
- **Low:** Minor inconvenience, cosmetic issues, rare scenario

#### Step 3: Risk Matrix

|  | **High Impact** | **Medium Impact** | **Low Impact** |
|--|-----------------|-------------------|----------------|
| **High Likelihood** | 🔴 Critical Risk (9) | 🟠 High Risk (6) | 🟡 Medium Risk (3) |
| **Medium Likelihood** | 🟠 High Risk (6) | 🟡 Medium Risk (4) | 🟢 Low Risk (2) |
| **Low Likelihood** | 🟡 Medium Risk (3) | 🟢 Low Risk (2) | 🟢 Low Risk (1) |

#### Step 4: Prioritize Testing

- **Critical Risk (9):** 🔴 Exhaustive testing, multiple techniques, review, automate
- **High Risk (6):** 🟠 Thorough testing, multiple test cases, document well
- **Medium Risk (3-4):** 🟡 Moderate testing, key scenarios covered
- **Low Risk (1-2):** 🟢 Minimal testing, smoke test only, or skip if time-constrained

### SauceDemo Risk Assessment Example

| Feature | Likelihood | Impact | Risk Level | Test Strategy |
|---------|-----------|--------|------------|---------------|
| Login authentication | High (complex) | High (no login = no access) | 🔴 Critical (9) | 25+ test cases, security testing, automation |
| Add to cart | Medium | High (core business) | 🟠 High (6) | 15 test cases, state testing |
| Product sort | Medium | Medium (UX) | 🟡 Medium (4) | 8 test cases, visual verification |
| Checkout process | High (multi-step) | High (completes order) | 🔴 Critical (9) | 30+ test cases, E2E automation |
| Product images | Low | Low (cosmetic) | 🟢 Low (1) | Visual check only |
| Footer links | Low | Low | 🟢 Low (1) | Quick smoke test |
| Remove from cart | Low (simple) | Medium | 🟡 Medium (3) | 5 test cases |

### Risk-Based Test Planning

**High Risk Areas → More testing:**
- Equivalence partitioning
- Boundary value analysis
- Decision tables
- Negative testing
- Error guessing
- Exploratory testing
- Automation

**Low Risk Areas → Less testing:**
- Smoke test
- Happy path only
- Manual spot check
- Skip if time-critical

### Steps to Apply Risk-Based Testing

1. **List all features/requirements**
2. **Assess likelihood for each**
3. **Assess impact for each**
4. **Calculate risk level (multiply)**
5. **Create risk matrix**
6. **Allocate testing effort proportionally**
7. **Document and communicate risks**
8. **Re-assess after each sprint/iteration**

### Risk-Based Testing Best Practices
- ✅ Involve stakeholders in risk assessment
- ✅ Document risk rationale
- ✅ Re-evaluate risks regularly
- ✅ Communicate untested low-risk areas
- ✅ Track if high-risk areas actually have more bugs (validate approach)
- ❌ Don't ignore all low-risk areas completely
- ❌ Don't let personal bias skew risk assessment

---

## 4️⃣ Exploratory Testing

### Definition
Exploratory Testing is simultaneous learning, test design, and test execution. Testers actively explore the application to discover unexpected behaviors.

**"Thinking while testing"**

### Key Concept
Scripted testing finds expected problems. Exploratory testing finds unexpected problems.

### Exploratory vs Scripted Testing

| Aspect | Scripted Testing | Exploratory Testing |
|--------|------------------|---------------------|
| **Test Design** | Upfront, documented | During execution |
| **Goal** | Verify requirements | Discover unknowns |
| **Approach** | Follow steps exactly | Adapt based on findings |
| **Documentation** | Detailed test cases | Session notes, bugs |
| **Best For** | Regression, compliance | New features, complex flows |
| **Skill Required** | Can be junior | Requires experience |

### When to Use Exploratory Testing
✅ New feature evaluation
✅ After major code changes
✅ When requirements are unclear
✅ To supplement scripted tests
✅ Under time pressure
✅ Usability evaluation

### Session-Based Test Management (SBTM)

**Structure:** Time-boxed sessions with clear objectives

#### Charter Template
```
**Explore:** [Area of application]
**With:** [Resources, tools, data]
**To discover:** [Type of information sought]
**Duration:** [Time-box, typically 60-90 min]
```

#### Example Charter: SauceDemo
```
**Explore:** Shopping cart functionality
**With:** standard_user, various products, browser dev tools
**To discover:** State management issues, edge cases, data validation bugs
**Duration:** 90 minutes
```

### Exploratory Testing Techniques

#### 1. Tours (Technique)
Explore the application like different types of users

**Tourist Tours:**
- **Guidebook Tour:** Follow happy path like first-time user
- **Money Tour:** Test most important features
- **Landmark Tour:** Visit all major features once
- **Intellectual Tour:** Test complex/interesting features
- **FedEx Tour:** Follow data through the system
- **Garbage Collector's Tour:** Test error handling, invalid inputs

#### 2. Attack Patterns
Focus on specific vulnerability types

- **User Interface Attack:** Visual bugs, alignment, mobile
- **Input Attack:** Special chars, long strings, injection
- **Data Attack:** Corrupt data, missing data, invalid formats
- **Computation Attack:** Math errors, overflow, rounding
- **State Attack:** Session, cache, concurrency issues

#### 3. Soap Opera Testing
Create dramatic scenarios users might encounter

**Examples:**
- User adds item, closes browser without logout, opens on mobile
- User starts checkout, phone dies, resumes on different device
- User's session expires during payment
- Two users share account, add items simultaneously

### SauceDemo Exploratory Session Example

**Charter:**
```
Explore: User journey from browse → cart → checkout
With: standard_user, all 6 products, Chrome DevTools
To discover: Workflow interruptions, state issues, data loss
Duration: 90 minutes
```

**Session Notes (Real-time):**

**00:00-00:15 - Setup & Reconnaissance**
- ✅ Logged in successfully
- ✅ Inventory page loads, 6 products visible
- 🤔 Noticed: Products sorted by default but no indicator which sort
- 🐛 **Potential Bug:** Sort dropdown says "Name (A to Z)" but products seem unsorted on load

**00:15-00:30 - Add to Cart Testing**
- ✅ Added Backpack to cart, badge shows "1"
- ✅ Badge updates correctly
- 🤔 Trying: Add multiple items
- ✅ Added Bike Light, badge shows "2"
- 🤔 **Question:** What's maximum cart size? Testing...
- ✅ All 6 items added successfully
- ❌ **Bug Found:** Badge shows "6" but overlaps with cart icon on mobile view (iPhone 12 Pro simulation)

**00:30-00:45 - Cart Page Testing**
- ✅ All 6 items display correctly
- ✅ Quantity shows "1" for each
- 🤔 Trying: Can I change quantity directly?
- ❌ **Bug:** No way to change quantity! Only remove.
- 🤔 Trying: Remove item
- ✅ Item removed, cart updates
- ⚠️ **UX Issue:** No "Are you sure?" confirmation when removing

**00:45-01:00 - Checkout Flow**
- ✅ Clicked "Checkout" button
- ✅ Form with First Name, Last Name, Zip Code
- 🤔 Trying: Submit empty form
- ✅ Error message displays
- 🤔 Trying: Fill only First Name
- ✅ Error: "Error: Last Name is required"
- ✅ Good validation, tested all combinations
- 🤔 Trying: XSS in first name `<script>alert(1)</script>`
- ✅ Appears sanitized (displays as text)
- ✅ Form submitted successfully

**01:00-01:15 - Review Page**
- ✅ Overview page shows items, payment info, shipping info
- ⚠️ **Observation:** Shipping info hardcoded (not from form)
- 🤔 Trying: Browser back button
- ⚠️ **Bug:** Can go back to form, change data, but changes don't reflect on review page
- 🐛 **Critical Bug:** Back button breaks checkout flow!

**01:15-01:30 - Completion & Wrap-up**
- ✅ Clicked "Finish"
- ✅ Success page displays
- ✅ Cart clears
- 🤔 Trying: Browser back button after completion
- ⚠️ **Bug:** Can click "Finish" again (idempotency issue?)

**Summary:**
- **Bugs Found:** 3
- **Usability Issues:** 2
- **Questions Raised:** 2
- **Test Ideas Generated:** 5

### Exploratory Testing Session Structure

**Before Session (10 min):**
- Review charter
- Gather tools, data, credentials
- Clear mind, remove distractions

**During Session (60-90 min):**
- Focus exclusively on testing
- Take notes in real-time
- Follow your curiosity
- Document bugs immediately
- Track time

**After Session (15 min):**
- Summarize findings
- File bug reports
- Document test ideas for future
- Rate session effectiveness

### Note-Taking Template

```
## Session Charter
[Charter details]

## Time: [Start - End]

## Timeline
00:00 - [Activity/Observation]
00:15 - [Finding/Bug]
00:30 - [Question/Idea]
...

## Bugs Found
1. [Bug description - severity]
2. [Bug description - severity]

## Test Ideas Generated
1. [Idea for future testing]
2. [Idea for future testing]

## Areas Not Covered
- [Area 1]
- [Area 2]

## Questions / Blockers
- [Question 1]
- [Blocker 1]
```

### Exploratory Testing Best Practices
- ✅ Use session charters (structure)
- ✅ Time-box sessions (60-90 min)
- ✅ Take real-time notes
- ✅ Pair with another tester (pair testing)
- ✅ Use heuristics and mnemonics (SFDIPOT, FEW HICCUPS)
- ✅ Vary personas (attacker, user, admin)
- ❌ Don't wander aimlessly - have focus
- ❌ Don't skip documentation
- ❌ Don't try to test everything in one session

---

## 5️⃣ Test Coverage Analysis

### Definition
Test Coverage measures how much of the application has been exercised by tests. It helps identify untested areas and assess testing thoroughness.

### Key Concept
**"You can't improve what you don't measure"**

Coverage shows what you've tested, NOT quality.

### Types of Coverage

#### 1. Requirements Coverage
**What:** Percentage of requirements that have test cases

**Formula:**
```
Requirements Coverage = (Requirements with tests / Total requirements) × 100%
```

**Example: SauceDemo**
```
Total Requirements: 25
Requirements with tests: 20
Coverage: 20/25 = 80%

❌ Not covered:
- Password reset
- Remember me functionality
- User profile management
- Order history
- Admin features
```

#### 2. Test Case Coverage
**What:** Percentage of test cases executed

**Formula:**
```
Test Case Coverage = (Executed test cases / Total test cases) × 100%
```

**Example:**
```
Total test cases: 150
Executed: 120
Skipped: 20 (blocked by defects)
Not run: 10 (out of scope)
Coverage: 120/150 = 80%
```

#### 3. Code Coverage (White-box)
**What:** Percentage of code executed by tests

**Types:**
- **Statement Coverage:** % of code lines executed
- **Branch Coverage:** % of decision points (if/else) executed
- **Path Coverage:** % of unique paths through code
- **Function Coverage:** % of functions called

**Note:** Usually measured by developers, but QA should understand

#### 4. Feature Coverage
**What:** Percentage of features tested

**Example: SauceDemo Features**
```
✅ Login (100%)
✅ Browse products (80%)
✅ Sort/filter (60%)
✅ Add to cart (90%)
⚠️ Remove from cart (40%)
✅ Checkout (85%)
❌ Social media links (0%)
```

#### 5. Scenario Coverage
**What:** Real user workflows tested

**Example:**
```
✅ Browse → Add to cart → Checkout → Complete order
✅ Browse → Add multiple → Remove one → Checkout
❌ Browse → Add to cart → Logout → Login → Complete order
❌ Browse → Add to cart → Cart expires → Re-add
```

### Coverage Metrics

#### Minimum Coverage Targets
- **Requirements Coverage:** 95-100% (critical requirements)
- **Critical Features:** 90-100%
- **Medium Priority:** 70-80%
- **Low Priority:** 40-60%
- **Code Coverage (Unit tests):** 80% (developer goal)

### SauceDemo Coverage Analysis Example

#### Requirements Traceability Matrix (RTM)

| Req ID | Requirement | Test Cases | Status | Coverage |
|--------|-------------|-----------|--------|----------|
| REQ-001 | User can login with valid credentials | TC-001, TC-002 | ✅ Pass | 100% |
| REQ-002 | User cannot login with invalid credentials | TC-003, TC-004, TC-005 | ✅ Pass | 100% |
| REQ-003 | User can view all products | TC-010 | ✅ Pass | 100% |
| REQ-004 | User can sort products | TC-011, TC-012, TC-013, TC-014 | ⚠️ Partial | 75% |
| REQ-005 | User can add items to cart | TC-020, TC-021 | ✅ Pass | 100% |
| REQ-006 | User can remove items from cart | TC-025 | ⚠️ Fail | 60% |
| REQ-007 | User can checkout | TC-030, TC-031, TC-032 | ✅ Pass | 85% |
| REQ-008 | Locked user cannot login | TC-006 | ✅ Pass | 100% |

**Overall Requirements Coverage: 89%**

#### Feature Coverage Report

```
🟢 Login Module: 95% coverage
   ✅ Valid login: 100%
   ✅ Invalid login: 100%
   ✅ Locked user: 100%
   ⚠️ Session management: 70%

🟡 Inventory Module: 75% coverage
   ✅ Product display: 100%
   ⚠️ Sorting: 75% (missing negative tests)
   ⚠️ Filtering: 0% (not implemented?)

🟢 Cart Module: 85% coverage
   ✅ Add to cart: 100%
   ⚠️ Remove from cart: 70%
   ✅ Cart persistence: 80%

🟢 Checkout Module: 88% coverage
   ✅ Form validation: 100%
   ✅ Order review: 90%
   ⚠️ Payment processing: 0% (simulated)
   ✅ Order completion: 100%
```

### Coverage Gaps Analysis

**How to find gaps:**

1. **List all features/requirements**
2. **Map test cases to each**
3. **Identify unmapped areas**
4. **Assess gap risk (use risk matrix)**
5. **Prioritize gap closure**

**Example Gaps Found:**

| Gap | Risk Level | Action |
|-----|-----------|--------|
| No logout testing | 🟡 Medium | Create 3 test cases |
| Social links not tested | 🟢 Low | Add to smoke test |
| Back button behavior | 🔴 High | Create 5 test cases immediately |
| Mobile responsiveness | 🟠 High | Add mobile test suite |
| Performance under load | 🟡 Medium | Plan performance testing |

### Improving Coverage

**Strategies:**

1. **Add tests for gaps**
   - Start with high-risk gaps
   - Use pairwise for combination coverage

2. **Refine existing tests**
   - Add negative scenarios
   - Add boundary values
   - Add error guessing tests

3. **Add exploratory sessions**
   - Target low-coverage areas
   - Charter-based exploration

4. **Automate regression**
   - Frees time for new coverage
   - Ensures coverage doesn't decay

5. **Track over time**
   - Sprint 1: 60% coverage
   - Sprint 2: 75% coverage
   - Sprint 3: 85% coverage

### Coverage Tools

**Requirements Management:**
- Jira + Xray (traceability)
- TestRail (RTM)
- qTest
- Zephyr

**Test Management:**
- TestRail
- Xray
- Azure Test Plans
- Zephyr Scale

**Code Coverage (for reference):**
- JaCoCo (Java)
- Istanbul/NYC (JavaScript)
- Coverage.py (Python)
- OpenCover (C#)

### Coverage Reporting Template

```markdown
## Test Coverage Report
**Project:** SauceDemo Testing
**Sprint:** Sprint 5
**Report Date:** 2024-01-15

### Executive Summary
- Requirements Coverage: 89%
- Test Case Execution: 85%
- Critical Features: 95%
- Overall Status: 🟢 On Track

### Coverage by Module
| Module | Coverage | Status | Gaps |
|--------|---------|--------|------|
| Login | 95% | 🟢 | Session timeout |
| Cart | 85% | 🟢 | Quantity update |
| Checkout | 88% | 🟡 | Back button flow |

### High-Priority Gaps
1. 🔴 Back button during checkout (Critical)
2. 🟠 Mobile responsive testing (High)
3. 🟡 Performance testing (Medium)

### Recommendations
1. Create 8 test cases for identified gaps
2. Add 2 exploratory sessions for checkout
3. Implement mobile test automation
```

### Coverage Best Practices
- ✅ Track coverage per sprint/release
- ✅ Set minimum coverage targets
- ✅ Focus on risk, not just numbers
- ✅ Communicate gaps to stakeholders
- ✅ Use coverage to guide test planning
- ❌ Don't chase 100% coverage blindly
- ❌ Don't confuse coverage with quality
- ❌ Don't ignore high-risk low-coverage areas

### Coverage Heuristics

**FEW HICCUPS** (James Bach)
- **Familiarity:** Have we tested this before?
- **Explainability:** Can we explain what this does?
- **World:** Real-world scenarios covered?
- **History:** Known problem areas tested?
- **Image:** Does it look right?
- **Comparable:** Consistency with similar features?
- **Claims:** Advertised functionality working?
- **User:** Actual user workflows?
- **Product:** Business goals met?
- **Structure:** Architectural elements tested?

---

## 🎯 Combining Advanced Techniques

### Layered Testing Strategy

**Layer 1: Risk-Based Foundation**
- Identify high-risk areas
- Allocate testing effort

**Layer 2: Formal Techniques**
- Pairwise for combinations
- EP/BVA for inputs
- Decision tables for logic

**Layer 3: Experience-Based**
- Error guessing for edge cases
- Exploratory for unknowns

**Layer 4: Measurement**
- Coverage analysis to find gaps
- Iterate and improve

### SauceDemo Complete Strategy Example

**1. Risk Assessment (Week 6, Day 1)**
```
🔴 Critical: Login, Checkout
🟠 High: Cart operations
🟡 Medium: Sorting, filtering
🟢 Low: Product images, social links
```

**2. Pairwise for Configurations (Week 6, Day 2)**
```
Users × Sort orders × Cart states = 12 pairwise tests
```

**3. Error Guessing Additions (Week 6, Day 3)**
```
Add 15 error guessing tests for login, cart, checkout
```

**4. Exploratory Sessions (Week 6, Day 4)**
```
2 × 90-min sessions: Cart workflow, Checkout workflow
```

**5. Coverage Analysis (Week 6, Day 5)**
```
Measure coverage, identify gaps
Current: 75% → Target: 90%
Add 10 tests for gaps
```

**Result:**
- Total test cases: ~70
- Coverage: 90%
- Execution time: ~6 hours
- High confidence in quality

---

## 📝 Summary

### Key Takeaways

1. **Pairwise Testing** - Test smarter, not harder
   - 70-90% coverage with 90% fewer tests
   - Use tools (PICT, ACTS)
   - Perfect for configurations

2. **Error Guessing** - Leverage experience
   - Bugs cluster in predictable patterns
   - Document your guesses
   - Supplement formal techniques

3. **Risk-Based Testing** - Prioritize by impact
   - Risk = Likelihood × Impact
   - Test high-risk areas thoroughly
   - Communicate what's untested

4. **Exploratory Testing** - Discover the unexpected
   - Time-boxed sessions with charters
   - Combine learning and testing
   - Document findings immediately

5. **Coverage Analysis** - Measure to improve
   - Track requirements, features, scenarios
   - Identify gaps systematically
   - Coverage ≠ Quality

### When to Use Each Technique

| Scenario | Recommended Technique |
|----------|----------------------|
| Many configuration combinations | Pairwise Testing |
| Testing new/changed features | Exploratory + Error Guessing |
| Limited time/resources | Risk-Based Testing |
| Unclear requirements | Exploratory Testing |
| Evaluating test completeness | Coverage Analysis |
| Complex user workflows | Exploratory (Tours) |
| Security testing | Error Guessing (Attack Patterns) |

### This Week's Focus

Apply all 5 techniques to SauceDemo:
1. Create pairwise test suite
2. Document 20 error guesses
3. Perform risk assessment
4. Execute 2 exploratory sessions
5. Measure and report coverage

**Next week:** We'll use these techniques to create a comprehensive test plan!

---

## 🤔 Self-Assessment Questions

1. How does pairwise testing achieve 70-90% coverage with so few tests?
2. What's the difference between error guessing and exploratory testing?
3. How do you calculate risk in risk-based testing?
4. Why is a charter important for exploratory testing?
5. Does 100% requirements coverage guarantee a bug-free application?
6. Name 3 "tours" you could use for exploratory testing
7. What are the top 3 risk factors in SauceDemo?
8. How would you create a pairwise test for browser × OS × resolution?
9. What coverage metric is most valuable for regression testing?
10. How do all 5 techniques complement each other?

### Answers to Check
1. Most bugs caused by 1-2 parameter interactions, not many
2. Error guessing = predict failures; Exploratory = discover unknowns during testing
3. Risk = Likelihood of failure × Impact of failure
4. Charter provides focus, scope, and time-box for the session
5. No - coverage shows what's tested, not quality; bugs could still exist in tested areas
6. Guidebook, Money, Landmark, Intellectual, FedEx, Garbage Collector (any 3)
7. Login (high complexity + high impact), Checkout (multi-step + high impact), Cart state (medium complexity + high impact)
8. List parameters → Use pairwise tool (PICT) → Generate minimum combination set → Create test cases from output
9. Requirements coverage (ensures regression tests cover all critical features)
10. Risk-based prioritizes → Pairwise optimizes → Error guessing finds edge cases → Exploratory discovers unknowns → Coverage validates completeness

---

## 🤖 Looking Ahead: Manual vs Automated Testing

### What You've Been Doing (Weeks 1-6):
**Manual testing** - You design test cases, then execute them by hand:
- Click through the UI
- Verify results visually
- Document findings

This is essential for:
- ✅ Exploratory testing (finding unexpected issues)
- ✅ Usability assessment (is this intuitive?)
- ✅ Ad-hoc verification (quick smoke tests)
- ✅ New feature validation (first-time testing)

---

### What's Coming (Weeks 10-11):
**Test automation** - You write code (Python/Selenium) to execute tests:
- Script clicks and inputs
- Assert expected results programmatically
- Run repeatedly without human intervention

This is essential for:
- ✅ Regression testing (run same tests on every build)
- ✅ Smoke tests (validate core functionality automatically)
- ✅ Data-driven tests (same test, 100 different inputs)
- ✅ CI/CD pipelines (tests run on every commit)

---

### The Decision Framework: When to Automate?

**✅ Automate when:**
- Test runs **frequently** (regression suite, smoke tests)
- Test is **repetitive** (login 100 times with different users)
- Test requires **precise data** (boundary values: 0, 1, 999, 1000)
- Test is **stable** (feature won't change for months)
- **ROI is positive** (time to automate < time saved from manual runs)

**❌ Stay manual when:**
- Test requires **human judgment** (usability, visual design)
- Test **changes frequently** (new feature under development)
- Test is **exploratory** (finding unknowns)
- Test is **one-time** (ad-hoc verification)
- **Automation cost > benefit** (takes 8 hours to automate a 5-minute test)

---

### Automation Pyramid (Industry Standard)

```
           /\
          /  \        Few UI Tests (Slow, Brittle)
         /____\
        /      \
       / API    \     More API Tests (Faster, Stable)
      / Tests    \
     /____________\
    /              \
   /  Unit Tests    \ Most Unit Tests (Fast, Reliable)
  /__________________\
```

**Your focus in weeks 1-6:** Understanding what to test (test design).
**Your focus in weeks 10-11:** How to automate what you designed (test implementation).

---

### Real-World Example: SauceDemo Test Suite

From your Week 5-6 work, here's how tests would split:

| Test Type | Manual or Automated? | Why |
|-----------|---------------------|-----|
| TC-LOGIN-001: Valid login | **Automate** | Runs on every build (smoke test) |
| TC-LOGIN-010: SQL injection | **Automate** | Security test, run in CI/CD |
| TC-PRODUCTS-002: Images displayed | **Manual** | Visual check, human judgment needed |
| TC-CART-001: Add to cart | **Automate** | Core functionality, repeatable |
| TC-CART-009: Cart calculation | **Automate** | Math validation, data-driven test |
| Exploratory session | **Manual** | By definition exploratory |
| TC-CHECKOUT-020: E2E flow | **Automate** | Regression test, smoke test |

**Typical split:** 70% automated (regression/smoke), 30% manual (exploratory/usability)

---

### Tools You'll Learn (Week 10-11 Preview)

**Python** - Programming language for test scripts
**Selenium** - Automates web browsers
**pytest** - Test framework for organizing and running tests
**Faker** - Generates test data
**requests** - Tests APIs

**Example (Week 11 preview):**
```python
# Automated test case
def test_login_with_valid_credentials():
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    assert "inventory.html" in driver.current_url
    assert driver.find_element(By.CLASS_NAME, "title").text == "Products"
```

**Don't worry if this looks foreign now.** Week 10-11 will teach you step-by-step.

---

### The Bridge: From Manual Test Cases to Automated Scripts

**Week 8:** You'll create 60+ manual test cases in structured format
**Week 10-11:** You'll select 10-15 of those cases and automate them

**The test design work you're doing now (weeks 5-6) is the foundation.**

Automation doesn't replace test design - it implements it. You still need to know:
- What to test (EP, BVA, decision tables)
- How to structure tests (preconditions, steps, assertions)
- What coverage means (requirements traceability)

**Automation is just faster execution of well-designed tests.**

---

### For Now: Focus on Design

**Weeks 1-6:** Master test design (manual execution is fine)
**Weeks 7-9:** Scale up test design (60+ cases, BDD, Agile)
**Weeks 10-11:** Learn automation (implement what you designed)

**The progression makes sense:** Learn to design good tests first, automate them later.

---

**📚 Continue to: exercises.md → Complete 5 hands-on exercises using these techniques on SauceDemo**

**⏭️ Next Week:** Test Planning & Strategy - Creating comprehensive test plans using everything learned so far
