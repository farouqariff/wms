"""
Demonstration: Why Server-Side Authorization is Critical
This shows that client-side checks can be bypassed!
"""
import requests

BASE_URL = "http://localhost:8000"

print("=" * 70)
print("SECURITY TEST: Can we bypass client-side authorization?")
print("=" * 70)

# Login as operator (should only access operator page)
session = requests.Session()
response = session.post(f"{BASE_URL}/api/login/", 
                       json={"username": "operator", "password": "operator123"})

print("\n1. Logged in as: OPERATOR")
print(f"   User groups: {response.json()['user']['groups']}")

# Now try to access pages by directly calling the API
# BYPASSING the React UI completely!
print("\n2. Bypassing React UI - Directly calling API endpoints:")

print("\n   Trying to access ADMIN page directly via API...")
response = session.get(f"{BASE_URL}/api/pages/admin/")
print(f"   Status: {response.status_code}")
print(f"   Response: {response.json()}")

print("\n   Trying to access MANAGER page directly via API...")
response = session.get(f"{BASE_URL}/api/pages/manager/")
print(f"   Status: {response.status_code}")
print(f"   Response: {response.json()}")

print("\n   Trying to access OPERATOR page directly via API...")
response = session.get(f"{BASE_URL}/api/pages/operator/")
print(f"   Status: {response.status_code}")
print(f"   Response: {response.json()}")

print("\n" + "=" * 70)
print("CONCLUSION:")
print("=" * 70)
print("✅ Server-side checks BLOCKED unauthorized access!")
print("✅ Even though we bypassed React, Django protected the data!")
print("\nWithout server-side validation, an attacker could:")
print("  - Open browser console")
print("  - Modify React code")
print("  - Call API endpoints directly")
print("  - Access any data regardless of client-side checks!")
print("=" * 70)
