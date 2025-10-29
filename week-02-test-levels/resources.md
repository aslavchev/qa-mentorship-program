# Week 2: Test Levels - Resources

## 🎥 Essential Videos

1. **Software Test Levels Explained**
   - Search: "Software test levels unit integration system acceptance"
   - Duration: 15-20 minutes
   - Topics: Overview of all four levels
   - Why watch: Visual explanation with examples

2. **The Test Pyramid**
   - Search: "Test pyramid Martin Fowler"
   - Duration: 10 minutes
   - Topics: Why pyramid shape, automation distribution
   - Why watch: Industry-standard concept

3. **Integration Testing Best Practices**
   - Search: "Integration testing best practices"
   - Duration: 12-15 minutes
   - Topics: Top-down, bottom-up, big bang approaches
   - Why watch: Practical integration strategies

4. **System Testing vs UAT**
   - Search: "Difference between system testing and UAT"
   - Duration: 8-10 minutes
   - Topics: When each happens, who does it
   - Why watch: Clear differentiation

---

## 📖 Reading Materials

### Essential Reading

1. **ISTQB Syllabus - Chapter 2**
   - URL: https://www.istqb.org/
   - Topic: Testing Throughout the SDLC
   - Time: 45-60 minutes
   - Why read: Official test level definitions

2. **Martin Fowler's Test Pyramid**
   - URL: https://martinfowler.com/articles/practical-test-pyramid.html
   - Time: 20 minutes
   - Why read: Authoritative source on test pyramid concept

3. **Google Testing Blog - Test Sizes**
   - URL: https://testing.googleblog.com/
   - Search: "Test sizes at Google"
   - Time: 15 minutes
   - Why read: How Google categorizes tests

### Supplementary Reading

4. **Integration Testing Patterns**
   - URL: https://www.guru99.com/integration-testing.html
   - Time: 15 minutes
   - Why read: Detailed integration approaches

5. **User Acceptance Testing Guide**
   - URL: https://www.softwaretestinghelp.com/user-acceptance-testing-uat/
   - Time: 20 minutes
   - Why read: UAT process and best practices

---

## 🔧 Tools

### Test Management (for organizing test levels)

1. **TestRail** (Free trial)
   - URL: https://www.gurock.com/testrail/
   - Purpose: Organize test cases by level
   - Why use: Industry-standard test management

2. **Zephyr** (Free version)
   - URL: https://www.getzephyr.com/
   - Purpose: Test case management for Jira
   - Why use: Integrates with development workflow

### Documentation Tools

3. **Miro** (Free)
   - URL: https://miro.com/
   - Purpose: Create test level diagrams
   - Why use: Collaborative visual boards

4. **Lucidchart** (Free tier)
   - URL: https://www.lucidchart.com/
   - Purpose: Draw test pyramid, flowcharts
   - Why use: Professional diagramming tool

---

## 📚 Books (Chapters)

1. **"Software Testing" by Ron Patton**
   - Chapters 3-4: Test levels and approaches
   - Level: Beginner-friendly
   - Why read: Clear explanations with examples

2. **"Agile Testing" by Lisa Crispin**
   - Chapter on Agile test levels
   - Level: Intermediate
   - Why read: Test levels in Agile context

---

## 🌐 Practice & Examples

### Test Level Examples

1. **GitHub - Sample Test Suites**
   - Search: "sample test suite unit integration system"
   - Look for: Open-source projects with clear test organization
   - Why explore: See real-world test level organization

2. **TestProject Examples**
   - URL: https://testproject.io/
   - Free test examples for different levels
   - Why use: Hands-on examples

---

## 🎓 Certifications Alignment

### ISTQB Foundation Level

Week 2 content aligns with:
- **Chapter 2:** Testing Throughout the SDLC
  - 2.1: Test levels
  - 2.2: Test types
  - 2.3: Maintenance testing

If preparing for ISTQB, focus on:
- Definitions of each test level
- Entry/exit criteria
- Test objects for each level
- Typical defects found at each level

---

## 📝 Templates

### Available in templates/ folder:

1. **test-case-template.md**
   - Use for: Writing test scenarios at any level

2. **test-plan-template.md**
   - Section on: Test levels and approach

---

## 🔍 Research Topics

### Optional Deep Dives

1. **How does Google/Facebook/Netflix organize testing?**
   - Research their engineering blogs
   - Look for test level strategies
   - Compare to traditional approaches

2. **Test Levels in Microservices**
   - How are test levels different?
   - Contract testing as integration level
   - Service-level vs system-level testing

3. **AI/ML Testing Levels**
   - Are test levels different for AI systems?
   - Data testing, model testing, system testing

---

## 💬 Community Discussion

### Questions to Ask in Communities

1. **Ministry of Testing Forum**
   - "How do you decide test level for a scenario?"
   - "What's your team's test pyramid look like?"

2. **Reddit r/QualityAssurance**
   - "How much unit testing should QA verify?"
   - "When is integration testing enough?"

---

## 🎯 Practice Exercises Beyond Curriculum

### Additional Practice

1. **Analyze an Open-Source Project**
   - Pick a project on GitHub
   - Examine their test organization
   - Document how they structure test levels

2. **Create Test Pyramid for Different Apps**
   - E-commerce site
   - Mobile game
   - Banking app
   - Social media platform
   - How would pyramid differ?

---

## ⏱️ Suggested Study Schedule

### Day 1-2: Theory
- Read tutorial.md
- Read ISTQB Chapter 2
- Watch test pyramid videos
- Take notes

### Day 3-4: Deep Dive
- Read Martin Fowler's article
- Watch integration testing videos
- Research Google's approach
- Practice identifying test levels

### Day 5-6: Practice
- Complete all exercises
- Write integration scenarios
- Write system scenarios
- Create test matrix

### Day 7: Documentation & Review
- Finalize all deliverables
- Review concepts
- Prepare for mentor session

---

## ❓ FAQ

### Q: Can I skip unit testing if I'm not a developer?
**A:** Understand unit testing concepts even if you don't write unit tests. You'll collaborate with developers and review their unit tests.

### Q: How much integration testing is enough?
**A:** Test all integration points. If Component A talks to Component B, test that interaction.

### Q: Should I do system testing if integration testing passed?
**A:** Yes! Integration tests component pairs. System testing tests end-to-end workflows that may involve multiple integrations.

### Q: What if my company doesn't follow this model?
**A:** Many companies have their own terminology. Understand the concepts - you can adapt to any naming.

---

## 🔗 Quick Reference Links

| Resource | Type | Time | Priority |
|----------|------|------|----------|
| ISTQB Chapter 2 | Reading | 45 min | ⭐⭐⭐ Must |
| Test Pyramid (Fowler) | Article | 20 min | ⭐⭐⭐ Must |
| Test Levels Video | Video | 15 min | ⭐⭐⭐ Must |
| Integration Testing | Video | 12 min | ⭐⭐ Should |
| Google Testing Blog | Reading | 15 min | ⭐ Optional |

---

## 📌 Key Takeaways to Remember

1. **Four main levels:** Unit → Integration → System → Acceptance
2. **Test Pyramid:** Many unit tests, fewer system tests, minimal E2E
3. **Each level has purpose:** Different scope, cost, responsibility
4. **Entry/Exit criteria:** Clear gates between levels
5. **Shift-left:** Test early and often at lower levels

---

**Happy Learning!** 🚀
