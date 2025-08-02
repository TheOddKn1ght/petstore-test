import pytest
from faker import Faker
from utils.api_client import ApiClient

@pytest.fixture(scope="session")
def fake():
    return Faker()

@pytest.fixture(scope="session")
def base_url():
    return "https://petstore.swagger.io/v2"

@pytest.fixture(scope="session")
def api_client(base_url):
    return ApiClient(base_url)

pytest_plugins = [
    "fixtures.common_fixtures",
]

