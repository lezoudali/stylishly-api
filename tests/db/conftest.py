import os

import pytest

from db.core import metadata
from db.core.utils import create_engine, get_scoped_session

pytest_plugins = [
    'tests.db.fixtures.user',
]


@pytest.fixture(scope='session')
def connection_params():
    return {
        'username': os.getenv('STYLISHLY_TEST_DB_USERNAME'),
        'password': os.getenv('STYLISHLY_TEST_DB_PASSWORD'),
        'database': os.getenv('STYLISHLY_TEST_DB_DATABASE'),
        'host': os.getenv('STYLISHLY_TEST_DB_HOST', '127.0.0.1'),
        'port': 5432
    }


@pytest.fixture()
def session(connection_params):
    """Returns a SQLA database session"""
    engine = create_engine(**connection_params)
    connection = engine.connect()

    Session = get_scoped_session(connection)
    sess = Session()
    metadata.create_all(engine)

    transaction = connection.begin()

    yield sess

    transaction.rollback()
    connection.close()
    metadata.drop_all(engine)


@pytest.fixture()
def save_model(session):
    def save(model):
        session.add(model)
        session.commit()
    return save


@pytest.fixture(scope='session')
def compare_attributes():
    def compare(model, attrs_to_compare_against):
        for attr, val in attrs_to_compare_against.items():
            assert getattr(model, attr) == val
    return compare
