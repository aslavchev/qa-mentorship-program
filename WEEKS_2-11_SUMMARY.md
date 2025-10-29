# Weeks 2-11: Quick Reference & Content Summary

## 📋 Purpose

This document provides a comprehensive summary of Weeks 2-11 content to accelerate your mentoring program setup. Each week folder contains detailed tutorial.md files - this summary helps you quickly understand the progression and key deliverables.

---

## Week 2: Test Levels

### Core Topics
- Unit Testing (developers, 95-100% automated, individual components)
- Integration Testing (dev+QA, 60-80% automated, component interactions)
- System Testing (QA, 40-60% automated, complete application)
- Acceptance Testing (users+QA, 20-30% automated, business validation)

### Key Exercises
1. Map SauceDemo features to appropriate test levels
2. Create test level matrix showing which tests belong where
3. Write 5 integration test scenarios for SauceDemo
4. Write 10 system test scenarios for end-to-end flows
5. Define entry/exit criteria for each level

### Deliverable
**Test Level Analysis Document** for SauceDemo with categorized test scenarios

---

## Week 3: Functional Testing Types

### Core Topics
- **Smoke Testing:** Quick validation of critical paths (login, add to cart, checkout)
- **Sanity Testing:** Focused validation after bug fixes
- **Regression Testing:** Ensure existing features still work
- **Exploratory Testing:** Unscripted testing to find unexpected issues
- **Positive vs Negative Testing:** Valid inputs vs invalid/error scenarios

### Key Exercises
1. Create smoke test suite (10 critical tests for SauceDemo)
2. Perform exploratory testing session (60 minutes, document findings)
3. Write 15 positive test cases for SauceDemo
4. Write 15 negative test cases (error handling, boundary violations)
5. Build regression test checklist for SauceDemo

### Deliverable
**15+ functional test cases** for SauceDemo covering smoke, positive, negative scenarios

---

## Week 4: Non-Functional Testing

### Core Topics
- **Performance Testing:** Load, stress, endurance testing concepts
- **Security Testing:** Authentication, authorization, data protection
- **Usability Testing:** User experience, accessibility, ease of use
- **Compatibility Testing:** Cross-browser, cross-device, cross-OS
- **Accessibility Testing:** WCAG 2.1 compliance, screen readers

### Key Exercises
1. Perform manual performance assessment of SauceDemo (page load times)
2. Security checklist for SauceDemo (password masking, session handling)
3. Usability evaluation (can new user complete purchase easily?)
4. Cross-browser testing matrix (Chrome, Firefox, Safari)
5. Accessibility audit using browser DevTools

### Deliverable
**NFR Test Report** for SauceDemo with performance, security, usability findings

---

## Week 5: Test Design Techniques (Basic)

### Core Topics
- **Equivalence Partitioning (EP):** Group inputs into valid/invalid classes
- **Boundary Value Analysis (BVA):** Test at boundaries of input ranges
- **Decision Tables:** Test complex business rules with multiple conditions
- **State Transition Testing:** Test state-based behavior and workflows

### Key Exercises
1. Apply EP to SauceDemo username field (valid, invalid, empty, special chars)
2. Apply BVA to cart quantity field (0, 1, 99, 100, 101 items)
3. Create decision table for checkout form validation (multiple required fields)
4. Map state transitions for cart (empty → has items → checkout → complete)
5. Generate test cases using each technique

### Deliverable
**Test Design Document** showing EP, BVA, Decision Tables, State Transitions applied to SauceDemo

---

## Week 6: Test Design Techniques (Advanced)

### Core Topics
- **Pairwise Testing (All-Pairs):** Test all pairs of parameters efficiently
- **Error Guessing:** Use experience to predict likely failures
- **Risk-Based Testing:** Prioritize based on risk (probability × impact)
- **Exploratory Testing Techniques:** Session-based, charter-based

### Key Exercises
1. Create pairwise matrix for SauceDemo (User Type × Browser × Product × Quantity)
2. Error guessing exercise: Identify 10 likely failure scenarios
3. Risk assessment matrix for SauceDemo features (prioritize testing)
4. Conduct 90-minute exploratory testing session with charter
5. Combine multiple techniques for comprehensive test coverage

### Deliverable
**Advanced Test Design Document** with pairwise combinations, risk matrix, exploratory session notes

---

## Week 7: Test Planning & Strategy

### Core Topics
- Test Plan components (scope, objectives, resources, schedule, risks)
- Test Strategy (approach, levels, types, tools)
- Risk Assessment & Mitigation
- Resource Estimation
- Entry/Exit Criteria
- Test Metrics & Reporting

### Key Exercises
1. Create complete Test Plan for SauceDemo using template
2. Define test strategy (what to test, how, when, with what tools)
3. Conduct risk assessment (identify risks, mitigation strategies)
4. Estimate testing effort (person-hours per feature)
5. Define entry/exit criteria for test cycles

### Deliverable
**Complete Test Plan** for SauceDemo (10-15 pages, professional document)

---

## Week 8: Test Case Design & Management

### Core Topics
- Writing effective test cases (clear, concise, repeatable)
- Test case organization & numbering
- Requirements Traceability Matrix (RTM)
- Test data management
- Test case reviews & maintenance

### Key Exercises
1. Write 50+ professional test cases for SauceDemo using template
2. Organize test cases by module (login, catalog, cart, checkout)
3. Create Requirements Traceability Matrix
4. Design test data sets for various scenarios
5. Review and improve existing test cases

### Deliverable
**50+ Well-Organized Test Cases** for SauceDemo with complete RTM

---

## Week 9: Agile Testing & Methodologies

### Core Topics
- Agile Testing Quadrants (Q1: Unit/Component, Q2: Functional, Q3: Exploratory/Usability, Q4: Performance/Security)
- Behavior-Driven Development (BDD) & Gherkin syntax
- Test-Driven Development (TDD) concepts
- Definition of Done (DoD) & Acceptance Criteria
- Testing in Sprints

### Key Exercises
1. Map SauceDemo tests to Agile Testing Quadrants
2. Write 15+ BDD scenarios in Gherkin format (Given-When-Then)
3. Define acceptance criteria for 5 SauceDemo user stories
4. Create Definition of Done checklist for SauceDemo features
5. Plan testing activities for a 2-week sprint

### Deliverable
**BDD Test Scenarios** (15+) for SauceDemo in Gherkin format

---

## Week 10: Defect Management

### Core Topics
- Bug lifecycle (New → Open → In Progress → Fixed → Closed)
- Writing effective bug reports (reproducible, clear, complete)
- Severity vs Priority (technical impact vs business urgency)
- Defect metrics (density, removal efficiency, leakage rate)
- Root cause analysis

### Key Exercises
1. Find and document 10+ real bugs in SauceDemo using template
2. Practice severity/priority assignment for each bug
3. Create defect metrics dashboard (defects by module, severity, status)
4. Perform root cause analysis on major defects
5. Track bug lifecycle through resolution

### Deliverable
**10+ Professional Bug Reports** for real SauceDemo defects with full lifecycle tracking

---

## Week 11: Python for Test Data & Basic API Testing

### Core Topics
- Python basics for QA (variables, loops, functions, file I/O)
- Reading/writing test data files (CSV, JSON)
- Test data generation scripts
- Basic API testing with requests library
- Automating repetitive QA tasks

### Key Exercises
1. Install Python and set up environment
2. Write script to generate test data (usernames, passwords, products)
3. Read/write test cases from CSV file
4. Create script to test SauceDemo login API (if accessible)
5. Build simple test data randomizer

### Deliverable
**Python test data scripts** (3-5 working scripts for test data manipulation)

---

## 📊 Week-by-Week Progression on SauceDemo

```
Week 1: Explore application, document features
Week 2: Categorize by test levels
Week 3: Write 15+ functional test cases
Week 4: Perform NFR testing (performance, security, usability)
Week 5: Apply basic test design techniques (EP, BVA, Decision Tables)
Week 6: Apply advanced techniques (pairwise, risk-based)
Week 7: Create complete test plan
Week 8: Expand to 50+ organized test cases with RTM
Week 9: Convert key scenarios to BDD format
Week 10: Find and document 10+ real bugs
Week 11: Automate test data creation with Python
```

**Result:** Portfolio-ready GitHub repository demonstrating systematic QA approach!

---

## 🎯 Key Deliverables Summary

| Week | Primary Deliverable | Estimated Pages/Items |
|------|---------------------|----------------------|
| 1 | Application analysis & feature map | 5-7 pages |
| 2 | Test level categorization | 3-5 pages |
| 3 | 15+ functional test cases | 8-10 pages |
| 4 | NFR test report | 5-7 pages |
| 5 | Basic test design document | 8-10 pages |
| 6 | Advanced test design document | 8-10 pages |
| 7 | Complete test plan | 10-15 pages |
| 8 | 50+ test cases + RTM | 25-30 pages |
| 9 | 15+ BDD scenarios | 5-7 pages |
| 10 | 10+ bug reports | 10-15 pages |
| 11 | Python scripts | 5 scripts |

**Total Portfolio:** 100+ pages of professional QA documentation + code

---

## 📚 Recommended Resources by Week

### Week 2
- ISTQB Ch. 2 (Testing Throughout SDLC)
- Martin Fowler's "Practical Test Pyramid"

### Week 3
- "Exploratory Testing" by James Whittaker
- Ministry of Testing - Exploratory Testing guides

### Week 4
- OWASP Top 10 Security Risks
- Web.dev - Web Vitals for Performance
- WCAG 2.1 Guidelines for Accessibility

### Week 5-6
- "A Practitioner's Guide to Software Test Design" by Lee Copeland
- ISTQB Ch. 4 (Test Design Techniques)

### Week 7
- IEEE 829 Standard for Test Documentation
- Template provided in `templates/test-plan-template.md`

### Week 8
- "How to Write Better Test Cases" articles
- Test management tool tutorials (TestRail, Zephyr)

### Week 9
- "Agile Testing" by Lisa Crispin & Janet Gregory
- Cucumber documentation (BDD/Gherkin)
- https://cucumber.io/docs/gherkin/

### Week 10
- "Software Testing" by Ron Patton (Ch. on Bug Reporting)
- Template: `templates/bug-report-template.md`

### Week 11
- "Automate the Boring Stuff with Python" (Ch. 1-8)
- Python requests library documentation
- Real Python tutorials for beginners

---

## 🏆 Mentor Guidance: Weekly Session Structure

### Every Week Follow This Format:

**Week Opening (10 min):**
- Review previous week's deliverables
- Discuss challenges faced
- Celebrate progress

**Concept Discussion (20 min):**
- Clarify tutorial concepts
- Answer mentee questions
- Provide real-world examples

**Hands-On Demo (20 min):**
- Live demonstration of techniques
- Work through an example together
- Show best practices

**Next Week Planning (10 min):**
- Preview next week's topics
- Assign exercises
- Set expectations

---

## 💡 Tips for Each Week

**Week 2:** Help mentee understand *why* different test levels exist - emphasize cost of finding bugs late

**Week 3:** Emphasize exploratory testing - let mentee "break things" and discover edge cases

**Week 4:** NFR testing is often overlooked - show real examples of security breaches, slow apps

**Week 5-6:** Test design techniques feel academic - connect to real ROI (fewer test cases, better coverage)

**Week 7:** Test planning seems tedious - explain how it saves time and manages stakeholder expectations

**Week 8:** 50 test cases is substantial - encourage reuse of templates, consistency in style

**Week 9:** BDD bridges communication gap - show how Given-When-Then clarifies requirements

**Week 10:** Bug reporting is an art - teach empathy (help developers fix it quickly)

**Week 11:** Python can be intimidating - start simple, celebrate small wins

---

## ✅ Quality Gates (Check These Each Week)

- [ ] Mentee completed all exercises
- [ ] Deliverables are professional quality
- [ ] Mentee can explain concepts in their own words
- [ ] GitHub repository updated with new work
- [ ] Progress tracker updated
- [ ] Ready to move to next week

---

## 🎉 Program Completion Criteria

After Week 11, mentee should have:

✅ Complete understanding of QA fundamentals
✅ Systematic testing approach demonstrated
✅ Portfolio-ready GitHub repository
✅ 50+ professional test cases
✅ 10+ professional bug reports
✅ Complete test plan
✅ BDD scenarios
✅ Python test data scripts
✅ Confidence to apply for mid-level QA roles

---

**This program transforms a junior QA into a confident, systematic tester ready for the next level!** 🚀

---

## 📞 For Mentors: Getting Started

1. **Week 1:** Review this summary and the detailed Week 1-2 materials already created
2. **Weeks 2-11:** Use this summary to guide content creation for remaining weeks
3. **Customize:** Adapt examples and exercises to your mentee's industry/interests
4. **Iterate:** Update based on what works and what doesn't
5. **Celebrate:** Recognize progress every week!

---

**Questions? Refer to main README.md for overall program structure.**
