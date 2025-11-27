# Week 4: SauceDemo Manual Performance Assessment (Safari)

---

## Performance Metrics Legend
- **Load Time:** When all resources are fully loaded (load event fired)  
- **Total Transfer Size:** Bytes transferred over the network  
- **Total Resource Size:** Size of all resources (uncompressed)  
- **Resource Count:** Number of resources loaded  
- **Domain Count:** Number of unique domains contacted  
- **Redirect Count:** Number of redirects for resources  
- **Slowest Resource:** Resource that took the longest to load  
- **Observations:** Anything unusual or notable  
- **Note**: All of the values are average of several refreshes of the pages and standard_user has been used for testing purposes.
---

## 1. Login Page
- **Load Time:** 50 ms
- **Total Transfer Size:** 220 KB
- **Total Resource Size:** 759 KB
- **Resource Count:** 9
- **Domain Count:** 3
- **Redirect Count:** 0
- **Slowest Resource:** https://www.saucedemo.com/static/js/main.018d2d1e.chunk.js
- **Observations:** Works fine and fast.

---

## 2. Product Catalog
- **Load Time:** 56 ms
- **Total Transfer Size:** 377 KB
- **Total Resource Size:** 915 KB
- **Resource Count:** 25
- **Domain Count:** 4
- **Redirect Count:** 0
- **Slowest Resource:** https://www.saucedemo.com/static/js/main.018d2d1e.chunk.js
- **Observations:** Works fine and fast.

---

## 3. Product Details (any product)
- **Load Time:** 42 ms
- **Total Transfer Size:** 246 KB
- **Total Resource Size:** 788 KB
- **Resource Count:** 19
- **Domain Count:** 4
- **Redirect Count:** 0
- **Slowest Resource:** https://www.saucedemo.com/static/js/main.018d2d1e.chunk.js
- **Observations:** Works fine and fast.

---

## 4. Shopping Cart
- **Load Time:** 151 ms
- **Total Transfer Size:** 225 KB
- **Total Resource Size:** 769 KB
- **Resource Count:** 18
- **Domain Count:** 4
- **Redirect Count:** 0
- **Slowest Resource:** https://www.saucedemo.com/manifest.json
- **Observations:** Works fine and fast, negligably slower than previous ones.

---

## 5. Checkout Overview
- **Load Time:** 35 ms
- **Total Transfer Size:** 226 KB
- **Total Resource Size:** 769 KB
- **Resource Count:** 18
- **Domain Count:** 4
- **Redirect Count:** 0
- **Slowest Resource:** https://www.saucedemo.com/static/js/main.018d2d1e.chunk.js
- **Observations:** Works fine and fast.

---

## 6. Checkout Complete
- **Load Time:** 37 ms
- **Total Transfer Size:** 226 KB
- **Total Resource Size:** 769 KB
- **Resource Count:** 18
- **Domain Count:** 4
- **Redirect Count:** 0
- **Slowest Resource:** https://www.saucedemo.com/static/js/main.018d2d1e.chunk.js
- **Observations:** Works fine and fast.
