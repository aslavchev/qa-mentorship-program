# api_post_test.py
# Test API POST request

import requests


def test_create_post():
    print("=" * 60)
    print("API TEST: POST /posts (Create New Post)")
    print("=" * 60)

    url = "https://jsonplaceholder.typicode.com/posts"
    new_post = {
        "userId": 1,
        "title": "QA Test Post - Automated",
        "body": "This post was created by Python API test"
    }

    print("\n📤 Sending POST request...")
    print(f"   URL: {url}")
    print(f"   Data: {new_post}")

    response = requests.post(url, json=new_post, timeout=10)

    print(f"\n✓ Status Code: {response.status_code}")
    assert response.status_code == 201, f"Expected 201 Created, got {response.status_code}"

    created = response.json()

    assert "id" in created, "Response should include new post ID"
    print(f"✓ Created Post ID: {created['id']}")

    assert created.get("title") == new_post["title"], "Title mismatch"
    print(f"✓ Title: {created['title']}")

    assert created.get("body") == new_post["body"], "Body mismatch"
    print(f"✓ Body: {created['body']}")

    print("\n" + "=" * 60)
    print("✅ TEST PASSED: POST /posts")
    print("=" * 60)


if __name__ == "__main__":
    test_create_post()
