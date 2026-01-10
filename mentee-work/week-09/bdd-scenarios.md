# BDD Scenarios – SauceDemo

### Feature: User Authentication
  As a registered user
  I want to securely log in and log out
  So that I can access products and manage my shopping cart


### Scenario 1: Successful login with valid credentials
Given I am on the SauceDemo login page
And I am logged out
When I enter "standard_user" in the username field
And I enter "secret_sauce" in the password field
And I click the LOGIN button
Then I should be redirected to the inventory page
And I should see 6 products displayed

### Scenario 2: Login fails with invalid username
Given I am on the SauceDemo login page
When I enter "invalid_user" in the username field
And I enter "secret_sauce" in the password field
And I click the LOGIN button
Then I should see an error message "Epic sadface: Username and password do not match any user in this service"
And I should remain on the login page

### Scenario 3: Locked user cannot log in
Given I am on the SauceDemo login page
When I enter "locked_out_user" in the username field
And I enter "secret_sauce" in the password field
And I click the LOGIN button
Then I should see an error message "Epic sadface: Sorry, this user has been locked out."
And I should remain on the login page

### Scenario 4: Login attempt with SQL injection is blocked
Given I am on the SauceDemo login page
When I enter "' OR '1'='1" in the username field
And I enter "' OR '1'='1" in the password field
And I click the LOGIN button
Then I should see error "Epic sadface: Username and password do not match any user in this service"
And I should not be logged in

### Scenario 5: User can logout successfully
Given I am logged in as "standard_user"
And I am on the inventory page
When I open the menu
And I click the Logout option
Then I should be redirected to the login page
And I should no longer have an active session

### Feature: Product Browsing
  As a shopper
  I want to browse products and view product details
  So that I can decide what to purchase


### Scenario 6: View all products on inventory page
Given I am logged in as "standard_user"
When I navigate to the inventory page
Then I should see 6 products listed
And each product should display a name, price, and image

### Scenario 7: Sort products by name from A to Z
Given I am logged in as "standard_user"
And I am on the inventory page
When I select "Name (A to Z)" from the sort dropdown
Then the products should be displayed in alphabetical order from A to Z

### Scenario 8: Open product details page
Given I am logged in as "standard_user"
And I am on the inventory page
When I click on a product name
Then I should be navigated to the product details page
And I should see product name, description, price, and image

### Feature: Shopping Cart
  As a shopper
  I want to add and remove items from my cart
  So that I can manage what I plan to buy before checkout


### Scenario 9: Add product to cart from inventory page
Given I am logged in as "standard_user"
And I am on the inventory page
When I click "Add to cart" for "Sauce Labs Backpack"
Then the cart badge should display "1"
And the button text should change to "Remove"

### Scenario 10: Remove product from cart
Given I have "Sauce Labs Backpack" added to the cart
And I am on the cart page
When I click the "Remove" button
Then the item should be removed from the cart
And the cart badge should not be displayed

### Scenario 11: Cart retains items after navigation
Given I have added an item to the cart
When I navigate to another page and return to the cart
Then the item should still be present in the cart

### Scenario 12: Checkout button navigates to checkout page
Given I have at least one item in the cart
And I am on the cart page
When I click the Checkout button
Then I should be redirected to the checkout information page

### Feature: Checkout
  As a shopper
  I want to complete checkout with my personal information
  So that I can place an order successfully


### Scenario 13: Checkout with valid information
Given I have items in my cart
And I am on the checkout information page
When I enter "John" as first name
And I enter "Doe" as last name
And I enter "12345" as zip code
And I click Continue
Then I should be navigated to the overview page

### Scenario 14: Checkout fails with empty first name
Given I am on the checkout information page
When I leave the first name field empty
And I fill last name and zip code
And I click Continue
Then I should see an error message "Error: First Name is required"
And I should remain on the checkout information page

### Scenario 15: Complete end-to-end purchase flow
Given I am on the SauceDemo login page
When I login as "standard_user" with password "secret_sauce"
And I add "Sauce Labs Backpack" to the cart
And I navigate to the cart
And I click Checkout
And I enter checkout information:
  | First Name | Last Name | Zip Code |
  | John       | Doe       | 12345    |
And I click Continue
And I click Finish
Then I should see the order confirmation page
And I should see the message "Thank you for your order"
And the cart should be empty

### Scenario Outlines

### Scenario Outline 1: Login validation errors
Given I am on the SauceDemo login page
When I enter "<username>" in the username field
And I enter "<password>" in the password field
And I click the LOGIN button
Then I should see an error message "<error_message>"
And I should remain on the login page

Examples:
  | username      | password      | error_message                                                |
  | invalid_user  | secret_sauce  | Username and password do not match any user in this service |
  | standard_user | wrong_pass    | Username and password do not match any user in this service |
  |               | secret_sauce  | Epic sadface: Username is required                           |
  | standard_user |               | Epic sadface: Password is required                           |

### Scenario Outline 2: Checkout required field validation
Given I am on the checkout information page
When I enter "<first_name>" as first name
And I enter "<last_name>" as last name
And I enter "<zip>" as zip code
And I click Continue
Then I should see an error message "<error_message>"

Examples:
  | first_name | last_name | zip   | error_message                    |
  |            | Doe       | 12345 | Error: First Name is required    |
  | John       |           | 12345 | Error: Last Name is required     |
  | John       | Doe       |       | Error: Postal Code is required  |

