from marshmallow import fields
from marshmallow import validate


def str_255_required():
    return fields.String(required=True,
                         validate=validate.Length(min=1, max=255))
