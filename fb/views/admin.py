from flask_admin.contrib.sqla import ModelView
from fb import admin, db, models


def register(app):
    admin.add_view(ModelView(models.User, db.session))
    admin.add_view(ModelView(models.Role, db.session))
