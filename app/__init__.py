from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app.defaults import db
import app.models as models
import app.views as views


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)
    views.register(app)
    return app


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(128))
