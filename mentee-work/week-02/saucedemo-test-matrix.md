## Exercise 2: SauceDemo Test Level Mapping (45 minutes)

### Objective
Map all SauceDemo features to appropriate test levels.

### Instructions

Create a comprehensive matrix showing which test levels apply to each SauceDemo feature.

---

| Feature/Module | Unit | Integration | System | Acceptance | Notes |
|----------------|------|-------------|--------|------------|-------|
| **Authentication** | | | | | |
| - Login validation | ✅ | ✅ | ✅ | ✅ | Unit: test different functions; Integration: UI + Backend; System: end-to-end login flow; Acceptance: confirm login works for user |
| - Session management | ✅ | ✅ | ✅ | ✅ | Validate session expiry |
| - Logout | ✅ | ✅ | ✅ | ✅ | Can be tested at all levels like login validation |
| **Product Catalog** | | | | | |
| - Display products | ❌ | ✅ | ❌ | ✅ | Integration between API and UI rendering |
| - Product details | ✅ | ✅ | ❌ | ✅ | Can be tested at all levels except system as it is a component|
| - Sorting | ✅ | ✅ | ❌ | ✅ | Unit: sort algorithm; Integration: product data + sort logic |
| - Filtering | ✅ | ✅ | ❌ | ✅ | Test filter function, API parameters, and UI updates |
| **Shopping Cart** | | | | | |
| - Add to cart | ✅ | ✅ | ❌ | ✅ | Unit: test different functions; Integration: UI + Backend |
| - Remove from cart | ✅ | ✅ | ❌ | ✅ | Verify both function logic and UI synchronization |
| - Update quantity | ✅ | ✅ | ❌ | ✅ | Ensure correct total recalculation and backend update |
| - Calculate total | ✅ | ✅ | ❌ | ✅ | Unit: calculation logic; Integration: cart and pricing API |
| **Checkout** | | | | | |
| - Form validation | ✅ | ✅ | ✅ | ✅ | Unit: input validation; System: checkout flow; Acceptance: user can’t proceed with invalid data |
| - Information step | ❌ | ✅ | ❌ | ✅ | Integration between frontend and backend; verify data persistence |
| - Overview step | ❌ | ✅ | ❌| ✅ | Check correct items, totals, and taxes shown |
| - Complete purchase | ❌ | ✅ | ✅ | ✅ | End-to-end test with backend order confirmation |

**Questions to Answer:**
1. Which features require testing at all levels? The more complex and risk-prone like Login validation, Session management, logout, Form validation.
2. Which features can skip certain levels? Why? The others because they are either components or like Complete purchase it is and end-to-end, no separate components needed to be tested.
3. Where would you focus most effort if time is limited? The most important based on risk level  - the authentication ones. Also the ones that are connected most to the UI and the user will use for sure while interacting with the product.