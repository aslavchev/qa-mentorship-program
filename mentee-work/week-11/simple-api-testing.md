# Week 11 - Exercise 4: Simple API Testing

**Your Name:** Kamen Asenov  
**Date:** 2026-01-26  

---

## Test Results

### GET /posts/1
============================================================
API TEST: GET /posts/1
============================================================

✓ Status Code: 200
✓ Response is JSON dict: <class 'dict'>
✓ Post ID: 1
✓ User ID: 1
✓ Title (preview): sunt aut facere repellat provident occaecati excep...
✓ Body (preview): quia et suscipit
suscipit recusandae consequuntur ...

============================================================
✅ TEST PASSED: GET /posts/1
============================================================

## POST /posts

============================================================
API TEST: POST /posts (Create New Post)
============================================================

📤 Sending POST request...
   URL: https://jsonplaceholder.typicode.com/posts
   Data: {'userId': 1, 'title': 'QA Test Post - Automated', 'body': 'This post was created by Python API test'}

✓ Status Code: 201
✓ Created Post ID: 101
✓ Title: QA Test Post - Automated
✓ Body: This post was created by Python API test

============================================================
✅ TEST PASSED: POST /posts
============================================================

## Error Scenarios

============================================================
API TEST: 404 Not Found
============================================================

✓ Status Code: 404
✅ TEST PASSED: 404 handled correctly

============================================================
API TEST: Invalid Endpoint
============================================================

✓ Status Code: 404
✅ TEST PASSED: Invalid endpoint handled correctly

============================================================
API TEST: Response Time
============================================================

✓ Response Time: 47.98 ms
✅ TEST PASSED: Response time acceptable

============================================================
✅ ALL API ERROR TESTS PASSED
============================================================

## Full Test Suite

============================================================
API TEST SUITE
============================================================
✅ GET /posts/1: PASS (0.09s)
✅ GET /posts: PASS (0.05s)
✅ POST /posts: PASS (0.41s)
✅ 404 Handling: PASS (0.05s)

============================================================
TEST SUMMARY
============================================================
Total: 4 | Passed: 4 | Failed: 0 | Errors: 0
============================================================

API vs UI Testing

Advantages of API testing:

Faster execution (no browser/UI rendering).

More stable and less flaky (UI changes don’t break API tests).

Easier to automate and run in CI/CD with clear assertions.

When would you use API testing instead of UI testing?
When I need fast validation of backend behavior (status codes, response schema, business rules) and I don’t need to verify UI elements/UX. Example: regression testing core flows via API on every commit.

Code Explanation

What does response = requests.get(url) do?
It sends an HTTP GET request to the given URL and returns a Response object (status code, headers, body, timing).

What does response.json() do?
It parses the response body as JSON and converts it to Python objects (dict/list). If the body is not valid JSON, it raises an error.

What is the difference between status code 200 and 201?

200 OK: request succeeded (typically GET/PUT).

201 Created: server created a new resource (typically POST) and returns the created object (often with an ID).

Real QA Use Case

How would you use this for SauceDemo?
If SauceDemo exposed APIs, I’d test authentication, cart operations, and checkout endpoints via API tests to cover core workflows quickly, then run a smaller set of UI tests for end-to-end confidence.

What APIs would you test in a real e-commerce app?

Auth API: login/logout/token refresh

Product API: list products, product details, search/filter

Cart API: add/remove items, get cart contents

Checkout API: submit shipping info, calculate totals/tax, create order

Orders API: order history, order details

