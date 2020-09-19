from flask import request
from flask_jwt_extended import jwt_required

from controllers.validaciones import *
from flask import request
#modulos del sistema
from models import *
from flask_restx import Resource

import datetime

class UserController(Resource):
    # BUSCAR un usuario por su id
    @jwt_required
    def get(self,id):
        user = User.query.get_or_404(id)
        return userSchema.dump(user)
    
    # ACTUALIZAR un usuario por su id validando los campos ingresados
    @jwt_required
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
        
    # eliminar un usuario por su id 
    @jwt_required        
    def delete(self,id):
        if validarIdUser(id):
            user = User.query.filter_by(id=id).first()
            db.session.delete(user)
            db.session.commit()
            return{"success":f"usuario de id {id}, eliminado exitosamente"}
        else:
            return {"error:"f"el usuario con id {id}, no se encuentra en la base de datos"}

class UserPostController(Resource):
    #Listar todos los usuarios
    @jwt_required
    def get(self):
        users = User.query.all()
        return usersSchema.dump(users)
    
    #validar un usuario validando el ingreso del movil ejm:+519xxxx
    @jwt_required
    def post(self):
        data = request.get_json()
        camposColumnas = ["nombre","apellido","password","email","movil","fechaNacimiento","foto","description","estado_id","sede_id","especialidad_id"]
        camposIguales=[]
        camposFaltantes=[]
        for campo in camposColumnas:
            if campo in data.keys():
                camposIguales.append(campo)
            else:
                camposFaltantes.append(campo)
        print(camposIguales)
        print(camposFaltantes)
        fotoDefault ="https://hackspaceimg.s3.amazonaws.com/person0.jpg"
        if len(camposColumnas) == len(camposIguales):
            if validarCaracteresAlfabeticos(data["nombre"]):
                nombre = data["nombre"]
            else:
                return {"error":"ingrese el nombre correctamente"}

            if validarCaracteresAlfabeticos(data["apellido"]):
                apellido = data["apellido"]
            else:
                return {"error":"ingrese el apellido correctamente"}

            if validarCorreo(data["email"]):
                email = data["email"]
            else:
                return {"error":"ingrese el email correctamente"}
                
            if validarMovil(data["movil"]).get("valor"):
                movil = data["movil"]
            else:
                mensaje=validarMovil(data["movil"]).get("mensaje")
                return {"error":""+mensaje}

            try:
                date_time_obj = datetime.datetime.strptime(data['fechaNacimiento'], '%Y-%m-%d')
            except Exception as ex:
                return {"error":str(ex)}
                
            if validarIdEstado(data['estado_id']):
                estado_id= data['estado_id']
            else:
                return {"error":"el estado no se encuentra en la base de datos"}
            if validarIdSede(data['sede_id']):
                    sede_id = data['sede_id']
            else:
                return {"error":"la sede no se encuentra en la base de datos"}
            if validarIdEspecialidad(data['especialidad_id']):
                especialidad_id = data['especialidad_id']
            else:
                return {"error":"la especialidad no se encuentra en la base de datos"}
            
            new_user = User(

                    nombre=nombre,
                    apellido=apellido,
                    password = data['password'],
                    email = email,
                    movil = movil,
                    fechaNacimiento = date_time_obj,
                    foto = data['foto'] if len(data['foto'])!=0 else fotoDefault,
                    description = data['description'],
                    estado_id = estado_id,
                    sede_id = sede_id,
                    especialidad_id = especialidad_id
                        )
            db.session.add(new_user)
            db.session.commit()
            return {"success":"usuario creado con exito","user":str(userSchema.dump(new_user))}
        else:
            return {"error": "falta ingresar los siguientes campos obligatorios: " + str(camposFaltantes)}

class UserOrderNameOrLastNameController(Resource):
  # LISTAR todos los usuarios por orden de apellido o nombre
    @jwt_required
    def get(self, nameOrLastName):
        if nameOrLastName == 'apellido' or nameOrLastName == 'nombre':
            users=''
            if nameOrLastName == 'apellido':
                users = User.query.order_by(User.apellido).all()
            if nameOrLastName == 'nombre':
                users = User.query.order_by(User.nombre).all()

            return usersSchema.dump(users)
        else:
            return {"error":"la opción ingresada es incorrecta- pruebe con: 'nombre' o 'apellido'"}

class UserListSpecializationController(Resource):
  # LISTAR todos los usuarios por su especialidad
    @jwt_required
    def get(self):
        data = request.get_json()
        idEspecializacion=data["idEspecialidad"]
        if validarIdEspecialidad(idEspecializacion):
            users= User.query.filter_by(especialidad_id=idEspecializacion).all()
            return usersSchema.dump(users)
        else:
            return {'error':'especialidad enviada no se encuentra en la base de datos'},400

class UserSearchController(Resource):
  # BUSCAR todos los usuarios ingresando algunas letras de su nombre
    @jwt_required
    def get(self, nombre):
        if validarCaracteresAlfabeticos(nombre):
            search =f'%{nombre}%'
            users = User.query.filter(User.nombre.like(search)).all()
            if len(users)!=0:
                return usersSchema.dump(users)
            else:
                return  {'error':f'no hay usuarios que contengan la cadena: {nombre}'},400
        else:
            return {'error':'la cadena debe contener solo letras'},400
class UserStateController(Resource):
  # LISTAR todos los usuarios por su estado
    @jwt_required
    def get(self):
        data = request.get_json()
        idEstado=data["idEstado"]

        if validarIdEstado(idEstado):
            if idEstado:
                users= User.query.filter_by(estado_id=idEstado).all()
            else:
                return {'error':'estado enviado no se encuentra en la base de datos'},400
            return usersSchema.dump(users)
        else:
            return {'error':'estado enviado no se encuentra en la base de datos'},400        
    
    @jwt_required
    def put(self):
        data = request.get_json()

        if validarIdUser(data['id']) and validarIdEstado(data['idEstado']):
            user = User.query.filter_by(id=data['id']).first()
            dic_user=userSchema.dump(user)
            if "idEstado" in data:
                user.estado_id = data['idEstado']
                if dic_user["estado_id"] == 1 and  data['idEstado']>1:
                    user.last_connection=datetime.datetime.now()
            else:
                return {'error':'nombre del campo incorrecto'},400

            db.session.commit()
            user = User.query.filter_by(id=data['id']).first()
            return userSchema.dump(user)
        else:
            return {'error':f'usuario {data["id"]} o estado {data["idEstado"]}, no se encuentra en la base de datos'},400

class UserLastConnectionController(Resource):
  # MOSTRAR la ultima conexion activa
    @jwt_required
    def get(self):
        
        data = request.get_json()
        if validarIdUser(data['idUser']):
            user = User.query.filter_by(id=data['idUser']).first()

            return userSchema.dump(user)
        else:
            return {'error':'usuario no encontrado en la base de datos'},400