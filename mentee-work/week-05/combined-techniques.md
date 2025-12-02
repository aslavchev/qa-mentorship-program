### Combined Test Scenarios (Using All Techniques)

### **Scenario 1 – Add valid product with boundary quantity**
- Product: valid  
- Quantity: 1, 2, 98, 99 (BVA)  
- State transition: Empty → With Items  
- Expected: Item successfully added  

### **Scenario 2 – Add invalid product**
- Product: invalid ID (EP)  
- Expected: Error  
- State: stays in Empty Cart  

### **Scenario 3 – Add valid product with invalid quantity**
- Quantity: 0, -1, 100, decimals  
- Expected: Error (BVA)  
- State: stays in Empty Cart  

### **Scenario 4 – Add same product twice**
- Product exists  
- Already in cart = yes  
- Decision table → Update quantity  
- State: With Items → With Items (updated)

### **Scenario 5 – Checkout with missing fields**
Use decision table:

- Missing first name  
- Missing last name  
- Missing zip code  
- All missing  

Expected: Correct error shown

### **Scenario 6 – Valid checkout flow**
- Add product → Checkout → Submit  
- Valid input partitions  
- Valid transitions:  
  Empty → With Items → In Progress → Complete  

