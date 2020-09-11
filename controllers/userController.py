from flask import request
from flask_jwt_extended import jwt_required

from flask import request

#modulos del sistema
from models import *

from flask_restx import Resource
import datetime

class UserController(Resource):
    # BUSCAR un usuario por su id
    def get(self,id):
        user = User.query.get_or_404(id)
        return userSchema.dump(user)
    # ACTUALIZAR un usuario por su id validando los campos ingresados        
    def delete(self,id):
        if validarIdUser(id):
            user = User.query.filter_by(id=id).first()
            db.session.delete(user)
            db.session.commit()
            return{"success":f"usuario de id {id}, eliminado exitosamente"}
        else:
            return {"error:"f"el usuario con id {id}, no se encuentra en la base de datos"}