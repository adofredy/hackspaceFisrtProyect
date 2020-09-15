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
    def put(self, id):

        data = request.get_json()
        
        if validarIdUser(id):
            user = User.query.filter_by(id=id).first()
            if "nombre" in data:
                if validarCaracteresAlfabeticos(data["nombre"]):
                        user.nombre = data["nombre"]
                else:
                    return {"error":"ingrese el nombre correctamente"}

            if "apellido" in data:
                if validarCaracteresAlfabeticos(data["apellido"]):
                    user.apellido = data["apellido"]
                else:
                    return {"error":"ingrese el apellido correctamente"}

            if "password" in data: user.password = data["password"]

            if "email" in data:
                if validarCorreo(data["email"]):
                    user.email = data["email"]
                else:
                    return {"error":"ingrese el email correctamente"}

            if "movil" in data:
                if validarMovil(data["movil"]).get("valor"):
                    user.movil = data["movil"]
                else:
                    mensaje=validarMovil(data["movil"]).get("mensaje")
                    return {"error":""+mensaje}

            if "fechaNacimiento" in data:
                try:
                    date_time_obj = datetime.datetime.strptime(data['fechaNacimiento'], '%Y-%m-%d')
                    user.fechaNacimiento = date_time_obj
                except Exception as ex:
                    return {"error":str(ex)}

            if "foto" in data: user.foto = data["foto"]

            if "description" in data: user.description = data["description"]

            if "estado_id" in data:
                if validarIdEstado(data['estado_id']):
                    user.estado_id= data['estado_id']
                else:
                    return {"error":"el estado no se encuentra en la base de datos"}

            if "sede_id" in data:
                if validarIdSede(data['sede_id']):
                    user.sede_id = data['sede_id']
                else:
                    return {"error":"la sede no se encuentra en la base de datos"}

            if "especialidad_id" in data:
                if validarIdEspecialidad(data['especialidad_id']):
                    user.especialidad_id = data['especialidad_id']
                else:
                    return {"error":"la especialidad no se encuentra en la base de datos"}

            db.session.commit()

            user = User.query.filter_by(id=id).first()
            return {"success":"usuario actualizado con exito","user":str(userSchema.dump(user))}
        else:
            return {"error":f"el usuario con id {id}, no se encuentra en la base de datos"}
        
    
    
    # ACTUALIZAR un usuario por su id validando los campos ingresados        
    def delete(self,id):
        if validarIdUser(id):
            user = User.query.filter_by(id=id).first()
            db.session.delete(user)
            db.session.commit()
            return{"success":f"usuario de id {id}, eliminado exitosamente"}
        else:
            return {"error:"f"el usuario con id {id}, no se encuentra en la base de datos"}
        


 