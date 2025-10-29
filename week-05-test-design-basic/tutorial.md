# Week 5: Test Design Techniques (Basic)

## 🎯 Learning Objectives
- Apply Equivalence Partitioning
- Use Boundary Value Analysis
- Create Decision Tables
- Map State Transitions
- Combine techniques for better coverage

## 📚 Why Test Design Techniques?

**Problem:** How do we test systematically without missing scenarios?
**Solution:** Use proven test design techniques

### Benefits
- ✅ Better test coverage with fewer tests
- ✅ Systematic, repeatable approach
- ✅ Find more defects
- ✅ Justify test case selection
- ✅ Optimize testing effort

## 1️⃣ Equivalence Partitioning (EP)

### Definition
Divide inputs into groups (partitions) that should behave the same way. Test one value from each partition.

### Key Concept
If one value in a partition works, all values in that partition should work.

### Example: Age Field
**Partitions:**
- Invalid: age < 0
- Valid: 0 ≤ age ≤ 150
- Invalid: age > 150

**Test Cases:** Test one value from each partition
- Test 1: age = -1 (invalid)
- Test 2: age = 25 (valid)
- Test 3: age = 200 (invalid)

### SauceDemo Example: Username Field
**Partitions:**
- Valid users: standard_user, problem_user, performance_glitch_user
- Invalid users: wrong_user, empty, special_chars
- Locked users: locked_out_user

**Test Cases:**
- Test valid partition: standard_user
- Test invalid partition: wrong_user
- Test locked partition: locked_out_user

### Steps to Apply EP
1. Identify input/output
2. Divide into valid and invalid partitions
3. Select one test value per partition
4. Create test cases

## 2️⃣ Boundary Value Analysis (BVA)

### Definition
Test at the boundaries between partitions. Defects often occur at boundaries.

### Key Concept
Test: minimum-1, minimum, minimum+1, maximum-1, maximum, maximum+1

### Example: Quantity Field (1-99 allowed)
**Boundary Values:**
- 0 (min-1, invalid)
- 1 (min, valid)
- 2 (min+1, valid)
- 98 (max-1, valid)
- 99 (max, valid)
- 100 (max+1, invalid)

### 2-Value vs 3-Value BVA
**2-Value BVA:** Test boundary and just outside
- 0, 1, 99, 100

**3-Value BVA:** Test boundary, just inside, just outside
- 0, 1, 2, 98, 99, 100

### SauceDemo Example: Cart Quantity
**Boundaries to Test:**
- Minimum: 0, 1, 2
- Maximum: 98, 99, 100 (if limit exists)
- Special: negative numbers, decimals, very large numbers

## 3️⃣ Decision Tables

### Definition
Test combinations of conditions and their resulting actions. Useful for complex business logic.

### Structure
| Condition 1 | Condition 2 | ... | Action/Result |
|-------------|-------------|-----|---------------|
| T | T | ... | Result A |
| T | F | ... | Result B |
| F | T | ... | Result C |
| F | F | ... | Result D |

### SauceDemo Example: Checkout Form Validation

| First Name | Last Name | Zip Code | Result |
|------------|-----------|----------|--------|
| Valid | Valid | Valid | Success |
| Empty | Valid | Valid | Error: First name required |
| Valid | Empty | Valid | Error: Last name required |
| Valid | Valid | Empty | Error: Zip code required |
| Empty | Empty | Empty | Error: All fields required |

### Steps to Create Decision Table
1. Identify conditions (inputs)
2. Identify actions (outputs)
3. Create all combinations
4. Reduce redundant combinations
5. Create test cases for each column

## 4️⃣ State Transition Testing

### Definition
Test state-based behavior: states, transitions, events, actions.

### Components
- **States:** Different conditions object can be in
- **Transitions:** Movement between states
- **Events:** Triggers causing transitions
- **Actions:** What happens during transition

### SauceDemo Example: Shopping Cart States

**States:**
1. Empty Cart
2. Cart with Items
3. Checkout in Progress
4. Order Complete

**Transitions:**
- Empty → With Items (Add product)
- With Items → Empty (Remove all)
- With Items → Checkout (Click checkout)
- Checkout → Complete (Submit order)
- Checkout → With Items (Cancel)

**State Diagram:**
```
[Empty] --Add--> [With Items] --Checkout--> [In Progress] --Submit--> [Complete]
   ↑               ↓                             ↓
   └─Remove All────┘←───────Cancel──────────────┘
```

### Test Cases from State Transitions
- Test each valid transition
- Test invalid transitions (should be rejected)
- Test all paths through states

## 🎯 Combining Techniques

### Powerful Approach
Use multiple techniques together for comprehensive coverage:

1. **EP for inputs** → Identify partitions
2. **BVA on boundaries** → Test edges
3. **Decision Tables for logic** → Test combinations
4. **State Transitions for workflows** → Test sequences

### SauceDemo Complete Example: Add to Cart

**1. EP on Product Selection:**
- Valid products
- Invalid/out of stock
- Already in cart

**2. BVA on Quantity:**
- 0, 1, 2, 98, 99, 100

**3. Decision Table for Add Logic:**
| Product Valid | Quantity Valid | Already in Cart | Result |
|---------------|----------------|-----------------|--------|
| Yes | Yes | No | Add success |
| Yes | Yes | Yes | Update quantity |
| Yes | No | - | Error |
| No | - | - | Error |

**4. State Transition:**
- Empty Cart → Add → Cart with Items
- Cart with Items → Add More → Cart Updated

## 💡 Best Practices

1. **Start with EP** - Partition inputs first
2. **Add BVA** - Test boundaries of partitions
3. **Use Decision Tables** - For complex logic with multiple conditions
4. **Map State Transitions** - For workflow-based features
5. **Document your approach** - Show which technique you used and why

## 📝 Key Takeaways
1. Test design techniques provide systematic coverage
2. EP reduces test cases while maintaining coverage
3. BVA finds boundary-related defects
4. Decision tables handle complex logic
5. State transitions test workflows
6. Combining techniques is powerful

## 🎓 Further Reading
- "A Practitioner's Guide to Software Test Design" by Lee Copeland
- ISTQB Syllabus Chapter 4 (Test Design Techniques)
- ISO/IEC 29119-4 (Test Techniques)
