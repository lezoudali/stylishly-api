import sqlalchemy as sa

from db.core import metadata, table_mixins

users_table = sa.Table(
    'users',
    metadata,
    sa.Column('email', sa.String(255), nullable=False, unique=True),
    sa.Column('hashed_password', sa.String(60), nullable=True),
    sa.Column('secret_key', sa.String(32), nullable=True),
    sa.Column('is_confirmed', sa.Boolean, nullable=False, default=False,
              server_default='0'),
    sa.Column('confirmation_token', sa.String(64), nullable=True),
    *table_mixins.base()
)
