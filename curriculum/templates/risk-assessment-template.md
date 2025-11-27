# Risk Assessment Template

## Document Control

| Field | Details |
|-------|---------|
| **Project Name** | [Application/Project Name] |
| **Document Title** | Test Risk Assessment |
| **Version** | 1.0 |
| **Author** | [Your Name] |
| **Created Date** | YYYY-MM-DD |
| **Last Updated** | YYYY-MM-DD |

---

## Purpose

This document identifies, analyzes, and prioritizes risks related to testing activities. It helps the team:
- Identify potential issues before they occur
- Prioritize testing efforts based on risk
- Plan mitigation strategies
- Make informed decisions about test coverage

---

## Risk Assessment Matrix

### Risk Rating Formula

**Risk Level = Probability × Impact**

| Probability | Impact | Risk Level |
|-------------|--------|------------|
| High (3) | High (3) | 9 - Critical |
| High (3) | Medium (2) | 6 - High |
| Medium (2) | High (3) | 6 - High |
| Medium (2) | Medium (2) | 4 - Medium |
| Low (1) | High (3) | 3 - Low |
| Low (1) | Medium (2) | 2 - Low |
| Low (1) | Low (1) | 1 - Low |

### Risk Level Definitions

- **Critical (7-9):** Immediate attention required, high-priority mitigation
- **High (5-6):** Needs mitigation planning, close monitoring
- **Medium (3-4):** Monitor and mitigate if resources available
- **Low (1-2):** Accept and monitor

---

## Identified Risks

### Risk #1: [Risk Title]

| Field | Details |
|-------|---------|
| **Risk ID** | RISK-001 |
| **Risk Title** | Payment gateway integration failure |
| **Category** | Technical |
| **Probability** | Medium (2) |
| **Impact** | High (3) |
| **Risk Level** | High (6) |
| **Owner** | QA Lead |

**Description:**
Third-party payment gateway may fail during high-traffic periods, causing transaction failures and revenue loss.

**Impact if Occurs:**
- Users cannot complete purchases
- Revenue loss estimated at $10K/hour
- Negative user experience and brand damage
- Potential data integrity issues

**Mitigation Strategy:**
- Conduct load testing with payment integration
- Implement fallback to secondary payment provider
- Add comprehensive error handling and logging
- Create monitoring alerts for payment failures
- Test retry mechanism for failed transactions

**Contingency Plan:**
- Have manual payment processing ready
- Communication plan for users
- Rollback to previous stable version if needed

**Current Status:** 🟡 Monitoring

---

### Risk #2: [Risk Title]

| Field | Details |
|-------|---------|
| **Risk ID** | RISK-002 |
| **Risk Title** | Insufficient test coverage due to tight timeline |
| **Category** | Schedule |
| **Probability** | High (3) |
| **Impact** | Medium (2) |
| **Risk Level** | High (6) |
| **Owner** | Test Manager |

**Description:**
Project deadline is aggressive, may not allow complete test coverage of all features, especially edge cases and NFRs.

**Impact if Occurs:**
- Critical bugs may slip to production
- Technical debt accumulates
- Post-release hotfixes required
- Team morale affected

**Mitigation Strategy:**
- Prioritize testing based on risk (risk-based testing)
- Focus on critical user journeys first
- Automate regression tests to save time
- Involve developers in testing (shift-left)
- Conduct exploratory testing sessions
- Use test design techniques for efficient coverage

**Contingency Plan:**
- Negotiate deadline extension if critical gaps found
- Plan phased release with core features first
- Allocate budget for post-release support

**Current Status:** 🔴 Active

---

### Risk #3: [Risk Title]

| Field | Details |
|-------|---------|
| **Risk ID** | RISK-003 |
| **Risk Title** | Test environment instability |
| **Category** | Infrastructure |
| **Probability** | Medium (2) |
| **Impact** | Medium (2) |
| **Risk Level** | Medium (4) |
| **Owner** | DevOps Lead |

**Description:**
Test environment frequently goes down or has configuration drift from production, causing testing delays and unreliable results.

**Impact if Occurs:**
- Testing delays (2-3 days per incident)
- Unreliable test results
- Team idle time
- Missed deadlines

**Mitigation Strategy:**
- Infrastructure as Code (IaC) for environment consistency
- Automated health checks for test environment
- Daily environment validation tests (smoke tests)
- Dedicated DevOps support during test cycles
- Document environment setup for quick recovery
- Maintain backup test environment

**Contingency Plan:**
- Use production mirror for critical testing
- Cloud-based temporary environments
- Test locally with Docker containers

**Current Status:** 🟢 Mitigated

---

### Risk #4: [Risk Title]

| Field | Details |
|-------|---------|
| **Risk ID** | RISK-004 |
| **Risk Title** | Unclear or changing requirements |
| **Category** | Requirements |
| **Probability** | Medium (2) |
| **Impact** | High (3) |
| **Risk Level** | High (6) |
| **Owner** | Product Manager |

**Description:**
Requirements are ambiguous or change frequently during testing, leading to rework and wasted effort.

**Impact if Occurs:**
- Test cases become invalid
- Time wasted on incorrect testing
- Scope creep delays release
- Team frustration and morale issues

**Mitigation Strategy:**
- Conduct thorough requirement reviews before testing
- Use acceptance criteria and examples
- Implement change control process
- Hold daily standups to catch changes early
- Document assumptions and get sign-off
- Use BDD format (Given-When-Then) for clarity

**Contingency Plan:**
- Re-prioritize testing based on stable requirements
- Park unstable features for next release
- Add buffer time for requirement changes

**Current Status:** 🟡 Monitoring

---

### Risk #5: [Risk Title]

| Field | Details |
|-------|---------|
| **Risk ID** | RISK-005 |
| **Risk Title** | Key team member unavailability |
| **Category** | Resource |
| **Probability** | Low (1) |
| **Impact** | Medium (2) |
| **Risk Level** | Low (2) |
| **Owner** | Project Manager |

**Description:**
Critical team members may become unavailable due to illness, resignation, or competing priorities.

**Impact if Occurs:**
- Knowledge loss
- Testing delays
- Quality may suffer
- Need to onboard replacement

**Mitigation Strategy:**
- Cross-train team members
- Document test processes and approach
- Maintain up-to-date test artifacts
- Have backup resources identified
- Knowledge sharing sessions weekly

**Contingency Plan:**
- Activate backup resources
- Extend timeline if critical expertise lost
- Hire contractor for short-term needs

**Current Status:** 🟢 Mitigated

---

## Risk Summary Dashboard

| Risk ID | Risk Title | Category | Probability | Impact | Risk Level | Status |
|---------|------------|----------|-------------|--------|------------|--------|
| RISK-001 | Payment gateway failure | Technical | 2 | 3 | 6 - High | 🟡 Monitoring |
| RISK-002 | Insufficient test coverage | Schedule | 3 | 2 | 6 - High | 🔴 Active |
| RISK-003 | Test environment instability | Infrastructure | 2 | 2 | 4 - Medium | 🟢 Mitigated |
| RISK-004 | Unclear requirements | Requirements | 2 | 3 | 6 - High | 🟡 Monitoring |
| RISK-005 | Team member unavailability | Resource | 1 | 2 | 2 - Low | 🟢 Mitigated |

---

## Risk Heatmap

```
Impact
High  │  [RISK-004]  │  [RISK-001]  │
(3)   │              │              │
      ├──────────────┼──────────────┤
Med   │              │  [RISK-003]  │  [RISK-002]
(2)   │  [RISK-005]  │              │
      ├──────────────┼──────────────┤
Low   │              │              │
(1)   │              │              │
      └──────────────┴──────────────┘
        Low (1)       Med (2)        High (3)
                    Probability
```

---

## Risk Categories

### Technical Risks
- RISK-001: Payment gateway failure (High)
- Browser compatibility issues (TBD)
- Performance degradation under load (TBD)

### Schedule Risks
- RISK-002: Insufficient test coverage (High)
- Late delivery of features (TBD)

### Resource Risks
- RISK-005: Team member unavailability (Low)
- Lack of skilled testers (TBD)

### Requirements Risks
- RISK-004: Unclear requirements (High)
- Scope creep (TBD)

### Infrastructure Risks
- RISK-003: Test environment instability (Medium)
- Production environment differences (TBD)

---

## Risk-Based Test Prioritization

### High-Risk Areas (Test First, Test Most)

| Feature/Module | Risk Level | Reason | Test Priority |
|----------------|-----------|--------|---------------|
| **Payment Processing** | Critical (9) | Revenue impact, external dependency | P0 - Must test |
| **User Authentication** | High (6) | Security, data access control | P0 - Must test |
| **Shopping Cart** | High (6) | Core user journey | P1 - Should test |
| **Checkout Flow** | High (6) | Directly impacts revenue | P1 - Should test |

### Medium-Risk Areas (Test Adequately)

| Feature/Module | Risk Level | Reason | Test Priority |
|----------------|-----------|--------|---------------|
| **Product Search** | Medium (4) | Usability impact | P2 - Test if time |
| **Product Filters** | Medium (4) | Enhancement, not critical | P2 - Test if time |
| **User Profile** | Medium (4) | Low usage frequency | P2 - Test if time |

### Low-Risk Areas (Test Lightly)

| Feature/Module | Risk Level | Reason | Test Priority |
|----------------|-----------|--------|---------------|
| **Footer Links** | Low (2) | Cosmetic, low impact | P3 - Optional |
| **About Us Page** | Low (1) | Static content | P3 - Optional |
| **Social Media Links** | Low (1) | External, no business logic | P3 - Optional |

---

## Monitoring and Review

### Risk Review Schedule

- **Daily:** Review active risks during standup
- **Weekly:** Update risk status and mitigation progress
- **Bi-weekly:** Add new risks identified during testing
- **End of Sprint:** Comprehensive risk review with team

### Risk Status Indicators

- 🟢 **Mitigated:** Risk addressed, low concern
- 🟡 **Monitoring:** Mitigation in progress, watching closely
- 🔴 **Active:** High concern, needs immediate attention
- ⚪ **Accepted:** Risk accepted, no mitigation planned

---

## Lessons Learned (Post-Testing)

### Risks That Materialized
- [Risk ID]: [What happened, impact, how handled]

### Risks That Didn't Occur
- [Risk ID]: [Why mitigation worked or why it didn't happen]

### New Risks Identified
- [New risks discovered during testing that weren't anticipated]

### Recommendations for Future
- [Process improvements based on risk management experience]

---

## Approvals

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **QA Manager** | [Name] | | YYYY-MM-DD |
| **Engineering Manager** | [Name] | | YYYY-MM-DD |
| **Product Manager** | [Name] | | YYYY-MM-DD |
| **Project Manager** | [Name] | | YYYY-MM-DD |

---

## Appendix: Risk Assessment Guidelines

### How to Assess Probability

- **High (3):** Likely to occur (>60% chance)
- **Medium (2):** May occur (30-60% chance)
- **Low (1):** Unlikely to occur (<30% chance)

### How to Assess Impact

- **High (3):** Severe impact on project goals, cost, or timeline
- **Medium (2):** Moderate impact, recoverable with effort
- **Low (1):** Minimal impact, easily managed

### When to Escalate

Escalate risk to management if:
- Risk level is Critical (7-9)
- Mitigation requires resources beyond team control
- Risk impacts project timeline significantly
- Multiple high risks are active simultaneously

---

**Template Version:** 1.0
**Last Updated:** October 2025
