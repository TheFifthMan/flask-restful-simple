from flask_restful import Resource
from flask import jsonify,request
from .models import User
from app import db

class RegisterResource(Resource):
    def post(self):
        args = request.json
        username = args['username']
        email = args['email']
        about_me = args.get('about_me','')
        password = args['password']
        password2 = args['password2']
      
        if password != password2:
            return jsonify({"message":"password not matched"})
        
        u = User(username=username,email=email,about_me=about_me)
        u.set_password(password)
        db.session.add(u)
        db.session.commit()
        return jsonify({"message":'add user successful'})