import uuid

from aiohttp.web_exceptions import HTTPNotFound
from aiohttp_apispec import docs, request_schema, response_schema

from app.crm.models import User
from app.crm.schemes import ListUsersResponseSchema, UserGetResponseSchema, UserAddSchema, UserGetRequestSchema
from app.web.app import View
from app.web.schemes import OkResponseSchema
from app.web.utils import json_response


class AddUserView(View):
    @docs(tags=['crm'], summary='Add new user', description='Add new user to database')
    @request_schema(UserAddSchema)
    @response_schema(OkResponseSchema, 200)
    async def post(self):
        data = self.request["data"]
        user = User(id_=uuid.uuid4(),
                    first_name=data['first_name'],
                    last_name=data['last_name'],
                    email=data['email'],
                    password=data['password'],
                    birthday=data['birthday']
                    )
        await self.request.app.crm_accessor.add_user(user)
        return json_response()


class ListUserView(View):
    @docs(tags=['crm'], summary='List user', description='List users from database')
    @response_schema(ListUsersResponseSchema, 200)
    async def get(self):
        users = await self.request.app.crm_accessor.list_users()
        raw_users = [{"id": str(user.id_),
                      "first_name": user.first_name,
                      "last_name": user.last_name,
                      "email": user.email,
                      "password": user.password,
                      "birthday": user.birthday} for user in users]
        return json_response(data={'users': raw_users})


class GetUserView(View):
    @docs(tags=['crm'], summary='Add new user', description='Add new user to database')
    @request_schema(UserGetRequestSchema)
    @response_schema(UserGetResponseSchema, 200)
    async def get(self):
        user_id = self.request.query["id"]
        user = await self.request.app.crm_accessor.get_user(uuid.UUID(user_id))
        if user:
            return json_response(data={"user": {"id": str(user.id_), "first_name": user.first_name,
                                       "last_name": user.last_name, "email": user.email,
                                       "password": user.password, "birthday": user.birthday}}
                                 )
        else:
            raise HTTPNotFound


class GetUserDeleteView(View):
    async def get(self):
        user_id = self.request.query["id"]
        user = await self.request.app.crm_accessor.delete_users(uuid.UUID(user_id))
        if user:
            return json_response(data={"user": {"user": user.first_name, "status": "DELETE"}})
        else:
            raise HTTPNotFound
