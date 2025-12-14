# Test Risk Assessment – SauceDemo

## Document Control

| Field              | Details              |
| ------------------ | -------------------- |
| **Project Name**   | SauceDemo            |
| **Document Title** | Test Risk Assessment |
| **Version**        | 1.0                  |
| **Author**         | Kamen Asenov         |
| **Created Date**   | 2025-12-13           |
| **Last Updated**   | 2025-12-13           |

---

## Purpose

This document identifies and evaluates the main testing risks for the SauceDemo application. It supports the Test Plan and Test Strategy by helping prioritize testing based on risk and define mitigation actions.

---

## Risk Rating Model

Risk Level is calculated as:

**Risk Level = Probability × Impact**

* **High (3)**
* **Medium (2)**
* **Low (1)**

---

## Identified Risks

## RISK-001: Login functionality failure

| Field       | Details      |
| ----------- | ------------ |
| Category    | Functional   |
| Probability | High (3)     |
| Impact      | High (3)     |
| Risk Level  | Critical (9) |
| Owner       | QA           |

**Description**
Users may not be able to log in with valid credentials.

**Impact**
Users cannot access the system. Core functionality is blocked.

**Mitigation**
Focus testing on login scenarios, positive and negative cases, error messages, and session handling.

**Status**
🔴 Active

---

## RISK-002: Checkout process issues

| Field       | Details    |
| ----------- | ---------- |
| Category    | Functional |
| Probability | Medium (2) |
| Impact      | High (3)   |
| Risk Level  | High (6)   |
| Owner       | QA         |

**Description**
Users may fail to complete checkout due to validation or flow issues.

**Impact**
Orders cannot be completed, affecting business flow.

**Mitigation**
Test full checkout flow end-to-end with different data sets.

**Status**
🟡 Monitoring

---

## RISK-003: Cart functionality defects

| Field       | Details    |
| ----------- | ---------- |
| Category    | Functional |
| Probability | Medium (2) |
| Impact      | Medium (2) |
| Risk Level  | Medium (4) |
| Owner       | QA         |

**Description**
Adding or removing products from the cart may not work as expected.

**Impact**
Incorrect cart content may confuse users.

**Mitigation**
Perform exploratory and regression testing on cart operations.

**Status**
🟡 Monitoring

---

## RISK-004: Sorting and filtering issues

| Field       | Details    |
| ----------- | ---------- |
| Category    | Usability  |
| Probability | Medium (2) |
| Impact      | Low (1)    |
| Risk Level  | Low (2)    |
| Owner       | QA         |

**Description**
Product sorting or filtering may not work correctly.

**Impact**
User experience degradation but no critical impact.

**Mitigation**
Basic functional testing and exploratory checks.

**Status**
🟢 Mitigated

---

## Risk Summary

| Risk ID  | Area     | Risk Level | Status        |
| -------- | -------- | ---------- | ------------- |
| RISK-001 | Login    | Critical   | 🔴 Active     |
| RISK-002 | Checkout | High       | 🟡 Monitoring |
| RISK-003 | Cart     | Medium     | 🟡 Monitoring |
| RISK-004 | Sorting  | Low        | 🟢 Mitigated  |

---

## Risk-Based Test Prioritization

* **High priority:** Login, Checkout
* **Medium priority:** Cart operations
* **Low priority:** Sorting, filtering, UI elements

This prioritization is aligned with the SauceDemo Test Plan and Test Strategy.

---

## Review and Monitoring

Risks are reviewed during testing sessions and updated when new issues are discovered. High and critical risks are tested first.
