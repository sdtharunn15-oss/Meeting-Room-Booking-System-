import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)


import pytest
from fastapi.testclient import TestClient

from main import app
from database import Base, engine


Base.metadata.create_all(bind=engine)


@pytest.fixture
def client():
    return TestClient(app)