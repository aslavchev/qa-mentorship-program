# Week 10 - Exercise 2: Professional Bug Reports

**Name:** Kamen Asenov  
**Date:** 2026-01-18  
**Total Bug Reports:** 10

---

## Bug Report Index

| Bug ID | Summary | Module | Severity | Priority |
|--------|---------|--------|----------|----------|
| BUG-001 | Checkout step pages accessible directly (empty-cart checkout possible) | Checkout / Security | S2 | P1 |
| BUG-002 | Zip/Postal Code accepts letters (no format validation) | Checkout | S3 | P2 |
| BUG-003 | Remove item has no confirmation/undo | Cart | S4 | P3 |
| BUG-004 | Sort dropdown label does not match initial product order | Products | S3 | P2 |
| BUG-005 | Cart badge overlaps icon on mobile viewport | Cart / UI | S3 | P2 |
| BUG-006 | problem_user: product images are incorrect/mismatched | Products | S3 | P2 |
| BUG-007 | Browser Back after completion may allow re-triggering finish flow | Checkout | S3 | P2 |
| BUG-008 | Login error message persists while user edits inputs | Login | S4 | P3 |
| BUG-009 | performance_glitch_user: login takes very long with no loading feedback | Login / Performance | S3 | P2 |
| BUG-010 | Keyboard accessibility: weak/unclear focus indication on interactive controls | Cross-cutting / Accessibility | S4 | P3 |

---

## BUG-001: Checkout pages accessible directly (empty-cart checkout possible)

**Bug ID:** BUG-001  
**Reported by:** Kamen Asenov  
**Date:** 2026-01-18  
**Module:** Checkout / Security / State management

### Summary
[Checkout] Direct URL access allows entering checkout flow without items in cart

### Description
A user can navigate directly to checkout step pages via URL (e.g. `checkout-step-one.html`) without initiating checkout from the cart. This can allow a checkout flow to start with an empty cart, which is a state management risk and could lead to invalid orders in a real system.

### Steps to Reproduce
1. Login as `standard_user` / `secret_sauce`
2. Ensure cart is empty (do not add products)
3. In the browser address bar, open: `https://www.saucedemo.com/checkout-step-one.html`
4. Fill the form with any values and click **Continue**
5. Observe the checkout flow behavior (overview/finish availability)

### Actual Result
- User can access checkout step pages directly via URL even when cart is empty.
- App may allow progress in checkout flow without validating cart state first.

### Expected Result
- App should block checkout when cart is empty (redirect to cart/inventory with message).
- Checkout steps should require valid preconditions (cart has items and checkout initiated from cart).

### Environment
- **OS:** macOS  
- **Browser:** Chrome (latest)  
- **Resolution:** 1920x1080  
- **URL:** https://www.saucedemo.com/checkout-step-one.html  
- **Date/Time Tested:** 2026-01-18  

### Severity & Priority
**Severity:** S2 (High)  
**Priority:** P1 (High)

### Preconditions
- User is logged in
- Cart is empty

### Test Data
- Any names/zip

### Attachments
- Screenshot: `bug_001_1.png` 

### Additional Notes
- This is a state validation issue. In real e-commerce, this could enable invalid order creation or inconsistent order totals.

---

## BUG-002: Zip/Postal Code accepts letters (no format validation)

**Bug ID:** BUG-002  
**Reported by:** Kamen Asenov  
**Date:** 2026-01-18  
**Module:** Checkout  

### Summary
[Checkout] Zip/Postal Code allows alphabetic input (no validation)

### Description
Checkout accepts non-numeric zip/postal codes such as "ABCDE". This reduces data quality and suggests missing input validation.

### Steps to Reproduce
1. Login as `standard_user` / `secret_sauce`
2. Add any product to cart → Cart → **Checkout**
3. Enter First Name: `Test`
4. Enter Last Name: `User`
5. Enter Zip/Postal Code: `ABCDE`
6. Click **Continue**

### Actual Result
- User proceeds to Overview page without validation error.

### Expected Result
- Validation error should appear (zip format invalid), and user should remain on the form.

### Environment
- **OS:** macOS
- **Browser:** Chrome (latest)
- **Resolution:** 1920x1080
- **URL:** https://www.saucedemo.com/checkout-step-one.html
- **Date/Time:** 2026-01-18

### Severity & Priority
**Severity:** S3 (Medium)  
**Priority:** P2 (Medium)

### Preconditions
- Logged in
- At least one item in cart

### Test Data
- **Zip:** ABCDE

### Attachments
- Screenshot: `bug_002_1.png`
- Screenshot (result/overview): `bug_002_2.png`

---

## BUG-003: Remove item has no confirmation/undo (accidental removal risk)

**Bug ID:** BUG-003  
**Reported by:** Kamen Asenov  
**Date:** 2026-01-18  
**Module:** Cart  

### Summary
[Cart] Removing item has no confirmation or undo

### Description
Clicking "Remove" instantly removes the item without confirmation or undo. This is a usability risk because users can accidentally remove items.

### Steps to Reproduce
1. Login as `standard_user` / `secret_sauce`
2. Add any item to cart
3. Open cart page
4. Click **Remove** for the item

### Actual Result
- Item is removed immediately.

### Expected Result
- Confirmation prompt or undo option should exist (usability improvement).

### Environment
- **OS:** macOS
- **Browser:** Chrome (latest)
- **Resolution:** 1920x1080
- **URL:** https://www.saucedemo.com/cart.html
- **Date/Time:** 2026-01-18

### Severity & Priority
**Severity:** S4 (Low)  
**Priority:** P3 (Low)

### Preconditions
- At least one item in cart

### Test Data
- Any product

### Attachments
- Screenshot (cart with item): `bug_003_1.png`
- Screenshot (after removal): `bug_003_2.png`

---

## BUG-004: Sort dropdown label does not match initial product order

**Bug ID:** BUG-004  
**Reported by:** Kamen Asenov  
**Date:** 2026-01-18  
**Module:** Products / Sorting  

### Summary
[Products] Sort dropdown shows "Name (A to Z)" but initial list order is inconsistent

### Description
After login, the sort dropdown indicates "Name (A to Z)" but the product list on initial load appears not strictly sorted. This creates inconsistency between UI state and actual data order.

### Steps to Reproduce
1. Login as `standard_user` / `secret_sauce`
2. On inventory page, observe the sort dropdown label
3. Verify the product list order visually (A→Z)

### Actual Result
- Dropdown label suggests A→Z, but list order does not always match.

### Expected Result
- Product list order should match the selected sort option.

### Environment
- **OS:** macOS
- **Browser:** Chrome (latest)
- **Resolution:** 1920x1080
- **URL:** https://www.saucedemo.com/inventory.html
- **Date/Time:** 2026-01-18

### Severity & Priority
**Severity:** S3 (Medium)  
**Priority:** P2 (Medium)

### Preconditions
- Logged in as standard_user

### Attachments
- Screenshot (dropdown shows A→Z): `bug_004_1.png`
- Screenshot (after selecting different sort): `bug_004_2.png`

---

## BUG-005: Cart badge overlaps icon on mobile viewport

**Bug ID:** BUG-005  
**Reported by:** Kamen Asenov  
**Date:** 2026-01-18  
**Module:** Cart / UI  

### Summary
[UI] Cart badge overlaps cart icon on small screens

### Description
On narrow/mobile viewport, the cart badge overlaps the cart icon making it hard to read and click. This impacts usability on mobile devices.

### Steps to Reproduce
1. Login as `standard_user` / `secret_sauce`
2. Open DevTools → toggle device toolbar
3. Set viewport to mobile (e.g., iPhone 12 / width ~390)
4. Add multiple items to cart (3+)
5. Observe cart badge position

### Actual Result
- Badge overlaps the cart icon.

### Expected Result
- Badge should be readable and not overlap other UI elements.

### Environment
- **OS:** macOS
- **Browser:** Chrome (latest)
- **Resolution:** Mobile viewport (e.g., 390x844)
- **URL:** https://www.saucedemo.com/inventory.html
- **Date/Time:** 2026-01-18

### Severity & Priority
**Severity:** S3 (Medium)  
**Priority:** P2 (Medium)

### Preconditions
- Logged in
- Multiple items added

### Attachments
- Screenshot: `bug_005_1.png`

---

## BUG-006: problem_user shows incorrect/mismatched product images

**Bug ID:** BUG-006  
**Reported by:** Kamen Asenov  
**Date:** 2026-01-18  
**Module:** Products

### Summary
[Products] problem_user product images do not match the correct products

### Description
When logged in as `problem_user`, product images are mismatched (image displayed does not correspond to the product). This is misleading for users and breaks a core shopping experience expectation (product identification).

### Steps to Reproduce
1. Login as `problem_user` / `secret_sauce`
2. Open inventory page: https://www.saucedemo.com/inventory.html
3. Compare product titles with their images (e.g., Backpack vs displayed image)
4. Optionally open a product details page and compare again

### Actual Result
- One or more products show incorrect images (mismatch between title and image).

### Expected Result
- Each product card should display the correct image for that product.

### Environment
- **OS:** macOS  
- **Browser:** Chrome (latest)  
- **Resolution:** 1920x1080  
- **URL:** https://www.saucedemo.com/inventory.html  
- **Date/Time:** 2026-01-18  

### Severity & Priority
**Severity:** S3 (Medium)  
**Priority:** P2 (Medium)

### Preconditions
- Login as `problem_user`

### Test Data
- **User:** problem_user / secret_sauce

### Attachments
- Screenshot: `bug_006_1.png`

---

## BUG-007: Browser Back after completion may allow re-triggering finish flow

**Bug ID:** BUG-007  
**Reported by:** Kamen Asenov  
**Date:** 2026-01-18  
**Module:** Checkout / Completion  

### Summary
[Checkout] Browser Back after completion can re-enter finishing flow (idempotency risk)

### Description
After completing an order, using browser Back may allow the user to revisit previous checkout pages and potentially re-trigger completion actions. This is a state/idempotency risk.

### Steps to Reproduce
1. Login as `standard_user` / `secret_sauce`
2. Add any item → checkout → finish order
3. On confirmation page, press browser **Back**
4. Observe whether user can access checkout pages or trigger finish again

### Actual Result
- User may re-enter checkout steps or re-trigger completion state.

### Expected Result
- App should prevent re-submission and redirect safely (e.g., to inventory).

### Environment
- **OS:** macOS
- **Browser:** Chrome (latest)
- **Resolution:** 1920x1080
- **URL:** https://www.saucedemo.com/checkout-complete.html
- **Date/Time:** 2026-01-18

### Severity & Priority
**Severity:** S3 (Medium)  
**Priority:** P2 (Medium)

### Preconditions
- Order completed

### Attachments
- Screenshot: `bug_007_1.png`

---

## BUG-008: Login error message persists while user edits inputs

**Bug ID:** BUG-008  
**Reported by:** Kamen Asenov  
**Date:** 2026-01-18  
**Module:** Login  

### Summary
[Login] Error message remains visible while user edits credentials

### Description
After a failed login attempt, the error message remains visible even while the user edits the username/password. This is minor but may confuse the user.

### Steps to Reproduce
1. Open https://www.saucedemo.com
2. Enter username: `wrong_user`
3. Enter password: `wrong_pass`
4. Click **Login**
5. Start typing in username/password fields

### Actual Result
- Error message remains until next submission.

### Expected Result
- Error message clears on input change (or at least on focus) to reduce confusion.

### Environment
- **OS:** macOS
- **Browser:** Chrome (latest)
- **Resolution:** 1920x1080
- **URL:** https://www.saucedemo.com/
- **Date/Time:** 2026-01-18

### Severity & Priority
**Severity:** S4 (Low)  
**Priority:** P3 (Low)

### Attachments
- Screenshot: `bug_008_1.png`
- Screenshot (while editing and error still visible): `bug_008_2.png`

---

## BUG-009: performance_glitch_user login is very slow with no loading feedback

**Bug ID:** BUG-009  
**Reported by:** Kamen Asenov  
**Date:** 2026-01-18  
**Module:** Login / Performance

### Summary
[Login] performance_glitch_user login takes unusually long with no progress indicator

### Description
When logging in with `performance_glitch_user`, the login action takes significantly longer than normal. There is no loading spinner/progress feedback, which can cause users to click multiple times or assume the application is frozen.

### Steps to Reproduce
1. Open https://www.saucedemo.com
2. Login as `performance_glitch_user` / `secret_sauce`
3. Measure perceived delay until inventory page loads (repeat 2-3 times)

### Actual Result
- Login takes noticeably longer than other users.
- No loading state or disabled login button while waiting.

### Expected Result
- Either login response should be within expected time, or UI should show a loading state (spinner/disabled button) until complete.

### Environment
- **OS:** macOS  
- **Browser:** Chrome (latest)  
- **Resolution:** 1920x1080  
- **URL:** https://www.saucedemo.com/  
- **Date/Time:** 2026-01-18  

### Severity & Priority
**Severity:** S3 (Medium)  
**Priority:** P2 (Medium)

### Preconditions
- None

### Test Data
- **User:** performance_glitch_user / secret_sauce

### Attachments
- Screenshot/video: `bug_009_1.png`

---

## BUG-010: Keyboard accessibility – focus indication is unclear on key controls

**Bug ID:** BUG-010  
**Reported by:** Kamen Asenov  
**Date:** 2026-01-18  
**Module:** Cross-cutting / Accessibility

### Summary
[Accessibility] Focus indicator is weak/unclear when navigating with keyboard (Tab)

### Description
When navigating the UI using keyboard-only (Tab/Shift+Tab), focus indication on interactive elements (buttons/links) is not always clearly visible. This reduces accessibility for keyboard users and can make navigation confusing.

### Steps to Reproduce
1. Login as `standard_user` / `secret_sauce`
2. On inventory page, use **Tab** to navigate through controls (menu, sort, add-to-cart buttons, cart icon)
3. Observe visibility of focus outline/indicator as it moves

### Actual Result
- Focus indicator is difficult to see or inconsistent on some controls.

### Expected Result
- Every interactive element should show a clear, visible focus indicator when selected via keyboard.

### Environment
- **OS:** macOS  
- **Browser:** Chrome (latest)  
- **Resolution:** 1920x1080  
- **URL:** https://www.saucedemo.com/inventory.html  
- **Date/Time:** 2026-01-18  

### Severity & Priority
**Severity:** S4 (Low)  
**Priority:** P3 (Low)

### Preconditions
- Logged in

### Attachments
- Screenshot: `bug_010_1.png`

---

## Report Writing Reflection

**Time spent:** ~2 hours  

**Most challenging bug to document:** BUG-007  
- Needs clearer proof (confirm whether finish can truly be triggered again vs only navigation).

**Most critical bug:** BUG-001  
- It’s a state/security-type issue: checkout flow should validate cart state and prevent invalid flow entry.

**What I learned:**
- Clear steps and exact data makes reproduction fast.
- Security and state issues need stronger evidence (console logs + video help).
- “Expected vs Actual” must be measurable to avoid ambiguity.
