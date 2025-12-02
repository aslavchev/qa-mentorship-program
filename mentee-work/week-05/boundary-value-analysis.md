# Boundary Value Analysis (BVA) – SauceDemo  

## Objective
Apply Boundary Value Analysis to real boundaries present in SauceDemo.

## System Under Test
Checkout Step One form.

### 1. **Minimum Input Length Boundary**
Each field must contain at least *one visible character*.

| Test | Input | Expected |
|------|--------|---------|
| min-1 | "" | Error |
| min | "A" | Accept |
| min+1 | "AB" | Accept |

### 2. **Whitespace Boundary**
| Test | Input | Expected |
|------|--------|---------|
| Empty | "" | Error |
| Whitespace | "   " | Error |
| Non-empty | "A" | Accept |

### 3. **Very Long Input Boundary**

Assume boundary at 255 chars (common frontend limit).

| Test | Input Length | Expected |
|------|---------------|----------|
| max-1 | 254 chars | Accept |
| max | 255 chars | Accept |
| max+1 | 256 chars | Accept (no restriction) |

### 4. **Zip Code Numeric Boundary**
Zip accepts anything except empty.

| Test | Input | Expected |
|------|--------|---------|
| min-1 | "" | Error |
| min | "1" | Accept |
| min+1 | "12" | Accept |

### Summary
SauceDemo provides no numeric limit fields, so real BVA applies only to:
- Empty vs non-empty
- Whitespace vs characters
- Various input lengths

These are the true system boundaries.
