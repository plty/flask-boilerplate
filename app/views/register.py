from flask_classy import FlaskView


class RegisterView(FlaskView):

    def index(self):
        return "Hello, this is the RegisterView"
