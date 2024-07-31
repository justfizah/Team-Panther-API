import requests

BASE_URL = "https://deployment.api-expressjs.boilerplate.hng.tech"

# Authorization details
REGISTER_PAYLOAD = {
    "first_name": "haffy",
    "last_name": "zah",
    "email": "lefiw61192@hostlace.com",
    "password": "Ltaf@1ert88"
}

LOGIN_PAYLOAD = {
    "email": "lefiw61192@hostlace.com",
    "password": "Ltaf@1ert88"
}

def test_register_endpoint():
    response = requests.post(f"{BASE_URL}/api/v1/auth/register", json=REGISTER_PAYLOAD)
    print("Register Response Status Code:", response.status_code)
    print("Register Response Text:", response.text)
    if response.status_code == 409:
        print("User already exists, proceeding with login.")
    else:
        assert response.status_code == 201, f"Expected status code 201 but got {response.status_code}"

def test_login_endpoint():
    # First, register the user (this can be done in a setup step)
    test_register_endpoint()

    response = requests.post(f"{BASE_URL}/api/v1/auth/login", json=LOGIN_PAYLOAD)
    print("Login Response Status Code:", response.status_code)
    print("Login Response Text:", response.text)
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

def get_token():
    response = requests.post(f"{BASE_URL}/api/v1/auth/login", json=LOGIN_PAYLOAD)
    print("Login Response Status Code:", response.status_code)
    print("Login Response Text:", response.text)
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    return response.json()['token']

def test_verify_otp_endpoint():
    token = get_token()

    verify_payload = {
        "otp": 282831,  # Use the correct OTP for verification
        "token": token
    }

    response = requests.post(f"{BASE_URL}/api/v1/auth/verify-otp", json=verify_payload)
    print("Verify OTP Response Status Code:", response.status_code)
    print("Verify OTP Response Text:", response.text)
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    assert "success" in response.json()

if __name__ == '__main__':
    test_register_endpoint()
    test_login_endpoint()
    test_verify_otp_endpoint()
