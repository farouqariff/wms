import requests
import json

BASE_URL = "http://localhost:8000"
session = requests.Session()

def print_result(title, response):
    print(f"\n{'='*50}")
    print(f"{title}")
    print(f"{'='*50}")
    print(f"Status Code: {response.status_code}")
    try:
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except:
        print(f"Response: {response.text}")

def test_user(username, password, expected_pages):
    print(f"\n\n{'#'*60}")
    print(f"# TESTING USER: {username}")
    print(f"{'#'*60}")
    
    # Login
    response = session.post(f"{BASE_URL}/api/login/", 
                           json={"username": username, "password": password})
    print_result(f"Login as {username}", response)
    
    if response.status_code != 200:
        print(f"❌ Login failed for {username}")
        return
    
    # Test each page
    pages = {
        "admin": f"{BASE_URL}/api/pages/admin/",
        "manager": f"{BASE_URL}/api/pages/manager/",
        "operator": f"{BASE_URL}/api/pages/operator/",
    }
    
    for page_name, url in pages.items():
        response = session.get(url)
        expected = "✓" if page_name in expected_pages else "✗"
        actual = "✓" if response.status_code == 200 else "✗"
        status = "✅ PASS" if expected == actual else "❌ FAIL"
        
        print_result(f"{status} - {page_name.upper()} page (Expected: {expected}, Got: {actual})", response)
    
    # Logout
    response = session.post(f"{BASE_URL}/api/logout/")
    print_result("Logout", response)

if __name__ == "__main__":
    print("\n" + "="*60)
    print("WMS AUTHENTICATION & AUTHORIZATION TEST")
    print("="*60)
    
    # Test 1: Admin user (should access all pages)
    test_user("admin", "admin123", ["admin", "manager", "operator"])
    
    # Test 2: Manager user (should only access manager page)
    test_user("manager", "manager123", ["manager"])
    
    # Test 3: Operator user (should only access operator page)
    test_user("operator", "operator123", ["operator"])
    
    print("\n" + "="*60)
    print("TEST COMPLETE!")
    print("="*60)
