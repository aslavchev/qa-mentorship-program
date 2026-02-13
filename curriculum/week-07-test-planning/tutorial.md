# Week 7: Test Planning & Strategy

---

## 🔄 Transition: From Test Design (Weeks 5-6) to Test Planning (Week 7)

### What You've Done So Far:

**Weeks 5-6: Test DESIGN**
- ✅ Learned HOW to design individual test cases systematically
- ✅ Techniques: EP, BVA, Decision Tables, Pairwise, Risk-Based
- ✅ Focus: "How do I create good test cases?"

**Think of it as:** Designing individual houses (architecture, materials, blueprints)

---

### What You'll Do This Week:

**Week 7: Test PLANNING**
- 🎯 Learn how to ORGANIZE 60+ test cases into a comprehensive test suite
- 🎯 Create test STRATEGY (what to test when, in what order)
- 🎯 Estimate resources (how long will this take? who does what?)
- 🎯 Define risk-based execution plan (test critical features first)
- 🎯 Set entry/exit criteria (when do we start? when do we stop?)

**Think of it as:** City planning (where do all these houses go? in what order? what infrastructure?)

---

### The Progression:

```
Week 5-6: "I know how to design a test case" ✅
           ↓
Week 7:   "I know how to organize 60 test cases into a plan" 🎯
           ↓
Week 8:   "I know how to execute and document 60 test cases" 📋
```

---

### Why This Matters:

**Without test planning (what you did in weeks 5-6):**
- You have 60 great test cases... in a random list
- No one knows which tests are critical vs nice-to-have
- No estimate of how long testing will take
- No clear start/stop criteria
- No way to communicate progress to stakeholders

**With test planning (what you'll learn this week):**
- 60 test cases organized by module, priority, risk
- Clear execution order (smoke → critical → edge cases)
- Resource estimates (8 hours for module A, 12 hours for module B)
- Quality gates defined (95% pass rate before release)
- Stakeholder communication ready (test summary report)

---

### Real-World Scenario:

**Scenario:** Your team is releasing SauceDemo v2.0 in 2 weeks.

**Without test planning:**
- "Uh, we have 60 test cases. I guess we'll run them all?"
- Starts with low-priority tests, runs out of time
- Critical tests (login, checkout) not tested before release
- Bug found in production 😞

**With test planning (this week's skill):**
- Test plan defines: Smoke tests (30 min) → Critical path (4 hours) → Full regression (12 hours)
- Risk-based execution: Login and checkout tested first
- Estimate: 16 hours total, need 2 QA engineers for 1 week
- Quality gate: All S0/S1 tests pass, 90% overall pass rate
- Bug found during testing, fixed before release ✅

**Test planning is the difference between "testing" and "professional QA."**

---

### This Week's Deliverables:

By end of week 7, you'll create:
1. **Test Plan** - Comprehensive document with scope, approach, resources, schedule
2. **Test Strategy** - High-level testing approach and techniques used
3. **Risk Assessment** - Identified risks with likelihood/impact and mitigation
4. **Resource Estimation** - Time and effort required per module
5. **Entry/Exit Criteria** - When testing starts and when it's "done"

**These are portfolio-ready artifacts** that demonstrate test lead capability.

---

### Let's Begin Week 7! 🚀

Now that you understand the transition from test design → test planning, let's dive into how to create professional test plans...

---

## 🎯 Learning Objectives
- Understand the difference between test strategy and test plan
- Create comprehensive test plans
- Define entry and exit criteria
- Estimate testing effort and resources
- Identify and mitigate testing risks
- Establish quality gates and success metrics

## 📚 Why Test Planning?

**Problem:** Testing without a plan leads to missed requirements, blown budgets, and poor quality.

**Solution:** A well-crafted test plan provides direction, sets expectations, and ensures comprehensive coverage.

### Benefits
- ✅ Clear scope and objectives
- ✅ Stakeholder alignment on testing approach
- ✅ Resource optimization
- ✅ Risk mitigation
- ✅ Progress tracking and reporting
- ✅ Repeatable, scalable process

---

## 🎨 Test Strategy vs Test Plan

### Test Strategy
**What:** High-level, long-term approach to testing (applies across projects)

**Scope:** Organization or product-wide

**Timeframe:** 1-3 years (updated periodically)

**Content:**
- Testing philosophy and principles
- Test levels and types to use
- Automation strategy
- Tool selection
- Defect management approach
- Roles and responsibilities
- Standards and best practices

**Example:**
```
"Our organization uses risk-based testing with 80% automation coverage
for regression tests. We follow shift-left principles and implement
testing at all levels (unit, integration, system, acceptance)."
```

### Test Plan
**What:** Detailed, project-specific plan for a release/sprint

**Scope:** Specific project or sprint

**Timeframe:** Days to months

**Content:**
- Scope (what will and won't be tested)
- Test objectives
- Test schedule
- Resources needed
- Test environment details
- Entry/exit criteria
- Deliverables
- Risk and contingencies

**Example:**
```
"For SauceDemo v2.1 release, we will execute 150 test cases over 2 weeks
with 2 testers, focusing on checkout flow changes and regression of
existing features. Testing will be 60% automated, 40% manual exploratory."
```

### Quick Comparison

| Aspect | Test Strategy | Test Plan |
|--------|--------------|-----------|
| **Level** | Strategic | Tactical |
| **Scope** | Organization/Product | Project/Release |
| **Duration** | Long-term | Short-term |
| **Detail** | High-level | Detailed |
| **Owner** | QA Manager/Director | QA Lead/Test Manager |
| **Updates** | Annually | Per release/sprint |
| **Audience** | Executives, Leadership | Project team |

---

## 1️⃣ Test Strategy Components

### 1.1 Testing Philosophy

**Define your approach:**
- **Shift-Left:** Test early in SDLC
- **Risk-Based:** Prioritize by risk
- **Continuous Testing:** Test throughout development
- **Exploratory + Scripted:** Balance structure and discovery

**Example Strategy Statement:**
```
We practice shift-left testing with continuous integration. Our approach
is risk-based, focusing 70% effort on high-risk features. We maintain
80% automated regression coverage and supplement with exploratory testing
for new features.
```

### 1.2 Test Levels

**Define which levels you'll test:**
- ✅ Unit Testing (Developer-owned, 95%+ coverage target)
- ✅ Integration Testing (Dev + QA, API and module integration)
- ✅ System Testing (QA-owned, end-to-end scenarios)
- ✅ Acceptance Testing (Product Owner + QA, business validation)

### 1.3 Test Types

**Functional:**
- Smoke testing (daily builds)
- Sanity testing (post-deployment)
- Regression testing (every release)
- End-to-end testing (critical workflows)

**Non-Functional:**
- Performance (load, stress)
- Security (OWASP Top 10)
- Usability (heuristic evaluation)
- Accessibility (WCAG 2.1 Level AA)
- Compatibility (browsers, devices)

### 1.4 Automation Strategy

**What to automate:**
- ✅ Regression tests (high value, stable)
- ✅ Smoke tests (run frequently)
- ✅ Data-driven tests (many combinations)
- ❌ Exploratory tests (require human judgment)
- ❌ One-time tests (not worth automation cost)
- ❌ Unstable features (constantly changing)

**Automation Targets:**
```
Year 1: 50% regression automated
Year 2: 75% regression automated
Year 3: 80% regression automated + API suite
```

### 1.5 Tool Stack

**Test Management:** TestRail, Xray, Zephyr
**Automation:** Selenium, Cypress, Playwright
**API Testing:** Postman, REST Assured
**Performance:** JMeter, K6
**CI/CD:** Jenkins, GitHub Actions
**Defect Tracking:** Jira, Azure DevOps

---

## 2️⃣ Test Plan Components

A comprehensive test plan answers: **What? Why? How? Who? When?**

### 2.1 Test Plan Identifier
**Example:** `TP-SauceDemo-v2.1-Sprint5`

### 2.2 Introduction

**Purpose of the test plan**
```
This test plan defines the scope, approach, resources, and schedule
for testing the SauceDemo v2.1 release, specifically the enhanced
checkout flow and cart persistence improvements.
```

**References**
- Requirements Document: PRD-SauceDemo-v2.1
- Test Strategy: TS-SauceDemo-2024
- Architecture Document: ARCH-SauceDemo

### 2.3 Test Items (Scope)

**Features IN SCOPE:**
✅ Login and authentication
✅ Product browsing and sorting
✅ Shopping cart operations
✅ Checkout flow (ENHANCED)
✅ Order completion
✅ Cart persistence (NEW FEATURE)

**Features OUT OF SCOPE:**
❌ Payment processing (simulated, not real)
❌ User registration (not implemented)
❌ Order history (future release)
❌ Admin functionality (separate plan)

### 2.4 Features to Test

| Feature ID | Feature Name | Priority | Test Approach |
|------------|-------------|----------|---------------|
| F-001 | User Login | Critical | Functional + Security + Automation |
| F-002 | Product Display | High | Functional + Visual + Automation |
| F-003 | Product Sorting | Medium | Functional + Automation |
| F-004 | Add to Cart | Critical | Functional + State Testing + Automation |
| F-005 | Cart Persistence (NEW) | Critical | Functional + Negative + Exploratory |
| F-006 | Checkout Flow (ENHANCED) | Critical | E2E + Exploratory + Automation |
| F-007 | Order Completion | Critical | Functional + Automation |

### 2.5 Features NOT to Test

| Feature | Reason |
|---------|--------|
| Payment Gateway | Mock/stub implementation only |
| Email Notifications | No email system integrated |
| User Registration | Not in scope for this release |
| Product Recommendations | Deferred to v2.2 |

### 2.6 Test Approach

**Test Levels:**
- System Testing (primary focus)
- Integration Testing (API endpoints)
- Acceptance Testing (business scenarios)

**Test Types:**
- **Functional:** 100 test cases
- **Regression:** 50 test cases (automated)
- **Exploratory:** 4 sessions × 90 minutes
- **Usability:** Heuristic evaluation
- **Compatibility:** 5 browser × OS combinations
- **Performance:** Basic load testing (50 concurrent users)

**Test Techniques:**
- Equivalence Partitioning (login, inputs)
- Boundary Value Analysis (cart quantity, input lengths)
- Decision Tables (checkout validation)
- State Transition (cart states, checkout workflow)
- Pairwise Testing (browser × OS combinations)
- Error Guessing (edge cases)
- Exploratory Testing (new features)

### 2.7 Pass/Fail Criteria

**Exit Criteria (when to stop testing):**
✅ All critical test cases executed
✅ 95%+ pass rate on regression tests
✅ Zero severity 1 (critical) defects open
✅ Maximum 2 severity 2 (high) defects open
✅ All exploratory sessions completed
✅ Requirements coverage ≥ 95%

**Suspension Criteria (when to pause testing):**
⛔ Build is not deployable (won't start)
⛔ Showstopper defects blocking > 30% of tests
⛔ Test environment unavailable for > 4 hours
⛔ Critical test data corrupted

**Resumption Requirements:**
✅ Build fixed and deployed to test environment
✅ Blocking defects resolved and verified
✅ Environment restored and validated
✅ Test data refreshed

### 2.8 Test Deliverables

**Before Testing:**
- Test plan (this document)
- Test cases (150 test cases in TestRail)
- Test data (test users, products)
- Test environment setup guide

**During Testing:**
- Daily test status reports
- Defect reports (in Jira)
- Test execution logs
- Exploratory session notes

**After Testing:**
- Test summary report
- Metrics and coverage analysis
- Defect analysis report
- Lessons learned document
- Updated automation scripts

### 2.9 Test Environment

**Hardware:**
- 2 × Windows 10 workstations
- 1 × MacBook Pro (macOS Ventura)
- Mobile devices: iPhone 13, Samsung Galaxy S21

**Software:**
- Browsers: Chrome 120, Firefox 121, Safari 17, Edge 120
- Test Management: TestRail
- Automation: Selenium Grid + Playwright
- API Testing: Postman
- Defect Tracking: Jira

**Test Environment URL:**
- Test: https://www.saucedemo.com
- Note: Public demo site, no dedicated environment

**Test Data:**
```
Users:
- standard_user / secret_sauce
- problem_user / secret_sauce
- performance_glitch_user / secret_sauce
- locked_out_user / secret_sauce

Products: 6 pre-configured items
```

### 2.10 Schedule & Milestones

| Phase | Activities | Duration | Dates |
|-------|-----------|----------|-------|
| **Planning** | Test plan, test case creation | 3 days | Jan 1-3 |
| **Setup** | Environment setup, test data | 1 day | Jan 4 |
| **Execution - Functional** | Execute functional test cases | 4 days | Jan 5-8 |
| **Execution - Regression** | Execute automated regression | 1 day | Jan 9 |
| **Execution - Exploratory** | 4 exploratory sessions | 2 days | Jan 10-11 |
| **Retesting** | Verify defect fixes | 2 days | Jan 12-13 |
| **Reporting** | Test summary, metrics | 1 day | Jan 14 |
| **TOTAL** | | **14 days** | **Jan 1-14** |

### 2.11 Staffing & Responsibilities

| Role | Responsibility | Person | Effort |
|------|---------------|--------|--------|
| **Test Manager** | Test planning, reporting, stakeholder communication | Sarah Johnson | 50% |
| **QA Lead** | Test case review, execution coordination, defect triage | Michael Chen | 100% |
| **QA Engineer** | Test execution, automation, exploratory testing | You (Mentee) | 100% |
| **Automation Engineer** | Regression automation, CI/CD integration | David Lopez | 50% |
| **Developer** | Defect fixes, unit testing | Dev Team | As needed |
| **Product Owner** | Acceptance criteria, UAT | Emily Davis | 25% |

### 2.12 Training Needs

| Team Member | Training Required | Duration |
|-------------|------------------|----------|
| Mentee | Selenium basics | 4 hours |
| Mentee | Exploratory testing techniques | 2 hours |
| Team | New checkout flow walkthrough | 1 hour |

### 2.13 Risks & Mitigation

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|-----------|
| Test environment instability | Medium | High | Use public demo site; have backup local environment |
| Incomplete requirements | Low | High | Requirements review session before testing starts |
| Automation delays | Medium | Medium | Have manual fallback; prioritize critical scenarios |
| Resource unavailability (sick leave) | Medium | High | Cross-train team members; document test procedures |
| Scope creep | High | Medium | Strict change control; re-estimate if scope changes |
| Defect backlog | Medium | High | Daily defect triage; prioritize critical bugs |

### 2.14 Assumptions & Dependencies

**Assumptions:**
- Test environment available 9am-6pm daily
- All requirements are final (no major changes)
- Test data can be reset daily
- Development team available for defect clarifications

**Dependencies:**
- Development completes features by Jan 4
- Build deployed to test environment by Jan 5
- TestRail access granted to all testers
- No blocking defects from previous sprint

### 2.15 Approvals

| Name | Role | Signature | Date |
|------|------|-----------|------|
| Sarah Johnson | Test Manager | ____________ | _____ |
| Emily Davis | Product Owner | ____________ | _____ |
| Michael Chen | QA Lead | ____________ | _____ |

---

## 3️⃣ Effort Estimation

### 3.1 Estimation Techniques

#### Test Point Method
**Formula:** Test Points = (Number of test cases) × (Complexity weight) × (Tester experience factor)

**Complexity Weights:**
- Simple: 1 (login with valid credentials)
- Medium: 2 (checkout flow)
- Complex: 3 (exploratory session, integration tests)

**Example:**
```
50 simple tests × 1 × 1.0 = 50 points
30 medium tests × 2 × 1.0 = 60 points
20 complex tests × 3 × 1.0 = 60 points
Total: 170 test points

If 1 test point = 15 minutes:
170 × 15 min = 2,550 minutes = 42.5 hours ≈ 5.3 days
```

#### Work Breakdown Structure (WBS)
Break testing into activities and estimate each:

```
Test Planning: 16 hours
  - Requirements review: 4h
  - Test plan creation: 8h
  - Test case design: 24h
  - Test case review: 4h

Test Environment Setup: 8 hours
  - Environment configuration: 4h
  - Test data creation: 2h
  - Tool setup: 2h

Test Execution: 48 hours
  - Functional testing: 32h
  - Regression testing: 8h
  - Exploratory testing: 12h (4 sessions)
  - Retesting defect fixes: 16h

Test Reporting: 8 hours
  - Daily status reports: 4h
  - Test summary report: 4h

TOTAL: 120 hours = 15 days (assuming 8h work day)
```

#### Historical Data Method
Use past projects as baseline:

```
Previous similar release (v2.0):
- Test cases: 120
- Execution time: 10 days
- Defects found: 25
- Retesting: 3 days

Current release (v2.1):
- Test cases: 150 (25% more)
- Estimated execution: 12 days
- Expected defects: 30
- Retesting: 4 days
```

### 3.2 SauceDemo Test Effort Estimation

**Test Case Count:**
- Login module: 15 test cases × 20 min = 5 hours
- Product browsing: 10 test cases × 15 min = 2.5 hours
- Cart operations: 20 test cases × 25 min = 8.3 hours
- Checkout flow: 30 test cases × 30 min = 15 hours
- Regression: 50 test cases × 10 min = 8.3 hours
- Exploratory: 4 sessions × 90 min = 6 hours
- Retesting: 15% of total = 6.75 hours

**Total Test Execution: ~52 hours**

**Add Supporting Activities:**
- Test planning: 16 hours
- Test case creation: 24 hours
- Environment setup: 4 hours
- Defect reporting: 8 hours
- Test reporting: 8 hours

**Grand Total: ~112 hours ≈ 14 days (2 weeks)**

---

## 4️⃣ Entry & Exit Criteria

### 4.1 Entry Criteria

**When can testing START?**

✅ **Code & Build:**
- Development declared feature complete
- Build deployed to test environment
- Build smoke tested (login works, app launches)

✅ **Test Readiness:**
- Test plan approved
- Test cases created and reviewed
- Test data prepared
- Test environment configured and validated

✅ **Documentation:**
- Requirements finalized
- Test environment access documented
- Known issues list published

✅ **Resources:**
- Testers assigned and available
- Tools and licenses available
- Training completed (if needed)

**Entry Checklist Example:**
```
[ ] Build #245 deployed to test environment
[ ] Smoke test passed (login, basic navigation)
[ ] 150 test cases created in TestRail
[ ] Test data reset and validated
[ ] All testers have environment access
[ ] Requirements document v2.1 final
[ ] Test plan approved by stakeholders
[ ] Zero blocking defects from previous sprint
```

### 4.2 Exit Criteria

**When can testing STOP?**

✅ **Test Execution:**
- 100% critical test cases executed
- 95%+ of all test cases executed
- All exploratory sessions completed
- All blocked tests resolved or deferred

✅ **Quality Metrics:**
- 95%+ test pass rate
- Requirements coverage ≥ 95%
- Automation coverage ≥ 60% (for regression)

✅ **Defect Metrics:**
- Zero Severity 1 (Critical) defects open
- ≤ 2 Severity 2 (High) defects open
- All must-fix defects resolved
- Remaining defects accepted by Product Owner

✅ **Regression:**
- Full regression suite executed
- No new regressions introduced

✅ **Documentation:**
- Test summary report completed
- All defects documented in Jira
- Metrics report published
- Known issues list updated

**Exit Checklist Example:**
```
[ ] 148/150 test cases executed (99%)
[ ] Pass rate: 142/148 = 96%
[ ] Requirements coverage: 24/25 = 96%
[ ] Severity 1 defects: 0 open
[ ] Severity 2 defects: 1 open (accepted by PO)
[ ] Regression suite: 50/50 passed (100%)
[ ] Test summary report published
[ ] Stakeholder approval received
```

### 4.3 Suspension & Resumption Criteria

**Suspend testing if:**
⛔ > 30% of test cases are blocked
⛔ Test environment down > 4 hours
⛔ Critical defect makes app unusable
⛔ Build is not deployable
⛔ Major requirement change (scope change)

**Resume testing when:**
✅ Blocking issues resolved
✅ Environment restored and validated
✅ New build deployed if needed
✅ Test cases updated for requirement changes

---

## 5️⃣ Test Metrics & Reporting

### 5.1 Key Metrics to Track

#### Test Progress Metrics
```
Test Execution Progress = (Tests executed / Total tests) × 100%
Example: 120/150 = 80%

Test Pass Rate = (Tests passed / Tests executed) × 100%
Example: 110/120 = 92%

Requirements Coverage = (Requirements tested / Total requirements) × 100%
Example: 23/25 = 92%
```

#### Defect Metrics
```
Defect Density = Total defects / Test cases executed
Example: 25 defects / 120 test cases = 0.21 defects per test

Defect Removal Efficiency = (Defects found in testing / Total defects) × 100%
Example: 25/(25+3 in prod) = 89%

Defect Leakage = (Defects in production / Total defects) × 100%
Example: 3/(25+3) = 11%
```

#### Automation Metrics
```
Automation Coverage = (Automated tests / Total tests) × 100%
Example: 90/150 = 60%

Automation ROI = (Manual effort saved / Automation effort)
Example: (50 tests × 5 runs × 15 min) / (50 tests × 60 min creation) = 1.25x
```

### 5.2 Daily Status Report Template

```markdown
## Daily Test Status Report
**Date:** January 8, 2024
**Project:** SauceDemo v2.1
**Prepared by:** QA Lead

### Executive Summary
Testing is ON TRACK. 80% test cases executed with 92% pass rate.
One high-severity defect found in checkout flow.

### Test Execution Status
- Total Test Cases: 150
- Executed Today: 25
- Total Executed: 120 (80%)
- Passed: 110 (92%)
- Failed: 8 (7%)
- Blocked: 2 (1%)

### Defects Summary
| Severity | New Today | Total Open | Resolved |
|----------|-----------|------------|----------|
| Critical (S1) | 0 | 0 | 1 |
| High (S2) | 1 | 2 | 3 |
| Medium (S3) | 2 | 5 | 4 |
| Low (S4) | 1 | 3 | 2 |

### Top Issues
1. **DEF-234** [S2] - Checkout fails when cart has 6 items (blocking 2 tests)
2. **DEF-231** [S3] - Sort order not persisting after page refresh

### Planned for Tomorrow
- Execute remaining 30 test cases (cart persistence)
- Retest 5 fixed defects
- Start exploratory session #1 (checkout flow)

### Risks/Blockers
- None

### Status: 🟢 ON TRACK
```

### 5.3 Test Summary Report Template

```markdown
## Test Summary Report
**Project:** SauceDemo v2.1 Release
**Test Period:** January 1-14, 2024
**Report Date:** January 14, 2024
**Prepared by:** Sarah Johnson, Test Manager

### Executive Summary
Testing for SauceDemo v2.1 is COMPLETE. 148/150 test cases executed
with 96% pass rate. All critical defects resolved. Recommend
RELEASE to production with 1 known medium-severity issue (accepted by PO).

### Test Objectives
✅ Validate enhanced checkout flow
✅ Verify cart persistence feature
✅ Ensure no regression in existing features
✅ Achieve 95% requirements coverage

### Test Execution Summary
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Test Cases Executed | 100% (150) | 99% (148) | 🟢 |
| Pass Rate | ≥ 95% | 96% | 🟢 |
| Requirements Coverage | ≥ 95% | 96% | 🟢 |
| Automation Coverage | ≥ 60% | 62% | 🟢 |

**Not Executed:** 2 test cases (blocked by environment limitation)

### Defect Summary
| Severity | Found | Fixed | Open | Deferred |
|----------|-------|-------|------|----------|
| Critical | 3 | 3 | 0 | 0 |
| High | 8 | 7 | 1 | 0 |
| Medium | 12 | 10 | 1 | 1 |
| Low | 7 | 3 | 2 | 2 |
| **Total** | **30** | **23** | **4** | **3** |

**Open Defects:**
- DEF-245 [S2] - Sort order resets on browser refresh (accepted by PO)
- DEF-251 [S3] - Minor alignment issue on mobile
- DEF-257 [S4] - Footer link color inconsistency
- DEF-259 [S4] - Tooltip typo

**Deferred to v2.2:**
- DEF-248 [S3] - Performance slow with performance_glitch_user
- DEF-253 [S4] - Image zoom feature request
- DEF-261 [S4] - Add product comparison feature

### Requirements Coverage
- Total Requirements: 25
- Tested: 24 (96%)
- Passed: 23 (92%)
- Failed: 1 (4%, accepted)
- Not Tested: 1 (payment gateway - out of scope)

### Test Approach
- Functional Testing: 100 test cases
- Regression Testing: 50 automated test cases
- Exploratory Testing: 4 sessions × 90 minutes
- Compatibility Testing: 5 browser/OS combinations
- Usability Testing: Heuristic evaluation

### Risks & Issues
✅ **Resolved:** Initial environment instability (days 1-2)
✅ **Resolved:** Scope clarification for cart persistence
⚠️ **Accepted:** Sort order reset issue (low user impact)

### Lessons Learned
**What Went Well:**
- Early exploratory testing found critical checkout bug
- Automation saved 12 hours in regression testing
- Daily standup improved team communication

**What Could Improve:**
- Requirements needed more clarity upfront
- Test data setup was manual (should automate)
- Need dedicated test environment (not public demo)

### Recommendations
✅ **RELEASE to production** - Quality criteria met
⚠️ **Monitor:** Sort order reset issue (analytics)
📝 **Future:** Automate test data setup
📝 **Future:** Secure dedicated test environment

### Attachments
- Detailed test results (TestRail report)
- Defect details (Jira export)
- Test coverage analysis (Excel)
- Exploratory session notes

**Approval:**
______________ ______
Test Manager   Date

______________ ______
Product Owner  Date
```

---

## 6️⃣ Creating a Test Plan for SauceDemo

### Step-by-Step Guide

#### Step 1: Understand the Product (30 min)
- Explore SauceDemo manually
- List all features
- Identify critical workflows
- Note any obvious issues

#### Step 2: Define Scope (20 min)
**In Scope:**
- Login
- Product browsing
- Cart operations
- Checkout
- Logout

**Out of Scope:**
- User registration (doesn't exist)
- Payment processing (simulated)
- Backend admin

#### Step 3: Identify Test Objectives (15 min)
```
1. Verify all user workflows function correctly
2. Ensure data integrity (cart persistence, state management)
3. Validate security (authentication, authorization)
4. Confirm usability across browsers
5. Achieve 95% requirements coverage
```

#### Step 4: List Features to Test (30 min)
Create table with all features, priority, approach (see 2.4 above)

#### Step 5: Choose Test Approach (30 min)
- Which test levels? (System, Integration)
- Which test types? (Functional, Regression, Exploratory, Compatibility)
- Which techniques? (EP, BVA, State Transition, Pairwise, Error Guessing)

#### Step 6: Define Entry/Exit Criteria (20 min)
Use templates from section 4 above

#### Step 7: Estimate Effort (45 min)
- Count expected test cases per feature
- Estimate time per test
- Add supporting activities (planning, setup, reporting)
- Calculate total effort

#### Step 8: Create Schedule (30 min)
- Break down into phases
- Assign dates
- Identify milestones
- Add buffer (10-15%)

#### Step 9: Identify Resources (15 min)
- How many testers?
- What tools needed?
- Any training required?

#### Step 10: Risk Assessment (45 min)
- List potential risks
- Assess probability and impact
- Define mitigation strategies

#### Step 11: Write the Plan (2-3 hours)
Use the template structure from section 2

#### Step 12: Review & Approval (30 min)
- Review with team
- Incorporate feedback
- Get stakeholder approval

**Total Time to Create Test Plan: ~8-10 hours**

---

## 7️⃣ Test Plan Best Practices

### DO's ✅
- **Involve stakeholders early** - Get buy-in from PM, Dev, PO
- **Be realistic with estimates** - Add 10-15% buffer
- **Define clear scope** - What's in and what's OUT
- **Use templates** - Don't start from scratch
- **Make it visual** - Charts, tables, diagrams
- **Keep it updated** - Living document, not write-once
- **Review past projects** - Learn from history
- **Define metrics early** - Know how you'll measure success
- **Plan for retesting** - Always allocate time for defect fixes
- **Document assumptions** - Make the implicit explicit

### DON'Ts ❌
- **Don't over-plan** - 10-page plan is enough; 100 pages is overkill
- **Don't ignore risks** - Hope is not a strategy
- **Don't commit to 100% coverage** - Unrealistic and wasteful
- **Don't skip exit criteria** - Prevents endless testing
- **Don't plan in isolation** - Collaborate with team
- **Don't use vague terms** - "Thorough testing" means what?
- **Don't forget regression** - Always plan for regression testing
- **Don't ignore dependencies** - Test data, environment, resources
- **Don't promise what you can't deliver** - Under-promise, over-deliver
- **Don't write and forget** - Review and update regularly

### Common Pitfalls
1. **Scope creep** - Features keep getting added
   - **Fix:** Formal change control process

2. **Unrealistic estimates** - Too optimistic
   - **Fix:** Use historical data, add buffer

3. **Unclear exit criteria** - Never know when to stop
   - **Fix:** Specific, measurable criteria

4. **Resource constraints** - Not enough people/tools
   - **Fix:** Flag early, re-negotiate scope or timeline

5. **Environment issues** - Can't test without stable environment
   - **Fix:** List as entry criteria, have backup plan

---

## 8️⃣ Agile vs Waterfall Test Planning

### Waterfall Test Planning
- **When:** Upfront, before development starts
- **Scope:** Entire project/release
- **Detail:** Very detailed, comprehensive
- **Duration:** Weeks to months
- **Changes:** Formal change control, difficult
- **Documentation:** Heavy (100+ pages possible)

**Example:** 6-month project, create complete test plan in month 1

### Agile/Scrum Test Planning
- **When:** Sprint planning (every 2 weeks)
- **Scope:** Sprint backlog only
- **Detail:** High-level strategy + sprint-specific tactics
- **Duration:** Hours to days
- **Changes:** Expected, embrace change
- **Documentation:** Lightweight (test strategy + sprint test plan)

**Example:** 2-week sprint, create sprint test plan in 2-hour planning session

### Agile Test Plan Structure

```markdown
## Sprint 5 Test Plan
**Sprint Goal:** Implement cart persistence

### Features in Sprint
1. Cart saves to local storage
2. Cart persists across sessions
3. Cart clears after order

### Test Approach
- 15 new test cases (cart persistence)
- 20 regression test cases (automated)
- 1 exploratory session (cart workflow)

### Entry Criteria
- User stories accepted by PO
- Dev environment deployed
- Test cases created

### Exit Criteria
- All acceptance criteria met
- Zero critical defects
- Regression suite passes

### Effort: 16 hours
### Risk: Medium (new technology - local storage)
```

**Key Difference:** Agile test planning is iterative, lightweight, and sprint-focused. Waterfall is comprehensive and upfront.

---

## 📝 Summary

### Key Takeaways

1. **Test Strategy vs Test Plan**
   - Strategy: Long-term, organizational approach
   - Plan: Short-term, project-specific tactics

2. **Test Plan Must Answer:**
   - What to test (scope)
   - Why to test (objectives)
   - How to test (approach, techniques)
   - Who will test (resources, roles)
   - When to test (schedule, milestones)

3. **Critical Components:**
   - Clear scope (in/out)
   - Entry/Exit criteria (when to start/stop)
   - Effort estimation (realistic timeline)
   - Risk assessment (mitigation strategies)
   - Metrics (measure success)

4. **Estimation Techniques:**
   - Test point method
   - Work breakdown structure
   - Historical data

5. **Entry/Exit Criteria:**
   - Entry: When CAN we start?
   - Exit: When CAN we stop?
   - Both must be specific and measurable

6. **Success Factors:**
   - Stakeholder involvement
   - Realistic estimates
   - Clear communication
   - Regular updates
   - Risk awareness

### This Week's Goal
**Create a comprehensive test plan for SauceDemo** using the template and techniques from this tutorial. Your plan should be 8-12 pages and include all key components.

**Next week:** We'll use this plan to design 50+ test cases with full traceability!

---

## 🤔 Self-Assessment Questions

1. What's the main difference between a test strategy and a test plan?
2. Name 5 essential components of a test plan
3. What are entry criteria and why are they important?
4. What are exit criteria and give 3 examples
5. How do you estimate testing effort?
6. What's the difference between suspension criteria and exit criteria?
7. Why is risk assessment important in test planning?
8. What should you do if scope changes mid-testing?
9. Name 3 key metrics to track during testing
10. How does Agile test planning differ from Waterfall?

### Answers to Check
1. Strategy = long-term organizational approach; Plan = short-term project-specific tactics
2. Scope, objectives, approach, schedule, resources, entry/exit criteria, risks, deliverables (any 5)
3. Entry criteria define when testing can start; Important to ensure readiness and prevent wasted effort
4. Examples: 100% critical tests executed, 95%+ pass rate, zero S1 defects, requirements coverage ≥ 95% (any 3)
5. Test point method, work breakdown structure, historical data analysis
6. Suspension = pause temporarily due to blockers; Exit = stop permanently because done
7. Identifies potential issues early; Allows mitigation planning; Manages stakeholder expectations
8. Assess impact, re-estimate effort, update test plan, get stakeholder approval, document changes
9. Test execution progress, pass/fail rate, defect density, requirements coverage, automation coverage (any 3)
10. Agile: iterative, lightweight, sprint-focused; Waterfall: comprehensive, upfront, project-focused

---

**📚 Continue to: exercises.md → Create your complete test plan for SauceDemo**

**⏭️ Next Week:** Test Case Design & Management - Writing 50+ detailed test cases with requirements traceability
