from flask_classy import FlaskView


class BaseView(FlaskView):
    @classmethod
    def build_rule(cls, rule, method=None):
        rule = rule.replace('_', '-')
        return super().build_rule(rule, method)
