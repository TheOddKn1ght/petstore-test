def test_get_store_inventory(api_client):
    r = api_client.get("/store/inventory")
    assert r.status_code == 200
    body = r.json()
    assert isinstance(body, dict), "response must be a JSON object"
    for key in ["available", "pending", "sold"]:
        assert key in body, f"missing key: {key}"
        assert isinstance(body[key], int), f"value for {key} should be an integer"

def test_order_pet(api_client, store_pet_data, order_data):
    r_pet = api_client.post("/pet", json=store_pet_data)
    assert r_pet.status_code == 200

    r_order = api_client.post("/store/order", json=order_data)
    assert r_order.status_code == 200
    order_body = r_order.json()
    assert order_body["petId"] == store_pet_data["id"]
    assert order_body["status"] == "placed"
    assert order_body["complete"] is True

    r_get = api_client.get(f"/store/order/{order_data['id']}")
    assert r_get.status_code == 200
    get_body = r_get.json()
    assert get_body["id"] == order_data["id"]
    assert get_body["petId"] == store_pet_data["id"]

    r_delete_order = api_client.delete(f"/store/order/{order_data['id']}")
    assert r_delete_order.status_code == 200

    r_delete_pet = api_client.delete(f"/pet/{store_pet_data['id']}")
    assert r_delete_pet.status_code == 200
