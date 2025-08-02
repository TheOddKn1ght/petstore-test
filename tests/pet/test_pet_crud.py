def test_create_pet(api_client, pet_data):
    r = api_client.post("/pet", json=pet_data)
    assert r.status_code == 200
    body = r.json()
    assert body["name"] == pet_data["name"]
    assert body["status"] == pet_data["status"]

def test_get_pet(api_client, pet_data):
    r = api_client.get(f"/pet/{pet_data['id']}")
    assert r.status_code == 200
    body = r.json()
    assert body["id"] == pet_data["id"]
    assert body["name"] == pet_data["name"]

def test_find_pets_by_status(api_client, pet_data):
    r = api_client.get("/pet/findByStatus", params={"status": pet_data["status"]})
    assert r.status_code == 200
    body = r.json()
    assert isinstance(body, list)
    assert any(p["id"] == pet_data["id"] for p in body)

def test_update_pet(api_client, pet_data, updated_pet_data):
    r = api_client.put("/pet", json=updated_pet_data)
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "sold"
    assert body["name"] == updated_pet_data["name"]

def test_delete_pet(api_client, pet_data):
    r = api_client.delete(f"/pet/{pet_data['id']}")
    assert r.status_code == 200
    r_verify = api_client.get(f"/pet/{pet_data['id']}")
    assert r_verify.status_code == 404
