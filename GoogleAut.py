import requests

BASE_URL = "https://deployment.api-expressjs.boilerplate.hng.tech"
AUTH_ENDPOINT = "/api/v1/auth/google"
API_TOKEN = "your_access_token_here"

def test_google_auth_api():
    url = BASE_URL + AUTH_ENDPOINT  # Using concatenation here
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(url, headers=headers)
    
    # Check response status code
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    # Check that the response is in JSON format
    assert response.headers["Content-Type"] == "application/json", f"Expected 'application/json', got {response.headers['Content-Type']}"
    
    # Parse the JSON response
    data = response.json()
    
    # Check that the response contains expected fields
    assert "users" in data, "Expected 'users' in response JSON"
    assert isinstance(data["users"], list), "Expected 'users' to be a list"
    
    # Further checks on the 'users' list
    for user in data["users"]:
        assert "id" in user, "Expected 'id' in user data"
        assert "username" in user, "Expected 'username' in user data"

if __name__ == "__main__":
    test_google_auth_api()
    print("Google Auth API tests passed!")

