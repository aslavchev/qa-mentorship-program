# Week 10 - Exercise 4: Defect Metrics Dashboard

**Name:** Kamen Asenov  
**Date:** 2026-01-18  
**Reporting Period:** Week 10 Testing Cycle

---

## Executive Summary

**Total Defects Found:** 10  
**Test Cases Executed:** 60 (from Week 8)  
**Defect Density:** 0.17 defects per test case  
**Defect Removal Efficiency (DRE):** 83.3%  
**Defect Leakage:** 16.7%

**Quality Assessment:** ⚠️ Concern  
**Key Finding:** Most defects are medium-severity usability and state issues, with checkout identified as the highest-risk area.

---

## Metric 1: Defect Density

**Formula:**  
Defect Density = Total Defects / Test Cases Executed

**Calculation:**  
10 defects / 60 test cases = **0.17 defects per test case**

**Interpretation:**
- Industry Benchmark (first test cycle): **0.10 – 0.25**
- Our Result: **Within benchmark**
- **Analysis:**  
  The defect density indicates a normal level of issues for a first full exploratory cycle. This suggests decent baseline quality, but also shows that exploratory testing successfully uncovered meaningful problems beyond scripted tests.

---

## Metric 2: Defect Distribution by Severity

| Severity | Count | Percentage | Target Range | Status |
|--------|-------|------------|--------------|--------|
| S1 (Critical) | 0 | 0% | < 10% | ✅ |
| S2 (High) | 1 | 10% | 20–30% | ⚠️ |
| S3 (Medium) | 5 | 50% | 40–50% | ✅ |
| S4 (Low) | 4 | 40% | 20–30% | ⚠️ |
| **Total** | **10** | **100%** | - | - |

**Text Chart:**
- S2 High: ████ 10%  
- S3 Medium: ████████████████ 50%  
- S4 Low: ██████████ 40%

**Analysis:**
- Healthy absence of critical (S1) defects
- High percentage of medium and low issues indicates usability, validation, and state management weaknesses
- Slightly elevated low-severity issues suggest polish gaps rather than functional failures

---

## Metric 3: Defect Distribution by Module

| Module | Count | Percentage | Status |
|------|-------|------------|--------|
| Login | 3 | 30% | Normal |
| Products | 2 | 20% | Normal |
| Cart | 2 | 20% | Normal |
| Checkout | 2 | 20% | ⚠️ Hotspot |
| Cross-cutting | 1 | 10% | Normal |
| **Total** | **10** | **100%** | - |

**Text Chart:**
- Login: ████████ (3)  
- Products: ██████ (2)  
- Cart: ██████ (2)  
- Checkout: ██████ (2) ⚠️  
- Cross-cutting: ███ (1)

**Defect Hotspot:** Checkout (20%)

**Analysis:**
Checkout-related defects involve state validation and navigation, which are high-risk areas in real e-commerce systems. These issues warrant deeper regression and security testing.

---

## Metric 4: Defect Removal Efficiency (DRE)

**Simulated Scenario:**
- Bugs found during testing: 10
- Bugs assumed to escape to production: 2  
  - BUG-003 (Remove without confirmation – UX)
  - BUG-008 (Persistent login error message)

**Total Defects:** 12

**Formula:**  
DRE = (Testing Defects / Total Defects) × 100%

**Calculation:**  
10 / 12 × 100% = **83.3%**

**Target:** 90%+

**Result:** ❌ Below target

**Analysis:**
Lower-severity usability issues are more likely to escape to production. Improving exploratory testing focus on UX and edge cases could raise DRE closer to industry standards.

---

## Metric 5: Defect Leakage

**Formula:**  
Defect Leakage = (Production Defects / Total Defects) × 100%

**Calculation:**  
2 / 12 × 100% = **16.7%**

**Target:** < 10%

**Result:** ❌ Exceeds target

**Escaped Bugs (Simulated):**
1. **BUG-003:** No confirmation on remove – easily overlooked, low impact
2. **BUG-008:** Error message persistence – cosmetic UX issue

**Analysis:**
Leakage is driven mainly by low-priority UX issues, suggesting the need for clearer UX acceptance criteria and explicit exploratory UX sessions.

---

## Metric 6: Defect Age (Not Applicable)

**Note:**  
Defect age metrics cannot be calculated in this exercise because bugs are not tracked across time states (New → Fixed → Closed). In a real project, defect aging would help identify process bottlenecks.

---

## Key Insights

### 1. Overall Quality
SauceDemo shows acceptable functional quality with no critical defects, but has notable usability and state-management gaps.

### 2. Testing Effectiveness
Exploratory testing was effective in finding medium-severity issues, but UX defects are still likely to leak.

### 3. Risk Areas
Checkout is the riskiest module due to state and navigation flaws.

### 4. Recommendations
- Add explicit checkout state validation test cases
- Increase exploratory UX testing sessions
- Add Definition of Done item: “State transitions validated (Back/Refresh/Direct URL)”
- Introduce basic input format validation rules

---

## Metrics Dashboard Summary

| Metric | Value | Target | Status |
|------|-------|--------|--------|
| Defect Density | 0.17 | 0.10–0.25 | ✅ |
| DRE | 83.3% | > 90% | ❌ |
| Defect Leakage | 16.7% | < 10% | ❌ |
| S1 Critical % | 0% | < 10% | ✅ |
| Defect Hotspot | Checkout | Even distribution | ⚠️ |

**Overall Grade:** **B**  
**Justification:** Solid functional quality with room for improvement in UX coverage and preventive testing.

---

## Reflection

**What surprised you about the metrics?**  
That most defects were not functional failures, but UX and state-related issues.

**Which metric is most valuable?**  
Defect Leakage – it clearly shows where testing needs to improve.

**If you were QA Lead, what would you do next?**  
Invest more time in exploratory UX testing and strengthen checkout-related test coverage.
