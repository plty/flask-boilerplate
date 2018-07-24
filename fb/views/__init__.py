from fb.views import admin as AdminView
from fb.views.main import MainView


def register(app):
    AdminView.register(app)
    MainView.register(app)
