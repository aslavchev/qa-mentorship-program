# api_error_test.py
# Test API error scenarios + response time

import requests


def test_not_found():
    print("\n" + "=" * 60)
    print("API TEST: 404 Not Found")
    print("=" * 60)

    url = "https://jsonplaceholder.typicode.com/posts/99999"
    response = requests.get(url, timeout=10)

    print(f"\n✓ Status Code: {response.status_code}")
    assert response.status_code == 404, f"Expected 404 Not Found, got {response.status_code}"

    print("✅ TEST PASSED: 404 handled correctly")


def test_invalid_endpoint():
    print("\n" + "=" * 60)
    print("API TEST: Invalid Endpoint")
    print("=" * 60)

    url = "https://jsonplaceholder.typicode.com/invalid"
    response = requests.get(url, timeout=10)

    print(f"\n✓ Status Code: {response.status_code}")
    assert response.status_code == 404, f"Expected 404, got {response.status_code}"

    print("✅ TEST PASSED: Invalid endpoint handled correctly")


def test_response_time():
    print("\n" + "=" * 60)
    print("API TEST: Response Time")
    print("=" * 60)

    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url, timeout=10)

    elapsed_ms = response.elapsed.total_seconds() * 1000
    print(f"\n✓ Response Time: {elapsed_ms:.2f} ms")
    assert elapsed_ms < 2000, "Response time should be < 2000 ms"

    print("✅ TEST PASSED: Response time acceptable")


if __name__ == "__main__":
    test_not_found()
    test_invalid_endpoint()
    test_response_time()

    print("\n" + "=" * 60)
    print("✅ ALL API ERROR TESTS PASSED")
    print("=" * 60)
