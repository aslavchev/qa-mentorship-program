# Test Data Management

## Document Control

| Field | Details |
|------|---------|
| Project Name | SauceDemo |
| Document Title | Test Data Management |
| Author | Kamen Asenov |
| Created Date | 2025-26-12 |
| Version | 1.0 |
| Status | Draft |

---

## Purpose

This document describes the test data strategy for SauceDemo.  
It defines valid, invalid, boundary, and security test data used during manual and automated testing to ensure good coverage and reliable results.

---

## 1. Valid Test Data

### 1.1 Users – Valid Login Credentials

| Username | Password | User Type | Notes |
|--------|----------|----------|------|
| standard_user | secret_sauce | Standard | Main happy-path user |
| problem_user | secret_sauce | Problem | Used for negative scenarios |
| performance_glitch_user | secret_sauce | Performance | Used for performance-related checks |

---

### 1.2 Products – Available Items

| Product ID | Product Name | Price | Notes |
|-----------|-------------|-------|------|
| 1 | Sauce Labs Backpack | $29.99 | Most commonly used |
| 2 | Sauce Labs Bike Light | $9.99 | Lowest price |
| 3 | Sauce Labs Bolt T-Shirt | $15.99 | Medium price |
| 4 | Sauce Labs Fleece Jacket | $49.99 | Highest price |
| 5 | Sauce Labs Onesie | $7.99 | Boundary value (cheapest) |
| 6 | Test.allTheThings() T-Shirt (Red) | $15.99 | Special characters in name |

---

### 1.3 Checkout Information – Valid Data

| Field | Valid Examples |
|-----|----------------|
| First Name | John, Maria, Alex, José |
| Last Name | Doe, Smith, O'Brien, Müller |
| Zip Code | 12345, 90210, 10001 |

---

## 2. Invalid Test Data

### 2.1 Invalid Login Data

| Scenario | Username | Password | Expected Error |
|--------|----------|----------|---------------|
| Invalid username | wrong_user | secret_sauce | Username and password do not match |
| Invalid password | standard_user | wrong_pass | Username and password do not match |
| Empty username | [empty] | secret_sauce | Username is required |
| Empty password | standard_user | [empty] | Password is required |
| Both empty | [empty] | [empty] | Username is required |
| Locked user | locked_out_user | secret_sauce | User has been locked out |

---

### 2.2 Invalid Checkout Data

| Field | Invalid Values | Purpose |
|------|---------------|--------|
| First Name | [empty], `<script>`, `12345`, `@#$%` | Required, XSS, numeric |
| Last Name | [empty], `"OR 1=1`, `--`, `😀` | Required, SQL injection |
| Zip Code | [empty], `ABCDE`, `-12345`, `9999999999` | Required, format, length |

---

## 3. Boundary Value Test Data

### 3.1 Cart Quantity Boundaries

| Case | Items in Cart | Expected Result |
|----|--------------|----------------|
| Minimum - 1 | 0 | Invalid (empty cart) |
| Minimum | 1 | Valid |
| Normal | 2 | Valid |
| Maximum | 6 | Valid (all products) |

---

### 3.2 Input Field Length Boundaries

| Field | Min | Max | Test Values |
|------|-----|-----|------------|
| First Name | 1 | 50 | "A", 50-char string |
| Last Name | 1 | 50 | "B", 50-char string |
| Zip Code | 1 | 10 | "1", "1234567890" |

---

## 4. Security Test Data

### 4.1 SQL Injection Payloads

| Payload | Purpose |
|-------|---------|
| `' OR '1'='1` | Basic SQL injection |
| `admin'--` | Comment-based SQL injection |
| `1' UNION SELECT NULL--` | Union-based injection |

---

### 4.2 XSS Payloads

| Payload | Purpose |
|--------|--------|
| `<script>alert('XSS')</script>` | Basic XSS |
| `<img src=x onerror=alert('XSS')>` | Image-based XSS |
| `javascript:alert('XSS')` | JS protocol injection |

Expected result for all: **Input rejected and no script executed**

---

## 5. Test Data Storage Strategy

### 5.1 Recommended Test Data Structure

test-data/
├── users.csv
├── users-invalid.csv
├── products.json
├── checkout-valid.csv
├── checkout-invalid.csv
├── boundary-values.csv
├── security-payloads.txt

---

### 5.2 Example: users.csv

```csv
username,password,expected_result,user_type
standard_user,secret_sauce,success,standard
problem_user,secret_sauce,success,problem
locked_out_user,secret_sauce,locked,locked
wrong_user,secret_sauce,invalid,invalid
standard_user,wrong_pass,invalid,invalid