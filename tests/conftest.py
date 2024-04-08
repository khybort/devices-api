import pytest
from fastapi.testclient import TestClient
from devices_api.main import app

from devices_api.core.database.postgresql.database import engine
from devices_api.core.models.postgres import models


client = TestClient(app)

@pytest.fixture(scope="function", autouse=True)
def run_around_tests():
    models.Base.metadata.create_all(engine)  # pylint: disable=no-member
    yield
    models.Base.metadata.drop_all(engine)  # pylint: disable=no-member