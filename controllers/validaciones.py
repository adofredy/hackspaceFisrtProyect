import datetime
import re
from models import *
#aqui iran algunas validaciones de los campos a consultar por postman

# validar que el id del usuario enviado se encuentre en la base de datos
def validarIdUser(idUser):
    user=User.query.with_entities(User.id)
    lista=usersSchema.dump(user)
    ids=[]
    for diccionario in lista:
        for key, value in diccionario.items():
            ids.append(value)
    if idUser in ids:
        return True
    else:
        return False
# validar que el id del estado enviado se encuentre en la base de datos
def validarIdEstado(idEstado):
    estado = Estado.query.with_entities(Estado.id)
    lista = estadosSchema.dump(estado)
    ids=[]
    for diccionario in lista:
        for key, value in diccionario.items():
            ids.append(value)
    if idEstado in ids:
        return True
    else:
        return False
    
# validar que el id de especialidad enviado se encuentre en la base de datos
def validarIdEspecialidad(idEspecialidad):
    especialidad = Especialidad.query.with_entities(Especialidad)
    lista=especialidadesSchema.dump(especialidad)
    ids=[]
    for diccionario in lista:
        for key, value in diccionario.items():
            ids.append(value)
    if idEspecialidad in ids:
        return True
    else:
        return False
# validar Movil
def validarMovil(movil):
    if len(movil) == 12:
        if movil[:4]=="+519":
            if movil[4:].isnumeric():
                return {"valor":True,"mensaje":"movil correcto"}
            else:
                return {"valor":False,'mensaje':'ingresar solo numeros del 0 al 9'}
        else:
            return {"valor":False, 'mensaje':'el codigo postal es +51 y el movil debe comenzar con 9'}
    else:
        return {"valor":False, 'mensaje':'tamano demasiado grande para el movil'}

# validar que el nombre y apellido sea puras letras
def validarCaracteresAlfabeticos(palabra):
    palabra = palabra.replace(' ','')
    if palabra.isalpha():
        return True
    else:
        return False
    
# validar el correo
def validarCorreo(email):
    if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$', email.lower()):
        return True
    else:
        return False
    
# validar sede
def validarIdSede(idSede):
    sede=Sede.query.with_entities(Sede.id)
    lista=sedesSchema.dump(sede)
    ids=[]
    for diccionario in lista:
        for key, value in diccionario.items():
            ids.append(value)
            
    if idSede in ids:
        return True
    else:
        return  False