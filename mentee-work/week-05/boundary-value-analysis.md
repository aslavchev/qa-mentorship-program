# Boundary Value Analysis (BVA) – SauceDemo  

- **min - 1**
- **min**
- **min + 1**
- **max - 1**
- **max**
- **max + 1**

### 3-Value BVA
Tests boundary, just inside, just outside.

| Purpose | Value | Expected Result |
|---------|--------|------------------|
| Below minimum | **0** | Invalid – item cannot be 0 |
| Minimum | **1** | Valid – add to cart works |
| Just above minimum | **2** | Valid |
| Just below maximum | **98** | Valid |
| Maximum | **99** | Valid |
| Above maximum | **100** | Invalid – should be rejected |


## 2-Value BVA
Tests only the boundary and one value outside it.

| Value | Expected Result |
|--------|------------------|
| 0 | Invalid |
| 1 | Valid |
| 99 | Valid |
| 100 | Invalid |


## Complete BVA Test Cases

### **TC1: Enter quantity = 0**  
Expected: System blocks adding item (invalid).

### **TC2: Enter quantity = 1**  
Expected: Item adds correctly.

### **TC3: Enter quantity = 2**  
Expected: Item adds correctly.

### **TC4: Enter quantity = 98**  
Expected: Works normally.

### **TC5: Enter quantity = 99**  
Expected: Works normally.

### **TC6: Enter quantity = 100**  
Expected: Error or rejection.

### **TC7: Negative quantity (-1)**  
Expected: Invalid.

### **TC8: Decimal quantity (0.5)**  
Expected: Invalid.

### **TC9: Very large quantity (99999)**  
Expected: Should be rejected.
 

