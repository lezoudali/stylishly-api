import os

import pytest

from db.core.utils import create_engine, get_scoped_session

pytest_plugins = []


@pytest.fixture(scope='session')
def database_connection_params():
    return {
        'username': os.getenv('STYLISHLY_TEST_DB_USERNAME', 'stylishly'),
        'password': os.getenv('STYLISHLY_TEST_DB_PASSWORD', 'stylishly'),
        'database': os.getenv('STYLISHLY_TEST_DB_DATABASE', 'stylishly'),
        'host': os.getenv('STYLISHLY_TEST_DB_HOST', '127.0.0.1'),
        'port': 5432
    }


@pytest.fixture(scope='function')
def session(database_connection_params):
    """Returns a SQLA database session"""
    engine = create_engine(**database_connection_params)
    connection = engine.connect()

    Session = get_scoped_session(connection)
    sess = Session()

    transaction = connection.begin()

    yield sess

    transaction.rollback()
    connection.close()
