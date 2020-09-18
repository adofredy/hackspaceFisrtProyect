# hackspaceFisrtProyect
#objetivo
API REST para ver la información de todo el grupo de Usuarios en TI (5 especialidades), delimitado por sedes, así como ver el estado de conexion , y dando la posibilidad que cada uno de ellos pueda editar su
Perfil. 

#Primeras Etapas del API

#paso 0:preparacion de ambiente de desarrollo y descarga de librerias en py3.8
#paso 1: Determinacion de carpetas del proyecto
#paso 1: Armado de la logica Ppal de Flask
#paso 2: Preparacion de Crud de Users
#paso 3: Validaciones de APIS en campos
#paso 4: seguridad de API (JWT)
#paso 5: TestUnitarios (no automatizados) - Postman
#Objetivos
#1 semana armado de logica de la API y conexiones
#2 semana pruebas en (inserciones)BD y Postman
#Herramientas
#Flask / Python / SQLALCHEMY / MYSQL / POstman

#REST API

API - Validar Usuario
🔔 Criterios - Formulario de Login
Validar ingreso en base a correo y password
Aplicar concepto de Json Token

API - Crear Usuario
🔔 Criterios - Formulario de Registro
Se debe guardar el año de nacimiento.
El número movil debera guardar el formato+519XXXXXXXX. Debe validar el ingreso de solo
números del 0 al 9.
Nombre y apellidos por separado.
Debe poder editar sus datos de registro.
Debe poder subir o cambiar su foto(en CDN) y tener una por defecto.
Validaciones en los datos de ingresos.

API List ALL Usuario
🔔 Criterios - View Principal
Devolver una lista de todos los usuarios el cual puede tener especialización y un orden especifico.
Devolver lista de usuario de acuerdo al campo de busqueda que seria el nombre.
todos los usuarios en relacion con su id de la especializacion:

1 back-end
2 front-end
3 diseñador-ux
4 desarrollor mobile
5 devOps
>=6 error:
{'error':'especialidad enviada no se encuentra en la base de datos'}

API Ver Usuario
🔔 View Detalle de Usuario

Devolver los datos de acuerdo al userID.
Devolver referencia de imagen en CDN

API Cambios de Estado
🔔 Criterios - Cambios de estado por usuario
Deberas devolver la lista de usuarios conectados y desconectados.
Deberas decidir en mostrar información de ultima conexión activa.
Debera existir un api para cambiar el estado del agente.
Se deberan definir los estados "Conectado, Ocupado, Ausente, No Disponible, Desconectado"
Se recuerda que los estados en relacion con su id son:

1 'conectado'
2 'ocupado'
3 'ausente'
4 'no_disponible'
5 'desconectado'