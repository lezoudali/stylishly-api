from .public import users


api_resources = {
    users: {
        'index': ('/index', ['GET'], {})
    },
}
