from flask import request
from flask_restplus import Resource

from app.main.role.dto import RoleDto
from app.main.role.service import RoleService
from app.main.role.model import Role
from app.shared.logger import log

api = RoleDto.api
_role = RoleDto.role


@api.route('/v1/role')
class RoleList(Resource):
    @api.doc('list_of_registered_roles')
    @api.marshal_list_with(_role, envelope='data')   # filtering functionality
    def get(self):
        """List all registered Roles"""   #this comes as side of the swagger ui
        response_object = RoleService.get_all_roles()
        log.info(response_object)
        return response_object

    @api.response(201, 'Role successfully created.')  # Will come in the Response Message section
    @api.doc('create a Role user')
    @api.expect(_role, validate=True)
    def post(self):
        """Creates a new Role """
        data = request.json
        log.info(f"New Role is Registered:{data}")
        response_object = RoleService.save_new_role(data=data)
        log.info(response_object)
        return response_object

    

@api.route('/v1/role/<role_name>')
@api.param('role_name', 'Update Role Status')# reflect in the response messages
@api.response(404,'Role not found.')# response message
class UpdateRoleStatus(Resource):
    @api.doc('update a role status')
    @api.marshal_with(_role)
    def put(self, role_name):
        """Updating Role Status"""
        log.info(f'The Role_id for which has to be deactivated:{role_name}')
        response_object = RoleService.update_status(role_name)
        log.info(response_object)
        return response_object
    





