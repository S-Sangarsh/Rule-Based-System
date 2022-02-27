from flask_restplus import Namespace, fields
from app.main.role.dto import RoleDto

class UserDto:
    role = RoleDto.role
    api = Namespace('user', description='user related operations')  # this comes in swagger ui page
    user = api.model('user', {
        'name': fields.String(required=True,max_length=25,description='user name'),
        'email_id':fields.String(required=True,max_length=25, description='user email address',pattern=r'[A-Za-z0-9._%+-]+@[A-Za-z]+\.[A-Za-z]'),
        'mobile_number': fields.String(required=True,max_length=12,min_length=10, description='user mobilennumber',pattern=r'[0-9]'),
        'role_id' :fields.Nested(role),
        'password':fields.String(required=True, description='passwords'),
        })




