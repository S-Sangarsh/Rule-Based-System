import datetime
from app.shared.constants import STATUS_PASS, STATUS_FAIL, HTTP_STATUS_CODE_CREATE, HTTP_STATUS_CODE_BAD_REQUEST,HTTP_STATUS_CODE_FORBIDDEN, HTTP_STATUS_CODE_RESPONSE_SUCCESS
from app.main import db
from app.main.role.model import Role

class RoleService:
 
    @staticmethod
    def save_new_role(data):
        role = Role.getByRoleName(data.get('role_name',None))
        if not role:
            new_role = Role(role_name=data['role_name'])
            Role.saveRole(new_role)
            response_object = {
             'status' : STATUS_PASS,
             'message':'Sucessfully Registered'
             }
            return response_object, HTTP_STATUS_CODE_CREATE
        response_object = {'status' : STATUS_FAIL,'message':'User already exist'}
        return response_object, HTTP_STATUS_CODE_BAD_REQUEST

    @staticmethod
    def get_all_roles():
        return Role.getallrole()

    @staticmethod
    def update_status(role_name):
        role = Role.getByRoleName(role_name)
        if not role:
            response_object = {
                'status' : STATUS_FAIL,
                'message':'User Status for already changed'
            }
            return response_object, HTTP_STATUS_CODE_BAD_REQUEST
        if role.role_status=='Active':
           role.role_status='Inactive'
           Role.commitRole()
           return {'message':'status changed'},HTTP_STATUS_CODE_RESPONSE_SUCCESS
        return {'message':'status changed'},HTTP_STATUS_CODE_RESPONSE_SUCCESS
        
