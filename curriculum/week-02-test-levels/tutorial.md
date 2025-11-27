# Week 2: Test Levels

## 🎯 Learning Objectives

By the end of this week, you will be able to:
- Differentiate between Unit, Integration, System, and Acceptance testing
- Understand when each test level is appropriate
- Identify entry and exit criteria for each level
- Map test levels to SDLC phases
- Apply test levels to SauceDemo

---

## 📚 What are Test Levels?

**Test Levels** are groups of test activities that are organized and managed together. Each level targets different aspects of the system and occurs at different times in the SDLC.

Think of it like building a house:
- **Unit Testing** = Testing individual bricks
- **Integration Testing** = Testing how bricks connect to form walls
- **System Testing** = Testing the complete house
- **Acceptance Testing** = Homeowner verifying it meets their needs

---

## 🏗️ Test Level Hierarchy

```
                    Acceptance Testing (End User Perspective)
                            ↑
                    System Testing (Complete System)
                            ↑
                Integration Testing (Components Combined)
                            ↑
                    Unit Testing (Individual Components)
```

---

## 1️⃣ Unit Testing

### Definition
**Unit Testing** validates individual components or units of code in isolation. A "unit" is the smallest testable part - usually a function, method, or class.

### Characteristics
- **Scope:** Single function/method/class
- **Who:** Developers (not typically QA)
- **When:** During development, before code is committed
- **Automation:** Highly automated (99-100%)
- **Dependencies:** Mocked or stubbed

### Example - Unit Test Scenarios

**For a login function `validateCredentials(username, password)`:**

✅ Test 1: Valid username and password returns true
✅ Test 2: Invalid username returns false
✅ Test 3: Invalid password returns false
✅ Test 4: Empty username returns false
✅ Test 5: Empty password returns false
✅ Test 6: SQL injection attempt is handled safely

### Tools
- **Python:** pytest, unittest
- **JavaScript:** Jest, Mocha
- **Java:** JUnit, TestNG
- **C#:** NUnit, xUnit

### Entry Criteria
- [ ] Code written and compiles without errors
- [ ] Unit test framework set up
- [ ] Test data prepared

### Exit Criteria
- [ ] All unit tests pass
- [ ] Code coverage > 80%
- [ ] No critical bugs in unit tests
- [ ] Code reviewed

### SauceDemo Example
If we had access to Sauce Demo's code, unit tests would validate:
- Password encryption function
- Cart calculation logic (total = item price × quantity)
- Form validation functions

---

## 2️⃣ Integration Testing

### Definition
**Integration Testing** validates that different modules or components work correctly together. It tests the interfaces and interactions between integrated units.

### Characteristics
- **Scope:** Multiple components/modules interacting
- **Who:** Developers + QA
- **When:** After unit testing, as modules are integrated
- **Automation:** 60-80% automated
- **Dependencies:** Real or test doubles

### Types of Integration Testing

#### A. Big Bang Integration
- All modules integrated at once
- Test everything together
- **Pro:** Quick to start
- **Con:** Hard to isolate failures

#### B. Incremental Integration
- Modules integrated and tested one at a time
- **Top-Down:** Start with high-level modules, stub lower ones
- **Bottom-Up:** Start with low-level modules, use drivers for higher ones
- **Sandwich:** Combination of top-down and bottom-up

### Example - Integration Test Scenarios

**SauceDemo Integration Tests:**

✅ Test 1: Login system integrates with product catalog (authenticated users see products)
✅ Test 2: Product catalog integrates with shopping cart (adding items updates cart)
✅ Test 3: Shopping cart integrates with checkout (cart items appear in checkout)
✅ Test 4: Checkout integrates with payment gateway (payment processes correctly)
✅ Test 5: Order confirmation integrates with email service (confirmation email sent)

### Tools
- **API Testing:** Postman, REST Assured, requests (Python)
- **Service Integration:** SoapUI, Karate
- **Database:** SQL clients, test data tools

### Entry Criteria
- [ ] Unit testing complete with >80% pass rate
- [ ] Modules to be integrated are available
- [ ] Integration test environment ready
- [ ] Test data for integration scenarios prepared

### Exit Criteria
- [ ] All integration tests executed
- [ ] All high/critical integration defects resolved
- [ ] Integration pass rate > 90%
- [ ] API contracts validated

### SauceDemo Integration Focus Areas
1. **Frontend ↔ Backend:** Login API validates credentials
2. **Cart ↔ Database:** Cart persists across sessions
3. **Checkout ↔ Payment:** Payment gateway integration
4. **UI ↔ API:** All frontend actions call correct API endpoints

---

## 3️⃣ System Testing

### Definition
**System Testing** validates the complete, integrated system against requirements. It tests end-to-end functionality from a user's perspective.

### Characteristics
- **Scope:** Entire application
- **Who:** QA Team
- **When:** After integration testing, before UAT
- **Automation:** 40-60% automated
- **Environment:** Test/QA environment (production-like)

### Types of System Testing

| Type | Purpose | Example |
|------|---------|---------|
| **Functional Testing** | Verify features work | Complete purchase flow |
| **Regression Testing** | Ensure old features still work | Previous release features |
| **Smoke Testing** | Verify critical paths | Login, add to cart, checkout |
| **Sanity Testing** | Quick check of specific area | New payment method |
| **End-to-End Testing** | Complete user journeys | Guest checkout flow |

### Example - System Test Scenarios

**SauceDemo System Tests:**

✅ Test 1: **End-to-End Happy Path** - User logs in, browses products, adds to cart, completes checkout
✅ Test 2: **Cart Functionality** - Add/remove items, update quantities, verify totals
✅ Test 3: **Product Sorting** - Sort by name (A-Z, Z-A), price (low-high, high-low)
✅ Test 4: **Checkout Validation** - Form validates required fields, postal code format
✅ Test 5: **Multi-item Purchase** - Order multiple different products successfully

### Tools
- **Web UI:** Selenium, Cypress, Playwright
- **Mobile:** Appium, XCUITest, Espresso
- **Test Management:** TestRail, Zephyr, qTest

### Entry Criteria
- [ ] Integration testing complete
- [ ] System test environment stable
- [ ] All major features developed
- [ ] Test cases reviewed and approved
- [ ] Test data ready

### Exit Criteria
- [ ] All planned system tests executed (>95%)
- [ ] Pass rate > 90%
- [ ] No open critical defects
- [ ] Regression testing passed
- [ ] Performance benchmarks met

### SauceDemo System Testing Focus
- Complete user workflows (login → browse → cart → checkout → confirmation)
- Cross-browser testing (Chrome, Firefox, Safari)
- UI functionality and usability
- Business logic validation

---

## 4️⃣ Acceptance Testing

### Definition
**Acceptance Testing** validates that the system meets business requirements and is acceptable for delivery. It's done from the customer's or end-user's perspective.

### Characteristics
- **Scope:** Business requirements, user acceptance
- **Who:** Product Owner, Business Users, QA
- **When:** After system testing, before production
- **Automation:** 20-30% automated
- **Environment:** Staging/Pre-production (identical to production)

### Types of Acceptance Testing

#### A. User Acceptance Testing (UAT)
- Performed by actual users
- Validates business requirements
- Real-world scenarios

#### B. Operational Acceptance Testing (OAT)
- Tests operational readiness
- Backup/recovery, security, performance
- Production environment checks

#### C. Contract Acceptance Testing
- Validates against contract terms
- Common in outsourced development

#### D. Alpha/Beta Testing
- **Alpha:** Internal testing by employees
- **Beta:** External testing by real users

### Example - Acceptance Test Scenarios

**SauceDemo UAT Tests:**

✅ Test 1: **Business Goal** - New customer can complete first purchase without assistance in < 5 minutes
✅ Test 2: **Usability** - Product information is clear and helps purchasing decision
✅ Test 3: **Workflow** - Checkout process feels intuitive and trustworthy
✅ Test 4: **Performance** - Application is responsive during peak hours
✅ Test 5: **Confirmation** - Order confirmation provides all necessary information

### Tools
- Often **manual testing** by users
- **Behavior-Driven Development (BDD):** Cucumber, SpecFlow
- **Test Management:** For tracking UAT progress

### Entry Criteria
- [ ] System testing complete
- [ ] All high-priority defects fixed
- [ ] UAT environment ready (production-like)
- [ ] UAT test cases approved by business
- [ ] Users available and trained

### Exit Criteria
- [ ] All UAT scenarios passed
- [ ] Business sign-off received
- [ ] No critical usability issues
- [ ] Acceptance criteria met for all user stories
- [ ] Production deployment checklist complete

### SauceDemo Acceptance Focus
- Can a new user successfully purchase products?
- Does the checkout process inspire confidence?
- Are error messages helpful?
- Is the overall experience satisfactory?

---

## 📊 Test Levels Comparison

| Aspect | Unit | Integration | System | Acceptance |
|--------|------|-------------|--------|------------|
| **Scope** | Single component | Multiple components | Entire system | Business requirements |
| **Responsibility** | Developers | Developers + QA | QA Team | Users + QA |
| **When** | During coding | After units ready | After integration | Before release |
| **Automation %** | 95-100% | 60-80% | 40-60% | 20-30% |
| **Cost to Fix Bug** | $ | $$ | $$$ | $$$$ |
| **Test Data** | Minimal, mocked | Test data sets | Comprehensive | Production-like |
| **Environment** | Local | Dev/QA | QA/Test | Staging/Pre-prod |

---

## 🔄 Test Levels in Different SDLC Models

### Waterfall Model
```
Requirements → Design → Development → Testing → Deployment
                                       ↑
                        Unit → Integration → System → Acceptance
```
All test levels happen in sequence after development.

### Agile/Scrum
```
Sprint 1: Unit → Integration → System → Mini-UAT
Sprint 2: Unit → Integration → System → Mini-UAT
Sprint 3: Unit → Integration → System → Mini-UAT
Release: Full System Testing → Full UAT
```
Test levels happen within each sprint, plus release testing.

### V-Model
```
Requirements ←→ Acceptance Testing
Design ←→ System Testing
Architecture ←→ Integration Testing
Detailed Design ←→ Unit Testing
```
Test levels are planned in parallel with corresponding development phases.

---

## 🎯 When to Focus on Each Level

### Heavy Unit Testing When:
- Complex business logic
- Mathematical calculations
- Data transformations
- Security-critical functions

### Heavy Integration Testing When:
- Microservices architecture
- Many third-party integrations
- API-heavy applications
- Distributed systems

### Heavy System Testing When:
- User-facing applications
- Complex user workflows
- UI-heavy applications
- Critical business processes

### Heavy Acceptance Testing When:
- Customer-facing features
- Compliance requirements
- High business impact
- Major releases

---

## 💡 Best Practices

### 1. Test Pyramid Approach
```
        /\
       /  \      E2E/Acceptance (Few, Expensive)
      /    \
     /      \    System/Integration (More, Moderate Cost)
    /        \
   /__________\  Unit Tests (Many, Cheap)
```

**Principle:** More unit tests, fewer system tests, minimal E2E tests.

**Why:** Lower-level tests are faster, cheaper, and easier to maintain.

### 2. Shift-Left Testing
Test at the lowest appropriate level. Don't wait for system testing to catch unit-level bugs.

### 3. Clear Boundaries
Understand what each level should test. Don't duplicate efforts.

### 4. Entry/Exit Criteria
Always define clear criteria for when to start and stop each level.

---

## 📝 Key Takeaways

1. **Four main test levels:** Unit, Integration, System, Acceptance
2. **Each level has a specific purpose** and tests different aspects
3. **Lower levels are cheaper** - find bugs early
4. **Test pyramid:** Many unit tests, fewer system tests
5. **Different SDLC models** execute test levels differently
6. **QA typically focuses** on Integration, System, and Acceptance levels
7. **Entry/Exit criteria** are crucial for quality gates

---

## 📖 Terminology

| Term | Definition |
|------|------------|
| **Test Level** | Group of test activities organized together |
| **Test Type** | Category of testing (functional, performance, etc.) |
| **Stub** | Dummy component that simulates lower-level modules |
| **Driver** | Component that calls modules being tested |
| **Mock** | Simulated object that mimics real object behavior |
| **Test Double** | Generic term for stubs, mocks, fakes, spies |
| **Regression** | Retesting to ensure existing functionality works |
| **Smoke Test** | Quick test of critical functionality |

---

## 🎓 Further Reading

- ISTQB Foundation Syllabus - Chapter 2 (Testing Throughout SDLC)
- "The Practical Test Pyramid" by Martin Fowler
- "Google Testing Blog" - Testing levels at Google scale

---

## 📝 Self-Assessment

1. What's the difference between Unit and Integration testing?
2. Which test level is most expensive to execute? Why?
3. Who typically performs System Testing?
4. What is Acceptance Testing validating?
5. Explain the Test Pyramid concept.
6. Why test early (shift-left)?
7. What are entry criteria for System Testing?
8. In Agile, when does each test level occur?

---

**Next:** Complete Week 2 exercises to apply test levels to SauceDemo.
