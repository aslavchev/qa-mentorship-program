# Week 10 - Exercise 1: Find Bugs in SauceDemo

**Your Name:** Kamen Asenov  
**Date:** 2026-01-18  
**Total Bugs Found:** 10

---

## Testing Summary

**Testing Duration:** ~2 hours  
**Modules Tested:** Login, Products, Cart, Checkout, Cross-cutting  
**Users Tested:** standard_user, problem_user, performance_glitch_user  
**Browsers Tested:** Chrome (macOS)  
**Tools Used:** Chrome DevTools (Console/Network), Device Toolbar (mobile emulation)

---

## Bug Discovery Log

### BUG-001: Checkout pages accessible directly (empty-cart checkout possible)
- **Module:** Checkout / Security / State management
- **Discovered via:** Cross-cutting testing → Direct URL access while logged in with empty cart
- **Reproducible:** Yes (100%)
- **Affects user(s):** All logged-in users
- **Quick notes:** User can open `/checkout-step-one.html` directly without initiating checkout or having items; app does not enforce cart-state preconditions.

---

### BUG-002: Zip/Postal Code accepts letters (no format validation)
- **Module:** Checkout
- **Discovered via:** Checkout form validation testing (invalid zip formats)
- **Reproducible:** Yes (100%)
- **Affects user(s):** All users
- **Quick notes:** Zip field accepts alphabetic input like `ABCDE` and still allows continuation to Overview.

---

### BUG-003: Remove item has no confirmation/undo
- **Module:** Cart
- **Discovered via:** Cart negative flow / UX testing (accidental click scenarios)
- **Reproducible:** Yes (100%)
- **Affects user(s):** All users
- **Quick notes:** Clicking Remove deletes item immediately; no confirmation dialog or undo action.

---

### BUG-004: Sort dropdown label does not match initial product order
- **Module:** Products / Sorting
- **Discovered via:** Products module exploratory testing (sorting verification on first load)
- **Reproducible:** Sometimes (observed in session; verify again across refresh/login)
- **Affects user(s):** standard_user (likely all)
- **Quick notes:** Dropdown shows default "Name (A to Z)" but list on initial load appears inconsistent with strict A→Z ordering.

---

### BUG-005: Cart badge overlaps icon on mobile viewport
- **Module:** Cart / UI
- **Discovered via:** Responsive testing (Chrome DevTools mobile emulation)
- **Reproducible:** Yes (100% on narrow viewport with multiple items)
- **Affects user(s):** All users on small screens
- **Quick notes:** Badge overlaps cart icon on mobile width (e.g., iPhone 12 ~390px), reducing readability/click accuracy.

---

### BUG-006: problem_user product images are incorrect/mismatched
- **Module:** Products
- **Discovered via:** Special user exploratory testing → `problem_user` product display verification
- **Reproducible:** Yes (100% for problem_user)
- **Affects user(s):** problem_user
- **Quick notes:** Product images do not match product titles (misleading product representation).

---

### BUG-007: Browser Back after completion may allow re-triggering finish flow
- **Module:** Checkout / Completion
- **Discovered via:** Checkout end-to-end flow + browser navigation testing (Back behavior)
- **Reproducible:** Sometimes (needs confirmation with repeated runs; potentially navigation-only vs re-submit)
- **Affects user(s):** All users
- **Quick notes:** After order completion, using browser Back may allow revisiting checkout steps; potential idempotency/state risk in real systems.

---

### BUG-008: Login error message persists while user edits inputs
- **Module:** Login
- **Discovered via:** Invalid login testing (UX/validation behavior after failure)
- **Reproducible:** Yes (100%)
- **Affects user(s):** All users
- **Quick notes:** Error banner remains visible while editing username/password; clears only after next submit.

---

### BUG-009: performance_glitch_user login takes very long with no loading feedback
- **Module:** Login / Performance
- **Discovered via:** Special user testing → `performance_glitch_user` response time observation
- **Reproducible:** Yes (observed consistently for this user)
- **Affects user(s):** performance_glitch_user
- **Quick notes:** Login takes significantly longer vs standard_user; no spinner/disabled button leading to “app frozen” perception.

---

### BUG-010: Keyboard accessibility focus indicator is unclear on interactive controls
- **Module:** Cross-cutting / Accessibility
- **Discovered via:** Accessibility testing (keyboard-only navigation with Tab/Shift+Tab)
- **Reproducible:** Sometimes (depends on control/background)
- **Affects user(s):** Keyboard-only users (all)
- **Quick notes:** Focus indicator is weak/inconsistent on some interactive elements, making keyboard navigation difficult.

---

## Testing Notes

**Modules with most bugs:** Checkout + Products (state/validation + display/sorting)  
**Most common bug type:** UI/UX + validation/state management  
**Hardest bug to find:** BUG-007 (needs strong evidence to confirm true “re-trigger” vs navigation only)  
**Easiest bug to find:** BUG-002 (straightforward invalid input validation check)

**What I learned:**
- Exploratory testing finds gaps beyond happy path (URL manipulation, back button behavior, mobile UI).
- Special users (`problem_user`, `performance_glitch_user`) quickly surface meaningful issues.
- Good defect notes = exact user, exact page, exact data, and clear expected vs actual.
