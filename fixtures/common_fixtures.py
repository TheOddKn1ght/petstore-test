import pytest
import random
from utils.api_client import ApiClient

@pytest.fixture(scope="session")
def pet_data(fake):
    return {
        "id": random.randint(1000000, 9999999),
        "name": fake.first_name(),
        "status": random.choice(["available", "pending", "sold"])
    }

@pytest.fixture(scope="session")
def updated_pet_data(pet_data, fake):
    return dict(pet_data, status="sold", name=fake.first_name())

@pytest.fixture(scope="session")
def user_data(fake):
    return {
        "id": random.randint(1000000, 9999999),
        "username": fake.user_name(),
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "email": fake.email(),
        "password": fake.password(),
        "phone": fake.phone_number(),
        "status": 1
    }
