import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


def unix_timestamp():
    """ Produces a BIGINT value of current UNIX timestamp """
    return sa.text('cast(EXTRACT(EPOCH FROM NOW()) as BIGINT)')


def int_pk():
    """ Used to add Integer primary key to the table """
    return (sa.Column('id', sa.Integer, primary_key=True), )


def uuid_pk():
    """ Used to add UUID v1 primary key to all tables.
    Requires uuid-ossp PostgreSQL module to be installed.
    See: https://www.postgresql.org/docs/9.5/static/uuid-ossp.html
    """
    return (sa.Column('id', UUID, primary_key=True,
                      server_default=sa.text('uuid_generate_v1()')), )


def timestamp():
    """ The function's purpose is to add `created_at` and `updated_at` columns
    to all tables.
    The values will be populated automatically on server side:
        - For `created_at` on INSERT;
        - For `updated_at` on INSERT and UPDATE.
    """
    return (
        sa.Column('created_at', sa.BigInteger,
                  default=unix_timestamp(),
                  server_default=unix_timestamp()),
        sa.Column('updated_at', sa.BigInteger,
                  default=unix_timestamp(),
                  server_default=unix_timestamp(),
                  onupdate=unix_timestamp(),
                  server_onupdate=unix_timestamp()),
    )


def base():
    """ The function returns base table mixin.
    It's used to add UUID v1 `id`, `created_at` and `updated_at` to all tables.
    """
    return uuid_pk() + timestamp()
