from app import db 
from werkzeug.security import generate_password_hash,check_password_hash


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),index=True,unique=True)
    email = db.Column(db.String(100),index=True,unique=True)
    about_me = db.Column(db.String(256))
    password_hash = db.Column(db.String(256))

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
    