# api_test_suite.py
# Simple API test suite with summary reporting

import time
import requests


class APITestSuite:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"
        self.results = []

    def run_test(self, name, func):
        try:
            start = time.time()
            func()
            elapsed = time.time() - start
            self.results.append({"name": name, "status": "PASS", "time": f"{elapsed:.2f}s"})
            print(f"✅ {name}: PASS ({elapsed:.2f}s)")
        except AssertionError as e:
            self.results.append({"name": name, "status": "FAIL", "error": str(e)})
            print(f"❌ {name}: FAIL - {e}")
        except requests.RequestException as e:
            self.results.append({"name": name, "status": "ERROR", "error": str(e)})
            print(f"❌ {name}: ERROR - {e}")

    def test_get_single_post(self):
        r = requests.get(f"{self.base_url}/posts/1", timeout=10)
        assert r.status_code == 200
        data = r.json()
        assert "title" in data and len(data["title"]) > 0

    def test_get_all_posts(self):
        r = requests.get(f"{self.base_url}/posts", timeout=10)
        assert r.status_code == 200
        data = r.json()
        assert isinstance(data, list) and len(data) > 0

    def test_create_post(self):
        payload = {"userId": 1, "title": "Test", "body": "Test body"}
        r = requests.post(f"{self.base_url}/posts", json=payload, timeout=10)
        assert r.status_code == 201

    def test_not_found(self):
        r = requests.get(f"{self.base_url}/posts/99999", timeout=10)
        assert r.status_code == 404

    def run_all(self):
        print("=" * 60)
        print("API TEST SUITE")
        print("=" * 60)

        self.run_test("GET /posts/1", self.test_get_single_post)
        self.run_test("GET /posts", self.test_get_all_posts)
        self.run_test("POST /posts", self.test_create_post)
        self.run_test("404 Handling", self.test_not_found)

        passed = sum(1 for r in self.results if r["status"] == "PASS")
        failed = sum(1 for r in self.results if r["status"] == "FAIL")
        errors = sum(1 for r in self.results if r["status"] == "ERROR")

        print("\n" + "=" * 60)
        print("TEST SUMMARY")
        print("=" * 60)
        print(f"Total: {len(self.results)} | Passed: {passed} | Failed: {failed} | Errors: {errors}")
        print("=" * 60)


if __name__ == "__main__":
    suite = APITestSuite()
    suite.run_all()
