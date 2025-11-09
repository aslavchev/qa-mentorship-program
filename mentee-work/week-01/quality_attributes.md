# Quality Attributes Analysis - SauceDemo

## Part A: Categorize Quality Attributes

| # | Quality Concern | Category |
|---|------------------|-----------|
| 1 | User can add items to cart | F|
| 2 | Page loads within 2 seconds | NF |
| 3 | Application works on Chrome, Firefox, Safari | NF |
| 4 | User receives order confirmation | F|
| 5 | Password is masked during entry | NF |
| 6 | Application is available 99% of the time | NF |
| 7 | New users can complete purchase without help | NF |
| 8 | Product sorting works correctly | F |
| 9 | Application supports 1000 concurrent users |NF |
| 10 | Checkout form validates required fields | F |

## Part B: NFR Checklist for SauceDemo

### **Performance:**
- [ ] Page load time < 2 seconds
- [ ] Product images load quickly
- [ ] Sorting/filtering is responsive
- [ ] Cart updates reflect instantly
- [ ] Checkout process completes in < 5 seconds

### **Security:**
- [ ] Password not visible in plain text
- [ ] Session expires after inactivity
- [ ] Data sent over HTTPS
- [ ] Sensitive information not stored in browser cache
- [ ] User cannot access cart without authentication

### **Usability:**
- [ ] Clear and consistent navigation
- [ ] Helpful error messages for login and checkout
- [ ] Checkout process intuitive for new users
- [ ] Product information clearly displayed
- [ ] Buttons and labels are descriptive

### **Compatibility:**
- [ ] Works on Chrome
- [ ] Works on Firefox
- [ ] Works on Safari
- [ ] Works on Edge
- [ ] Works on mobile

### **Accessibility:**
- [ ] Screen reader compatible 
- [ ] Keyboard navigation works (Tab, Enter)
- [ ] Color contrast meets accessibility standards


## Part C: Prioritization

| Area | Priority | Justification |
|------|----------|---------------|
| **Login/Authentication** | 1 | Most important as also most security demanding |
| **Checkout Process** | 2 | Most impactful for business |
| **Shopping Cart** | 3 | Important as it Leads to Checkout |
| **Product Catalog** | 4 | Important to be working properly |
| **Sorting/Filtering** | 5 | Not as important as the above but good for UI |
| **Product Details** | 6 | Least important part with lowest risk |

