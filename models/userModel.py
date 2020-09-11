# importando el init
from . import db,ma
import datetime
from flask_bcrypt import generate_password_hash, check_password_hash
#Aqui ira los modelos a plantear
#la clase user creara la tabla users en la BD
class User(db.Model):
    __tablename__='users'
    id = db.Colum(db.Integer,primary_key=True)
    nombre = db.Column(db.String(45),nullable=False)
    apellido = db.Column(db.String(45),nullable=False)
    password = db.Column(db.String(115),nullable=False)
    email = db.Column(db.String(100),unique=True,nullable=False)
    movil = db.Comun(db.String(15), unique=True, nullable=False)
    fechaNacimiento = db.Column(db.Date, default=datetime.datetime.now())
    foto = db.Column(db.String(100),nullable=False)
    description = db.Column(db.Text(),nullable=False)
    estado_id = db.Column(db.Integer,db.ForeignKey('estados.id'))
    sede_id = db.Column(db.Integer, db.ForeignKey('sedes.id'))
    especialidad_id = db.Column(db.DateTime, db.ForeignKey('especialidades.id'))
    last_connection = db.Column(db.DateTime, default=datetime.datetime.now())
    
    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
class UserSchema(ma.Schema):
    
    class Meta:
        fields = ("id","nombre","apellido","password","email","movil",
                  "fechaNacimiento","foto","description","estado_id","sede_id",
                  "especialidad_id","last_connection")
        
 userSchema = UserSchema()
 usersSchema = UserSchema(many=True)
 
     