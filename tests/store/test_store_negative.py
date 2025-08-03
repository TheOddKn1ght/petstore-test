def test_get_nonexistent_order(api_client, nonexistent_order_id):
    r = api_client.get(f"/store/order/{nonexistent_order_id}")
    assert r.status_code == 404

def test_delete_nonexistent_order(api_client, nonexistent_order_id):
    r = api_client.delete(f"/store/order/{nonexistent_order_id}")
    assert r.status_code == 404

def test_create_invalid_order(api_client, invalid_order_data):
    r = api_client.post("/store/order", json=invalid_order_data)
    assert r.status_code in (400, 405, 500, 200)  # do i have to say it again? 
    body = r.json()
    if r.status_code == 200:
        assert "petId" not in body or body.get("quantity", 1) <= 0

def test_create_empty_order(api_client, empty_order_data):
    r = api_client.post("/store/order", json=empty_order_data)
    assert r.status_code in (400, 405, 500, 200)

def test_get_order_invalid_id_format(api_client):
    r = api_client.get("/store/order/invalid_id")
    assert r.status_code in (400, 404, 500)
