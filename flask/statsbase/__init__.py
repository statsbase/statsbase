from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from statsbase.config import Config
import os

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from statsbase.users.routes import users
    from statsbase.posts.routes import posts
    from statsbase.api.routes import api
    from statsbase.main.routes import main
    from statsbase.errors.handlers import errors
    from statsbase.teams.routes import teams
    from statsbase.players.routes import players
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(api)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    app.register_blueprint(teams)
    app.register_blueprint(players)

    return app

