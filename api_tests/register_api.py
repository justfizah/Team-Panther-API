import requests

BASE_URL = "https://deployment.api-expressjs.boilerplate.hng.tech"

# Authorization details
REGISTER_PAYLOAD = {
    "first_name": "haffy",
    "last_name": "zah",
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