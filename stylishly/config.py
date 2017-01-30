from os import getenv


class Config(object):
    DEBUG = False
    HOST = getenv('STYLISHLY_HOST', '0.0.0.0')
    PORT = getenv('STYLISHLY_PORT', 80)
    SECRET_KEY = getenv('STYLISHLY_SECRET_KEY',
                        '30i3FNPCQMePwlUKPKyoo9OBbeo1mjDhoFdfQVjngEE=\n')
    # AUTH_HEADER_PREFIX = 'STYLISHLY-HMAC-SHA256'
    # AUTH_TIMESTAMP_HEADER = 'Unix-Timestamp'
    # REQUEST_LIFETIME = 30
    DB = {
        'username': getenv('STYLISHLY_DB_USERNAME'),
        'password': getenv('STYLISHLY_DB_PASSWORD'),
        'host': getenv('STYLISHLY_DB_HOST', '127.0.0.1'),
        'port': getenv('STYLISHLY_DB_PORT', '5432'),
        'database': getenv('STYLISHLY_DB_DATABASE')
    }
    # AWS_REGION = getenv('STYLISHLY_AWS_REGION', 'eu-central-1')
    # AWS_BUCKET = getenv('STYLISHLY_AWS_BUCKET', 'stylishly_media')
    # AWS_ACCESS_KEY = getenv('STYLISHLY_AWS_ACCESS_KEY')
    # AWS_SECRET_KEY = getenv('STYLISHLY_AWS_SECRET_KEY')


class DevelopmentConfig(Config):
    DEBUG = True
    PORT = getenv('STYLISHLY_PORT', 5000)
    # DB = {**Config.DB,
    #       'database': getenv('STYLISHLY_DEVELOPMENT_DB_DATABASE', 'stylishly_development')}
    # AWS_BUCKET = getenv('STYLISHLY_DEVELOPMENT_AWS_BUCKET', 'stylishly_media_development')
    # REQUEST_LIFETIME = 0  # don't check against replay attacks


# class ProductionConfig(Config):
#     AWS_BUCKET = getenv('STYLISHLY_PRODUCTION_AWS_BUCKET', 'stylishly_media_production')
#     DB = {**Config.DB,
#           'database': getenv('STYLISHLY_PRODUCTION_DB_DATABASE', 'stylishly_production')}


# class StagingConfig(ProductionConfig):
#     AWS_BUCKET = getenv('STYLISHLY_TESTING_AWS_BUCKET', 'stylishly_media_staging')
#     DB = {**ProductionConfig.DB,
#           'database': getenv('STYLISHLY_STAGING_DB_DATABASE', 'stylishly_staging')}


class TestingConfig(DevelopmentConfig):
    TESTING = True
    # AWS_BUCKET = getenv('STYLISHLY_TESTING_AWS_BUCKET', 'stylishly_media_testing')
    DB = {**DevelopmentConfig.DB,
          'database': getenv('STYLISHLY_TEST_DB_DATABASE')}
