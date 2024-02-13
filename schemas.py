from marshmallow import Schema, fields

class PostSchema(Schema):
    id = fields.Int(dump_only=True)
    author = fields.Str(required=True)
    post = fields.Str(required=True)

class AccountSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)

class AuthAccount(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)