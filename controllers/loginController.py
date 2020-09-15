import datetime
from flask import request


from models import *
from flask_restx import Resource

class LoginController(Resource):
    # Logearse validando el email y password
    def post(self):
        data= request.get_json()
        email = data.get("email")
        password = data.get("password")
        
        user= User.query.filter_by(email=email).first()
        
        user1=userSchema.dump(user)
        
        authorized = True if user1['password']==password and user1['email']==email else False
        
        if not authorized:
            return {'error':'Email or password invalid'},401
        else:
            user.estado_id = 1
            db.session.commit()
        expires = datetime.timedelta(days=8)
        access_token = create_access_token(identity=str(1),expires_delta=expires)
        return {'token':access_token},200