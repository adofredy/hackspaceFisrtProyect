from flask import Flask
from flask_restx import Api

from flask_bcrypt import Bcrypt#JWT
from flask_jwt_extended import JWTManager#JWT

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = "HolaMensajedePruebas"#JWT
app.config['JWT_ALGORITHM'] = "HS256"#JWT

bcrypt = Bcrypt(app)
jwt = JWTManager(app)

api = Api(
        app,
        title='Proyecto API CRUD Users',
        version='1.0',
        description='aplicacion CRUD',
    )

from utils.environment import Environment
config = Environment().configGeneral()