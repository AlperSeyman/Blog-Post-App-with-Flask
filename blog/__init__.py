import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = " " # os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = f'' # os.enviroen.get('SQLALCHEMY_DATABASE_URI')

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "users.login_page"
login_manager.login_message_category = "info"

app.config['MAIL_SERVER'] = ''
app.config['MAIL_PORT'] = ''
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = '' # os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = '' # os.environ.get('MAIL_PASSWORD')
mail = Mail(app)


from blog.main.routes import main
from blog.users.routes import users
from blog.posts.routes import posts
from blog.errors.handlers import errors

app.register_blueprint(main)
app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(errors)