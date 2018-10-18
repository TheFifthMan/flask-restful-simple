from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    db.init_app(app)

    def init_app(self):
        pass

    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    
    return app
