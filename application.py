from server import *
# aqui se importarian los modelos
from models import *

from controllers.userController import UserController,UserPostController, UserOrderNameOrLastNameController,UserListSpecializationController, UserSearchController, UserStateController, UserLastConnectionController
from controllers.userController import UserController,UserPostController
from controllers.loginController import LoginController

user = api.namespace('api',description='User Api')
user.add_resource(UserPostController,'/user')
user.add_resource(UserController,'/user/<int:id>')

user.add_resource(UserOrderNameOrLastNameController,'/user/list/<string:nameOrLastName>')
user.add_resource(UserListSpecializationController,'/user/list/specialization')

user.add_resource(UserSearchController,'/user/search/<string:nombre>')
user.add_resource(UserStateController,'/user/state')

user.add_resource(UserLastConnectionController,'/user/active/connection')

login = api.namespace('api', description='Login API')
login.add_resource(LoginController, '/login')

if __name__ == "__main__":
	app.run(port=config["PORTAPI"], debug=config['DEBUG'])
 