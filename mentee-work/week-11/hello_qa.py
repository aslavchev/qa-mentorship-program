# hello_qa.py
# My first Python script for QA

print("=" * 50)
print("QA AUTOMATION ENVIRONMENT CHECK")
print("=" * 50)

# Check Python version
import sys
print(f"\nPython Version: {sys.version}")

# Check platform
import platform
print(f"Operating System: {platform.system()} {platform.release()}")

# Test basic data types
username = "standard_user"
test_count = 60
passed = True

print(f"\nTest Data:")
print(f"  Username: {username}")
print(f"  Test Cases: {test_count}")
print(f"  All Passed: {passed}")

print("\n✅ Python environment is ready for QA automation!")
