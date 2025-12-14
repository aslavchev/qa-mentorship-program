# Resource Estimation – SauceDemo

## Document Control

| Field              | Details             |
| ------------------ | ------------------- |
| **Project Name**   | SauceDemo           |
| **Document Title** | Resource Estimation |
| **Version**        | 1.0                 |
| **Author**         | Kamen Asenov        |
| **Created Date**   | 2025-12-14          |
| **Last Updated**   | 2025-12-14          |
| **Status**         | Draft               |

---

## Purpose

This document estimates the testing effort, time, and resources needed for testing the SauceDemo application. The estimation is based on the Test Plan, Test Strategy, and Risk Assessment documents.

---

## Scope of Estimation

The estimation covers the following testing activities:

* Test planning and preparation
* Test case design
* Manual test execution
* Exploratory testing
* Defect retesting and regression testing
* Test reporting and closure

Automation effort is considered limited and not part of the main estimation.

---

## Assumptions

* SauceDemo is a demo web application with limited scope
* Requirements are mostly stable
* Testing is focused on core user flows (login, cart, checkout)
* One Junior QA is responsible for execution
* Test environment is stable and available

---

## Test Activities and Effort Estimation

| Activity              | Description                              | Estimated Effort |
| --------------------- | ---------------------------------------- | ---------------- |
| Test Planning         | Review requirements, Test Plan, Strategy | 2 hours          |
| Test Case Design      | Create manual test cases                 | 6 hours          |
| Test Data Preparation | Prepare users and data                   | 1 hour           |
| Test Execution        | Execute functional test cases            | 8 hours          |
| Exploratory Testing   | Exploratory sessions (cart, checkout)    | 4 hours          |
| Defect Retesting      | Verify fixed defects                     | 3 hours          |
| Regression Testing    | Re-run core test cases                   | 4 hours          |
| Test Reporting        | Test summary and metrics                 | 2 hours          |

**Total Estimated Effort:** **30 hours**

---

## Resource Allocation

| Role               | Number of Resources | Responsibility         | Allocation |
| ------------------ | ------------------- | ---------------------- | ---------- |
| Junior QA Engineer | 1                   | All testing activities | 100%       |
| Mentor / Reviewer  | 1                   | Review and feedback    | As needed  |

---

## Test Schedule (High-Level)

| Day   | Activities                                     |
| ----- | ---------------------------------------------- |
| Day 1 | Test planning and test case design             |
| Day 2 | Test execution (login, products, cart)         |
| Day 3 | Test execution (checkout), exploratory testing |
| Day 4 | Defect retesting and regression testing        |
| Day 5 | Test reporting and closure                     |

---

## Risk Impact on Estimation

| Risk                 | Impact on Effort  | Mitigation          |
| -------------------- | ----------------- | ------------------- |
| Unclear requirements | Additional rework | Early clarification |
| Environment issues   | Testing delays    | Flexible schedule   |
| Limited experience   | Slower execution  | Mentor support      |

---

## Estimation Confidence

* **Confidence Level:** Medium
* Estimation may change if new features or risks are introduced
* Buffer of 10–15% may be required if issues occur

---

## Conclusion

The estimated effort for testing SauceDemo is approximately **30 hours**, performed by **one Junior QA Engineer**. This estimation supports a risk-based testing approach and aligns with the overall Test Plan and Test Strategy.
