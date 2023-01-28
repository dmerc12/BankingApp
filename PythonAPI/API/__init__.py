from flask_bcrypt import Bcrypt
from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail


bcrypt = Bcrypt()
login_manager = LoginManager
def create_app(config_class=Config):
    app: Flask = Flask(__name__)
    app.config.from_object(Config)
    bcrypt.init(app)
    login_manager.init_app(app)