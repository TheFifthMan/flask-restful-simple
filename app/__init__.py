from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Configuration
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(Configuration[config_name])

    db.init_app(app)
    migrate.init_app(app,db)

    def init_app(self):
        pass

    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    
    return app
