from flask import render_template
from fb.views.base import BaseView


class MainView(BaseView):
    route_base = '/'

    def index(self):
        return "Hello, this is the MainView"

    def weird_page(self):
        return render_template('some_weird_template.html')
