# Week 1: Exercises

## 🎯 Exercise Overview

These hands-on exercises will help you apply Week 1 concepts to real-world scenarios, specifically using **SauceDemo** as your test application.

**Total Estimated Time:** 3-4 hours

---

## Exercise 1: QA vs QC vs Testing (30 minutes)

### Objective
Clearly differentiate between QA, QC, and Testing with real examples.

### Instructions

**Part A: Create a Comparison Chart**

Create a table comparing QA, QC, and Testing:

| Aspect | QA (Quality Assurance) | QC (Quality Control) | Testing |
|--------|------------------------|----------------------|---------|
| Definition | | | |
| Focus | | | |
| Approach | | | |
| Timing | | | |
| Responsibility | | | |
| Example Activity | | | |

**Part B: Real-World Examples**

For each category, provide 3 real-world examples:

**QA Examples:**
1.
2.
3.

**QC Examples:**
1.
2.
3.

**Testing Examples:**
1.
2.
3.

**Part C: Scenario Classification**

Classify each scenario as QA, QC, or Testing:

1. __ Executing test cases for the login feature
2. __ Establishing coding standards for the development team
3. __ Conducting code reviews before merging pull requests
4. __ Running automated regression tests
5. __ Creating a checklist for deployment process
6. __ Reporting a bug found during test execution
7. __ Implementing a peer review process
8. __ Validating that requirements are testable

### Deliverable
Save as `mentee-work/week-01/qa-qc-testing-comparison.md`

---

## Exercise 2: SDLC Model Comparison (45 minutes)

### Objective
Understand when different SDLC models are appropriate and how QA's role changes.

### Instructions

**Part A: SDLC Comparison Matrix**

Fill out this comparison matrix for 4 SDLC models:

| Criteria | Waterfall | Agile | V-Model | DevOps |
|----------|-----------|-------|---------|--------|
| **Best suited for** | | | | |
| **Project size** | | | | |
| **Requirement stability** | | | | |
| **Customer involvement** | | | | |
| **When testing occurs** | | | | |
| **Documentation level** | | | | |
| **Flexibility to change** | | | | |
| **Risk level** | | | | |

**Part B: QA Role by Model**

For each SDLC model, describe QA's role:

**Waterfall:**
- Key activities:
- Challenges:
- When QA is most active:

**Agile:**
- Key activities:
- Challenges:
- When QA is most active:

**V-Model:**
- Key activities:
- Challenges:
- When QA is most active:

**DevOps:**
- Key activities:
- Challenges:
- When QA is most active:

**Part C: Scenario Matching**

Match each project to the most appropriate SDLC model and justify:

1. A startup building a new social media app with evolving features
   - **Best Model:**
   - **Justification:**

2. A medical device with strict regulatory requirements
   - **Best Model:**
   - **Justification:**

3. A government contract with fixed requirements and timeline
   - **Best Model:**
   - **Justification:**

4. A SaaS product requiring weekly releases
   - **Best Model:**
   - **Justification:**

### Deliverable
Save as `mentee-work/week-01/sdlc-comparison.md`

---

## Exercise 3: SauceDemo Application Analysis (90 minutes)

### Objective
Thoroughly explore the SauceDemo application and document its features, preparing for future testing.

### Instructions

**Part A: Application Exploration**

1. Navigate to https://www.saucedemo.com/
2. Login with username: `standard_user`, password: `secret_sauce`
3. Explore every page, button, link, and feature
4. Take notes on what you discover

**Part B: Feature Map**

Create a comprehensive feature map of SauceDemo. You can use:
- Mind map (XMind, Coggle, draw.io)
- Hierarchical list
- Flowchart

**Example Structure:**
```
SauceDemo E-Commerce Application
├── Authentication
│   ├── Login
│   ├── Logout
│   └── User Roles
├── Product Catalog
│   ├── Product Grid
│   ├── Product Details
│   ├── Sorting
│   └── Filtering
├── Shopping Cart
│   ├── Add Items
│   ├── Remove Items
│   └── View Cart
├── Checkout Process
│   ├── Checkout Information
│   ├── Checkout Overview
│   └── Checkout Complete
└── [Continue mapping all features...]
```

**Part C: User Workflows**

Document the main user workflows (user journeys):

1. **Happy Path - Complete Purchase:**
   - Step 1:
   - Step 2:
   - Step 3:
   - [...continue]

2. **Browse Products:**
   - Step 1:
   - Step 2:
   - [...continue]

3. **Manage Cart:**
   - Step 1:
   - Step 2:
   - [...continue]

**Part D: Functional Requirements**

Based on your exploration, document 10 functional requirements:

**Example Format:**
- **REQ-001:** User shall be able to login with valid credentials
- **REQ-002:** User shall see error message for invalid credentials
- **REQ-003:** User shall be able to view all products on the catalog page

**Your Requirements:**
1. REQ-001:
2. REQ-002:
3. REQ-003:
4. REQ-004:
5. REQ-005:
6. REQ-006:
7. REQ-007:
8. REQ-008:
9. REQ-009:
10. REQ-010:

**Part E: Non-Functional Requirements**

Identify 5 non-functional requirements (NFRs) for SauceDemo:

1. **Performance:**
2. **Usability:**
3. **Security:**
4. **Compatibility:**
5. **Accessibility:**

**Part F: Initial Observations**

Document your initial observations:

**Strengths (what works well):**
-
-
-

**Potential Issues (things that seem odd or broken):**
-
-
-

**User Experience Notes:**
-
-
-

### Deliverable
Save as `mentee-work/week-01/saucedemo-analysis.md` (include feature map as image or embedded link)

---

## Exercise 4: Quality Attributes Analysis (30 minutes)

### Objective
Apply quality attribute knowledge to SauceDemo.

### Instructions

**Part A: Categorize Quality Attributes**

Categorize these quality concerns for SauceDemo as Functional (F) or Non-Functional (NF):

1. __ User can add items to cart
2. __ Page loads within 2 seconds
3. __ Application works on Chrome, Firefox, Safari
4. __ User receives order confirmation
5. __ Password is masked during entry
6. __ Application is available 99% of the time
7. __ New users can complete purchase without help
8. __ Product sorting works correctly
9. __ Application supports 1000 concurrent users
10. __ Checkout form validates required fields

**Part B: NFR Checklist for SauceDemo**

Create a checklist of non-functional requirements to test:

**Performance:**
- [ ] Page load time < X seconds
- [ ] Product images load quickly
- [ ] Sorting/filtering responsive
- [ ] Add more...

**Security:**
- [ ] Password not visible in plain text
- [ ] Session expires after inactivity
- [ ] Add more...

**Usability:**
- [ ] Clear navigation
- [ ] Error messages are helpful
- [ ] Add more...

**Compatibility:**
- [ ] Works on Chrome
- [ ] Works on Firefox
- [ ] Works on mobile devices
- [ ] Add more...

**Accessibility:**
- [ ] Screen reader compatible
- [ ] Keyboard navigation works
- [ ] Add more...

**Part C: Prioritization**

If you had limited time, prioritize these areas for testing (1 = highest priority):

| Area | Priority | Justification |
|------|----------|---------------|
| Login/Authentication | | |
| Product Catalog | | |
| Shopping Cart | | |
| Checkout Process | | |
| Sorting/Filtering | | |
| Product Details | | |

### Deliverable
Save as `mentee-work/week-01/quality-attributes.md`

---

## Exercise 5: SDLC Activities Mapping (30 minutes)

### Objective
Understand QA's role throughout the SDLC.

### Instructions

**Part A: Activity Mapping**

For a fictional SauceDemo v2.0 project using **Agile/Scrum**, map QA activities to SDLC phases:

**Sprint Planning Phase:**

QA Activities:
1.
2.
3.

**Development Phase (During Sprint):**

QA Activities:
1.
2.
3.

**Testing Phase (During Sprint):**

QA Activities:
1.
2.
3.

**Sprint Review:**

QA Activities:
1.
2.

**Sprint Retrospective:**

QA Activities:
1.
2.

**Part B: Shift-Left Example**

Provide 3 examples of how QA can "shift left" in the SauceDemo project:

1. **Instead of:** Testing login after development complete
   **Shift-left to:**

2. **Instead of:** Finding usability issues during testing
   **Shift-left to:**

3. **Instead of:** Discovering missing requirements during testing
   **Shift-left to:**

**Part C: Reflection Questions**

Answer these questions based on your learning:

1. **Why is QA involved in requirements phase?**
   - Your answer:

2. **What happens if QA only tests at the end of development?**
   - Your answer:

3. **How does early QA involvement save money?**
   - Your answer:

4. **What questions should QA ask during design phase?**
   - Your answer:

### Deliverable
Save as `mentee-work/week-01/sdlc-activities.md`

---

## 🎯 Bonus Exercise (Optional): Real-World Research

### Objective
Connect learning to industry practices.

### Instructions

1. **Research a Famous Software Failure**
   - Find a real-world example (e.g., Therac-25, Mars Climate Orbiter, Knight Capital)
   - Analyze: What went wrong from a QA perspective?
   - What SDLC model was likely used?
   - How could better QA have prevented it?

2. **Interview a QA Professional** (if possible)
   - Ask about their typical day
   - What SDLC model do they use?
   - What's the biggest challenge in their QA role?
   - What advice do they have for junior QA engineers?

### Deliverable
Save as `mentee-work/week-01/bonus-research.md`

---

## ✅ Exercise Completion Checklist

- [ ] Exercise 1: QA vs QC vs Testing - Completed
- [ ] Exercise 2: SDLC Comparison - Completed
- [ ] Exercise 3: SauceDemo Analysis - Completed (most important!)
- [ ] Exercise 4: Quality Attributes - Completed
- [ ] Exercise 5: SDLC Activities Mapping - Completed
- [ ] All deliverables saved in `mentee-work/week-01/` folder
- [ ] All files committed to GitHub
- [ ] Ready to discuss in mentor session

---

## 📤 Submission

1. Create folder structure: `mentee-work/week-01/`
2. Save all deliverables as markdown files
3. Commit to GitHub with meaningful commit message:
   ```
   Week 1 exercises complete: QA foundations and SauceDemo analysis
   ```
4. Share repository link with mentor
5. Be prepared to walk through your work in mentor session

---

## 💡 Tips for Success

- **Take your time with SauceDemo exploration** - this is the foundation for all future weeks
- **Be thorough with documentation** - you'll reference this later
- **Ask questions** - if anything is unclear, note it for your mentor session
- **Think like a user** - when exploring SauceDemo, imagine you're a real customer
- **Have fun!** - Exploration and learning should be enjoyable

---

**Good luck with your exercises! Remember: The goal is learning, not perfection.** 🚀
