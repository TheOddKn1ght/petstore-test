import pytest
from faker import Faker
import random

fake = Faker()

def test_get_store_inventory(api_client):
    r = api_client.get("/store/inventory")
    assert r.status_code == 200
    body = r.json()
    assert isinstance(body, dict), "response must be a JSON object"
    for key in ["available", "pending", "sold"]:
        assert key in body, f"missing key: {key}"
        assert isinstance(body[key], int), f"value for {key} should be an integer"

def test_order_pet(api_client):
    pet_id = random.randint(2000000, 2999999)
    pet_data = {"id": pet_id, "name": fake.first_name(), "status": "available"}
    r_pet = api_client.post("/pet", json=pet_data)
    assert r_pet.status_code == 200

    order_data = {
        "id": random.randint(3000000, 3999999),
        "petId": pet_id,
        "quantity": 1,
        "shipDate": "2025-07-31T00:00:00.000Z",
        "status": "placed",
        "complete": True
    }

    r_order = api_client.post("/store/order", json=order_data)
    assert r_order.status_code == 200
    order_body = r_order.json()
    assert order_body["petId"] == pet_id
    assert order_body["status"] == "placed"
    assert order_body["complete"] is True

    r_get = api_client.get(f"/store/order/{order_data['id']}")
    assert r_get.status_code == 200
    get_body = r_get.json()
    assert get_body["id"] == order_data["id"]
    assert get_body["petId"] == pet_id

    r_delete = api_client.delete(f"/store/order/{order_data['id']}")
    assert r_delete.status_code == 200
    r_delete_pet = api_client.delete(f"/pet/{pet_id}")
    assert r_delete_pet.status_code == 200
