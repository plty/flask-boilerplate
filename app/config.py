# flask
DEBUG = True
SECRET_KEY = 'ifthisisnotsecretenoughidontknowwhatis'

# flask_mail_sendgrid
MAIL_SENDGRID_API_KEY = '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'

# flask_sqlalchemy
SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/boilerplate'
SQLALCHEMY_TRACK_MODIFICATIONS = True


# flask_security
SECURITY_TRACKABLE = True

SECURITY_REGISTERABLE = True

SECURITY_PASSWORD_SALT = SECRET_KEY

SECURITY_TOKEN_MAX_AGE = 20 * 60
