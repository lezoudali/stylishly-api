from __future__ import with_statement

import os
import sys
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool
from sqlalchemy.engine.url import URL

from db.core import metadata

sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__),
                '..', '..')))


# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def get_database_url():
    connection_params = {
        'username': os.getenv('STYLISHLY_DB_USERNAME'),
        'password': os.getenv('STYLISHLY_DB_PASSWORD'),
        'database': os.getenv('STYLISHLY_DB_DATABASE'),
        'host': os.getenv('STYLISHLY_DB_HOST', '127.0.0.1'),
        'port': 5432
    }

    return URL('postgresql', **connection_params)


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = get_database_url()

    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    alembic_config = config.get_section(config.config_ini_section)
    alembic_config['sqlalchemy.url'] = get_database_url()

    connectable = engine_from_config(
        alembic_config,
        prefix='sqlalchemy.',
        poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
