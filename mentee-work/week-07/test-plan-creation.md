# Test Plan — SauceDemo

## Document Control

| Field              | Details     |
| ------------------ | ----------- |
| **Project Name**   | SauceDemo   |
| **Document Title** | Test Plan   |
| **Version**        | 1.0         |
| **Author**         | Kamen Asenov|
| **Created Date**   | 2025-12-13  |
| **Last Updated**   | 2025-12-13  |
| **Status**         | Draft       |

---

## 1. Introduction

### 1.1 Purpose

The purpose of this test plan is to describe the testing approach, scope, resources, and schedule for testing the SauceDemo web application. The document defines how testing activities will be performed to ensure the core functionality works as expected and major risks are covered.

### 1.2 Project Background

SauceDemo is a demo e-commerce web application used for QA training. It allows users to log in, browse products, add items to a cart, and complete a checkout flow. The application is intentionally simplified but contains known issues useful for learning testing techniques.

### 1.3 Document Conventions

High priority refers to critical functionality that must be tested. Medium priority refers to important functionality that should be tested. Low priority refers to optional or cosmetic functionality that will be tested if time allows.

---

## 2. Test Objectives

The main objectives of testing are to validate that the core user flows work correctly, identify functional and usability defects, ensure application stability, and increase confidence in the quality of the application before further training activities.

---

## 3. Scope

### 3.1 In Scope

The following features will be tested:
User authentication (login and logout)
Product inventory page
Product sorting
Shopping cart functionality
Checkout process (information, overview, completion)
Basic UI behavior on desktop and mobile view

### 3.2 Out of Scope

The following areas are not included in this test cycle:
Admin or backend functionality
Real payment processing
Performance and load testing
Accessibility compliance testing

---

## 4. Test Strategy

### 4.1 Test Levels

| Test Level          | Description                    | Responsibility |
| ------------------- | ------------------------------ | -------------- |
| Unit Testing        | Component-level testing        | Developers     |
| Integration Testing | Interaction between components | QA             |
| System Testing      | End-to-end testing             | QA             |
| Acceptance Testing  | Validation of main user flows  | QA + Mentor    |

### 4.2 Test Types

Functional testing will be used to verify features work as expected. Regression testing will ensure existing functionality is not broken. Smoke testing will validate critical paths after changes. Exploratory testing will be used to discover unexpected issues. Compatibility testing will cover different browsers and mobile viewports.

### 4.3 Test Design Techniques

Equivalence Partitioning and Boundary Value Analysis will be used for input fields. Decision tables will be applied to checkout logic. Exploratory testing and error guessing will be used to find edge cases and state-related issues.

---

## 5. Test Environment

### 5.1 Hardware

Testing will be performed on desktop and laptop devices with standard screen resolutions and mobile viewports using browser developer tools.

### 5.2 Software

Browsers used for testing include Chrome, Firefox, and Edge (latest versions). Testing will be documented using Markdown files and GitHub. Defects will be tracked using GitHub Issues if needed.

### 5.3 Test Data

Standard SauceDemo users such as standard_user, locked_out_user, and problem_user will be used. Test data includes all available products and predefined checkout information.

---

## 6. Test Schedule

| Phase               | Duration |
| ------------------- | -------- |
| Test Planning       | 1 day    |
| Test Design         | 2 days   |
| Test Execution      | 3 days   |
| Exploratory Testing | 1 day    |
| Test Summary        | 1 day    |

---

## 7. Resources

Testing activities will be performed by one Junior QA tester with guidance and review from a mentor. No automation resources are planned for this phase.

---

## 8. Risks and Mitigation

| Risk                   | Probability | Impact | Mitigation                              |
| ---------------------- | ----------- | ------ | --------------------------------------- |
| Limited requirements   | Medium      | Medium | Exploratory testing and mentor feedback |
| Known application bugs | High        | Medium | Document and analyze issues clearly     |
| Limited time           | Medium      | Medium | Focus on critical user flows            |

---

## 9. Deliverables

The following artifacts will be produced during testing:
Test Plan document
Exploratory session reports
Test coverage analysis
Bug reports
Test summary notes

---

## 10. Entry and Exit Criteria

### Entry Criteria

Testing starts when the application is accessible, test users are available, and the test environment is stable.

### Exit Criteria

Testing is completed when all planned tests are executed, major defects are documented, and a test summary is prepared.

---

## 11. Suspension and Resumption

Testing may be suspended if the application becomes unavailable or blocking issues prevent further testing. Testing will resume once the environment is stable and blocking issues are resolved.

---

## 12. Approvals

| Role      | Name        | Date       |
| --------- | ----------- | ---------- |
| QA Tester | kamenAsenov | YYYY-MM-DD |
| Mentor    | aslavchev   | YYYY-MM-DD |

---

## Appendix

### Glossary

QA: Quality Assurance
UI: User Interface

### References

SauceDemo application
QA Fundamentals 11-week program
