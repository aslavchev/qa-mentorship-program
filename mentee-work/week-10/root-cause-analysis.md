# Week 10 - Exercise 5: Root Cause Analysis

**Name:** Kamen Asenov  
**Date:** 2026-01-18  
**Bugs Analyzed:** 3

---

## RCA Summary

| Bug ID | Summary | Root Cause Category | Preventive Action |
|------|--------|--------------------|------------------|
| BUG-001 | Checkout pages accessible directly without cart | State management / Validation gap | Enforce preconditions for checkout flow |
| BUG-007 | Browser Back allows re-entering checkout flow | State handling / Idempotency | Block re-submission and stale navigation |
| BUG-009 | Slow login for performance_glitch_user without feedback | UX / Performance handling | Add loading states and response time checks |

---

## RCA #1: BUG-001 – Checkout pages accessible directly (empty-cart checkout possible)

### Problem Statement
Checkout step pages can be accessed directly via URL even when the cart is empty, allowing invalid checkout flow entry.

### 5 Whys Analysis

1. **Why can the user access checkout without items?**  
   → Checkout pages do not verify cart state on load.

2. **Why is cart state not verified?**  
   → Page access is based only on authentication, not business preconditions.

3. **Why were business preconditions not enforced?**  
   → Checkout flow was implemented assuming navigation only happens via Cart page.

4. **Why was this assumption made?**  
   → Direct URL access and state manipulation were not considered during implementation.

5. **Why was this scenario not detected earlier?**  
   → No test cases or DoD items covered direct URL access or invalid state entry.

### Root Cause
**Root Cause:** Missing state validation for checkout flow entry.

**Category:** Testing Gap / State Management

### How It Escaped Testing
- Test cases focused on happy-path checkout from cart page.
- No negative or security-oriented test cases for direct URL access.
- Exploratory testing initially focused on UI interactions, not URL manipulation.

### Corrective Actions (Fix This Bug)
1. Validate cart state before allowing access to any checkout step.
2. Redirect users with empty cart to inventory or cart page.
3. Add server-side validation for checkout flow entry.
4. Re-test checkout flow across browsers.

### Preventive Actions (Prevent Future Bugs)

**Testing Improvements:**
- Add test case: “Verify checkout pages cannot be accessed with empty cart”
- Add exploratory checklist item: “Test direct URL access to protected pages”

**Development Process Improvements:**
- Add DoD item: “All flows validate required state on entry”
- Include negative flow review in code reviews

**Quality Process Improvements:**
- Expand security/state validation coverage
- Add checklist for URL manipulation scenarios

### Lessons Learned
- Never assume users follow intended navigation paths
- State validation must be enforced, not implied
- Security and state issues often hide outside happy paths

---

## RCA #2: BUG-007 – Browser Back after completion may allow re-triggering finish flow

### Problem Statement
After completing checkout, using browser Back may allow access to previous checkout pages, creating a risk of re-triggering completion actions.

### 5 Whys Analysis

1. **Why can the user navigate back after completion?**  
   → Browser history still contains checkout pages.

2. **Why does navigating back expose checkout pages?**  
   → Application does not invalidate checkout session after completion.

3. **Why is checkout session not invalidated?**  
   → Completion logic focuses on success page rendering, not session cleanup.

4. **Why was session cleanup not implemented?**  
   → Idempotency and back-navigation scenarios were not considered.

5. **Why were these scenarios missed?**  
   → No test cases for browser navigation behavior after order completion.

### Root Cause
**Root Cause:** Missing handling of post-completion state and browser navigation.

**Category:** Code Quality / State Management

### How It Escaped Testing
- Testing focused on successful completion only.
- Browser navigation behavior was not part of acceptance criteria.
- Assumption that users would continue forward, not backward.

### Corrective Actions (Fix This Bug)
1. Invalidate checkout session after completion.
2. Prevent access to checkout pages once order is finished.
3. Redirect stale navigation to inventory page.
4. Verify behavior using browser Back/Forward buttons.

### Preventive Actions (Prevent Future Bugs)

**Testing Improvements:**
- Add test case: “Verify checkout cannot be re-entered after completion”
- Include browser navigation tests in checkout regression suite

**Development Process Improvements:**
- Add DoD item: “Idempotency verified for critical actions”
- Require session/state cleanup review for completion flows

**Quality Process Improvements:**
- Add exploratory checklist: “Test browser Back/Refresh behavior”
- Include state-reset validation in sprint reviews

### Lessons Learned
- Browser navigation is part of user behavior, not an edge case
- Completion flows must be idempotent
- State cleanup is as important as success logic

---

## RCA #3: BUG-009 – performance_glitch_user login is very slow with no loading feedback

### Problem Statement
Login for performance_glitch_user takes significantly longer than normal with no loading indicator or disabled state, causing poor user experience.

### 5 Whys Analysis

1. **Why does login feel slow?**  
   → Backend response is delayed for this user.

2. **Why does the UI feel unresponsive during delay?**  
   → No loading indicator or button disable is implemented.

3. **Why was no loading state implemented?**  
   → UI assumed fast response times.

4. **Why was this assumption made?**  
   → Performance edge cases were not tested during development.

5. **Why weren’t performance scenarios tested earlier?**  
   → Performance testing was not part of regular QA checks.

### Root Cause
**Root Cause:** Missing UX handling for slow responses and lack of performance testing.

**Category:** UX / Performance Testing Gap

### How It Escaped Testing
- Focus was on functional correctness, not response times.
- No performance-related acceptance criteria.
- No user feedback mechanisms tested under delay conditions.

### Corrective Actions (Fix This Bug)
1. Add loading spinner during login request.
2. Disable login button while request is pending.
3. Add timeout handling and user feedback.
4. Re-test with simulated slow responses.

### Preventive Actions (Prevent Future Bugs)

**Testing Improvements:**
- Add test case: “Verify loading indicator shown during slow login”
- Add performance exploratory sessions

**Development Process Improvements:**
- Define acceptable response time thresholds
- Add DoD item: “Loading states implemented for async actions”

**Quality Process Improvements:**
- Include performance checks in QA cycles
- Track response times during testing

### Lessons Learned
- Perceived performance is as important as actual performance
- Users need feedback during delays
- Performance testing should be part of functional testing

---

## Pattern Analysis

### Common Root Causes
**Most common category:** State Management / Testing Gap (2 of 3 bugs)

### Systemic Issues Identified
1. Missing validation of state transitions
2. Over-reliance on happy-path assumptions
3. Insufficient exploratory coverage for navigation and performance

### Shared Preventive Actions
- Expand negative and exploratory test coverage
- Strengthen Definition of Done for state and navigation handling
- Add UX and performance considerations to QA checklists

---

## Recommendations to Development Team

### Immediate Actions (This Sprint)
1. Fix checkout state validation (BUG-001)
2. Prevent re-entry into checkout after completion (BUG-007)

### Short-Term Actions (Next 2 Sprints)
1. Improve loading states and UX feedback
2. Expand regression coverage for checkout flows
3. Add browser navigation testing to QA process

### Long-Term Actions (Next Quarter)
1. Introduce formal state management standards
2. Add performance testing to CI pipeline
3. Train team on negative-flow and idempotency risks

---

## Reflection

**What was most surprising about this RCA?**  
That many issues stem from assumptions about user behavior rather than code complexity.

**Which root cause category is most common?**  
State management and testing gaps.

**How does RCA differ from just fixing bugs?**  
RCA focuses on preventing entire classes of bugs, not just resolving individual issues.

**What preventive action would have the biggest impact?**  
Expanding exploratory testing to include state, navigation, and performance scenarios.
