# Week 5 — Exercise 1: Equivalence Partitioning (Improved)

## Objective  
Apply Equivalence Partitioning (EP) to input fields in SauceDemo.
## Scope
- Login form (username & password)
- Checkout form (first name, last name, postal code)

# Login Form — Username

## Partitions
| Partition Type | Description | Example Value | Expected Result |
|----------------|-------------|---------------|-----------------|
| Valid user | Correct, active account | `standard_user` | Login success |
| Locked user | Account exists but blocked | `locked_out_user` | Error: User locked |
| Invalid user | Wrong or non-existing | `wrong_user`, `aaaa` | Invalid credentials |
| Empty | No input | `""` | Username required |
| Whitespace-only | Appears empty | `"   "` | Username required |
| Very long string | Stress test | `"a"*200` | Invalid credentials |
| Special characters | Unlikely username | `"!@#"` | Invalid credentials |
| Unicode characters | Non-Latin username | `"Иван"` | Invalid credentials |

## Representative Test Cases
- EP-U1: `standard_user` → success  
- EP-U2: `locked_out_user` → locked error  
- EP-U3: random invalid username → invalid credentials  
- EP-U4: `""` → required error  
- EP-U5: `"   "` → required error  
- EP-U6: `"aaaa...200 chars"` → invalid  
- EP-U7: `"!@#"` → invalid  
- EP-U8: `"Иван"` → invalid  

# Login Form — Password

## Partitions
| Partition Type | Description | Example | Expected |
|----------------|-------------|---------|----------|
| Valid password | Correct password | `secret_sauce` | Success (if username valid) |
| Invalid password | Wrong input | `abc123` | Invalid credentials |
| Empty | No input | `""` | Password required |
| Whitespace-only | Only spaces | `"   "` | Password required |
| Very long | 200+ chars | `"p"*200` | Invalid credentials |
| Special characters | `#@!!?` | Invalid credentials |
| Unicode | `"парола"` | Invalid credentials |

# Checkout Form — All Fields  
Fields:  
✔ First Name  
✔ Last Name  
✔ Zip Code  

## Partitions by Input Type

### 1. **Empty vs Non-Empty**
| Field | Empty | Non-Empty |
|-------|--------|------------|
| First Name | `""` | `"Kamen"` |
| Last Name | `""` | `"Asenov"` |
| Zip Code | `""` | `"11111"` |

### 2. **Whitespace-Only Inputs**
All treated as empty by the app.
| Field | Example | Expected |
|--------|----------|----------|
| First Name | `"   "` | Error |
| Last Name | `"   "` | Error |
| Zip Code | `"   "` | Error |

### 3. **Length Boundaries**
(No UI limit, but realistic equivalence partitions)

| Boundary | Example | Expected |
|----------|---------|----------|
| min-1 | `""` | Error |
| min | `"A"` | Valid |
| typical | `"Alexander"` | Valid |
| max (255 chars) | `"A"*255` | Valid |
| beyond-max | `"A"*300` | Valid (no restriction) |

### 4. **Special Characters**
All accepted in Checkout.

| Type | Example | Expected |
|-------|---------|----------|
| Special chars | `"@#$"` | Accepted |
| Mixed name formats | `"Kamen-Asenov"` | Accepted |
| Punctuation | `"O'Connor"` | Accepted |

### 5. **Numeric & Alphanumeric**
All allowed.

| Partition | Example | Expected |
|-----------|----------|----------|
| Numeric name | `"123"` | Accepted |
| Alphanumeric | `"John99"` | Accepted |

### 6. **Unicode / Non-Latin**
Front-end fully accepts these.

| Example | Expected |
|----------|----------|
| `"Иван"` | Accepted |
| `"Γιώργος"` | Accepted |
| `"李明"` | Accepted |

# Representative Checkout Tests
- EP-C1: All valid → Proceed  
- EP-C2: First name empty → First name error  
- EP-C3: Last name empty → Last name error  
- EP-C4: Zip empty → Zip required  
- EP-C5: FN whitespace → error  
- EP-C6: FN = 255 chars → valid  
- EP-C7: Unicode FN `"Иван"` + valid LN/ZIP → success  
- EP-C8: FN `"@#"` + valid LN/ZIP → success  

## Summary
- deeper character-type partitions  
- whitespace-only values  
- realistic length boundaries  
- unicode and mixed inputs  
- both login and checkout coverage  
