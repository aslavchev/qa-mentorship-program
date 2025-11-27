# Week 4 – Security Checklist 

## 1. Authentication
- [x] Password is hidden
- [x] Invalid login shows error message
- [x] Empty username/password is not allowed
- [x] Logout redirects to login page
- [x] Cannot access inventory page after logout

## 2. Session Management
- [x] Session cookie appears after login
- [x] Cookie is removed after logout
- [x] Cannot open `/inventory.html` without logging in

## 3. Input Validation (Checkout)
- [x] Required fields block empty input (First Name, Last Name, Postal Code)
- [x] Error message appears for missing field
- [x] Entering special characters does not break the page
- [x] Script tags (`<script>`) do not execute

## 4. URL Protection
- [ ] Cannot access checkout steps directly without items in cart - You actually can!
- [x] Cannot skip to step two before step one
- [x] Direct URL access without login redirects to login page

## 5. HTTPS / Basic Security
- [x] Site uses HTTPS
- [x] No mixed content warnings
- [x] No sensitive data visible in URL or page source

## Notes
- In the site there is an issue concerning the Checkout Information page, where the user can enter First name/Last name/Zip code with inappropriate format.
