import pytest
from faker import Faker
import random

fake = Faker()

@pytest.fixture(scope="session")
def pet_data():
    return {
        "id": random.randint(1000000, 9999999),
        "name": fake.first_name(),
        "status": random.choice(["available", "pending", "sold"])
    }

def test_create_pet(api_client, pet_data):
    r = api_client.post("/pet", json=pet_data)
    assert r.status_code == 200
    body = r.json()
    assert body["name"] == pet_data["name"]
    assert body["status"] == pet_data["status"]

def test_get_pet(api_client, pet_data):
    api_client.post("/pet", json=pet_data)
    r = api_client.get(f"/pet/{pet_data['id']}")
    assert r.status_code == 200
    body = r.json()
    assert body["id"] == pet_data["id"]
    assert body["name"] == pet_data["name"]

def test_update_pet(api_client, pet_data):
    api_client.post("/pet", json=pet_data)
    updated = dict(pet_data, status="sold", name=fake.first_name())
    r = api_client.put("/pet", json=updated)
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "sold"
    assert body["name"] == updated["name"]

def test_delete_pet(api_client, pet_data):
    api_client.post("/pet", json=pet_data)
    r = api_client.delete(f"/pet/{pet_data['id']}")
    assert r.status_code == 200
    r_verify = api_client.get(f"/pet/{pet_data['id']}")
    assert r_verify.status_code == 404
