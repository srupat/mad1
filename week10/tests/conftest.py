import pytest
from main import app
from application.database import db

@pytest.fixture(scope="module")
def client():
    print("Setting up client")
    client = app.test_client()
    ctx = app.app_context()
    ctx.push()

    yield client

    print("Cleaning up client")
    ctx.pop()

@pytest.fixture()
def init_database(scope="module"):
    print("setting up db")
    db.create_all()

    yield db

    print("Cleaning up db")
    db.drop_all()
