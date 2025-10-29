# Bug Report Template

## Bug Information

| Field | Details |
|-------|---------|
| **Bug ID** | BUG-[Number] (e.g., BUG-001) |
| **Summary** | Short, clear description of the issue (one sentence) |
| **Reported By** | Your name |
| **Reported Date** | YYYY-MM-DD |
| **Status** | New / Open / In Progress / Fixed / Closed / Reopened |
| **Severity** | Critical / High / Medium / Low |
| **Priority** | P0 / P1 / P2 / P3 |
| **Assigned To** | Developer name |

---

## Severity and Priority Guidelines

### Severity (Technical Impact)
- **Critical:** Application crash, data loss, security vulnerability
- **High:** Major functionality broken, no workaround available
- **Medium:** Functionality partially working, workaround exists
- **Low:** Minor UI issues, cosmetic defects

### Priority (Business Impact)
- **P0:** Blocks release, must fix immediately
- **P1:** High business impact, fix before release
- **P2:** Moderate impact, fix in next release
- **P3:** Low impact, fix when time permits

---

## Bug Details

### Environment

| Component | Details |
|-----------|---------|
| **Application URL** | https://www.saucedemo.com/ |
| **Environment** | Production / Staging / QA |
| **OS** | Windows 11 / macOS Sonoma / Ubuntu 22.04 |
| **Browser** | Chrome 118.0.5993.88 |
| **Screen Resolution** | 1920x1080 |
| **User Role** | Standard User / Admin |

---

## Description

Provide a clear and detailed description of the bug. Include:
- What functionality is affected
- What is happening (actual behavior)
- What should happen (expected behavior)
- Impact on users or business

Example:
> When attempting to add the "Sauce Labs Backpack" to the shopping cart, clicking the "Add to Cart" button does not update the cart counter. The item is not added to the cart, preventing users from completing purchases.

---

## Steps to Reproduce

Detailed, numbered steps that consistently reproduce the issue:

1. Navigate to https://www.saucedemo.com/
2. Login with username "standard_user" and password "secret_sauce"
3. Click on the "Sauce Labs Backpack" product image
4. On the product detail page, click "Add to Cart" button
5. Observe the cart badge in the top-right corner
6. Click on the cart icon
7. Verify items in the cart

**Reproducibility:** Always / Sometimes / Rarely

---

## Expected Result

What should happen when following the steps above:

- Cart badge should show "1" after clicking "Add to Cart"
- Product should appear in the shopping cart
- User can proceed to checkout

---

## Actual Result

What actually happens:

- Cart badge remains at "0"
- Cart is empty when clicked
- No error message is displayed

---

## Attachments

### Screenshots
- [ ] Screenshot of the issue attached
- [ ] Screenshot showing expected behavior (if available)

### Videos
- [ ] Screen recording of bug reproduction attached

### Logs
- [ ] Browser console errors copied below
- [ ] Network tab errors documented
- [ ] Server logs attached (if available)

**Browser Console Errors:**
```
Error: Cannot read property 'add' of undefined
  at addToCart (app.js:245)
  at HTMLButtonElement.onclick (product-detail.html:12)
```

**Network Errors:**
```
POST /api/cart/add - 500 Internal Server Error
```

---

## Test Data Used

| Field | Value |
|-------|-------|
| Username | standard_user |
| Password | secret_sauce |
| Product ID | 4 (Sauce Labs Backpack) |
| Session ID | abc123xyz789 |

---

## Workaround

Is there a temporary workaround until the bug is fixed?

- **Yes:** Add item from the products list page instead of product detail page
- **No:** No workaround available

---

## Additional Information

### Related Test Cases
- Test Case ID: TC-CART-003
- Test Case Title: Add product to cart from detail page

### Related Bugs
- Similar to BUG-045 (fixed in v1.2)
- Possibly related to BUG-089 (cart sync issues)

### Root Cause (if known)
- JavaScript function `addToCart()` fails when cart is initially empty
- Missing null check for cart object

### Suggested Fix (optional)
- Add defensive null check: `if (!cart) { cart = []; }`
- Initialize cart on page load

---

## Impact Analysis

### User Impact
- **Frequency:** 100% of users adding first item to cart
- **Affected Users:** All users (standard, problem users, performance users)
- **Business Impact:** High - Prevents all purchases

### Regression Risk
- Low - Fix is isolated to cart functionality
- Requires regression testing of all cart operations

---

## Verification Steps

Steps to verify the fix once deployed:

1. Deploy fix to QA environment
2. Clear browser cache and cookies
3. Login with test user
4. Add product to cart from detail page
5. Verify cart badge updates
6. Verify product appears in cart
7. Complete checkout to ensure no downstream issues

---

## Bug Lifecycle

| Status | Date | Updated By | Comment |
|--------|------|------------|---------|
| New | 2025-10-29 | QA Engineer | Initial report |
| Open | 2025-10-29 | Dev Lead | Assigned to John Doe |
| In Progress | 2025-10-30 | John Doe | Investigating root cause |
| Fixed | 2025-10-31 | John Doe | Fix deployed to QA |
| Closed | 2025-11-01 | QA Engineer | Verified fixed, closing |

---

## Notes / Comments

Any additional observations, context, or discussion:

- Bug introduced in v2.3.0 release
- Was not caught in regression testing
- Add test case to regression suite
- Consider automated test for this scenario

---

## Approval (for Critical/High bugs)

| Role | Name | Approved | Date |
|------|------|----------|------|
| **QA Lead** | [Name] | Yes/No | YYYY-MM-DD |
| **Dev Lead** | [Name] | Yes/No | YYYY-MM-DD |
| **Product Owner** | [Name] | Yes/No | YYYY-MM-DD |

---

**Template Version:** 1.0
**Last Updated:** October 2025

---

## Quick Tips for Writing Good Bug Reports

✅ **Do:**
- Use clear, descriptive titles
- Include detailed reproduction steps
- Attach screenshots/videos
- Specify exact environment details
- Indicate severity and priority correctly
- Provide test data used
- Check if bug already reported

❌ **Don't:**
- Be vague or ambiguous
- Use subjective language ("looks weird")
- Combine multiple bugs in one report
- Assign incorrect severity/priority
- Skip reproduction steps
- Forget to attach evidence
- Assume developers know the context
