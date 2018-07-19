from flask_classy import FlaskView


class LoginView(FlaskView):

    def index(self):
        return "Hello, this is the LoginView"
