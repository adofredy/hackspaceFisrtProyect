import os

# VARIABLES DEL SERVICIO
os.environ["PORTA"]="85"
# en desarrollo
# os.environ["DEBUG"]="TRUE"
# en produccion
os.environ["DEBUG"]="FALSE"

# variables para la Base de Datos (por defecto sqlite)

# os.environ["BD"]          = ''
# os.environ["HOST"]        = ''
# os.environ["DATABASE"]    = ''
# os.environ["PORTBD"]        = ''
# os.environ["USER"]        = ''
# os.environ["PASSWORD"]    = ''


#probando mysql en mi local
os.environ["BD"]          = 'mysql'
os.environ["HOST"]        = 'localhost'
os.environ["DATABASE"]    = 'dtuser'
os.environ["PORTBD"]      = '3306'
os.environ["USER"]        = 'root'
os.environ["PASSWORD"]    = 'root'