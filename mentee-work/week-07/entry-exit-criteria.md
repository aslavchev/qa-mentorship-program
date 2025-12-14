# Entry & Exit Criteria – SauceDemo

## Document Control

| Field          | Details               |
| -------------- | --------------------- |
| Project Name   | SauceDemo             |
| Document Title | Entry & Exit Criteria |
| Version        | 1.0                   |
| Author         | Kamen Asenov          |
| Created Date   | 2025-12-14            |
| Last Updated   | 2025-12-14            |
| Status         | Draft                 |

---

## 1. Purpose

This document defines the quality gates for SauceDemo testing. It describes when testing can start (Entry Criteria), when testing can stop (Exit Criteria), and when testing should be suspended or resumed. The criteria are aligned with the Test Plan, Test Strategy, and Risk Assessment.

---

## 2. Entry Criteria

Testing can START when the following conditions are met.

### 2.1 Code and Build Readiness

* Development declares features complete
* Build is deployed to the test environment
* Basic smoke testing is successful
* Application loads correctly
* Login functionality works

### 2.2 Test Readiness

* Test Plan is reviewed and approved
* Test cases are created and reviewed
* Exploratory test charters prepared
* Test data is available and validated
* Test environment is configured and stable

### 2.3 Documentation

* Requirements are finalized and approved
* Known issues list is shared
* Test environment access is documented

### 2.4 Resources

* QA tester assigned and available
* Required tools are accessible
* No blocking issues from previous sprint

### Entry Checklist (Example)

* Build deployed to test environment
* Smoke test passed (login and inventory page)
* Test cases created for login, cart, and checkout
* Test data reset and verified
* QA has access to the environment
* Test Plan approved
* No critical open defects from previous iteration

---

## 3. Exit Criteria

Testing can STOP when the following conditions are met.

### 3.1 Test Execution

* 100% of critical test cases executed
* At least 95% of all planned test cases executed
* All planned exploratory sessions completed
* Blocked tests resolved or officially deferred

### 3.2 Quality Metrics

* Test pass rate is at least 95%
* Requirements coverage is at least 95%
* Regression test suite executed successfully

### 3.3 Defect Metrics

* Zero Critical (Severity 1) defects open
* Maximum 1–2 High (Severity 2) defects open and accepted by Product Owner
* All must-fix defects resolved

### 3.4 Documentation

* Test Summary Report completed
* All defects logged and updated in tracking tool
* Known issues list updated
* Stakeholder approval received

### Exit Checklist (Example)

* Test cases executed: 148/150 (99%)
* Test pass rate: 96%
* Requirements coverage: 96%
* Critical defects open: 0
* High defects open: 1 (accepted)
* Regression suite passed
* Test summary report published
* Product Owner sign-off received

---

## 4. Suspension and Resumption Criteria

### 4.1 Suspension Criteria

Testing will be SUSPENDED if any of the following occur:

* More than 30% of test cases are blocked
* Test environment is unavailable for more than 4 hours
* Critical defect makes the application unusable
* Build cannot be deployed or tested
* Major requirement or scope change

### 4.2 Resumption Criteria

Testing will RESUME when:

* Blocking defects are fixed
* Test environment is restored and validated
* New stable build is deployed
* Test cases are updated if requirements changed

---

## 5. Relation to Other Test Documents

* Test Plan: Defines overall scope and objectives
* Test Strategy: Defines testing approach and quality goals
* Risk Assessment: Defines high-risk areas that must meet stricter exit criteria
