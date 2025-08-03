import pytest
import random
import os

@pytest.fixture(scope="session")
def pet_data(fake):
    return {
        "id": random.randint(99999999, 9999999999),
        "name": fake.first_name(),
        "status": random.choice(["available", "pending", "sold"])
    }

@pytest.fixture(scope="session")
def updated_pet_data(pet_data, fake):
    return dict(pet_data, status="sold", name=fake.first_name())

@pytest.fixture
def sample_pet_image():
    media_dir = os.path.join(os.path.dirname(__file__), "..", "tests", "resources", "images")
    image_path = os.path.abspath(os.path.join(media_dir, "test_pet.jpg"))

    if not os.path.exists(image_path):
        pytest.skip("image not found in tests/media/")

    with open(image_path, "rb") as img:
        yield {"file": ("test_pet.jpg", img, "image/jpeg")}

@pytest.fixture(scope="session")
def user_data(fake):
    return {
        "username": fake.user_name(),
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "email": fake.email(),
        "password": fake.password(),
        "phone": fake.phone_number(),
        "status": 1
    }

@pytest.fixture(scope="session")
def store_pet_data(fake):
    return {
        "id": random.randint(9999999, 9999999999),
        "name": fake.first_name(),
        "status": "available",
    }

@pytest.fixture(scope="session")
def order_data(store_pet_data):
    return {
        "id": random.randint(3000000, 3999999),
        "petId": store_pet_data["id"],
        "quantity": 1,
        "shipDate": "2025-07-31T00:00:00.000Z",
        "status": "placed",
        "complete": True,
    }

@pytest.fixture
def bulk_users(fake):
    users = []
    for i in range(3):
        users.append({
            "username": fake.user_name(),
            "firstName": fake.first_name(),
            "lastName": fake.last_name(),
            "email": fake.email(),
            "password": fake.password(),
            "phone": fake.phone_number(),
            "userStatus": 1,
        })
    return users
