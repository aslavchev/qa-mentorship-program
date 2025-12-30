# Week 10: Defect Management - Exercises

## 📋 Exercise Overview

This week focuses on **practical defect management** for SauceDemo. You'll find real bugs, write professional bug reports, assign severity/priority, calculate metrics, and perform root cause analysis.

**Total Time:** 5 hours
**Deliverables:** 5 markdown files in `mentee-work/week-10/`

---

## Exercise 1: Find Bugs in SauceDemo (90 min)

### Objective
Discover **10+ real bugs** in SauceDemo using exploratory testing

### Why This Matters
Exploratory testing uncovers bugs that scripted test cases miss. FAANG interviews ask: "How do you find bugs beyond test cases?" This exercise builds that skill.

---

### Instructions

#### Step 1: Set Up Testing Environment (5 min)

**Prepare your workspace:**
1. Open SauceDemo: https://www.saucedemo.com
2. Open browser DevTools (F12)
   - Console tab (watch for JavaScript errors)
   - Network tab (watch for failed requests)
3. Create document: `mentee-work/week-10/find-bugs.md`
4. Prepare screen recording tool (Loom, OBS, or browser extension)

**Test Users Available:**
```
standard_user / secret_sauce
locked_out_user / secret_sauce
problem_user / secret_sauce
performance_glitch_user / secret_sauce
error_user / secret_sauce
visual_user / secret_sauce
```

---

#### Step 2: Exploratory Testing - Login Module (15 min)

**Test ideas to explore:**
- ✅ Valid login
- ❌ Invalid credentials (wrong username, wrong password, both wrong)
- 🔒 Locked out user
- 📝 SQL injection attempts: `' OR '1'='1`, `admin'--`, `'; DROP TABLE users--`
- 📝 XSS attempts: `<script>alert('XSS')</script>`, `<img src=x onerror=alert(1)>`
- 🔤 Case sensitivity (Standard_User vs standard_user)
- 🔤 Leading/trailing spaces in username/password
- 🔤 Empty fields (submit without entering anything)
- 🔤 Special characters: `test@user`, `user!name`, `pass word`
- 🖱️ Tab order (can you navigate with keyboard only?)
- 📱 Password masking (is password field type="password"?)
- 🔄 Login button state (can you click twice? Does it disable?)
- ⏱️ Response time (how long does login take?)

**Look for:**
- Console errors
- Unclear error messages
- Missing validation
- Crashes
- Unexpected behavior
- Security issues

**Document bugs as you find them** (don't wait until the end)

---

#### Step 3: Exploratory Testing - Products Module (20 min)

**Test ideas to explore:**
- 🛍️ Product display (images load? descriptions visible?)
- 🔢 Product count (should be 6 products for standard_user)
- 💰 Price display (format correct? decimals shown?)
- 🔄 Sort functionality:
  - Name (A to Z)
  - Name (Z to A)
  - Price (low to high)
  - Price (high to low)
- 🔄 Sort persistence (does selection persist after navigation?)
- 🖼️ Image quality (broken images? wrong images?)
- 🔗 Product links (clickable? go to correct detail page?)
- ➕ Add to cart buttons (all working? state change?)
- 🔴 Remove from cart buttons (when do they appear?)
- 📱 Responsive design (resize browser window - does layout break?)

**Special users to test:**
- `problem_user` - Known to have product issues
- `visual_user` - Known to have UI/UX issues

**Look for:**
- Broken images
- Wrong product data
- Sort bugs
- Layout issues
- Button state bugs

---

#### Step 4: Exploratory Testing - Cart Module (20 min)

**Test ideas to explore:**
- 🛒 Add to cart (does badge update?)
- 🛒 Add multiple items (badge count correct?)
- 🛒 Remove from cart (badge decrements?)
- 🔢 Cart badge persistence (stays after page refresh?)
- 🔢 Cart badge accuracy (matches actual cart contents?)
- 📝 Cart page display (items listed correctly?)
- 💰 Cart total calculation (sum correct?)
- ➖ Remove from cart page (button works?)
- ↩️ Continue Shopping button (returns to inventory?)
- ➡️ Checkout button (navigates to checkout?)
- 🔄 Cart state (persists across pages?)
- 🧹 Empty cart behavior (what happens when cart is empty?)

**Edge cases to test:**
- Add all 6 products
- Remove all products
- Add → Remove → Add same product
- Navigate away and back to cart

**Look for:**
- Badge count bugs
- Calculation errors
- State management issues
- Navigation bugs

---

#### Step 5: Exploratory Testing - Checkout Module (20 min)

**Test ideas to explore:**
- 📝 Form validation:
  - Empty fields (all, some, one)
  - First name (valid, invalid, special chars, numbers)
  - Last name (valid, invalid, special chars, numbers)
  - Zip code (valid, invalid, letters, too short, too long)
- 🔤 Input sanitization (XSS attempts, SQL injection)
- ❌ Error messages (clear? specific? helpful?)
- ✅ Form submission (all fields valid)
- 📋 Order summary (products listed? prices correct? total correct?)
- 💰 Tax calculation (tax added? amount correct?)
- 💰 Final total (item total + tax = total?)
- ✅ Finish button (completes order?)
- 🎉 Order confirmation (thank you page shows?)
- ↩️ Back Home button (returns to inventory?)
- 🛒 Cart state after order (cart cleared?)

**Look for:**
- Validation bugs
- Calculation errors
- State bugs (cart not cleared)
- Navigation bugs
- Security issues

---

#### Step 6: Exploratory Testing - Cross-Cutting Concerns (10 min)

**Test ideas to explore:**
- 📱 **Responsiveness:** Resize browser window (320px, 768px, 1024px, 1920px)
- 🌐 **Cross-browser:** Test on Chrome, Firefox, Safari, Edge
- 🖱️ **Accessibility:**
  - Keyboard navigation (Tab, Enter, Esc)
  - Screen reader compatibility
  - Color contrast
  - Focus indicators
- ⚡ **Performance:**
  - Page load times
  - Button response times
  - Image loading
- 🔒 **Security:**
  - Session management (can you access inventory without login?)
  - Direct URL access (go to /cart.html when logged out)
  - Browser back button behavior
- 🌍 **Localization:** Special characters in input fields (José, François, 北京)

---

#### Step 7: Document All Bugs Found (10 min)

**For each bug, capture:**
1. Bug number (BUG-001, BUG-002, etc.)
2. Brief summary (one line)
3. Module (Login, Products, Cart, Checkout)
4. How discovered (exploratory scenario)

**Template for this exercise (simplified):**

```markdown
## Bug Discovery Log

### BUG-001: [Brief Summary]
- **Module:** Login / Products / Cart / Checkout
- **Discovered via:** [What were you testing when you found it?]
- **Reproducible:** Yes / No / Sometimes
- **Affects user(s):** standard_user / all users / specific user
- **Quick notes:** [1-2 sentences on what's wrong]

### BUG-002: [Brief Summary]
...
```

**Example:**

```markdown
### BUG-001: Cart badge not updating after removal
- **Module:** Cart
- **Discovered via:** Testing cart badge accuracy after removing items
- **Reproducible:** Yes (100% of the time)
- **Affects user(s):** All users
- **Quick notes:** When removing item from cart page, badge still shows old count. Must refresh page to see correct count.
```

---

### Deliverable Format

Save as `mentee-work/week-10/find-bugs.md`

```markdown
# Week 10 - Exercise 1: Find Bugs in SauceDemo

**Your Name:** [Your name]
**Date:** [Date]
**Total Bugs Found:** [Number]

---

## Testing Summary

**Testing Duration:** [X hours]
**Modules Tested:** Login, Products, Cart, Checkout, Cross-cutting
**Users Tested:** standard_user, problem_user, visual_user, [others]
**Browsers Tested:** Chrome, [others if applicable]

---

## Bug Discovery Log

### BUG-001: [Summary]
- **Module:** [Module name]
- **Discovered via:** [Testing scenario]
- **Reproducible:** Yes / No / Sometimes
- **Affects user(s):** [Which users]
- **Quick notes:** [Description]

### BUG-002: [Summary]
...

[Continue for all bugs - minimum 10 bugs]

---

## Testing Notes

**Modules with most bugs:** [Module name]
**Most common bug type:** [Type - validation, UI, state management, etc.]
**Hardest bug to find:** [BUG-XXX - why?]
**Easiest bug to find:** [BUG-XXX - why?]

**What I learned:**
- [Reflection on exploratory testing]
- [What techniques worked best]
- [What surprised you]
```

---

### Success Criteria

- ✅ **Minimum 10 bugs found** (more is better)
- ✅ All bugs reproducible (you can recreate them)
- ✅ Bugs span multiple modules (not all from one area)
- ✅ Mix of bug types (functional, UI, validation, state management)
- ✅ At least 1 security-related bug (SQL injection, XSS attempt, session management)

---

## Exercise 2: Write Professional Bug Reports (90 min)

### Objective
Write **10+ professional bug reports** using FAANG-level bug report template

### Why This Matters
In interviews, you'll be asked: "Show me a bug report you wrote." This exercise creates portfolio-quality bug reports that demonstrate professional QA skills.

---

### Instructions

#### Step 1: Review Bug Report Template (10 min)

**Read tutorial.md Section 2: Writing Effective Bug Reports**

**Essential components checklist:**
- [ ] Bug ID
- [ ] Summary/Title
- [ ] Description (2-3 sentences)
- [ ] Steps to Reproduce (numbered, detailed)
- [ ] Expected Result
- [ ] Actual Result
- [ ] Environment (OS, browser, resolution, URL, date/time)
- [ ] Severity & Priority (assigned in Exercise 3)
- [ ] Preconditions
- [ ] Test Data
- [ ] Attachments (screenshot, video, logs)
- [ ] Additional Notes (optional)

**Study the complete bug report example in tutorial.md (DEF-045)**

---

#### Step 2: Select 10+ Bugs to Document (5 min)

**From Exercise 1, select bugs that:**
- Are reproducible (100% repro rate)
- Span multiple modules (Login, Products, Cart, Checkout)
- Include variety (functional, UI, validation, security)
- Have clear impact (not too trivial)

**Recommended selection:**
- 2-3 Login bugs
- 2-3 Products bugs
- 2-3 Cart bugs
- 2-3 Checkout bugs
- 1-2 Cross-cutting bugs

---

#### Step 3: Capture Evidence (20 min)

**For each selected bug, gather:**

1. **Screenshots:**
   - Annotate with arrows, highlights, circles
   - Show the bug clearly
   - Include full browser window (to show URL, timestamp)

2. **Screen recording (optional but recommended):**
   - Record full reproduction flow
   - 30-60 seconds per bug
   - Tools: Loom (free), OBS, Chrome screen recorder

3. **Console logs (if applicable):**
   - Open DevTools → Console
   - Right-click → Save as
   - Include in report or paste relevant errors

4. **Network logs (if applicable):**
   - DevTools → Network tab
   - Export as HAR file (for API failures)

**Save all evidence in:** `mentee-work/week-10/evidence/`
- `BUG-001-screenshot.png`
- `BUG-001-video.mp4`
- `BUG-001-console.txt`

---

#### Step 4: Write Bug Reports (50 min)

**Time allocation:** 5 minutes per bug report (10 bugs = 50 min)

**Use this template:**

```markdown
---

## BUG-XXX: [Summary]

**Bug ID:** BUG-XXX
**Reported by:** [Your name]
**Date:** [YYYY-MM-DD]
**Module:** [Login / Products / Cart / Checkout]

### Summary
[Component] Brief description of issue (one line, searchable)

**Example:** [Cart] Cart badge displays incorrect count after removing item

### Description
[2-3 sentences explaining what's wrong, who's affected, and overall impact]

**Example:**
When a user removes an item from the cart, the cart badge in the header does not update correctly. It continues to show the old count instead of decrementing by 1. This causes confusion as users think items are still in the cart.

### Steps to Reproduce

1. [Step 1 - be specific]
2. [Step 2 - include exact data]
3. [Step 3 - include exact actions]
4. [Step 4 - ...]

**Example:**
1. Login as "standard_user" / "secret_sauce"
2. Navigate to inventory page (https://www.saucedemo.com/inventory.html)
3. Click "Add to cart" for "Sauce Labs Backpack"
4. Observe cart badge shows "1"
5. Click cart icon to go to cart page
6. Click "Remove" button for "Sauce Labs Backpack"

### Actual Result

- [What actually happens - the bug]
- [Be specific, describe the broken behavior]

**Example:**
- Item is removed from cart (cart shows empty)
- Cart badge still shows "1" (incorrect)

### Expected Result

- [What should happen according to requirements]
- [Describe the correct behavior]

**Example:**
- Item is removed from cart
- Cart badge should show "0" or disappear entirely

### Environment

- **OS:** [Windows 11 / macOS Ventura / Ubuntu 22.04]
- **Browser:** [Chrome 120.0.6099.129 / Firefox 121 / Safari 17]
- **Screen Resolution:** [1920x1080 / 1366x768 / ...]
- **URL:** [https://www.saucedemo.com/cart.html]
- **Date/Time Tested:** [2024-01-15 10:30 AM PST]

### Severity & Priority

**Severity:** [Assigned in Exercise 3]
**Priority:** [Assigned in Exercise 3]
**Justification:** [Will be filled in Exercise 3]

### Preconditions

- [State required before bug occurs]

**Example:**
- User logged in as standard_user
- At least one item added to cart
- Testing from cart page (not inventory page)

### Test Data

- **User:** [standard_user / problem_user / ...]
- **Product:** [Sauce Labs Backpack / ...]
- **Input data:** [If applicable]

### Attachments

- Screenshot: `evidence/BUG-XXX-screenshot.png`
- Video: `evidence/BUG-XXX-video.mp4` (if applicable)
- Console log: `evidence/BUG-XXX-console.txt` (if applicable)

### Additional Notes

[Optional: Any extra observations, related bugs, workarounds]

**Example:**
- Bug does NOT occur when using "Remove" from inventory page (only from cart page)
- Badge updates correctly when adding items (only broken on removal)
- Observed on all tested browsers (Chrome, Firefox, Safari)

---
```

---

#### Step 5: Review and Polish (15 min)

**Self-review checklist for EACH bug report:**

- [ ] Summary is clear and searchable
- [ ] Steps to Reproduce are detailed enough for anyone to follow
- [ ] Expected vs Actual is clearly differentiated
- [ ] Environment details are complete
- [ ] Test data is specific (no placeholders like "valid user")
- [ ] Evidence is attached and referenced
- [ ] Preconditions are stated
- [ ] No typos or grammar errors
- [ ] Professional tone (no blame, no emotion)

**Common mistakes to avoid:**
- ❌ Vague summary: "Cart doesn't work"
- ❌ Missing steps: "Try to remove item"
- ❌ Vague results: "Error shown" (which error?)
- ❌ Missing environment: "On my computer"
- ❌ Emotional language: "This stupid bug..."

**FAANG standard:** A developer should be able to reproduce the bug in under 2 minutes using your report.

---

### Deliverable Format

Save as `mentee-work/week-10/write-bug-reports.md`

```markdown
# Week 10 - Exercise 2: Professional Bug Reports

**Your Name:** [Your name]
**Date:** [Date]
**Total Bug Reports:** [Number]

---

## Bug Report Index

| Bug ID | Summary | Module | Severity | Priority |
|--------|---------|--------|----------|----------|
| BUG-001 | [Summary] | [Module] | [TBD in Ex3] | [TBD in Ex3] |
| BUG-002 | [Summary] | [Module] | [TBD in Ex3] | [TBD in Ex3] |
| ... | ... | ... | ... | ... |

---

[Insert all 10+ bug reports using template above]

---

## Report Writing Reflection

**Time spent:** [X hours]
**Most challenging bug to document:** [BUG-XXX - why?]
**Most critical bug:** [BUG-XXX - why?]

**What I learned:**
- [About writing clear reproduction steps]
- [About capturing evidence]
- [About professional bug reporting]
```

---

### Success Criteria

- ✅ **Minimum 10 complete bug reports** (all fields filled)
- ✅ All reports follow template exactly
- ✅ Steps to Reproduce are detailed and reproducible
- ✅ Evidence captured (screenshots for all bugs)
- ✅ Professional tone (no blame, clear communication)
- ✅ Specific data (no placeholders like "user" or "product")

---

## Exercise 3: Assign Severity & Priority (30 min)

### Objective
Classify all 10+ bugs with **correct severity and priority** based on impact and urgency

### Why This Matters
FAANG interviews test your judgment: "Is this a P0 or P1?" Getting this wrong wastes resources (over-prioritizing trivial bugs) or ships critical bugs (under-prioritizing blockers).

---

### Instructions

#### Step 1: Review Severity Definitions (5 min)

**Read tutorial.md Section 3: Severity vs Priority**

**Severity = Technical Impact (How bad is it?)**

| Level | Impact | Example |
|-------|--------|---------|
| **S1 - Critical** | Application unusable, data loss, security breach | Login completely broken for all users |
| **S2 - High** | Major functionality broken, no workaround | Add to cart doesn't work |
| **S3 - Medium** | Feature partially broken, workaround exists | Sort by price broken (but name sort works) |
| **S4 - Low** | Cosmetic, minor inconvenience | Typo in button text |

---

#### Step 2: Review Priority Definitions (5 min)

**Priority = Business Urgency (How soon must it be fixed?)**

| Level | Urgency | Timeline | Example |
|-------|---------|----------|---------|
| **P0 - Immediate** | Production down, fix NOW | Hours | Payment processing broken during sale |
| **P1 - High** | Fix this sprint/release | Days | Core feature broken |
| **P2 - Medium** | Fix next sprint | Weeks | Minor feature issue, workaround available |
| **P3 - Low** | Fix when convenient | Whenever | Cosmetic issues, nice-to-haves |

---

#### Step 3: Classify Each Bug (15 min)

**For each bug, answer:**

1. **What's the technical impact?** (S1, S2, S3, S4)
   - Does it block core functionality?
   - How many users affected?
   - Is there a workaround?
   - Does it cause data loss/corruption?

2. **What's the business urgency?** (P0, P1, P2, P3)
   - Is production down?
   - How soon is next release?
   - What's the business impact?
   - Are there external deadlines (demos, launches)?

3. **Write justification** (2-3 sentences explaining your classification)

**Example:**

```markdown
### BUG-001: Cart badge incorrect after removal

**Severity:** S3 (Medium)
**Priority:** P2 (Medium)

**Justification:**
Severity is Medium because the cart functionality still works correctly (users can see actual cart contents on cart page), but the badge UX is confusing. This is not blocking any core workflows. Priority is Medium because it's a quality issue that should be fixed, but it's not urgent - users have a workaround (check cart page directly). Fix in next sprint.
```

---

#### Step 4: Create Severity/Priority Matrix (5 min)

**Map all bugs on matrix:**

```markdown
## Severity/Priority Matrix

| Bug ID | Summary | Severity | Priority | Quadrant |
|--------|---------|----------|----------|----------|
| BUG-XXX | [Summary] | S1 | P0 | Critical/Immediate |
| BUG-XXX | [Summary] | S2 | P1 | High/High |
| BUG-XXX | [Summary] | S3 | P2 | Medium/Medium |
| BUG-XXX | [Summary] | S4 | P3 | Low/Low |
```

**Identify interesting cases:**
- **High Severity + Low Priority:** Critical bug in rarely-used feature
- **Low Severity + High Priority:** Cosmetic bug in high-visibility area

---

### Deliverable Format

Save as `mentee-work/week-10/severity-priority.md`

```markdown
# Week 10 - Exercise 3: Severity & Priority Classification

**Your Name:** [Your name]
**Date:** [Date]
**Bugs Classified:** [Number]

---

## Classification Summary

| Severity | Count | % of Total |
|----------|-------|------------|
| S1 (Critical) | X | X% |
| S2 (High) | X | X% |
| S3 (Medium) | X | X% |
| S4 (Low) | X | X% |
| **Total** | **X** | **100%** |

| Priority | Count | % of Total |
|----------|-------|------------|
| P0 (Immediate) | X | X% |
| P1 (High) | X | X% |
| P2 (Medium) | X | X% |
| P3 (Low) | X | X% |
| **Total** | **X** | **100%** |

---

## Bug Classifications

### BUG-001: [Summary]

**Severity:** S1 / S2 / S3 / S4
**Priority:** P0 / P1 / P2 / P3

**Justification:**
[2-3 sentences explaining why you assigned this severity and priority. Consider impact, workarounds, urgency, business context.]

---

### BUG-002: [Summary]

**Severity:** [Level]
**Priority:** [Level]

**Justification:**
[Explanation]

---

[Continue for all bugs]

---

## Severity/Priority Matrix

| Bug ID | Summary | Severity | Priority | Fix Timeline |
|--------|---------|----------|----------|--------------|
| BUG-XXX | [Summary] | S1 | P0 | Immediate (hours) |
| BUG-XXX | [Summary] | S2 | P1 | This sprint (days) |
| BUG-XXX | [Summary] | S3 | P2 | Next sprint (weeks) |
| BUG-XXX | [Summary] | S4 | P3 | Backlog (whenever) |

---

## Analysis

**Most critical bug:** BUG-XXX (SX/PX) - [Why?]
**Most common severity:** [S1/S2/S3/S4] - [X bugs]
**Most common priority:** [P0/P1/P2/P3] - [X bugs]

**Interesting cases:**
- **High Severity + Low Priority:** [If any - explain why]
- **Low Severity + High Priority:** [If any - explain why]

**Fix order recommendation:**
1. [BUG-XXX] - P0/P1 bugs first
2. [BUG-XXX]
3. [BUG-XXX]
...

---

## Reflection

**What was challenging about classification?**
[Your thoughts]

**Did any bugs surprise you in their severity/priority?**
[Which ones and why?]

**How would you explain severity vs priority to a non-technical stakeholder?**
[Your explanation]
```

---

### Success Criteria

- ✅ All bugs have severity AND priority assigned
- ✅ Justifications are logical and well-reasoned
- ✅ Severity/Priority matrix completed
- ✅ Distribution analyzed (percentages calculated)
- ✅ Fix order recommended based on classifications
- ✅ At least 1-2 bugs are S1 or S2 (if you found none, revisit bug hunting)

---

## Exercise 4: Defect Metrics Dashboard (45 min)

### Objective
Calculate **defect metrics** and create a metrics dashboard

### Why This Matters
FAANG QA roles require data-driven decision making. Metrics like Defect Removal Efficiency (DRE) and Defect Leakage show testing effectiveness. This is asked in senior QA interviews.

---

### Instructions

#### Step 1: Review Metric Definitions (10 min)

**Read tutorial.md Section 5: Defect Metrics & Reporting**

**Key metrics to calculate:**
1. **Defect Density** = Total Defects / Test Cases Executed
2. **Defect Distribution** (by severity, by module, by state)
3. **Defect Removal Efficiency (DRE)** = (Defects found in testing / Total defects) × 100%
4. **Defect Leakage** = (Defects in production / Total defects) × 100%

---

#### Step 2: Gather Data (5 min)

**You'll need:**
- Total bugs found (from Exercise 1)
- Total test cases executed (from Week 8: 60 test cases)
- Bugs by severity (from Exercise 3)
- Bugs by module (Login, Products, Cart, Checkout)
- Simulated production bugs (for DRE calculation - see below)

**Note:** Since this is a learning exercise, we'll simulate production defects for DRE/Leakage calculations.

---

#### Step 3: Calculate Defect Density (5 min)

**Formula:**
```
Defect Density = Total Defects Found / Test Cases Executed
```

**Example:**
```
12 defects found / 60 test cases = 0.20 defects per test case
```

**Interpretation:**
- **< 0.10:** Low density (good quality OR insufficient testing)
- **0.10 - 0.25:** Normal density for first test cycle
- **> 0.25:** High density (quality issues OR excellent testing depth)

---

#### Step 4: Calculate Defect Distribution (10 min)

**A. By Severity:**

```markdown
| Severity | Count | Percentage | Target |
|----------|-------|------------|--------|
| S1 (Critical) | X | X% | < 10% |
| S2 (High) | X | X% | 20-30% |
| S3 (Medium) | X | X% | 40-50% |
| S4 (Low) | X | X% | 20-30% |
| **Total** | **X** | **100%** | - |
```

**B. By Module:**

```markdown
| Module | Count | Percentage |
|--------|-------|------------|
| Login | X | X% |
| Products | X | X% |
| Cart | X | X% |
| Checkout | X | X% |
| Cross-cutting | X | X% |
| **Total** | **X** | **100%** |
```

**Identify defect hotspots:** Module with highest defect count

---

#### Step 5: Simulate Defect Removal Efficiency (10 min)

**Scenario (simulated):**

Imagine SauceDemo went to production BEFORE you tested it. Of the bugs you found:
- **You found X bugs during testing** (your Exercise 1 bugs)
- **Assume 2-3 bugs escaped to production** (pick 2-3 of your lower-severity bugs that might have been missed)

**Formula:**
```
DRE = (Defects found in testing / Total defects) × 100%

Total defects = Testing defects + Production defects
```

**Example:**
```
Testing: 12 bugs found
Production: 2 bugs escaped (BUG-007, BUG-010)
Total: 14 bugs

DRE = 12 / 14 × 100% = 85.7%
```

**Target:** 90%+ (industry standard for FAANG)

**Defect Leakage:**
```
Defect Leakage = (Production defects / Total defects) × 100%

Leakage = 2 / 14 × 100% = 14.3%
```

**Target:** < 10%

**Analysis:** If leakage > 10%, testing missed too many bugs (need more coverage, better test cases, exploratory testing).

---

#### Step 6: Create Metrics Dashboard (5 min)

**Combine all metrics into one dashboard view**

---

### Deliverable Format

Save as `mentee-work/week-10/defect-metrics.md`

```markdown
# Week 10 - Exercise 4: Defect Metrics Dashboard

**Your Name:** [Your name]
**Date:** [Date]
**Reporting Period:** Week 10 Testing Cycle

---

## Executive Summary

**Total Defects Found:** [X]
**Test Cases Executed:** 60 (from Week 8)
**Defect Density:** [X.XX] defects per test case
**Defect Removal Efficiency (DRE):** [XX.X%]
**Defect Leakage:** [XX.X%]

**Quality Assessment:** [Pass / Concern / Fail]
**Key Finding:** [One sentence - biggest insight from metrics]

---

## Metric 1: Defect Density

**Formula:** Total Defects / Test Cases Executed
**Calculation:** [X] defects / 60 test cases = **[X.XX]** defects per test case

**Interpretation:**
- Industry Benchmark: 0.10 - 0.25 defects per test case (first cycle)
- Our Result: [Above/Below/Within] benchmark
- **Analysis:** [What does this tell us about SauceDemo quality or testing depth?]

---

## Metric 2: Defect Distribution by Severity

| Severity | Count | Percentage | Target Range | Status |
|----------|-------|------------|--------------|--------|
| S1 (Critical) | [X] | [X%] | < 10% | ✅/⚠️/❌ |
| S2 (High) | [X] | [X%] | 20-30% | ✅/⚠️/❌ |
| S3 (Medium) | [X] | [X%] | 40-50% | ✅/⚠️/❌ |
| S4 (Low) | [X] | [X%] | 20-30% | ✅/⚠️/❌ |
| **Total** | **[X]** | **100%** | - | - |

**Chart (Text-based):**
```
S1 Critical: ███ [X%]
S2 High:     ████████ [X%]
S3 Medium:   ████████████████ [X%]
S4 Low:      ████████ [X%]
```

**Analysis:**
[What does this distribution tell us? Is it healthy? Any concerns?]

---

## Metric 3: Defect Distribution by Module

| Module | Count | Percentage | Status |
|--------|-------|------------|--------|
| Login | [X] | [X%] | Normal/Hotspot |
| Products | [X] | [X%] | Normal/Hotspot |
| Cart | [X] | [X%] | Normal/Hotspot |
| Checkout | [X] | [X%] | Normal/Hotspot |
| Cross-cutting | [X] | [X%] | Normal/Hotspot |
| **Total** | **[X]** | **100%** | - |

**Chart (Text-based):**
```
Login:        ████ [X bugs]
Products:     ████████ [X bugs]
Cart:         ████████████ [X bugs] ⚠️ HOTSPOT
Checkout:     ████████ [X bugs]
Cross-cutting: ██ [X bugs]
```

**Defect Hotspot:** [Module name] ([X] bugs, [X%] of total)

**Analysis:**
[Why might this module have more bugs? What does this suggest about risk or test coverage?]

---

## Metric 4: Defect Removal Efficiency (DRE)

**Scenario (Simulated):**
- Bugs found during testing: [X]
- Bugs that would escape to production: [X] (assumed: [BUG-XXX, BUG-XXX])
- Total bugs: [X]

**Formula:** (Testing defects / Total defects) × 100%
**Calculation:** [X] / [X] × 100% = **[XX.X%]**

**Target:** 90%+ (FAANG standard)
**Result:** [✅ Exceeds / ⚠️ Meets / ❌ Below] target

**Analysis:**
[If < 90%: What types of bugs escaped? How can we improve test coverage?]
[If >= 90%: What testing techniques were effective?]

---

## Metric 5: Defect Leakage

**Formula:** (Production defects / Total defects) × 100%
**Calculation:** [X] / [X] × 100% = **[XX.X%]**

**Target:** < 10%
**Result:** [✅ Within / ❌ Exceeds] target

**Escaped Bugs (Simulated):**
1. [BUG-XXX]: [Summary] - Why it might escape: [Reason]
2. [BUG-XXX]: [Summary] - Why it might escape: [Reason]

**Analysis:**
[What patterns do escaped bugs have? How can we prevent this in future?]

---

## Metric 6: Defect Age (Not Applicable)

**Note:** Since this is a testing exercise (not a real project), we cannot track defect age (time from NEW to CLOSED). In a real project, we'd track:
- Average age: [X days]
- Oldest defect: [X days]
- Target: Close 80% within 14 days

---

## Key Insights

**1. Overall Quality:**
[Is SauceDemo high-quality or bug-prone? What's the evidence?]

**2. Testing Effectiveness:**
[Did our testing find most bugs? What's our DRE/Leakage telling us?]

**3. Risk Areas:**
[Which module is riskiest? Where should we focus more testing?]

**4. Recommendations:**
- [Action 1: e.g., "Add 10 more Cart test cases (defect hotspot)"]
- [Action 2: e.g., "Improve exploratory testing for checkout (2 bugs escaped)"]
- [Action 3: e.g., "Security testing needed (found SQL injection vulnerability)"]

---

## Metrics Dashboard Summary

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Defect Density | [X.XX] | 0.10-0.25 | ✅/⚠️/❌ |
| DRE | [XX%] | > 90% | ✅/⚠️/❌ |
| Defect Leakage | [XX%] | < 10% | ✅/⚠️/❌ |
| S1 Critical % | [XX%] | < 10% | ✅/⚠️/❌ |
| Defect Hotspot | [Module] | Evenly distributed | ⚠️ |

**Overall Grade:** [A/B/C/D/F] - [Justification]

---

## Reflection

**What surprised you about the metrics?**
[Your thoughts]

**Which metric is most valuable for decision-making?**
[Your answer and why]

**If you were QA Lead, what would you do based on these metrics?**
[Your recommendations]
```

---

### Success Criteria

- ✅ Defect density calculated correctly
- ✅ Defect distribution by severity analyzed (percentages add to 100%)
- ✅ Defect distribution by module analyzed (percentages add to 100%)
- ✅ DRE calculated with realistic simulation
- ✅ Defect leakage calculated
- ✅ Defect hotspot identified
- ✅ Insights and recommendations provided
- ✅ Professional dashboard format

---

## Exercise 5: Root Cause Analysis (45 min)

### Objective
Perform **Root Cause Analysis (RCA)** on 2-3 critical bugs using the "5 Whys" technique

### Why This Matters
Fixing bugs is reactive. RCA is proactive - it prevents future bugs. FAANG teams expect QA to identify patterns and suggest systemic improvements, not just log defects.

---

### Instructions

#### Step 1: Review RCA Techniques (10 min)

**Read tutorial.md Section 6: Root Cause Analysis**

**5 Whys Technique:**
Ask "Why?" 5 times to reach the root cause (not just symptoms)

**Example:**
```
Bug: Users cannot login

Why? → Login button doesn't respond
Why? → JavaScript error in console
Why? → Undefined variable in auth.js
Why? → Developer forgot to declare variable
Why? → No code review process

Root Cause: Missing code review process
```

---

#### Step 2: Select 2-3 Bugs for RCA (5 min)

**Choose bugs that are:**
- Critical or High severity (S1, S2)
- Representative of larger patterns
- Not one-off edge cases

**Ideal candidates:**
- Security bugs (SQL injection, XSS)
- State management bugs (cart badge, persistence)
- Validation bugs (missing input validation)

---

#### Step 3: Perform 5 Whys Analysis (20 min)

**For each selected bug:**

1. **State the problem** (the bug symptom)
2. **Ask "Why?" 5 times** (drill down to root cause)
3. **Identify root cause category:**
   - Requirements issue (unclear, missing, conflicting)
   - Code quality issue (poor practices, no tests)
   - Testing gap (insufficient coverage, missed scenarios)
   - Environmental issue (dev vs prod differences)
   - Communication issue (misunderstood requirements)
4. **Propose corrective actions** (fix this bug)
5. **Propose preventive actions** (prevent similar bugs)

**Example:**

```markdown
### RCA: BUG-001 - Cart Badge Incorrect After Removal

**Problem Statement:**
Cart badge does not update when item removed from cart page

**5 Whys Analysis:**

1. **Why does badge not update?**
   → No event listener triggered when clicking "Remove" on cart page

2. **Why is event listener not triggered?**
   → Event listener only attached to inventory page "Remove" buttons

3. **Why wasn't event listener added to cart page buttons?**
   → Developer implemented add-to-cart but forgot remove-from-cart flow

4. **Why did developer forget this scenario?**
   → No test case specifically covering cart badge updates on removal

5. **Why was there no test case for this?**
   → Test cases focused on happy path (add items), not negative flows (remove items)

**Root Cause:** Testing gap - no test coverage for cart removal flows

**Root Cause Category:** Testing Gap

**How it escaped testing:**
- Test cases focused on add-to-cart (happy path)
- No test case for "Verify cart badge updates when removing item from cart page"
- Exploratory testing didn't include cart badge verification after removal
- Assumption that add/remove are symmetric (they're not in this implementation)

**Corrective Actions (Fix This Bug):**
1. Add event listener to cart page "Remove" buttons
2. Ensure listener updates badge count correctly
3. Add unit test for cart badge update on removal
4. Verify fix in all browsers

**Preventive Actions (Prevent Similar Bugs):**
1. Expand cart test coverage:
   - TC-CART-020: Verify badge updates when adding from inventory
   - TC-CART-021: Verify badge updates when removing from inventory
   - TC-CART-022: Verify badge updates when removing from cart page
   - TC-CART-023: Verify badge updates when adding/removing multiple items
2. Update Definition of Done: "All event listeners tested (add AND remove flows)"
3. Exploratory testing checklist: "Test negative flows, not just positive"
4. Code review checklist: "Verify symmetric operations implemented (add ⟷ remove, open ⟷ close)"

**Lessons Learned:**
- Don't assume symmetric operations work the same way
- Test negative flows (remove, cancel, undo) as thoroughly as positive flows
- Cart badge is a cross-cutting concern (affects inventory + cart pages)
- Exploratory testing should verify UI state across page navigation
```

---

#### Step 4: Identify Patterns Across Bugs (10 min)

**After completing RCA for 2-3 bugs, look for patterns:**

- Do multiple bugs share the same root cause?
- Is there a systemic issue (e.g., "No input validation anywhere")?
- What's the most common root cause category?
- What preventive actions would help the most?

**Example patterns:**
- "3 out of 5 bugs are validation issues → No validation framework in place"
- "2 bugs related to state management → Need Redux or state management library"
- "Security bugs found → No security testing in QA process"

---

### Deliverable Format

Save as `mentee-work/week-10/root-cause-analysis.md`

```markdown
# Week 10 - Exercise 5: Root Cause Analysis

**Your Name:** [Your name]
**Date:** [Date]
**Bugs Analyzed:** [Number]

---

## RCA Summary

| Bug ID | Summary | Root Cause Category | Preventive Action |
|--------|---------|---------------------|-------------------|
| BUG-XXX | [Summary] | [Category] | [Key action] |
| BUG-XXX | [Summary] | [Category] | [Key action] |
| BUG-XXX | [Summary] | [Category] | [Key action] |

---

## RCA #1: [BUG-XXX] - [Summary]

### Problem Statement
[Clear description of the bug - the symptom, not the cause]

### 5 Whys Analysis

1. **Why does [problem] occur?**
   → [Answer]

2. **Why does [previous answer]?**
   → [Answer]

3. **Why does [previous answer]?**
   → [Answer]

4. **Why does [previous answer]?**
   → [Answer]

5. **Why does [previous answer]?**
   → [Answer - this should be the root cause]

### Root Cause

**Root Cause:** [One sentence summary of the true underlying cause]

**Category:** [Requirements / Code Quality / Testing Gap / Environmental / Communication]

### How It Escaped Testing

[2-3 sentences explaining why testing didn't catch this bug]

**Factors:**
- [Factor 1: e.g., "Test cases didn't cover negative flows"]
- [Factor 2: e.g., "No exploratory testing of cart badge"]
- [Factor 3: e.g., "Assumed add/remove operations symmetric"]

### Corrective Actions (Fix This Bug)

1. [Action to fix this specific bug]
2. [Action to verify the fix]
3. [Action to test the fix thoroughly]

### Preventive Actions (Prevent Future Bugs)

1. **Testing Improvements:**
   - [New test case 1]
   - [New test case 2]
   - [Testing process change]

2. **Development Process Improvements:**
   - [Code review checklist item]
   - [Definition of Done update]
   - [Development standard]

3. **Quality Process Improvements:**
   - [Exploratory testing guideline]
   - [Test coverage requirement]
   - [QA checklist item]

### Lessons Learned

- [Lesson 1: What did we learn?]
- [Lesson 2: What assumption was wrong?]
- [Lesson 3: What will we do differently?]

---

## RCA #2: [BUG-XXX] - [Summary]

[Repeat structure above]

---

## RCA #3: [BUG-XXX] - [Summary]

[Repeat structure above]

---

## Pattern Analysis

### Common Root Causes

**Most common category:** [Category] ([X] out of [X] bugs)

**Systemic issues identified:**
1. [Issue 1: e.g., "No input validation framework"]
2. [Issue 2: e.g., "State management inconsistent across pages"]
3. [Issue 3: e.g., "Security testing not part of QA process"]

### Cross-Bug Insights

**Themes:**
- [Theme 1: e.g., "Validation bugs across all modules"]
- [Theme 2: e.g., "State management bugs in cart/checkout"]
- [Theme 3: e.g., "Missing negative flow test coverage"]

**Shared preventive actions:**
[If multiple bugs would be prevented by the same action, list it here]

Example:
- "Adding comprehensive input validation test cases would prevent BUG-003, BUG-007, BUG-009"

---

## Recommendations to Development Team

Based on RCA findings, I recommend:

### Immediate Actions (This Sprint)
1. [High-priority fix or process change]
2. [High-priority fix or process change]

### Short-term Actions (Next 2 Sprints)
1. [Process improvement]
2. [Testing enhancement]
3. [Code quality initiative]

### Long-term Actions (Next Quarter)
1. [Systemic change]
2. [Framework/tooling adoption]
3. [Team training]

---

## Reflection

**What was most surprising about this RCA?**
[Your thoughts]

**Which root cause category is most common in SauceDemo?**
[Your answer and why you think that is]

**How does RCA differ from just fixing bugs?**
[Your explanation - why is RCA valuable?]

**What preventive action would have the biggest impact?**
[Your choice and justification]
```

---

### Success Criteria

- ✅ 2-3 critical bugs analyzed using 5 Whys
- ✅ All 5 Whys answered (not stopping at 2-3)
- ✅ Root cause identified (not just symptoms)
- ✅ Root cause categorized correctly
- ✅ Corrective actions are specific and actionable
- ✅ Preventive actions address systemic issues
- ✅ Patterns identified across multiple bugs
- ✅ Recommendations prioritized (immediate, short-term, long-term)

---

## 📂 Week 10 Submission Checklist

Before submitting, ensure you have:

### Deliverables
- [ ] `mentee-work/week-10/find-bugs.md` (10+ bugs documented)
- [ ] `mentee-work/week-10/write-bug-reports.md` (10+ professional reports)
- [ ] `mentee-work/week-10/severity-priority.md` (All bugs classified)
- [ ] `mentee-work/week-10/defect-metrics.md` (Metrics dashboard completed)
- [ ] `mentee-work/week-10/root-cause-analysis.md` (2-3 RCAs completed)
- [ ] `mentee-work/week-10/evidence/` folder (screenshots, videos for all bugs)

### Quality Gates
- [ ] All bug reports follow template exactly
- [ ] Steps to Reproduce are detailed and reproducible
- [ ] Severity/Priority justified for all bugs
- [ ] Metrics calculated correctly (percentages add to 100%)
- [ ] RCA uses 5 Whys technique properly
- [ ] Professional tone throughout (no blame, clear communication)

### Portfolio Quality
- [ ] At least 3 bug reports are "portfolio-worthy" (could show in interview)
- [ ] Metrics dashboard is professional and data-driven
- [ ] RCA demonstrates critical thinking and systemic analysis

---

## 🎯 Learning Outcomes

By completing these exercises, you should be able to:

- ✅ Find bugs using exploratory testing techniques
- ✅ Write professional, reproducible bug reports
- ✅ Differentiate between severity and priority
- ✅ Justify severity/priority classifications
- ✅ Calculate and interpret defect metrics (density, DRE, leakage)
- ✅ Identify defect hotspots and patterns
- ✅ Perform root cause analysis using 5 Whys
- ✅ Propose corrective and preventive actions
- ✅ Communicate findings professionally to stakeholders

---

## 💡 Tips for Success

**Exercise 1 (Find Bugs):**
- Test edge cases, not just happy paths
- Try different users (problem_user, visual_user)
- Watch browser console for errors
- Test negative flows (remove, cancel, invalid input)

**Exercise 2 (Bug Reports):**
- Write reports immediately after finding bug (don't batch)
- Take screenshots WHILE reproducing, not after
- Test reproduction steps yourself before submitting
- Use specific data (not "valid user" but "standard_user")

**Exercise 3 (Severity/Priority):**
- Severity = Impact (technical), Priority = Urgency (business)
- They're independent - S4 can be P1, S1 can be P3
- Justify your choices - "because it's critical" isn't enough
- Consider workarounds when assigning severity

**Exercise 4 (Metrics):**
- Double-check your math (percentages must add to 100%)
- Compare to industry benchmarks (DRE > 90%, Leakage < 10%)
- Identify actionable insights, not just numbers
- Be honest - if metrics are bad, explain why and what to do

**Exercise 5 (RCA):**
- Don't stop at first "why" - keep drilling down
- Root cause should be systemic, not "developer made mistake"
- Preventive actions > corrective actions (prevent future bugs)
- Look for patterns across multiple bugs

---

**Good luck! This is your most practical week - these skills directly translate to FAANG QA roles.**
