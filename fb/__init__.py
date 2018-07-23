# flask
from flask import Flask
app = Flask(__name__)
app.config.from_pyfile('config.py')


# flask_mail_sendgrid
from flask_mail_sendgrid import MailSendGrid
mail = MailSendGrid(app)


# flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)


# flask_migrations
from flask_migrate import Migrate, MigrateCommand
migrate = Migrate(app, db)


# flask_security
from flask_security import Security, SQLAlchemyUserDatastore
from fb import models
user_datastore = SQLAlchemyUserDatastore(db, models.User, models.Role)
security = Security(app, user_datastore)


# flask_classy
from fb import views
views.register(app)
