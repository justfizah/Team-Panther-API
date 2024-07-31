import requests

BASE_URL = "https://deployment.api-expressjs.boilerplate.hng.tech"

# Registration payload
REGISTER_PAYLOAD = {
    "first_name": "haffy",
    "last_name": "zah",
    "email": "lefiw61192@hostlace.com",
    "password": "Ltaf@1ert88"
}

def register_user():
    response = requests.post(f"{BASE_URL}/api/v1/auth/register", json=REGISTER_PAYLOAD)
    print("Register Response Status Code:", response.status_code)
    print("Register Response Text:", response.text)
    if response.status_code == 201:
        print("User registered successfully. Please check your email for OTP and token.")
    elif response.status_code == 409:
        print("User already exists. Proceeding with OTP verification.")
    else:
        print("Registration failed.")
        return False
    return True

def verify_otp():
    otp = input("Enter the OTP sent to your email: ")
    token = input("Enter the token sent to your email: ")

    verify_payload = {
        "otp": otp,
        "token": token
    }

    response = requests.post(f"{BASE_URL}/api/v1/auth/verify-otp", json=verify_payload)
    print("Verify OTP Response Status Code:", response.status_code)
    print("Verify OTP Response Text:", response.text)
    if response.status_code == 200 and response.json().get("success"):
        print("OTP verified successfully.")
        return True
    else:
        print("OTP verification failed.")
        return False

def login_user():
    login_payload = {
        "email": REGISTER_PAYLOAD["email"],
        "password": REGISTER_PAYLOAD["password"]
    }

    response = requests.post(f"{BASE_URL}/api/v1/auth/login", json=login_payload)
    print("Login Response Status Code:", response.status_code)
    print("Login Response Text:", response.text)
    if response.status_code == 200:
        print("Login successful.")
    else:
        print("Login failed.")

if __name__ == '__main__':
    if register_user():
        if verify_otp():
            login_user()
