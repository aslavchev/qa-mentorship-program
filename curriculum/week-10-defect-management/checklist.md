# Week 10: Defect Management - Checklist

## 📋 Weekly Goals
- [ ] Master defect lifecycle and states
- [ ] Write FAANG-level professional bug reports
- [ ] Understand severity vs priority classification
- [ ] Calculate and interpret defect metrics (DRE, leakage, density)
- [ ] Perform root cause analysis using 5 Whys
- [ ] Find 10+ real bugs in SauceDemo using exploratory testing

---

## 📚 Tutorial Completion
- [ ] Read complete tutorial.md (2-3 hours)
- [ ] Study Section 1: Defect Lifecycle (NEW → CLOSED states)
- [ ] Study Section 2: Writing Effective Bug Reports
- [ ] Study Section 3: Severity vs Priority
- [ ] Study Section 4: Defect Triage process
- [ ] Study Section 5: Defect Metrics & Reporting
- [ ] Study Section 6: Root Cause Analysis (5 Whys)
- [ ] Study Section 7: SauceDemo Bug Examples
- [ ] Study Section 8: Defect Management Best Practices
- [ ] Answer self-assessment questions at end of tutorial

---

## 🧪 Exercises Completion

### Exercise 1: Find Bugs in SauceDemo (90 min)
- [ ] Testing environment set up (DevTools, screen recording)
- [ ] Login module tested (15 min)
  - [ ] Valid/invalid credentials tested
  - [ ] SQL injection attempts tested
  - [ ] XSS attempts tested
  - [ ] Edge cases tested (spaces, special chars, case sensitivity)
- [ ] Products module tested (20 min)
  - [ ] Product display verified
  - [ ] Sort functionality tested (all 4 options)
  - [ ] Add/Remove buttons tested
  - [ ] Special users tested (problem_user, visual_user)
- [ ] Cart module tested (20 min)
  - [ ] Cart badge accuracy tested
  - [ ] Cart calculations verified
  - [ ] State persistence tested
  - [ ] Edge cases tested (empty cart, multiple items)
- [ ] Checkout module tested (20 min)
  - [ ] Form validation tested (all fields)
  - [ ] Order summary calculations verified
  - [ ] Cart state after order tested
- [ ] Cross-cutting concerns tested (10 min)
  - [ ] Responsiveness tested (multiple screen sizes)
  - [ ] Accessibility tested (keyboard navigation)
  - [ ] Security tested (session management, direct URLs)
- [ ] **Minimum 10 bugs found** ✅
- [ ] All bugs documented in find-bugs.md
- [ ] Bugs span multiple modules (not all from one area)
- [ ] At least 1 security-related bug found
- [ ] Bugs are reproducible (100% repro rate)

### Exercise 2: Write Professional Bug Reports (90 min)
- [ ] Bug report template reviewed
- [ ] 10+ bugs selected for documentation
- [ ] Evidence captured for all bugs:
  - [ ] Screenshots taken (annotated)
  - [ ] Screen recordings (optional)
  - [ ] Console logs captured (if applicable)
  - [ ] Evidence saved in mentee-work/week-10/evidence/
- [ ] **All 10+ bug reports written** ✅
- [ ] Bug reports follow template exactly:
  - [ ] Bug ID assigned (BUG-001, BUG-002, etc.)
  - [ ] Summary clear and searchable
  - [ ] Description (2-3 sentences)
  - [ ] Steps to Reproduce detailed and numbered
  - [ ] Expected Result stated
  - [ ] Actual Result stated
  - [ ] Environment details complete
  - [ ] Preconditions stated
  - [ ] Test data specific (no placeholders)
  - [ ] Attachments referenced
- [ ] Self-review checklist completed for each report
- [ ] Professional tone maintained (no blame, clear communication)
- [ ] Bug report index table created

### Exercise 3: Assign Severity & Priority (30 min)
- [ ] Severity definitions reviewed (S1-S4)
- [ ] Priority definitions reviewed (P0-P3)
- [ ] **All bugs classified** (severity AND priority) ✅
- [ ] Justification written for each classification (2-3 sentences)
- [ ] Severity distribution calculated:
  - [ ] S1 count and percentage
  - [ ] S2 count and percentage
  - [ ] S3 count and percentage
  - [ ] S4 count and percentage
  - [ ] Total = 100% ✅
- [ ] Priority distribution calculated:
  - [ ] P0 count and percentage
  - [ ] P1 count and percentage
  - [ ] P2 count and percentage
  - [ ] P3 count and percentage
  - [ ] Total = 100% ✅
- [ ] Severity/Priority matrix created
- [ ] Most critical bug identified
- [ ] Fix order recommended
- [ ] Interesting cases noted (High Sev + Low Pri, or vice versa)

### Exercise 4: Defect Metrics Dashboard (45 min)
- [ ] Metric definitions reviewed
- [ ] Data gathered (bugs, test cases, modules, severity)
- [ ] **Defect Density calculated** ✅
  - [ ] Formula applied correctly
  - [ ] Compared to benchmark (0.10-0.25)
  - [ ] Interpretation written
- [ ] **Defect Distribution by Severity calculated** ✅
  - [ ] Counts per severity level
  - [ ] Percentages calculated (total = 100%)
  - [ ] Compared to target ranges
  - [ ] Text-based chart created
  - [ ] Analysis written
- [ ] **Defect Distribution by Module calculated** ✅
  - [ ] Counts per module
  - [ ] Percentages calculated (total = 100%)
  - [ ] Defect hotspot identified
  - [ ] Text-based chart created
  - [ ] Analysis written
- [ ] **Defect Removal Efficiency (DRE) simulated** ✅
  - [ ] 2-3 escaped bugs selected
  - [ ] DRE formula applied
  - [ ] Compared to target (90%+)
  - [ ] Analysis written
- [ ] **Defect Leakage simulated** ✅
  - [ ] Leakage formula applied
  - [ ] Compared to target (<10%)
  - [ ] Escaped bugs explained
  - [ ] Analysis written
- [ ] Key insights documented (4+ insights)
- [ ] Recommendations provided (3+ actions)
- [ ] Metrics dashboard summary table created
- [ ] Overall grade assigned with justification
- [ ] Reflection questions answered

### Exercise 5: Root Cause Analysis (45 min)
- [ ] RCA techniques reviewed (5 Whys)
- [ ] 2-3 critical bugs selected for RCA (S1 or S2 bugs)
- [ ] **RCA #1 completed** ✅
  - [ ] Problem statement written
  - [ ] All 5 Whys answered
  - [ ] Root cause identified (not just symptom)
  - [ ] Root cause categorized (Requirements/Code/Testing/Environment/Communication)
  - [ ] How it escaped testing explained
  - [ ] Corrective actions listed (3+ actions)
  - [ ] Preventive actions listed (3+ actions)
  - [ ] Lessons learned documented (3+ lessons)
- [ ] **RCA #2 completed** ✅
  - [ ] Problem statement written
  - [ ] All 5 Whys answered
  - [ ] Root cause identified
  - [ ] Root cause categorized
  - [ ] How it escaped testing explained
  - [ ] Corrective actions listed
  - [ ] Preventive actions listed
  - [ ] Lessons learned documented
- [ ] **RCA #3 completed** (if applicable) ✅
  - [ ] Problem statement written
  - [ ] All 5 Whys answered
  - [ ] Root cause identified
  - [ ] Root cause categorized
  - [ ] How it escaped testing explained
  - [ ] Corrective actions listed
  - [ ] Preventive actions listed
  - [ ] Lessons learned documented
- [ ] Pattern analysis completed:
  - [ ] Most common root cause category identified
  - [ ] Systemic issues identified (3+ issues)
  - [ ] Cross-bug themes documented
  - [ ] Shared preventive actions identified
- [ ] Recommendations provided:
  - [ ] Immediate actions (2+ actions)
  - [ ] Short-term actions (3+ actions)
  - [ ] Long-term actions (3+ actions)
- [ ] Reflection questions answered (4 questions)

---

## 📂 Deliverables

### Week 10 Deliverables (5 files + evidence folder)
- [ ] `mentee-work/week-10/find-bugs.md` - 10+ bugs discovered
- [ ] `mentee-work/week-10/write-bug-reports.md` - 10+ professional reports
- [ ] `mentee-work/week-10/severity-priority.md` - All bugs classified
- [ ] `mentee-work/week-10/defect-metrics.md` - Metrics dashboard
- [ ] `mentee-work/week-10/root-cause-analysis.md` - 2-3 RCAs
- [ ] `mentee-work/week-10/evidence/` - Screenshots, videos, logs
- [ ] All work committed to GitHub with clear commit messages
- [ ] Pull Request created with Week 10 submission template

---

## ⏱️ Time Tracking

| Activity | Estimated | Actual |
|----------|-----------|--------|
| Tutorial Reading | 2-3 hrs | ___ |
| Exercise 1 (Find Bugs) | 90 min | ___ |
| Exercise 2 (Bug Reports) | 90 min | ___ |
| Exercise 3 (Severity/Priority) | 30 min | ___ |
| Exercise 4 (Metrics) | 45 min | ___ |
| Exercise 5 (RCA) | 45 min | ___ |
| Documentation & Commit | 30 min | ___ |
| **Total** | **8-9 hrs** | **___** |

---

## 🎯 Key Learning Outcomes

By the end of Week 10, you should be able to:
- [ ] Explain the defect lifecycle (all 8 states)
- [ ] Write professional bug reports with all required fields
- [ ] Differentiate between severity and priority
- [ ] Justify severity/priority classifications with business context
- [ ] Calculate defect density, DRE, and defect leakage
- [ ] Interpret defect metrics and make recommendations
- [ ] Identify defect hotspots from distribution data
- [ ] Perform root cause analysis using 5 Whys technique
- [ ] Differentiate between corrective and preventive actions
- [ ] Identify systemic issues from bug patterns
- [ ] Write reproduction steps that anyone can follow
- [ ] Capture and present evidence (screenshots, videos)
- [ ] Communicate findings professionally to stakeholders

---

## ✅ Quality Gates (Must Pass Before Submission)

### Minimum Requirements
- [ ] ✅ **Minimum 10 bugs found** (Exercise 1)
- [ ] ✅ **All 10+ bug reports complete** (Exercise 2)
  - [ ] All fields filled (no "TBD" or placeholders)
  - [ ] Steps to Reproduce detailed and reproducible
  - [ ] Evidence attached (screenshots minimum)
- [ ] ✅ **All bugs classified** with severity AND priority (Exercise 3)
  - [ ] Justifications written (not just labels)
  - [ ] Distributions calculated (percentages = 100%)
- [ ] ✅ **Metrics dashboard complete** (Exercise 4)
  - [ ] All 5 metrics calculated
  - [ ] Math correct (verified)
  - [ ] Insights and recommendations provided
- [ ] ✅ **2-3 RCAs completed** using 5 Whys (Exercise 5)
  - [ ] All 5 Whys answered (not stopping at 2-3)
  - [ ] Root causes identified (systemic, not "developer error")
  - [ ] Preventive actions proposed

### FAANG-Level Excellence
- [ ] 🌟 **15+ bugs found** (exceeds minimum)
- [ ] 🌟 **At least 3 bug reports are portfolio-quality**
  - [ ] Could be shown in an interview
  - [ ] Professional formatting, clear evidence
  - [ ] Developer could reproduce in <2 minutes
- [ ] 🌟 **Severity/Priority justified with business context**
  - [ ] Not just technical impact, but business urgency
  - [ ] Considers workarounds, timelines, user impact
- [ ] 🌟 **Metrics dashboard is data-driven and actionable**
  - [ ] Compares to industry benchmarks
  - [ ] Identifies specific actions (not just observations)
  - [ ] Executive-level summary provided
- [ ] 🌟 **RCA identifies systemic patterns**
  - [ ] Cross-bug analysis reveals themes
  - [ ] Preventive actions address root causes
  - [ ] Recommendations prioritized (immediate/short/long-term)
- [ ] 🌟 **Evidence is professional**
  - [ ] Screenshots annotated (arrows, highlights)
  - [ ] Screen recordings provided (optional but excellent)
  - [ ] Console logs captured for technical bugs
- [ ] 🌟 **DRE >= 90%** (simulated)
- [ ] 🌟 **Defect Leakage < 10%** (simulated)

---

## 📊 Self-Assessment

Before submitting Week 10, rate yourself:

| Dimension | Rating (1-5) | Notes |
|-----------|--------------|-------|
| **Completeness** | ___ / 5 | All 5 exercises completed, 10+ bugs found/documented |
| **Quality** | ___ / 5 | Bug reports professional, metrics accurate, RCA thorough |
| **Accuracy** | ___ / 5 | Severity/priority justified, metrics calculations correct |
| **Critical Thinking** | ___ / 5 | RCA identifies systemic issues, recommendations actionable |
| **Professionalism** | ___ / 5 | Evidence captured, tone professional, formatting clean |
| **Portfolio Readiness** | ___ / 5 | Could show bug reports/metrics/RCA in interview |
| **Overall** | ___ / 5 | |

**Reflection:**
- What was most challenging this week?
- What are you most proud of?
- Which bug was hardest to find and why?
- What surprised you about RCA?
- How do defect metrics help decision-making?

---

## 🔗 Related Resources

### Templates Used
- Bug report template (in exercises.md Exercise 2)
- Severity/Priority classification guide (tutorial.md Section 3)
- Defect metrics formulas (tutorial.md Section 5)
- 5 Whys RCA template (tutorial.md Section 6)

### Week 8 Connection
- Uses Week 8 test cases (60 test cases) for defect density calculation
- Applies exploratory testing beyond scripted test cases
- Demonstrates real-world bug discovery (not just test execution)

### Tutorial Sections to Review if Stuck
- Section 2: Bug report components (if reports incomplete)
- Section 3: Severity vs Priority matrix (if classification unclear)
- Section 5: Metric formulas (if calculations wrong)
- Section 6: 5 Whys example (if RCA shallow)

---

## ✅ Week Completion

**Status:**
- [ ] Not Started
- [ ] In Progress (after reading tutorial)
- [ ] Exercises In Progress (after completing Exercise 1)
- [ ] Ready for Review (all 5 exercises complete)
- [ ] Completed (PR approved and merged)

**Completion Date:** _____________

**Mentor Sign-Off:** _____________

---

## 💡 Tips for Success

**Exercise 1 (Find Bugs):**
- Don't just test happy paths - test negative flows, edge cases, boundary values
- Use different test users (problem_user has known bugs)
- Watch browser console - many bugs show JavaScript errors
- Test cross-cutting concerns (responsive, accessibility, security)
- Document bugs immediately (don't wait until end of session)

**Exercise 2 (Bug Reports):**
- Write reports while bug is fresh in your mind
- Take screenshots DURING reproduction (not after)
- Test your own reproduction steps before submitting
- Use specific values: "standard_user" not "valid user"
- Professional tone: describe what's wrong, don't blame
- FAANG standard: Developer should reproduce in <2 minutes

**Exercise 3 (Severity/Priority):**
- Severity = Technical impact (how bad is it?)
- Priority = Business urgency (how soon to fix?)
- They're independent: S4 can be P1 (typo in CEO demo), S1 can be P3 (critical bug in rare feature)
- Justify with business context, not just technical impact
- Consider workarounds when assigning severity

**Exercise 4 (Metrics):**
- Double-check all math (percentages must add to 100%)
- Compare to industry benchmarks: DRE > 90%, Leakage < 10%
- Metrics without action are useless - always recommend next steps
- Be honest: if metrics are bad, explain why and how to improve
- Defect hotspot = where to focus more testing

**Exercise 5 (RCA):**
- Don't stop at first "why" - dig 5 levels deep
- Root cause should be systemic ("no code review"), not blame ("developer error")
- Preventive actions > corrective actions (prevent future bugs, not just fix current)
- Look for patterns: do 3 bugs share same root cause?
- Recommendations should be specific and actionable

**Portfolio Thinking:**
- Imagine showing this work in a FAANG interview
- "Show me a bug report you wrote" - can you show Exercise 2?
- "How do you measure testing effectiveness?" - can you show Exercise 4?
- "Tell me about a time you prevented future bugs" - can you show Exercise 5?

---

**Remember:** Week 10 is your most practical week. These are the exact skills FAANG QA roles use daily: finding bugs, documenting professionally, analyzing metrics, and preventing future issues. Make this week count! 🚀
