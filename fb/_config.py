# flask
DEBUG = True
SECRET_KEY = ''

# flask_mail_sendgrid
MAIL_SENDGRID_API_KEY = ''

# flask_sqlalchemy
SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/boilerplate'
SQLALCHEMY_TRACK_MODIFICATIONS = True


# flask_security
SECURITY_CONFIRMABLE = True
SECURITY_REGISTERABLE = True
SECURITY_RECOVERABLE = True
SECURITY_TRACKABLE = True

SECURITY_PASSWORD_SALT = 'password-salt'
SECURITY_CONFIRM_SALT = 'confirm-salt'
SECURITY_RESET_SALT = 'reset-salt'
SECURITY_LOGIN_SALT = 'login-salt'
SECURITY_REMEMBER_SALT = 'remember-salt'

SECURITY_TOKEN_MAX_AGE = 20 * 60
