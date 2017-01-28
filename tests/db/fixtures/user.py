import pytest

from db.user.model import User


@pytest.fixture()
def user_data():
    return dict(email='john_doe@example.com', hashed_password='test123',
                secret_key='it is very secret')


@pytest.fixture()
def user_model(user_data):
    return User(**user_data)
