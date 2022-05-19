from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager

from .config import Config
from .auth import auth

login_manager = LoginManager()
# login_manager.login_view= 'templates.inicio

def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap5(app)
    app.config.from_object(Config)
    # login_manager.init_app(app)
    app.register_blueprint(auth)

    return app

