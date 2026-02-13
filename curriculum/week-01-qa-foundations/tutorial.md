# 🎯 About This Program's Structure

This 11-week QA Fundamentals program has **TWO intentional phases** designed to build different skillsets:

---

## Phase 1: Weeks 1-5 - "Learn to Learn" 🔍

### What You'll Notice:
- ✅ Curriculum provides core concepts and frameworks
- ⚠️ Exercises are less prescriptive (fewer step-by-step instructions)
- ⚠️ You'll need to research, Google, and figure things out
- ⚠️ Templates and examples are minimal

### Why This Design:
**Real QA work involves incomplete requirements.** Product specs are vague. Documentation is outdated. Requirements change mid-sprint. These weeks build your **research and self-sufficiency skills**.

If you have theoretical knowledge (ISTQB, CS degree, bootcamp) but lack hands-on practice, this phase helps you bridge theory to application **the way real QA work happens**.

### Your Job in Weeks 1-5:
- 🔍 Don't expect step-by-step instructions for every detail
- 🔍 Google: "examples of decision tables for testing"
- 🔍 Find test case templates online
- 🔍 Ask yourself: "What would 'good' look like for this exercise?"
- 🔍 Research best practices and industry standards

**This is intentionally challenging.** The struggle builds skill. Stick with it.

### Skills You're Building:
- Self-sufficiency (figure things out independently)
- Research ability (find answers when docs are incomplete)
- Critical thinking (decide what "good enough" means)
- Adaptability (work with ambiguity)

---

## Phase 2: Weeks 6-11 - "Learn to Execute" 🚀

### What You'll Notice:
- ✅ Curriculum becomes comprehensive and detailed
- ✅ Exercises have specific deliverables ("write 60 test cases")
- ✅ Clear templates, examples, and step-by-step guides provided
- ✅ Standards are higher, expectations are explicit

### Why This Design:
**Once you've proven you can figure things out, we raise the bar.** These weeks simulate **FAANG-level expectations**: detailed requirements, professional output, high quality standards, portfolio-ready work.

This is where companies assess: "Can you execute at scale?" Not just "can you write A test case" but "can you create a comprehensive test suite with 60+ cases, proper structure, and full traceability?"

### Your Job in Weeks 6-11:
- 📋 Follow detailed instructions carefully
- 📋 Meet specific criteria (test case counts, formats, coverage targets)
- 📋 Produce portfolio-ready, professional-quality work
- 📋 Apply all the research skills you built in weeks 1-5

**This is where you demonstrate readiness for mid-level QA roles.**

### Skills You're Building:
- Execution at scale (large test suites, comprehensive documentation)
- Professional standards (industry-quality output)
- Systematic thinking (structured approaches to complex problems)
- Portfolio building (GitHub-ready work samples)

---

## The Progression is Intentional 📈

```
Weeks 1-5: Research → Figure Out → Apply
Weeks 6-11: Execute → Deliver → Master
```

**Both phases are necessary.**

- ❌ Don't skip weeks 1-5 thinking they're "less important"
- ❌ Don't get frustrated if weeks 1-5 feel harder (that's the point)
- ✅ Trust the process - the struggle in weeks 1-5 makes weeks 6-11 easier
- ✅ By week 11, you'll have both self-sufficiency AND execution skills

---

## What to Expect Week by Week

| Week | Phase | Style | What You'll Feel |
|------|-------|-------|------------------|
| 1-2 | Learn to Learn | Sparse | "I have to research a lot" |
| 3-5 | Learn to Learn | Sparse | "Getting better at finding answers" |
| **6** | **Transition** | **Comprehensive** | **"Oh, now it's detailed!"** |
| 7-9 | Learn to Execute | Comprehensive | "Clear expectations, high bar" |
| 10-11 | Learn to Execute | Comprehensive | "Portfolio-ready work" |

---

## For Mentors Using This Curriculum

**If you're a mentor:** Explain this two-phase structure to your mentee upfront. It prevents early frustration and helps them understand why weeks 1-5 require more independent research.

**If you're self-studying:** Don't interpret sparse curriculum as "low quality." It's intentional. Use it as practice for real-world QA where requirements are always incomplete.

---

**Ready? Let's begin Week 1!** 🚀

---

# Week 1: QA Foundations & SDLC

## 🎯 Learning Objectives

By the end of this week, you will be able to:
- Explain the role and importance of QA in software development
- Understand different SDLC models and where QA fits
- Define quality and quality attributes
- Identify QA activities throughout the software development lifecycle
- Understand the difference between QA, QC, and Testing

---

## 📚 What is Quality Assurance?

### Definition

**Quality Assurance (QA)** is a systematic process of ensuring that a product or service meets specified requirements and customer expectations. It's a **proactive** approach focused on preventing defects rather than just finding them.

### QA vs QC vs Testing

| Aspect | Quality Assurance (QA) | Quality Control (QC) | Testing |
|--------|------------------------|----------------------|---------|
| **Focus** | Process-oriented | Product-oriented | Product-oriented |
| **Approach** | Proactive (Prevention) | Reactive (Detection) | Reactive (Detection) |
| **Scope** | Entire SDLC | Specific deliverables | Specific features |
| **Goal** | Prevent defects | Identify defects | Find defects |
| **Activities** | Process improvement, standards, audits | Reviews, inspections, testing | Test execution, bug reporting |
| **Example** | Implement code reviews | Code review execution | Execute test cases |

**Remember:** QA prevents problems, QC detects problems, Testing validates functionality.

---

## 🎯 The Role of QA in Software Development

### Why QA Matters

1. **Cost Savings:** Finding bugs early is 10-100x cheaper than fixing them in production
2. **Customer Satisfaction:** Higher quality = happier customers = better retention
3. **Brand Reputation:** Quality products build trust and brand loyalty
4. **Risk Mitigation:** Identify risks before they become critical issues
5. **Compliance:** Meet regulatory and industry standards

### The QA Engineer's Responsibilities

#### Primary Responsibilities
- 📝 Review requirements and specifications
- 🧪 Design and execute test cases
- 🐛 Identify, document, and track defects
- 📊 Report on quality metrics and test progress
- 🔍 Perform exploratory testing
- 🤝 Collaborate with developers, product owners, and stakeholders
- 📚 Maintain test documentation and artifacts
- 🔄 Participate in Agile ceremonies (standup, retrospectives, planning)

#### Skills Required
- **Technical:** Testing techniques, tools, basic coding
- **Analytical:** Problem-solving, critical thinking, attention to detail
- **Communication:** Clear bug reports, status updates, collaboration
- **Domain Knowledge:** Understanding business requirements and user needs
- **Automation:** (Advanced) Test automation frameworks and scripting

---

## 🔄 Software Development Life Cycle (SDLC)

### What is SDLC?

SDLC is a structured process for developing software, from initial concept to deployment and maintenance. Different models exist, each with unique approaches to development and testing.

---

### 1. Waterfall Model

```
Requirements → Design → Implementation → Testing → Deployment → Maintenance
```

**Characteristics:**
- Linear and sequential
- Each phase must be completed before the next begins
- Heavy documentation
- Testing happens after implementation

**QA Role:**
- Requirements review (early phase)
- Test planning during design phase
- Test execution after development complete
- Acceptance testing before deployment

**Pros:**
- ✅ Clear structure and milestones
- ✅ Well-documented
- ✅ Works well for small, well-defined projects

**Cons:**
- ❌ Inflexible to changes
- ❌ Late defect detection
- ❌ Customer sees product late in cycle
- ❌ High risk if requirements misunderstood

**Best For:** Projects with stable, well-understood requirements (e.g., government projects, medical devices)

---

### 2. Agile Model (Scrum)

```
Sprint Planning → Daily Standup → Development → Testing → Sprint Review → Retrospective
                        ↑_____________________________________________↓
                                    (Repeat every 2-4 weeks)
```

**Characteristics:**
- Iterative and incremental
- Short development cycles (sprints)
- Continuous feedback
- Cross-functional teams
- Testing integrated throughout

**QA Role:**
- Participate in sprint planning
- Define acceptance criteria
- Test during sprint (shift-left testing)
- Automated regression testing
- Collaborate daily with developers
- Demo in sprint review

**Pros:**
- ✅ Flexible to changes
- ✅ Early and continuous testing
- ✅ Frequent customer feedback
- ✅ Fast defect detection

**Cons:**
- ❌ Requires discipline and collaboration
- ❌ Less documentation
- ❌ Can be challenging to estimate timelines
- ❌ Requires skilled, self-organizing team

**Best For:** Projects with evolving requirements, need for rapid delivery (e.g., web apps, startups, SaaS products)

---

### 3. V-Model (Verification and Validation)

```
Requirements ←→ Acceptance Testing
     ↓                    ↑
Design ←→ System Testing
     ↓                    ↑
Architecture ←→ Integration Testing
     ↓                    ↑
Detailed Design ←→ Unit Testing
     ↓                    ↑
         Implementation
```

**Characteristics:**
- Extension of Waterfall
- Testing activities defined in parallel with development
- Each development phase has corresponding test phase
- Emphasis on verification and validation

**QA Role:**
- Define acceptance tests during requirements
- Define system tests during design
- Define integration tests during architecture
- Execute tests on right side of V

**Pros:**
- ✅ Testing planned early
- ✅ Clear test milestones
- ✅ Good traceability (requirements → tests)
- ✅ High quality outputs

**Cons:**
- ❌ Inflexible like Waterfall
- ❌ No early prototypes
- ❌ Late risk discovery
- ❌ Expensive to make changes

**Best For:** Safety-critical systems, regulated industries (e.g., aerospace, automotive, medical)

---

### 4. Spiral Model

```
    Plan → Risk Analysis → Engineering → Evaluation →
     ↑____________________________________________↓
                  (Repeat in spirals)
```

**Characteristics:**
- Risk-driven
- Multiple iterations (spirals)
- Prototyping and risk assessment each iteration
- Combines Waterfall and iterative approaches

**QA Role:**
- Risk assessment in each spiral
- Test prototypes early
- Focus testing on high-risk areas
- Continuous testing throughout spirals

**Pros:**
- ✅ Good for large, complex projects
- ✅ Risk management built-in
- ✅ Customer can see prototypes
- ✅ Changes accommodated

**Cons:**
- ❌ Complex to manage
- ❌ Expensive
- ❌ Requires risk expertise
- ❌ May spiral indefinitely

**Best For:** Large, high-risk projects (e.g., enterprise systems, government projects)

---

### 5. DevOps / Continuous Delivery

```
Plan → Code → Build → Test → Release → Deploy → Operate → Monitor
 ↑_______________________________________________________________↓
                        (Continuous Loop)
```

**Characteristics:**
- Automation-heavy
- Continuous integration and deployment
- Infrastructure as code
- Collaboration between Dev and Ops
- Fast feedback loops

**QA Role:**
- Automate tests (unit, integration, E2E)
- Shift-left testing (test early)
- Continuous testing in CI/CD pipeline
- Monitor production (shift-right testing)
- Performance and security testing automated

**Pros:**
- ✅ Fast delivery to production
- ✅ High automation
- ✅ Quick feedback
- ✅ Reduced manual effort

**Cons:**
- ❌ Requires significant automation investment
- ❌ Cultural shift needed
- ❌ Complex toolchain
- ❌ Not all testing can be automated

**Best For:** Modern web apps, SaaS, microservices, cloud-native applications

---

## 🎯 Quality Attributes

Quality is multi-dimensional. Software quality includes:

### Functional Quality

**Definition:** Does the software do what it's supposed to do?

- **Correctness:** Accurate results for given inputs
- **Completeness:** All requirements implemented
- **Compliance:** Meets standards and regulations

### Non-Functional Quality

**Definition:** How well does the software perform its functions?

| Attribute | Description | Example Test |
|-----------|-------------|--------------|
| **Performance** | Speed, responsiveness, throughput | Page loads in <2 seconds |
| **Reliability** | System uptime, failure rate | 99.9% uptime (3 nines) |
| **Usability** | Ease of use, user satisfaction | New user completes task without help |
| **Security** | Protection from threats | Login prevents SQL injection |
| **Maintainability** | Ease of modifying code | Add new feature in 2 days |
| **Scalability** | Handle growth in users/data | Support 10,000 concurrent users |
| **Portability** | Works across platforms | Runs on Windows, macOS, Linux |
| **Compatibility** | Works with other systems | Integrates with Stripe API |

**ISO 25010 Quality Model** defines 8 main quality characteristics - research this for deeper understanding!

---

## 🧪 QA Activities Throughout SDLC

### Phase 1: Requirements

**QA Activities:**
- ✅ Review requirements for completeness, clarity, testability
- ✅ Identify ambiguities and missing details
- ✅ Participate in requirement workshops
- ✅ Define acceptance criteria
- ✅ Create high-level test plan

**Questions QA Asks:**
- Is the requirement clear and unambiguous?
- Is it testable? How will we verify it?
- Are there edge cases or exceptions?
- What's the expected behavior for invalid inputs?

---

### Phase 2: Design

**QA Activities:**
- ✅ Review design documents
- ✅ Identify testability concerns
- ✅ Create test strategy
- ✅ Design test cases for major flows
- ✅ Plan test data needs
- ✅ Identify test environments needed

**Questions QA Asks:**
- How will this design be tested?
- Are there integration points that need testing?
- What are the failure scenarios?
- Do we need test doubles (mocks, stubs)?

---

### Phase 3: Development

**QA Activities:**
- ✅ Create detailed test cases
- ✅ Prepare test data
- ✅ Set up test environments
- ✅ Develop automated tests (if applicable)
- ✅ Perform smoke tests on builds
- ✅ Collaborate with developers on testability

**Questions QA Asks:**
- Are unit tests being written?
- Can we test this feature in isolation?
- What logs/diagnostics will help debugging?

---

### Phase 4: Testing

**QA Activities:**
- ✅ Execute test cases
- ✅ Log and track defects
- ✅ Perform exploratory testing
- ✅ Regression testing
- ✅ Retest fixed bugs
- ✅ Report test progress and quality metrics

**Questions QA Asks:**
- Have all test cases been executed?
- Are there any high-priority defects?
- Is regression testing complete?
- Are we ready for release?

---

### Phase 5: Deployment

**QA Activities:**
- ✅ Validate deployment in staging
- ✅ Smoke test production deployment
- ✅ Monitor production for issues
- ✅ Validate rollback plan works
- ✅ Document release notes

**Questions QA Asks:**
- Is staging identical to production?
- Have we tested the deployment process?
- Are rollback procedures tested?

---

### Phase 6: Maintenance

**QA Activities:**
- ✅ Monitor production defects
- ✅ Test hotfixes
- ✅ Update regression test suite
- ✅ Analyze defect trends
- ✅ Process improvement

**Questions QA Asks:**
- Why did defects escape to production?
- How can we prevent similar issues?
- Should we add new test coverage?

---

## 🏆 Best Practices for QA

### 1. Shift-Left Testing
**Definition:** Test early in the SDLC, not just at the end.

**Benefits:**
- Find defects when they're cheapest to fix
- Influence design for testability
- Reduce rework

**How:** Participate in requirements review, pair with developers, write tests early

---

### 2. Risk-Based Testing
**Definition:** Prioritize testing based on risk (probability × impact).

**Benefits:**
- Optimize limited testing time
- Focus on critical functionality first
- Better ROI on testing effort

**How:** Identify high-risk areas (payment, security, core flows) and test thoroughly

---

### 3. Continuous Improvement
**Definition:** Regularly review and improve testing processes.

**Benefits:**
- Increase efficiency
- Learn from past mistakes
- Adapt to new technologies

**How:** Conduct retrospectives, track metrics, experiment with new techniques

---

### 4. Collaboration
**Definition:** Work closely with developers, product, and stakeholders.

**Benefits:**
- Better understanding of requirements
- Faster defect resolution
- Shared quality ownership

**How:** Daily standups, pair testing, clear communication

---

## 💡 Key Takeaways

1. **QA is preventive, QC is detective** - QA focuses on processes, QC on products
2. **Different SDLC models require different QA approaches** - Agile vs Waterfall testing is very different
3. **Quality has multiple dimensions** - Functional and non-functional
4. **QA is involved throughout SDLC** - Not just during "testing phase"
5. **Early testing saves money** - The cost of fixing defects increases exponentially over time
6. **Communication is key** - QA must collaborate with the entire team

---

## 📖 Terminology to Remember

| Term | Definition |
|------|------------|
| **Defect** | A flaw in the product that causes incorrect results |
| **Bug** | Same as defect (informal term) |
| **Failure** | Deviation from expected behavior |
| **Error** | Human action that introduces a defect |
| **Verification** | "Are we building the product right?" (process check) |
| **Validation** | "Are we building the right product?" (product check) |
| **Test Case** | A set of conditions to verify a requirement |
| **Test Plan** | Document describing testing approach and scope |
| **Regression** | Retesting to ensure existing functionality still works |

---

## 🎓 Further Reading

- ISTQB Foundation Level Syllabus (Chapter 1 & 2)
- "The Art of Software Testing" by Glenford Myers (Chapter 1)
- "Agile Testing" by Lisa Crispin and Janet Gregory
- IEEE 829 - Standard for Software Test Documentation
- ISO/IEC 25010 - Software Quality Model

---

## 📝 Self-Assessment Questions

Test your understanding:

1. What is the difference between QA, QC, and Testing?
2. Name 3 SDLC models and when each is most appropriate
3. List 5 non-functional quality attributes
4. What does "shift-left testing" mean?
5. Why is QA involved in the requirements phase?
6. What's the difference between verification and validation?
7. Name 3 QA activities in the development phase
8. Why is early defect detection important?

If you can answer these confidently, you're ready for the exercises!

---

**Next:** Complete Week 1 exercises to apply these concepts to SauceDemo.
