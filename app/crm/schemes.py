from marshmallow import Schema, fields
from app.web.schemes import OkResponseSchema



class UserAddSchema(Schema):
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    birthday = fields.Str(required=True)


class UserSchema(UserAddSchema):
    id = fields.UUID(required=True)


class UserGetRequestSchema(Schema):
    id = fields.UUID(required=True)


class UserGetSchema(Schema):
    user = fields.Nested(UserSchema)


class UserGetResponseSchema(OkResponseSchema):
    data = fields.Nested(UserGetSchema)


class ListUserSchema(Schema):
    users = fields.Nested(UserSchema, many=True)


class ListUsersResponseSchema(OkResponseSchema):
    data = fields.Nested(ListUserSchema)
