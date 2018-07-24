# flask
SECRET_KEY = 'secretpassword'

# flask_mail_sendgrid
MAIL_DEFAULT_SENDER = 'john@doe.com'
MAIL_SENDGRID_API_KEY = 'someweirdapikey'

# flask_sqlalchemy
SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/boilerplate'
SQLALCHEMY_TRACK_MODIFICATIONS = True


# flask_security
SECURITY_EMAIL_SENDER = "john@doe.com"

SECURITY_PASSWORDLESS = False
SECURITY_CHANGEABLE = True
SECURITY_CONFIRMABLE = True
SECURITY_REGISTERABLE = True
SECURITY_RECOVERABLE = True
SECURITY_TRACKABLE = True

SECURITY_PASSWORD_SALT = 'password-salt'
SECURITY_CONFIRM_SALT = 'confirm-salt'
SECURITY_RESET_SALT = 'reset-salt'
SECURITY_LOGIN_SALT = 'login-salt'
SECURITY_REMEMBER_SALT = 'remember-salt'

SECURITY_LOGIN_URL = '/login/'
SECURITY_LOGOUT_URL = '/logout/'
SECURITY_REGISTER_URL = '/register/'
SECURITY_RESET_URL = '/reset/'
SECURITY_CHANGE_URL = '/change/'
SECURITY_CONFIRM_URL = '/confirm/'

SECURITY_TOKEN_MAX_AGE = 20 * 60
