
import os
import logging
from flask import Flask
from stylishly.utils import http
from stylishly.api.utils import register_resources
from stylishly.api.v1.resources import api_resources as api_v1_resources
from db.core.utils import create_engine, get_scoped_session
from webargs.flaskparser import parser
from marshmallow import ValidationError


class App(Flask):
    def __init__(self, *args, db_session=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_db_session(db_session)

    @property
    def db_session(self):
        return self._db_session

    def set_db_session(self, db_session):
        self._db_session = db_session


def configure_logging(app):
    """Logging configuration """
    logger = logging.getLogger(app.logger_name)
    del logger.handlers[:]
    logging.basicConfig(
        level=logging.ERROR,
        format='[%(levelname)s] %(asctime)s|%(name)s:%(lineno)d  %(message)s',
        datefmt='%Y%m%d-%H:%M%p'
    )


def configure_from_default_config(app):
    config_name = os.getenv('STYLISHLY_ENV', 'development').lower().title()
    app.config.from_object('stylishly.config.{}Config'.format(config_name))
    app.logger.info('Config: %s', config_name)


def configure_app(app, config_obj=None):
    """ Flask application instance configuration """
    if config_obj:
        app.config.from_object(config_obj)
    else:
        configure_from_default_config(app)


def get_db_session(app):
    engine = create_engine(**app.config['DB'])
    Session = get_scoped_session(engine)

    return Session()


def init_api(app):
    register_resources(app, api_v1_resources)


def setup_error_handlers(app):
    @parser.error_handler
    def handle_error(err):
        if isinstance(err, ValidationError):
            headers = err.headers or {}
            http.abort(err.messages, err.status_code, headers=headers)
        http.abort({'error': str(err)}, 400)


def create_app(app_name='stylishly', config_obj=None):
    """ App factory """
    app = App(app_name)
    configure_app(app, config_obj=config_obj)
    configure_logging(app)
    app.set_db_session(get_db_session(app))
    init_api(app)
    setup_error_handlers(app)
    return app


# The application instance to use directly or by Gunicorn
app = create_app()


if __name__ == '__main__':
    app.run()
