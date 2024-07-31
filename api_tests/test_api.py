import requests
import pytest

BASE_URL = "https://deployment.api-expressjs.boilerplate.hng.tech"

# Example payloads
REGISTER_PAYLOAD = {
    "first_name": "fat",
    "last_name": "gat",
    "email": "ronot41523@maxturns.com",
    "password": "Ltaf@1ert"
}

LOGIN_PAYLOAD = {
    "email": "ronot41523@maxturns.com",
    "password": "Ltaf@1ert"
}

# Assuming we need to perform login first to get the token for other requests
def get_token():
    response = requests.post(f"{BASE_URL}/api/v1/auth/login", json=LOGIN_PAYLOAD)
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    response_json = response.json()
    assert "token" in response_json, f"Expected 'token' key in response but got {response_json}"
    return response_json["token"]

# Tests for the endpoints
def test_register_endpoint():
    response = requests.post(f"{BASE_URL}/api/v1/auth/register", json=REGISTER_PAYLOAD)
    print("Register Response Status Code:", response.status_code)
    print("Register Response Text:", response.text)
    assert response.status_code == 201, f"Expected status code 201 but got {response.status_code}"

def test_login_endpoint():
    response = requests.post(f"{BASE_URL}/api/v1/auth/login", json=LOGIN_PAYLOAD)
    print("Login Response Status Code:", response.status_code)
    print("Login Response Text:", response.text)
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

def test_verify_otp_endpoint():
    token = get_token()
    AUTH_PAYLOAD = {
        "otp": 120735,  # Ensure this OTP is valid
        "token": token
    }
    response = requests.post(f"{BASE_URL}/api/v1/auth/verify-otp", json=AUTH_PAYLOAD)
    print("Verify OTP Response Status Code:", response.status_code)
    print("Verify OTP Response Text:", response.text)
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

# Run the tests
if __name__ == "__main__":
    pytest.main(["-v"])
