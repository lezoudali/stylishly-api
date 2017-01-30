from flask import current_app
from flask import Blueprint
from flask import jsonify
from webargs.flaskparser import use_args
from stylishly.marshalling.v1.user.schema import CreateUserSchema
from stylishly.marshalling.v1.user.schema import UserSchema
from db.models import User
from sqlalchemy.exc import IntegrityError


blueprint = Blueprint('users', __name__, url_prefix='/v1')


@use_args(CreateUserSchema())
def post(args):
    sess = current_app.db_session
    user = User(hashed_password='hashed_password',
                **UserSchema().dump(args).data)
    try:
        sess.add(user)
        sess.commit()
    except IntegrityError:
        sess.rollback()

    return jsonify(UserSchema().dump(user).data), 201, {}
