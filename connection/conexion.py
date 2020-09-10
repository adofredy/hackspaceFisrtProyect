from utils.environment import Environment

class ConnexionBD(Environment):

    def __init__(self):
        # obtener los valores de las variables de entorno
        data = self.settingsBD()
        # iniciando variables privadas
        self.__BD = data["BD"]
        self.__HOST = data["HOST"]
        self.__DATABASE = data["DATABASE"]
        self.__PORT = data["PORTBD"]
        self.__USER = data["USER"]
        self.__PASS = data["PASS"]
        # variables de configuracion de alchemy
        self.__TRACK_MODIFICATIONS = False
        self.__ECHO = True

    # funcion para obtener los datos para la conexion a la Base de datos
    def runDB(self):
        #diccionario de los tipos de base de datos a ejecutar
        dbConexion={
            "sqlLite"   : self.__sqlLite(),
            "mysql"     : self.__mysql(),
        }

        return {
            "URI": dbConexion[self.__BD],
            "TRACK_MODIFICATIONS": self.__TRACK_MODIFICATIONS,
            "ECHO": self.__ECHO
        }
    # funcion que retornara la uri de conexion a sqlite
    def __sqlLite(self):
        return "sqlite:///TESTSQ.db"

    # funcion que retornara la uri de conexion a mysql
    def __mysql(self):
        return f"mysql+mysqlconnector://{self.__USER}:{self.__PASS}@{self.__HOST}:{self.__PORT}/{self.__DATABASE}"


# instanciando la clase ConnexionBD
connexionBD = ConnexionBD().runDB()
print(connexionBD)