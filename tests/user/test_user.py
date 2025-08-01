import pytest
from faker import Faker
import random

fake = Faker()

@pytest.fixture
def user_data():
    return {
        "id": random.randint(1000000, 9999999),
        "username": fake.user_name(),
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "email": fake.email(),
        "password": fake.password(),
        "phone": fake.phone_number(),
        "status": 1
    }

#TODO: separate to different tests
def test_create_user(api_client, user_data):
    r_create = api_client.post("/user", json=user_data)
    assert r_create.status_code == 200 #kinda meanigless since it's always 200 for some reason

    r_get = api_client.get(f"/user/{user_data['username']}")
    assert r_get.status_code == 200
    body = r_get.json()
    assert body["username"] == user_data["username"]
    assert body["email"] == user_data["email"]

    r_delete = api_client.delete(f"/user/{user_data['username']}")
    assert r_delete.status_code == 200

    r_verify = api_client.get(f"/user/{user_data['username']}")
    assert r_verify.status_code == 404
