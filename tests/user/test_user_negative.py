def test_get_nonexistent_user(api_client, nonexistent_username):
    r = api_client.get(f"/user/{nonexistent_username}")
    assert r.status_code == 404

def test_delete_nonexistent_user(api_client, nonexistent_username):
    r = api_client.delete(f"/user/{nonexistent_username}")
    assert r.status_code == 404

def test_create_user_with_empty_data(api_client, empty_user_data):
    r = api_client.post("/user", json=empty_user_data)
    assert r.status_code in (400, 405, 500)

def test_create_invalid_user(api_client, invalid_user_data, nonexistent_username):
    r = api_client.post("/user", json=invalid_user_data)
    assert r.status_code in (200, 400, 405, 500)
    r_verify = api_client.get(f"/user/{nonexistent_username}")
    assert r_verify.status_code == 404

def test_login_with_wrong_credentials(api_client, nonexistent_username):
    r = api_client.get(
        "/user/login",
        params={"username": nonexistent_username, "password": "wrongPass123"}
    )
    assert r.status_code in (200, 400, 401) #yet again stupid api!!!
    body = r.json()
    assert "message" in body
    assert "logged in user session" not in body["message"]
