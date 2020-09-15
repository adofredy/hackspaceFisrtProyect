from flask import Flask
from flask_restx import Api


app = Flask(__name__)



api = Api(
        app,
        title='Proyecto API CRUD Users',
        version='1.0',
        description='aplicacion CRUD',
    )

from utils.environment import Environment
config = Environment().configGeneral()