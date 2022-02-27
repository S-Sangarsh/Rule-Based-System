import datetime
from app.shared.constants import STATUS_PASS, STATUS_FAIL, HTTP_STATUS_CODE_CREATE, HTTP_STATUS_CODE_BAD_REQUEST,HTTP_STATUS_CODE_FORBIDDEN, HTTP_STATUS_CODE_RESPONSE_SUCCESS
from app.main import db
from app.main.user.model import User
from app.main.role.model import Role




class UserService:
    @staticmethod
    def save_new_user(data):
        user = User.getByUserID(data.get('email_id',None))
        print(data)
        if not user:
            role = Role.getByRoleName(data.get('role_id',None).get('role_name',None))
            if not role:
                response_object = {
                    'status' : STATUS_FAIL,
                    'message':'Role Not Found'
                }
                return response_object, HTTP_STATUS_CODE_BAD_REQUEST       
            new_user = User(
                name=data.get('name',None),
                email_id=data.get('email_id',None),
                mobile_number=data.get('mobile_number',None),
                role_id=role.role_id,
                password=data.get('password',None))
            User.saveUser(new_user)
            response_object = {
                'status' : STATUS_PASS,
                'message':'Sucessfully Registered'
            }
            return response_object, HTTP_STATUS_CODE_CREATE
        response_object = {
            'status' : STATUS_FAIL,
            'message':'User already exist'
        }
        return response_object, HTTP_STATUS_CODE_BAD_REQUEST

    @staticmethod
    def get_user(email_id):
        user = User.getByUserID(email_id)
        if not user:
            response_object = {
               'status' : STATUS_FAIL,
               'message':'User Not Found'
           }
            return response_object, HTTP_STATUS_CODE_BAD_REQUEST
        response_object={
            'name':user.name,
            'email_id':user.email_id,
            'mobile_number':user.mobile_number,
            'role_id':{'role_name':Role.getByRoleId(role_id=user.role_id).role_name},
            'password':user.password_hash
            }
        return response_object, HTTP_STATUS_CODE_RESPONSE_SUCCESS
   
    @staticmethod
    def get_all_user():
        return User.getalluser()

    @staticmethod
    def update_status(email_id):
        user = User.getByUserID(email_id)
        if not user:
            response_object = {
                'status' : STATUS_FAIL,
                'message':'User Status for already changed'
            }
            return response_object, HTTP_STATUS_CODE_BAD_REQUEST
        if user.user_status=='Active':
            user.user_status='Inactive'
            User.commitUser()
            return {'message':'status changed'},HTTP_STATUS_CODE_RESPONSE_SUCCESS
        return {'message':'status changed'},HTTP_STATUS_CODE_RESPONSE_SUCCESS
        
    
    
    @staticmethod
    def getalluserbyPage(page):
        user = User.pagination(page)
        return user
    