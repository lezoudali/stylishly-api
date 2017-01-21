import os

import pytest

from db.core.utils import create_engine, get_scoped_session

pytest_plugins = []


@pytest.fixture(scope='session')
def connection_params():
    return {
        'host': 'postgres',
        'port': 5432,
        'database': 'stylishly-test',
        'username': os.getenv('TEST_DB_USERNAME', 'stylishly'),
        'password': os.getenv('TEST_DB_PASSWORD', 'stylishly')
    }


@pytest.fixture(scope='function')
def session(connection_params):
    """Returns a SQLA database session"""
    engine = create_engine(**connection_params)
    connection = engine.connect()

    Session = get_scoped_session(connection)
    sess = Session()

    transaction = connection.begin()

    yield sess

    transaction.rollback()
    connection.close()
