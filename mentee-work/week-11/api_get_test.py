# api_get_test.py
# Test API GET request

import requests


def test_get_post():
    print("=" * 60)
    print("API TEST: GET /posts/1")
    print("=" * 60)

    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url, timeout=10)

    print(f"\n✓ Status Code: {response.status_code}")
    assert response.status_code == 200, f"Expected 200 OK, got {response.status_code}"

    data = response.json()

    print(f"✓ Response is JSON dict: {type(data)}")
    assert isinstance(data, dict), "Expected JSON object (dict)"

    for key in ["userId", "id", "title", "body"]:
        assert key in data, f"Missing '{key}' field"

    print(f"✓ Post ID: {data['id']}")
    assert data["id"] == 1, "Expected post ID = 1"

    print(f"✓ User ID: {data['userId']}")
    assert data["userId"] == 1, "Expected user ID = 1"

    print(f"✓ Title (preview): {data['title'][:50]}...")
    assert len(data["title"]) > 0, "Title should not be empty"

    print(f"✓ Body (preview): {data['body'][:50]}...")
    assert len(data["body"]) > 0, "Body should not be empty"

    print("\n" + "=" * 60)
    print("✅ TEST PASSED: GET /posts/1")
    print("=" * 60)


if __name__ == "__main__":
    test_get_post()
