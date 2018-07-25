from flask_admin.contrib.sqla import ModelView
from flask_security import current_user
from fb import admin
from fb import db, models


class AdminView(ModelView):
    def is_accessible(self):
        return current_user.has_role('admin')


def register(app):
    admin.add_view(AdminView(models.User, db.session))
    admin.add_view(AdminView(models.Role, db.session))
