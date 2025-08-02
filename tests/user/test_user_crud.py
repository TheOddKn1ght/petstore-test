def test_create_user(api_client, user_data):
    r_post = api_client.post(f"/user", json=user_data)
    assert r_post.status_code == 200 # kinda meaningless since it's always 200 for some reason

def test_get_user(api_client, user_data):
    r_get = api_client.get(f"/user/{user_data['username']}")
    assert r_get.status_code == 200
    assert r_get.json()["username"] == user_data["username"]

def test_user_login(api_client, user_data):
    params = {
        "username": user_data["username"],
        "password": user_data["password"]
    }
    r_login = api_client.get("/user/login", params=params) # i f***ing hate this api
    assert r_login.status_code == 200
    body = r_login.json()
    assert "message" in body
    assert "logged in user session" in body["message"]

def test_user_logout(api_client):
    r_logout = api_client.get("/user/logout")
    assert r_logout.status_code == 200
    body = r_logout.json()
    assert body["code"] == 200
    assert body["message"] == "ok"

def test_update_user(api_client, user_data, fake):
    updated = dict(user_data, firstName=fake.first_name(), lastName=fake.last_name())
    r_update = api_client.put(f"/user/{user_data['username']}", json=updated)
    assert r_update.status_code == 200

    r_verify = api_client.get(f"/user/{user_data['username']}")
    assert r_verify.status_code == 200
    body = r_verify.json()
    assert body["firstName"] == updated["firstName"]
    assert body["lastName"] == updated["lastName"]

def test_delete_user(api_client, user_data):
    r_delete = api_client.delete(f"/user/{user_data['username']}")
    assert r_delete.status_code == 200

    r_verify = api_client.get(f"/user/{user_data['username']}")
    assert r_verify.status_code == 404
