from flask_classy import FlaskView


class MainView(FlaskView):
    route_base = '/'

    def index(self):
        return "Hello, this is the MainView"

    def otto(self):
        return "hai kamu"
