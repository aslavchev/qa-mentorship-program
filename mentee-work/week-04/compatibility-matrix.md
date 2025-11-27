# Week 4: Compatibility Matrix

## Exercise 4: Compatibility Matrix (45 min)

### Objective
Test SauceDemo across different browsers and devices to ensure proper functionality and layout.

### Instructions
1. Open SauceDemo on each browser/device combination.
2. Perform key actions (login, browse products, add to cart, checkout).
3. Note any issues with layout, functionality, or responsiveness.
4. Fill in the matrix below.

### Compatibility Matrix

| Browser / Device | Login | Product Catalog | Shopping Cart | Checkout | Notes |
|-----------------|-------|----------------|---------------|----------|-------|
| Chrome Desktop  | Works | Loads normally |  Works, but issues found |  Works, but validation issues | - Can continue to checkout with an empty cart. Cannot change item quantity in cart (always 1). Checkout accepts invalid formats for First/Last name and ZIP. |
| Safari Desktop  | Works | Loads normally |  Works, but issues found |  Validation issues | - Same behavior as Chrome: can proceed with empty cart. Item quantity cannot be edited. Checkout fields accept invalid data (letters, numbers, single characters). |
| Chrome Mobile   |  Login OK     |Images of products are stretched, also there are big gaps between description and price. When user opens the product, the picture is too big and takes up the whole screen so they have to scroll.|Shopping cart requires horizontal scrolling.|Checkout page is not fitting into the screen, the user has to unzoom to see it fully, just like in Product Catalog page.|Overall things do not look good on mobile, it is not suited well enough so it is hard to navigate. Also the same issue is present in the Shopping Cart about not being able to add more than one of a product.|
| Safari Mobile   |  Login OK     |Images of products are stretched, also there are big gaps between description and price. When user opens the product, the picture is too big and takes up the whole screen so they have to scroll.|Shopping cart seems to be working fine.|Checkout page is not fitting into the screen, the user has to unzoom to see it fully, just like in Product Catalog page.|A bit better than on Chrome mobile, but still not suited.|

