# Week 4: Accessibility Audit

## Exercise 5: Accessibility Audit (60 min)

### Objective
Evaluate SauceDemo for accessibility compliance with WCAG guidelines.

### Instructions
1. Navigate through SauceDemo using keyboard only (Tab, Enter, Shift+Tab).
2. Check screen reader compatibility if available.
3. Look for:
   - Proper use of headings and labels
   - Alt text on images
   - Focus order and visibility
   - Color contrast
4. Record any accessibility issues found.

### Accessibility Audit Table

| Feature / Page | Issue Observed | Severity | Notes |
|----------------|----------------|----------|-------|
| Login Page     |       No issues|          |       |
| Product Catalog|Unable to navigate with keyboard to the cart button with voiceover, no alt text visible for pictures, nothing can be navigated without voice over|Big severity|No way to navigate|
| Shopping Cart  |Unable to navigate with keyboard, with voice over it is working correctly|Medium severity|No way to navigate, however this is not that big of an issue as the Product catalog because it has only one button to be pressed to proceed to checkout.|
| Checkout       |No way to go to the continue button with keyboard only|Medium severity|The fields with First name/ Last name/ Zip code work correctly.|
| Notes    - The other pages are also not responsive with keyboard only. This is an issue for the whole site! The color contrast looks fine, everything is visible and the focus order seems okay - the most important things are right in the center of the screen. The headings and labels also seem descriptive enough. With voice over ON, navigating gets easier but still not every time the focus logic is correct.|

