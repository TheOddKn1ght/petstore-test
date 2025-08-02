def test_create_users_with_list(api_client, bulk_users):
    r_post = api_client.post("/user/createWithList", json=bulk_users)
    assert r_post.status_code == 200
    body = r_post.json()
    assert body["code"] == 200

    for user in bulk_users:
        r_get = api_client.get(f"/user/{user['username']}")
        assert r_get.status_code == 200
        fetched = r_get.json()
        assert fetched["username"] == user["username"]
        assert fetched["email"] == user["email"]

    for user in bulk_users:
        r_delete = api_client.delete(f"/user/{user['username']}")
        assert r_delete.status_code == 200

def test_create_users_with_array(api_client, bulk_users):
    r_post = api_client.post("/user/createWithArray", json=bulk_users)
    assert r_post.status_code == 200
    body = r_post.json()
    assert body["code"] == 200

    for user in bulk_users:
        r_get = api_client.get(f"/user/{user['username']}")
        assert r_get.status_code == 200
        fetched = r_get.json()
        assert fetched["username"] == user["username"]
        assert fetched["email"] == user["email"]

    for user in bulk_users:
        r_delete = api_client.delete(f"/user/{user['username']}")
        assert r_delete.status_code == 200
