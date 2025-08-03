import pytest
import random
from datetime import datetime
from faker import Faker

fake = Faker()

@pytest.fixture
def nonexistent_pet_id():
    return random.randint(9000000000, 9999999999)

@pytest.fixture
def invalid_pet_data():
    return {
            "id":"id"
    }

@pytest.fixture
def nonexistent_username():
    return f"nonexistent_user_{random.randint(1000000000, 9999999999)}"

@pytest.fixture
def invalid_user_data():
    return {
        "id": random.randint(10000000000, 99999999999),
        "firstName": fake.first_name(),
        "lastName": fake.last_name()
    }

@pytest.fixture
def empty_user_data():
    return {}

@pytest.fixture
def nonexistent_order_id():
    return random.randint(9000000000, 9999999999)

@pytest.fixture
def invalid_order_data():
    return {
        "id": random.randint(3000000000, 3999999999),
        "quantity": -1,
        "shipDate": datetime.now().isoformat(),
    }

@pytest.fixture
def empty_order_data():
    return {}

