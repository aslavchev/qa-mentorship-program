# Week 10: Defect Management

## 🎯 Learning Objectives
- Understand defect lifecycle and states
- Write clear, actionable bug reports
- Differentiate between severity and priority
- Track and analyze defect metrics
- Perform root cause analysis
- Facilitate defect triage meetings
- Recognize defect patterns and trends

## 📚 Why Defect Management Matters

**Problem:** Poor bug reports lead to:
- Wasted time (developers can't reproduce)
- Bugs not fixed (unclear or incomplete information)
- Finger-pointing (who's responsible?)
- Missed releases (too many open defects)

**Solution:** Structured defect management ensures bugs are tracked, prioritized, and resolved efficiently.

### Benefits
- ✅ Clear communication (dev knows exactly what's wrong)
- ✅ Prioritization (fix critical bugs first)
- ✅ Accountability (who's working on what)
- ✅ Metrics (track quality trends)
- ✅ Historical data (learn from patterns)
- ✅ Release decisions (ship or delay?)

---

## 1️⃣ Defect Lifecycle

### What is a Defect Lifecycle?

**Definition:** The journey of a bug from discovery to closure

**Why it matters:** Ensures every bug is handled systematically

### Standard Defect States

```
┌─────────┐
│   NEW   │ ← Bug reported by QA
└────┬────┘
     │
     ▼
┌──────────┐
│ ASSIGNED │ ← Assigned to developer
└────┬─────┘
     │
     ▼
┌─────────┐
│   OPEN  │ ← Developer acknowledged, working on it
└────┬────┘
     │
     ├──────────┐
     │          ▼
     │     ┌──────────┐
     │     │ REJECTED │ ← Not a bug / Won't fix / Duplicate
     │     └──────────┘
     │
     ▼
┌────────┐
│ FIXED  │ ← Developer completed fix, ready for testing
└────┬───┘
     │
     ├──────────┐
     │          ▼
     │     ┌──────────┐
     │     │ REOPENED │ ← QA verified, bug still exists
     │     └────┬─────┘
     │          │
     │          └───────► (Back to ASSIGNED/OPEN)
     │
     ▼
┌──────────┐
│ VERIFIED │ ← QA confirmed fix works
└────┬─────┘
     │
     ▼
┌─────────┐
│ CLOSED  │ ← Bug resolved, release deployed
└─────────┘
```

### State Definitions

| State | Description | Who | Next State |
|-------|-------------|-----|------------|
| **NEW** | Bug just reported, not yet reviewed | QA | ASSIGNED / REJECTED |
| **ASSIGNED** | Assigned to developer, not started | Dev Lead | OPEN |
| **OPEN** | Developer working on fix | Developer | FIXED / REJECTED |
| **FIXED** | Fix implemented, ready for testing | Developer | VERIFIED / REOPENED |
| **VERIFIED** | QA confirmed fix works | QA | CLOSED |
| **REOPENED** | Bug still exists after fix attempt | QA | ASSIGNED / OPEN |
| **REJECTED** | Not a bug, duplicate, or won't fix | Dev/Lead | CLOSED |
| **CLOSED** | Bug resolved and deployed | Release Manager | - (final) |

### Rejection Reasons

- **Not a bug:** Working as designed
- **Duplicate:** Already reported (link to original)
- **Cannot reproduce:** QA needs to provide more info
- **Won't fix:** Too low priority, not worth effort
- **By design:** Intentional behavior, not a defect
- **Works for me:** Cannot reproduce on dev environment

---

## 2️⃣ Writing Effective Bug Reports

### Essential Components of a Bug Report

#### 1. Bug ID
**Example:** `DEF-1234`, `BUG-567`

#### 2. Summary/Title
**Purpose:** One-line description (searchable, scannable)

**Format:** `[Component] Brief description of issue`

**Good Examples:**
```
✅ [Login] User cannot login with valid credentials
✅ [Cart] Cart total shows incorrect price when discount applied
✅ [Checkout] Error message displays even when all fields filled
```

**Bad Examples:**
```
❌ Login doesn't work (vague)
❌ Bug in the application (too vague)
❌ User reported issue (not descriptive)
```

#### 3. Description/Summary
**Purpose:** Explain what's wrong in 2-3 sentences

**Example:**
```
When a user attempts to login with valid credentials (standard_user/secret_sauce),
the login fails and displays an error message. Expected behavior is successful
login and redirect to inventory page. This affects all valid users.
```

#### 4. Steps to Reproduce
**Purpose:** Exact steps for developer to see the bug

**Format:** Numbered list, detailed, specific

**Good Example:**
```
Steps to Reproduce:
1. Navigate to https://www.saucedemo.com
2. Enter "standard_user" in Username field
3. Enter "secret_sauce" in Password field
4. Click LOGIN button

Actual Result:
Error message "Username and password do not match" displays
User remains on login page

Expected Result:
User is logged in and redirected to /inventory.html
6 products visible on inventory page
```

**Bad Example:**
```
❌ Steps:
1. Try to login
2. It doesn't work

(Not specific enough - which user? what password? what happens?)
```

#### 5. Expected vs Actual Result
**Purpose:** Clarify the gap between what should happen and what does happen

**Format:**
```
Expected Result:
[What should happen according to requirements]

Actual Result:
[What actually happens - the bug]
```

#### 6. Environment Details
**Purpose:** Help reproduce in same conditions

**Include:**
- OS: Windows 10, macOS Ventura, Ubuntu 22.04
- Browser: Chrome 120, Firefox 121, Safari 17
- Screen Resolution: 1920×1080, 1366×768
- Device: Desktop, iPhone 13, Samsung Galaxy S21
- URL/Build: https://www.saucedemo.com, Build #234

**Example:**
```
Environment:
- OS: Windows 11
- Browser: Chrome 120.0.6099.129
- Screen Resolution: 1920x1080
- URL: https://www.saucedemo.com
- Date/Time: 2024-01-15 14:30 PST
```

#### 7. Severity & Priority
(Covered in detail in section 3)

**Severity:** How bad is the impact?
- Critical, High, Medium, Low

**Priority:** How soon must it be fixed?
- P0 (immediate), P1 (this sprint), P2 (next sprint), P3 (backlog)

#### 8. Attachments
**Include:**
- Screenshots (annotated with arrows/highlights)
- Screen recording (video of the bug)
- Console logs (browser DevTools Console)
- Network logs (HAR files)
- Test data (what inputs were used)

**Tools:**
- Screenshot: Snipping Tool, Snagit, Lightshot
- Screen recording: Loom, OBS, QuickTime
- Browser logs: Chrome DevTools → Console → Save

#### 9. Preconditions
**Purpose:** State required before bug occurs

**Example:**
```
Preconditions:
- User account exists: standard_user / secret_sauce
- User is logged out (no active session)
- Browser cookies cleared
- Test data: Cart is empty
```

#### 10. Test Data
**Purpose:** Exact data used when bug occurred

**Example:**
```
Test Data:
- Username: standard_user
- Password: secret_sauce
- Product: Sauce Labs Backpack ($29.99)
- Checkout Data: John / Doe / 12345
```

### Complete Bug Report Example

```markdown
**Bug ID:** DEF-045

**Summary:** [Cart] Cart badge displays incorrect count after removing item

**Description:**
When a user removes an item from the cart, the cart badge in the header
does not update correctly. It continues to show the old count instead of
decrementing by 1. This causes confusion as users think items are still
in the cart.

**Steps to Reproduce:**
1. Login as "standard_user" / "secret_sauce"
2. Navigate to inventory page (https://www.saucedemo.com/inventory.html)
3. Click "Add to cart" for "Sauce Labs Backpack"
4. Observe cart badge shows "1"
5. Click cart icon to go to cart page
6. Click "Remove" button for "Sauce Labs Backpack"

**Actual Result:**
- Item is removed from cart (cart shows empty)
- Cart badge still shows "1" (incorrect)

**Expected Result:**
- Item is removed from cart
- Cart badge should show "0" or disappear entirely

**Environment:**
- OS: Windows 11
- Browser: Chrome 120.0.6099.129
- Screen Resolution: 1920x1080
- URL: https://www.saucedemo.com
- Tested: 2024-01-15 10:30 AM PST

**Severity:** Medium (functionality works, but confusing UX)
**Priority:** P2 (fix in next sprint)

**Preconditions:**
- User logged in
- At least one item added to cart

**Test Data:**
- User: standard_user
- Product: Sauce Labs Backpack

**Attachments:**
- Screenshot: cart-badge-bug.png (shows badge still at "1" after removal)
- Video: cart-badge-bug.mp4 (reproduces the issue)

**Additional Notes:**
- Bug does NOT occur when using "Remove" from inventory page (only from cart page)
- Badge updates correctly when adding items (only broken on removal)
- Observed on all tested browsers (Chrome, Firefox, Safari)

**Related Issues:**
- Possibly related to DEF-032 (cart state management)
```

---

## 3️⃣ Severity vs Priority

### Severity: Technical Impact

**Definition:** How badly does this bug affect the application functionality?

**Levels:**

#### Severity 1 - Critical (S1)
**Impact:** Application is unusable, complete system failure, data loss/corruption

**Examples:**
```
- Application won't start/load
- Database corruption
- Security breach (passwords exposed)
- Payment processing broken (no revenue)
- Data loss (user's cart deleted permanently)
```

**SauceDemo Example:**
```
S1: All users unable to login (authentication system down)
S1: Checkout completes but doesn't record order (data loss)
S1: SQL injection vulnerability allows unauthorized access
```

#### Severity 2 - High (S2)
**Impact:** Major functionality broken, no workaround, affects many users

**Examples:**
```
- Core feature not working
- Major workflow blocked
- No reasonable workaround
```

**SauceDemo Example:**
```
S2: Users cannot add items to cart (core functionality)
S2: Checkout button doesn't work (blocks purchase workflow)
S2: Cart total calculates incorrectly (wrong charges)
```

#### Severity 3 - Medium (S3)
**Impact:** Feature partially broken, workaround exists, affects some users

**Examples:**
```
- Minor functionality issue
- Workaround available
- Affects limited scenarios
```

**SauceDemo Example:**
```
S3: Sort by price doesn't work (but sort by name does - workaround)
S3: Product images don't load (text still visible)
S3: Cart badge shows wrong count (but cart page is correct)
```

#### Severity 4 - Low (S4)
**Impact:** Cosmetic issue, minor inconvenience, trivial

**Examples:**
```
- UI alignment issues
- Typos in text
- Color inconsistencies
- Minor usability issues
```

**SauceDemo Example:**
```
S4: Button text has typo ("Logn" instead of "Login")
S4: Footer links have wrong color
S4: Product description has spelling error
S4: Logo image slightly misaligned
```

### Priority: Business Urgency

**Definition:** How soon must this bug be fixed?

**Levels:**

#### Priority 0 (P0) - Immediate
**Urgency:** Fix immediately, block release, all hands on deck

**Timeline:** Within hours

**Examples:**
```
- Production is down
- Security breach discovered
- Data corruption in progress
```

#### Priority 1 (P1) - High
**Urgency:** Fix in current sprint/release

**Timeline:** Within days

**Examples:**
```
- Blocks critical user workflows
- Affects many users
- No acceptable workaround
```

#### Priority 2 (P2) - Medium
**Urgency:** Fix in next sprint/release

**Timeline:** Within weeks

**Examples:**
```
- Minor feature issues
- Workaround available
- Affects some users
```

#### Priority 3 (P3) - Low
**Urgency:** Fix when convenient, backlog

**Timeline:** Whenever time allows

**Examples:**
```
- Cosmetic issues
- Nice-to-have improvements
- Rare scenarios
```

### Severity vs Priority Matrix

| Severity | Priority | Example |
|----------|----------|---------|
| **S1 Critical** | **P0 Immediate** | Production login completely broken - ALL users cannot access |
| **S1 Critical** | **P1 High** | Checkout broken, but only affects 10% of users (others can use workaround) |
| **S1 Critical** | **P2 Medium** | Critical bug in rarely-used admin feature |
| **S2 High** | **P0 Immediate** | Payment processing down during Black Friday sale |
| **S2 High** | **P1 High** | Add to cart doesn't work (core functionality) |
| **S2 High** | **P2 Medium** | Feature broken but affects beta users only (not production) |
| **S3 Medium** | **P1 High** | Minor bug but CEO will demo feature tomorrow |
| **S3 Medium** | **P2 Medium** | Sort feature broken, workaround available |
| **S4 Low** | **P1 High** | Typo in marketing banner for major campaign launch |
| **S4 Low** | **P3 Low** | Alignment issue in footer (cosmetic, not critical) |

**Key Insight:** Severity ≠ Priority

```
High Severity + Low Priority: Critical bug in rarely-used feature
Low Severity + High Priority: Cosmetic bug in high-visibility area (CEO demo)
```

---

## 4️⃣ Defect Triage

### What is Defect Triage?

**Definition:** Meeting where team reviews new bugs and decides: severity, priority, assignment, action

**Participants:**
- QA Lead (facilitates)
- Development Lead
- Product Owner
- Scrum Master (optional)

**Frequency:** Daily (critical bugs) or 2-3x per week

**Duration:** 30-60 minutes

### Triage Agenda

1. **Review new bugs** (state: NEW)
2. **Assign severity** (S1, S2, S3, S4)
3. **Assign priority** (P0, P1, P2, P3)
4. **Assign owner** (which developer)
5. **Set target fix date** (this sprint, next sprint)
6. **Reject if needed** (duplicate, not a bug, won't fix)

### Triage Decisions

**For each bug, decide:**
- ✅ **Accept:** Assign to developer, set priority
- ❌ **Reject:** Not a bug, duplicate, by design
- ⏸️ **Defer:** Low priority, move to backlog
- ❓ **Need Info:** QA needs to provide more details

### Example Triage Session

```
Bug DEF-045: Cart badge shows wrong count
  - Severity: S3 (Medium - functionality works, UX issue)
  - Priority: P2 (Fix next sprint)
  - Assigned to: Developer B
  - Decision: ACCEPT

Bug DEF-046: Logo misaligned by 2px
  - Severity: S4 (Low - cosmetic)
  - Priority: P3 (Backlog)
  - Assigned to: Unassigned
  - Decision: DEFER

Bug DEF-047: Cannot login
  - Questions: Which user? All browsers?
  - Decision: NEED MORE INFO from QA

Bug DEF-048: Error message when clicking logout twice
  - Analysis: User shouldn't click logout twice (edge case)
  - Decision: REJECT (by design, add validation)
```

---

## 5️⃣ Defect Metrics & Reporting

### Key Defect Metrics

#### 1. Defect Density
**Formula:**
```
Defect Density = Total Defects / Size of Application

Size = Test cases, lines of code, function points
```

**Example:**
```
25 defects found / 150 test cases executed = 0.17 defects per test case
```

**Interpretation:**
- High density → Poor code quality, more testing needed
- Low density → Good quality OR insufficient testing

#### 2. Defect Discovery Rate
**Formula:**
```
Defects found per day/week/sprint
```

**Example:**
```
Sprint 1: 15 defects
Sprint 2: 22 defects (trending up - concern)
Sprint 3: 10 defects (improving)
```

#### 3. Defect Removal Efficiency (DRE)
**Formula:**
```
DRE = (Defects found before release / Total defects) × 100%

Total defects = Defects in testing + Defects in production
```

**Example:**
```
Testing: 25 defects found
Production: 3 defects found (escaped)
DRE = 25 / (25+3) × 100% = 89%
```

**Target:** 90%+ (catch 90% of bugs before release)

#### 4. Defect Leakage
**Formula:**
```
Defect Leakage = (Defects in production / Total defects) × 100%
```

**Example:**
```
3 production bugs / 28 total bugs = 11% leakage
```

**Target:** < 10%

#### 5. Defect Age
**Measurement:** Days from "NEW" to "CLOSED"

**Example:**
```
DEF-001: 2 days (good)
DEF-002: 45 days (concerning - why so long?)
DEF-003: 120 days (very bad - forgotten?)
```

**Target:** Close 80% of defects within 14 days

#### 6. Reopened Defects
**Formula:**
```
Reopen Rate = (Defects reopened / Total defects fixed) × 100%
```

**Example:**
```
10 defects reopened / 50 defects fixed = 20% reopen rate
```

**Target:** < 10%

**High reopen rate indicates:**
- Incomplete fixes
- Poor root cause analysis
- Inadequate testing of fixes

### Defect Distribution

#### By Severity
```
S1 (Critical): 3 (10%)
S2 (High): 8 (27%)
S3 (Medium): 12 (40%)
S4 (Low): 7 (23%)
Total: 30 defects
```

#### By Module
```
Login: 5 defects
Cart: 12 defects (hotspot!)
Checkout: 8 defects
Products: 5 defects
```

**Insight:** Cart module needs attention (defect hotspot)

#### By State
```
NEW: 2
OPEN: 5
FIXED: 10
VERIFIED: 8
CLOSED: 5
REJECTED: 0
```

**Insight:** 10 defects fixed but not verified (QA backlog)

### Defect Trend Analysis

**Track over time:**

```
Week 1: 5 defects opened, 2 closed (net +3)
Week 2: 8 defects opened, 6 closed (net +2)
Week 3: 4 defects opened, 9 closed (net -5) ← improving!
```

**Burndown Chart:**
```
Sprint Start: 30 open defects
Week 1: 33 open
Week 2: 35 open (trending up - concern!)
Sprint End Goal: 0 open defects
```

---

## 6️⃣ Root Cause Analysis (RCA)

### Why RCA?

**Problem:** Fixing symptoms, not root causes → bugs keep coming back

**Solution:** Analyze why the bug happened, prevent similar bugs

### 5 Whys Technique

**Method:** Ask "Why?" 5 times to reach root cause

**Example:**

```
Bug: Users cannot login

Why? → Login button doesn't respond to clicks
Why? → JavaScript error in console
Why? → Undefined variable in auth.js
Why? → Developer forgot to declare variable
Why? → No code review process

Root Cause: Missing code review process
Action: Implement mandatory code reviews
```

### Common Root Causes

#### 1. Requirements Issues
```
- Unclear requirements
- Missing requirements
- Changing requirements
- Conflicting requirements
```

**Prevention:**
- Detailed acceptance criteria
- Requirements review sessions
- Prototypes/mockups

#### 2. Code Quality Issues
```
- Poor coding practices
- Lack of unit tests
- Code complexity
- Copy-paste errors
```

**Prevention:**
- Code reviews
- Coding standards
- Static analysis tools
- Pair programming

#### 3. Testing Gaps
```
- Insufficient test coverage
- Missed test scenarios
- Inadequate exploratory testing
```

**Prevention:**
- Risk-based testing
- Test coverage metrics
- Exploratory sessions

#### 4. Environmental Issues
```
- Different environments (dev vs prod)
- Data inconsistencies
- Configuration errors
```

**Prevention:**
- Environment parity (dev = staging = prod)
- Infrastructure as Code
- Automated deployments

#### 5. Communication Issues
```
- Misunderstood requirements
- Lack of collaboration
- Siloed teams
```

**Prevention:**
- Daily standups
- Backlog refinement
- Cross-functional teams

### RCA Report Template

```markdown
## Root Cause Analysis

**Defect ID:** DEF-045
**Summary:** Cart badge incorrect after item removal

**Impact:**
- 15 users reported confusion
- Customer support received 8 tickets
- Cart functionality still works, but UX degraded

**Timeline:**
- Jan 5: Feature deployed (cart badge implemented)
- Jan 10: First user report
- Jan 12: Bug logged
- Jan 15: RCA conducted

**Root Cause:**
Event listener for cart updates not triggered on item removal
from cart page (only triggered from inventory page)

**Why it happened:**
- Developer implemented add-to-cart listener
- Forgot to implement remove-from-cart listener
- No unit test for cart badge updates
- No exploratory testing of cart removal flow

**How it escaped testing:**
- Test cases focused on add-to-cart (happy path)
- No test case for remove-from-cart badge update
- Exploratory testing skipped cart removal

**Corrective Actions:**
1. Implement cart badge update listener for removal events
2. Add unit tests for cart badge (add + remove scenarios)
3. Add test case: "Verify cart badge updates on removal"
4. Code review checklist: "Verify all event listeners implemented"

**Preventive Actions:**
1. Expand test coverage for cart operations (10 new test cases)
2. Mandatory exploratory session for new features
3. Pair programming for complex features

**Lessons Learned:**
- Don't assume symmetric operations (add ≠ remove)
- Test negative flows, not just happy path
- Exploratory testing catches these UI issues
```

---

## 7️⃣ SauceDemo Bug Examples

### Bug 1: High Severity, High Priority

```markdown
**Bug ID:** DEF-101

**Summary:** [Checkout] Order completes but cart doesn't clear

**Description:**
After completing an order, the user is shown "THANK YOU FOR YOUR ORDER"
page, but when returning to inventory, the cart still contains the
previously ordered items. This causes duplicate orders if user checks
out again.

**Steps to Reproduce:**
1. Login as standard_user
2. Add "Sauce Labs Backpack" to cart
3. Proceed to checkout, fill in details
4. Click FINISH to complete order
5. Click "BACK HOME" button
6. Observe cart badge

**Actual Result:**
Cart still shows "1" item
Previous order items remain in cart

**Expected Result:**
Cart should be empty (badge shows 0 or hidden)
User starts fresh shopping session

**Severity:** S2 (High) - Causes duplicate orders
**Priority:** P1 (Fix immediately)

**Environment:**
- Browser: Chrome 120
- OS: Windows 11
```

### Bug 2: Medium Severity, Medium Priority

```markdown
**Bug ID:** DEF-102

**Summary:** [Products] Sort order doesn't persist after page refresh

**Description:**
When a user sorts products (e.g., Price high-to-low) and then refreshes
the page, the sort order resets to default. Users must re-select their
preferred sort each time.

**Steps to Reproduce:**
1. Login as standard_user
2. On inventory page, select "Price (high to low)" from sort dropdown
3. Observe products sorted correctly (Fleece Jacket first, $49.99)
4. Refresh page (F5 or Ctrl+R)

**Actual Result:**
Products revert to default order
Sort dropdown shows "Name (A to Z)"

**Expected Result:**
Products remain sorted by "Price (high to low)"
Sort dropdown shows "Price (high to low)"

**Severity:** S3 (Medium) - UX issue, workaround available
**Priority:** P2 (Fix next sprint)

**Environment:**
- Browser: All browsers
- OS: All OS
```

### Bug 3: Low Severity, Low Priority

```markdown
**Bug ID:** DEF-103

**Summary:** [Footer] Social media icon alignment inconsistent

**Description:**
The Twitter icon in the footer is 2px higher than the Facebook and
LinkedIn icons, creating visual misalignment.

**Steps to Reproduce:**
1. Navigate to any page on SauceDemo
2. Scroll to footer
3. Observe social media icons

**Actual Result:**
Twitter icon positioned 2px higher than others

**Expected Result:**
All social media icons aligned horizontally

**Severity:** S4 (Low) - Cosmetic only
**Priority:** P3 (Backlog)

**Attachments:**
- Screenshot: footer-alignment.png

**Environment:**
- Browser: Chrome 120
- Screen Resolution: 1920x1080
```

---

## 8️⃣ Defect Management Best Practices

### DO's ✅

1. **Write clear, reproducible bug reports**
   - Anyone should be able to reproduce
   - Include all necessary details

2. **Assign correct severity/priority**
   - Don't inflate (S4 bug isn't S1)
   - Justify your classification

3. **Include evidence**
   - Screenshots, videos, logs
   - Show, don't just tell

4. **Retest thoroughly**
   - Verify fix works
   - Check for regressions

5. **Close bugs promptly**
   - Don't leave verified bugs open for weeks
   - Update status regularly

6. **Track metrics**
   - Defect trends
   - Identify hotspots

7. **Perform RCA on critical bugs**
   - Learn from failures
   - Prevent recurrence

8. **Communicate proactively**
   - Alert team to critical bugs
   - Update stakeholders on status

### DON'Ts ❌

1. **Don't report duplicates**
   - Search first before logging
   - Reference existing bug

2. **Don't be vague**
   - "Doesn't work" → useless
   - "Login fails with valid credentials" → good

3. **Don't skip steps to reproduce**
   - Developer can't fix what they can't reproduce

4. **Don't over-report**
   - 5 similar bugs → 1 bug with 5 scenarios
   - Floods the backlog

5. **Don't assign severity based on emotion**
   - "I hate this bug" ≠ S1
   - Base on impact, not feeling

6. **Don't reopen without evidence**
   - "Still broken" without details → unhelpful
   - Provide new repro steps

7. **Don't blame**
   - "Developer didn't test" → unprofessional
   - Focus on fix, not fault

---

## 📝 Summary

### Key Takeaways

1. **Defect Lifecycle:**
   - NEW → ASSIGNED → OPEN → FIXED → VERIFIED → CLOSED
   - Can be REOPENED or REJECTED

2. **Bug Reports Must Include:**
   - Clear summary
   - Steps to reproduce
   - Expected vs Actual
   - Environment details
   - Severity & Priority
   - Screenshots/evidence

3. **Severity vs Priority:**
   - Severity = Technical impact (how bad)
   - Priority = Business urgency (how soon)
   - They're independent (S1 can be P3, S4 can be P1)

4. **Key Metrics:**
   - Defect density
   - Defect removal efficiency (target: 90%+)
   - Defect leakage (target: < 10%)
   - Defect age
   - Reopen rate (target: < 10%)

5. **Root Cause Analysis:**
   - Use "5 Whys"
   - Fix root cause, not symptoms
   - Implement preventive actions
   - Learn and improve

### This Week's Challenge

**Find 10+ real bugs in SauceDemo** (use exploratory testing)

**Write professional bug reports** for each bug found

**Classify bugs** with correct severity and priority

**Create defect metrics dashboard**

---

## 🤔 Self-Assessment Questions

1. What are the states in a defect lifecycle?
2. What's the difference between severity and priority?
3. What are the 5 essential components of a bug report?
4. Why are "steps to reproduce" important?
5. What is defect triage?
6. What is defect removal efficiency?
7. What does a defect leakage rate of 15% mean?
8. What is root cause analysis and why is it important?
9. Give an example of S1 Critical but P3 Low Priority
10. What's the target reopen rate for defects?

### Answers to Check
1. NEW, ASSIGNED, OPEN, FIXED, VERIFIED, CLOSED, REOPENED, REJECTED
2. Severity = technical impact (how bad); Priority = business urgency (how soon)
3. Summary, steps to reproduce, expected vs actual, environment, severity/priority (+ attachments, test data)
4. Developers need exact steps to reproduce the bug to fix it; without it, they can't fix
5. Meeting where team reviews new bugs, assigns severity/priority/owner, decides accept/reject/defer
6. Percentage of defects caught before release (target: 90%+); Formula: (Defects in testing / Total defects) × 100%
7. 15% of bugs escaped to production (only caught 85% during testing); Target is < 10%
8. Analyzing why bugs happen (not just fixing symptoms) to prevent similar bugs; Use "5 Whys" technique
9. Critical bug in admin feature used once per year (S1 = critical impact, P3 = not urgent)
10. < 10% (if 20%+ bugs are reopened, fixes are incomplete or testing is poor)

---

**📚 Continue to: exercises.md → Find 10+ bugs in SauceDemo and write professional bug reports**

**⏭️ Next Week:** Python for Test Data & APIs - Automate test data creation and basic API testing (light automation intro)
