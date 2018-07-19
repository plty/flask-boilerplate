from app.views.main import MainView
from app.views.login import LoginView
from app.views.register import RegisterView


def register(app):
    MainView.register(app)
    LoginView.register(app)
    RegisterView.register(app)
