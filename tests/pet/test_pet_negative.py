def test_get_nonexistent_pet(api_client, nonexistent_pet_id):
    r = api_client.get(f"/pet/{nonexistent_pet_id}")
    assert r.status_code == 404

def test_delete_nonexistent_pet(api_client, nonexistent_pet_id):
    r = api_client.delete(f"/pet/{nonexistent_pet_id}")
    assert r.status_code == 404

def test_create_invalid_pet(api_client, invalid_pet_data):
    r = api_client.post("/pet", json=invalid_pet_data)
    assert r.status_code in (400, 405, 500)

def test_update_nonexistent_pet(api_client, nonexistent_pet_id, fake):
    invalid_pet = {
        "id": nonexistent_pet_id,
        "name": fake.first_name(),
        "status": "available"
    }
    r = api_client.put("/pet", json=invalid_pet)
    assert r.status_code in (404, 500)

def test_find_by_invalid_status(api_client):
    invalid_status = "invalid_status"
    r = api_client.get("/pet/findByStatus", params={"status": invalid_status})
    assert r.status_code in (200, 400)
    if r.status_code == 200:
        assert isinstance(r.json(), list)
