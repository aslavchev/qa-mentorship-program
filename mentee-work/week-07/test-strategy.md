# Test Strategy — SauceDemo

## Document Control

| Field              | Details       |
| ------------------ | ------------- |
| **Project Name**   | SauceDemo     |
| **Document Title** | Test Strategy |
| **Version**        | 1.0           |
| **Author**         | Kamen Asenov  |
| **Created Date**   | 2025-12-13    |
| **Last Updated**   | 2025-12-13    |
| **Status**         | Draft         |

---

## 1. Introduction

### 1.1 Purpose

This Test Strategy document supports and complements the **SauceDemo Test Plan**. While the Test Plan describes *what* will be tested and *when*, this Test Strategy defines *how* testing activities are performed and *which approaches* are used to achieve the test objectives.

### 1.2 Scope

This strategy applies to all testing activities described in the SauceDemo Test Plan, including functional, regression, and exploratory testing of the SauceDemo web application during the QA Fundamentals 11-week program.

### 1.3 Audience

This document is intended for the QA trainee, mentor, and reviewers who need a clear understanding of the testing approach used to execute the SauceDemo Test Plan.

---

## 2. Test Approach

### 2.1 Testing Philosophy

The testing approach is based on risk-based testing, focusing first on critical user flows such as login, cart, and checkout. Scripted test cases are combined with exploratory testing to discover unexpected behavior. Testing is performed continuously during development and learning activities.

### 2.2 Test Cycle

Testing activities include test planning, test design, manual test execution, defect reporting, exploratory testing sessions, and test summary reporting. Feedback from the mentor is used to improve test coverage and strategy.

---

## 3. Test Levels

Unit testing is performed by developers and is out of scope for this strategy. Integration testing focuses on interactions between pages and features such as cart and checkout. System testing covers end-to-end user flows. Acceptance testing validates that the main business flows meet expectations.

---

## 4. Test Types

Functional testing is used to verify that features work as expected. Smoke testing is performed to ensure that critical paths such as login and checkout are working. Regression testing ensures that existing functionality is not broken after changes. Exploratory testing is used regularly to find edge cases, usability issues, and state-related problems. Basic compatibility testing is performed across different browsers and mobile viewports.

---

## 5. Test Design Techniques

Equivalence Partitioning and Boundary Value Analysis are used for input validation, especially in login and checkout forms. Decision tables are applied to checkout logic where applicable. Exploratory testing and error guessing are used to identify unexpected behavior and known problem areas.

---

## 6. Test Automation Strategy

At the current stage of the project, testing is primarily manual, as defined in the SauceDemo Test Plan. The focus is on building strong fundamentals in test design, exploratory testing, and defect analysis. Automation is considered out of scope for this phase and may be introduced later for smoke and regression testing once stable test scenarios are identified.

---

## 7. Defect Management

Defects are documented with clear steps to reproduce, expected and actual results, and severity. Defects are reviewed together with the mentor. Severity levels are classified as Critical, High, Medium, or Low based on impact.

---

## 8. Test Metrics

Basic metrics are tracked, including number of test cases executed, number of defects found, defect severity distribution, and overall test coverage estimation.

---

## 9. Risk Assessment

Login and checkout are considered high-risk areas due to their impact on the user journey. Cart functionality is considered medium risk. UI and visual issues are considered low risk. Testing effort is allocated based on these risk levels.

---

## 10. Quality Gates

Quality gates defined in this strategy are aligned with the entry and exit criteria described in the SauceDemo Test Plan. Testing begins only after the application is accessible and test users are available. Testing is considered complete when all planned tests from the Test Plan are executed, critical defects are documented, and a test summary is reviewed with the mentor.

---

## 11. Continuous Improvement

Test results and mentor feedback are reviewed regularly. The test strategy is updated as new risks are identified and testing skills improve.

---

## 12. Approvals

| Role       | Name        | Date       |
| ---------- | ----------- | ---------- |
| QA Trainee | kamenAsenov | YYYY-MM-DD |
| Mentor     | aslavchev   | YYYY-MM-DD |

---

**Document Version:** 1.0
