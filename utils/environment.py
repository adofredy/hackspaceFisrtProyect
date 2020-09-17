import os
import os.path

from distutils.util import strtobool
if os.path.isfile('utils/env.py'):
    import utils.env

class Environment():

    def configGeneral(self):
        return {
            "PORTAPI": int(os.environ["PORTA"]),
            'DEBUG': strtobool(os.environ["DEBUG"])
        }

    def settingsBD(self):
        return{
            'BD': os.environ["BD"],
            'HOST': os.environ["HOST"],
            'DATABASE': os.environ["DATABASE"],
            'PORTBD': int(os.environ["PORTBD"]),
            'USER': os.environ["USER"],
            'PASS': os.environ["PASSWORD"],
        }