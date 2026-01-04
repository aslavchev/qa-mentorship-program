# SauceDemo Test Suite Organization

## 📁 Test Suite Structure

### Module 1: Login / Authentication (15 tests)
- **Priority S0–S1 (5 tests)** – Critical path  
  TC-LOGIN-001, TC-LOGIN-002, TC-LOGIN-008, TC-LOGIN-014, TC-LOGIN-015
- **Priority S2–S3 (10 tests)** – Standard coverage  
  TC-LOGIN-003 to TC-LOGIN-007, TC-LOGIN-009 to TC-LOGIN-013

---

### Module 2: Product Browsing & Sorting (10 tests)
- **Priority S1–S2 (6 tests)** – Core functionality  
  TC-PRODUCTS-001, TC-PRODUCTS-003, TC-PRODUCTS-004,  
  TC-SORT-001, TC-SORT-002, TC-SORT-003
- **Priority S3–S4 (4 tests)** – Secondary features  
  TC-SORT-004, TC-PRODUCTS-002, TC-PRODUCTS-005, TC-PRODUCTS-006

---

### Module 3: Shopping Cart (15 tests)
- **Priority S0–S1 (7 tests)** – Critical cart operations  
  TC-CART-001, TC-CART-002, TC-CART-003, TC-CART-004,  
  TC-CART-009, TC-CART-013, TC-CART-015
- **Priority S2–S3 (8 tests)** – Edge cases  
  TC-CART-005 to TC-CART-008, TC-CART-010 to TC-CART-012, TC-CART-014

---

### Module 4: Checkout (20 tests)
- **Priority S0–S1 (10 tests)** – Payment-critical  
  TC-CHECKOUT-001, TC-CHECKOUT-005, TC-CHECKOUT-010,  
  TC-CHECKOUT-013, TC-CHECKOUT-015, TC-CHECKOUT-016,  
  TC-CHECKOUT-017, TC-CHECKOUT-019, TC-CHECKOUT-020, TC-CHECKOUT-011
- **Priority S2–S3 (10 tests)** – Validation & edge cases  
  TC-CHECKOUT-002 to TC-CHECKOUT-004,  
  TC-CHECKOUT-006 to TC-CHECKOUT-009,  
  TC-CHECKOUT-012, TC-CHECKOUT-014, TC-CHECKOUT-018

---

## 📊 Priority Matrix

| Priority | Count | % of Total | Examples |
|--------|-------|------------|----------|
| S0 – Blocker | 3 | 5% | TC-LOGIN-001, TC-CHECKOUT-020 |
| S1 – Critical | 19 | 32% | TC-CART-001, TC-CHECKOUT-001 |
| S2 – Major | 21 | 35% | TC-SORT-001, TC-CART-010 |
| S3 – Minor | 15 | 25% | TC-LOGIN-011, TC-PRODUCTS-005 |
| S4 – Trivial | 2 | 3% | TC-PRODUCTS-002 |
| **TOTAL** | **60** | **100%** | |

---

## 🧪 Test Suite Assignments

| Suite | Test Count | Test IDs (Examples) | Execution Time |
|-----|------------|---------------------|----------------|
| **Smoke** | 12 | TC-LOGIN-001, TC-CART-001, TC-CHECKOUT-001, TC-CHECKOUT-020 | ~30 min |
| **Regression** | 38 | All S0–S2 tests | ~2 hours |
| **Full** | 60 | All test cases | ~3 hours |

---

## ▶️ Recommended Execution Order

### Phase 1: Smoke Testing (Run First)
1. Authentication  
   - TC-LOGIN-001  
   - TC-LOGIN-002  
2. Shopping Cart  
   - TC-CART-001  
3. Checkout  
   - TC-CHECKOUT-001  
   - TC-CHECKOUT-020  

---

### Phase 2: Module Testing
1. Login / Authentication  
   TC-LOGIN-001 → TC-LOGIN-015
2. Product Browsing & Sorting  
   TC-PRODUCTS-001 → TC-SORT-004
3. Shopping Cart  
   TC-CART-001 → TC-CART-015
4. Checkout  
   TC-CHECKOUT-001 → TC-CHECKOUT-020

---

### Phase 3: Regression Suite
- Re-run **all S0–S2 tests** after:
  - Bug fixes
  - New feature merge
  - Release candidate build
