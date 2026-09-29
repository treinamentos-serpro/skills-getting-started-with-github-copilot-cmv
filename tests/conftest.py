import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities as app_activities
from src.app import app

_original_activities = copy.deepcopy(app_activities)


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    # Restore the in-memory "database" to its pristine state before every test
    app_activities.clear()
    app_activities.update(copy.deepcopy(_original_activities))
    yield
