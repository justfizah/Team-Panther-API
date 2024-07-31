import requests
import pytest

BASE_URL = "https://deployment.api-expressjs.boilerplate.hng.tech"

def test_users_endpoint():
    response = requests.get(f"{BASE_URL}/api/v1/users")
    assert response.status_code == 200
    assert "users" in response.json()

def test_orders_endpoint():
    response = requests.get(f"{BASE_URL}/api/v1/orders")
    assert response.status_code == 200
    assert "orders" in response.json()
