# flask
DEBUG = True
SECRET_KEY = 'ifthisisnotsecretenoughidontknowwhatis'

# flask_mail_sendgrid
MAIL_SENDGRID_API_KEY = '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'

# flask_sqlalchemy
SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/boilerplate'
SQLALCHEMY_TRACK_MODIFICATIONS = True


# flask_security
SECURITY_PASSWORD_SALT = 'password-salt'
SECURITY_TOKEN_MAX_AGE = 20 * 60

SECURITY_CONFIRMABLE = True
SECURITY_REGISTERABLE = True
SECURITY_RECOVERABLE = True
SECURITY_TRACKABLE = True

# SECURITY_CONFIRM_SALT = 'confirm-salt'
# SECURITY_RESET_SALT = 'reset-salt'
# SECURITY_LOGIN_SALT = 'login-salt'
# SECURITY_REMEMBER_SALT = 'remember-salt'
