from flask_restplus import Namespace, fields


class RoleDto:
    api = Namespace('role', description='role related operations')
    role = api.model('role', {
        'role_name': fields.String(required=True,min_length =2, max_length = 20,description='role name'),
        })
