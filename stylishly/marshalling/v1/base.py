from marshmallow import fields
from marshmallow import Schema


class Base(Schema):

    id = fields.UUID(dump_only=True)
    created_at = fields.Integer(dump_only=True)
    updated_at = fields.Integer(dump_only=True)
