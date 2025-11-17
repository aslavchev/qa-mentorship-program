# Exploratory Testing: Shopping Cart (SauceDemo)

**Charter:** Explore the shopping cart and check for unexpected behavior and edge cases.

**Focus Areas:**
- Adding/removing items
- Cart badge updates
- Checkout behavior
- Navigation between pages
- Basic data handling

---

## Bugs Found

1. Cannot change item quantity inside the cart
- The cart only allows adding/removing items.
- No option to change quantity once the item is added.
- This is not typical for a shopping cart.

2. Checkout form accepts invalid inputs
- First Name, Last Name, and Postal Code accept:
  - Only numbers  
  - Only one letter  
  - Random characters
- No validation or error messages appear.

3. Cancel button in Checkout Overview goes back to product catalog
- When clicking "Cancel" on the overview page, the user is returned to the Products page.
- Expected behavior would be to return to the Cart or previous step.


 Questions Raised
- Should users be able to change quantities in the cart?
- What are the correct input rules for the checkout fields?
- Is the navigation during checkout working as intended?
- Should invalid checkout data be blocked?


 Test Ideas
- Test adding/removing items quickly to see if the cart badge updates correctly.
- Refresh the page after adding items to see if cart state remains.
- Try different input combinations in checkout (symbols, long strings, empty fields).
- Navigate back and forth during checkout to look for inconsistencies.
- Try cancelling at each step to check expected behavior.


 Areas of Concern
- Missing input validation on checkout fields.
- Confusing navigation when cancelling checkout.
- No quantity controls in the cart.
- Possible issues with cart state persistence.

