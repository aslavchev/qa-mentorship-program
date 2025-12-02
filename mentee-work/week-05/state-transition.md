# State Transition Testing – SauceDemo  

## Objective  
Map and test state transitions for the shopping cart in SauceDemo.

##  What Is State Transition Testing?  
State Transition Testing examines how the system behaves based on its current state, and how it changes when specific events occur.  
Key components:  
- **States** – different conditions of the system  
- **Events** – triggers  
- **Transitions** – movement from one state to another  
- **Actions** – system behavior during transition  

##  Cart States in SauceDemo

1. **Empty Cart** – no products added  
2. **Cart with Items** – one or more items added  
3. **Checkout in Progress** – checkout form started  
4. **Order Complete** – order successfully submitted  

##  Valid State Transitions

| Current State | Event | New State | Action |
|---------------|--------|-----------|--------|
| Empty Cart | Add Item | Cart with Items | Item appears in cart |
| Cart with Items | Remove All Items | Empty Cart | Cart resets to zero |
| Cart with Items | Click Checkout | Checkout in Progress | User navigates to checkout form |
| Checkout in Progress | Submit Order | Order Complete | Confirmation page displayed |
| Checkout in Progress | Cancel | Cart with Items | Return to cart with previous items |

##  State Diagram

[Empty Cart] --Add--> [Cart with Items] --Checkout--> [Checkout in Progress] --Submit--> [Order Complete]
↑ ↓ ↓
└────── Remove All ─────┘ ←──────────── Cancel ───────────────┘

##  Test Cases Based on State Transitions

### **TC1 – Empty → Cart with Items**  
**Event:** Add a product  
**Expected Result:** Cart shows 1 item.

### **TC2 – Cart with Items → Empty**  
**Event:** Remove all products  
**Expected Result:** Cart becomes empty; badge disappears.

### **TC3 – Cart with Items → Checkout in Progress**  
**Event:** Click “Checkout”  
**Expected Result:** User moves to Checkout Step One.

### **TC4 – Checkout in Progress → Order Complete**  
**Event:** Fill form → Click “Finish”  
**Expected Result:** “THANK YOU FOR YOUR ORDER” page loads.

### **TC5 – Checkout in Progress → Cart with Items**  
**Event:** Click “Cancel”  
**Expected Result:** Return to cart with all items still present.

##  Invalid / Negative Transitions

| Invalid Transition | Expected Behavior |
|--------------------|------------------|
| Attempt checkout with empty cart | Should be blocked |
| Submit order with empty cart | Impossible |
| Add item while on Order Complete page | Impossible without navigating back |
| Cancel checkout when not in checkout | Cannot occur |
