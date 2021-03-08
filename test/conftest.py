import pytest,sys
sys.path.append('../')
from app import app

@pytest.fixture
def client():
    client = app.test_client()
    return client
