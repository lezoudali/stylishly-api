from marshmallow import fields
from marshmallow import validate
from marshmallow import ValidationError
from marshmallow import validates_schema
from ..base import Base


def password_field():
    return fields.String(required=True,
                         validate=validate.Length(min=6, max=255),
                         load_only=True)


class UserSchema(Base):
    email = fields.Email()
    password = password_field()
    confirm_password = password_field()

    @validates_schema
    def check_password_confirmation(self, data):
        try:
            if data['password'] != data['confirm_password']:
                raise ValidationError('Passwords are not equal.',
                                      'confirm_password')
        except KeyError:
            pass


def CreateUserSchema(UserSchema):

    class Meta(object):
        strict = True
