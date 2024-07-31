import requests

BASE_URL = "https://deployment.api-expressjs.boilerplate.hng.tech"

def prompt_user_details():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    return {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password
    }

def register_user(user_details):
    response = requests.post(f"{BASE_URL}/api/v1/auth/register", json=user_details)
    print("Register Response Status Code:", response.status_code)
    print("Register Response Text:", response.text)
    if response.status_code == 201:
        print("User registered successfully. Please check your email for OTP.")
        return response.json().get("access_token")
    elif response.status_code == 409:
        print("User already exists. Please use a different email.")
        return None
    else:
        print("Registration failed.")
        return None

def verify_otp(access_token):
    otp = input("Enter the OTP sent to your email: ")

    verify_payload = {
        "otp": otp,
        "token": access_token
    }

    response = requests.post(f"{BASE_URL}/api/v1/auth/verify-otp", json=verify_payload)
    print("Verify OTP Response Status Code:", response.status_code)
    print("Verify OTP Response Text:", response.text)
    if response.status_code == 200 and response.json().get("success"):
        print("OTP verified successfully.")
        return True
    else:
        print("OTP verification failed.")
        print(f"Details: {response.json()}")
        return False

def login_user(email, password):
    login_payload = {
        "email": email,
        "password": password
    }

    response = requests.post(f"{BASE_URL}/api/v1/auth/login", json=login_payload)
    print("Login Response Status Code:", response.status_code)
    print("Login Response Text:", response.text)
    if response.status_code == 200:
        print("Login successful.")
        return True
    else:
        print("Login failed.")
        return False

if __name__ == '__main__':
    user_details = prompt_user_details()
    access_token = register_user(user_details)
    if access_token:
        if verify_otp(access_token):
            if login_user(user_details["email"], user_details["password"]):
                print("User has been successfully registered, verified, and logged in.")
            else:
                print("Login failed.")
        else:
            print("OTP verification failed.")
    else:
        print("User registration failed.")
