from server import *
# aqui se importarian los modelos
from models import *

from controllers.userController import UserController
from controllers.loginController import LoginController

user = api.namespace('api',description='User Api')


login = api.namespace('api', description='Login API')
login.add_resource(LoginController, '/login')

if __name__ == "__main__":
	app.run(port=config["PORTAPI"], debug=config['DEBUG'])
 