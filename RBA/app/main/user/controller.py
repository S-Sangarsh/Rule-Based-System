from flask import request
from flask_restplus import Resource

from app.main.user.dto import UserDto
from app.main.user.service import UserService
from app.shared.logger import log


api = UserDto.api
_user = UserDto.user


# @api.route: A decorator to route resources
# api.expect: A decorator to Specify the expected input dto ( we have defined in dto file)

@api.route('/v1/user')
class UserList(Resource):
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(_user, envelope='data')   # filtering functionality
    def get(self):
        """List all registered users"""   #this comes as side of the swagger ui
        response_object = UserService.get_all_user()
        log.info(response_object)
        return response_object

    @api.response(201, 'User successfully created.')  # Will come in the Response Message section
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        log.info(f"New User is Registered:{data}")
        response_object = UserService.save_new_user(data=data)
        log.info(response_object)
        return response_object


@api.route('/v1/user/<email_id>')
@api.param('email_id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_user)
    def get(self, email_id):
        """get a user given its identifier"""
        log.info(f'The User_id give is:{email_id}')
        response_object = UserService.get_user(email_id)
        log.info(response_object)
        return response_object
    

    
    
        
        
        
@api.route('/v1/user/update/<email_id>')
@api.param('email_id', 'Update User Status')# reflect in the response messages
@api.response(404,'User not found.')# response message
class UpdateUserStatus(Resource):
    @api.doc('update a user status')
    @api.marshal_with(_user)
    def put(self, email_id):
        """Updating User Status"""
        log.info(f'The User_id for which has to be deactivated:{email_id}')
        response_object = UserService.update_status(email_id)
        log.info(response_object)
        return response_object

@api.route('/v1/user/<page>')
@api.param('page', 'Getting User by Page')# reflect in the response messages
class pagein(Resource):
    #@api.doc('update a user status')
    @api.marshal_with(_user) 
    def get(self,page):
        """Updating User Status"""
        #log.info(f'The User_id for which has to be deactivated:{email_id}')
        response_object = UserService.getalluserbyPage(page)
        print(response_object)
        return response_object


