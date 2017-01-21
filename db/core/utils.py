import sqlalchemy as sa
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import scoped_session, sessionmaker


def create_engine(**connection_params):
    """ Creates and returns a SQLAlchemy PostgreSQL engine from using options.

    Parameters:
        - host
        - port
        - database
        - username
        - password
        - query
    """
    return sa.create_engine(URL('postgresql', **connection_params))


def get_scoped_session(engine):
    """ Creates and returns a SQLAlchemy scoped session.

    Example of usage:

    ```
    Session = get_scoped_session(create_engine(**connection_params))
    my_session = Session()

    try:
        my_session.add(User())
        my_session.commit()
    except Exception as e:
        my_session.rollback()
        raise e
    ```
    """
    return scoped_session(sessionmaker(bind=engine))


def uuid_foreign_key_column(column_name, foreign_column,
                            default=None, **foreign_key_options):
    """ Helper function for foreign key definition.

    Example of usage:

    ```
    from ..utils import uuid_foreign_key_column
    media_table = sa.Table(
        'media',
        metadata,
        # ...
        uuid_foreign_key_column('author_id', 'user.id', ondelete='CASCADE')
        # ...
    )
    ```
    """
    fk_name = '{}__{}_fkey'.format(column_name,
                                   foreign_column.replace('.', '_'))
    fk_options = {'name': fk_name, **foreign_key_options}
    return sa.Column(column_name, UUID,
                     sa.ForeignKey(foreign_column, **fk_options),
                     default=default)
