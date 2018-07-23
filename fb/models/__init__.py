from fb import db
from flask_security import UserMixin, RoleMixin

# Define models
roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    # security-default
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    # security-confirmable
    confirmed_at = db.Column(db.DateTime(timezone=False))

    # security-trackable
    current_login_at = db.Column(db.DateTime(timezone=False))
    current_login_ip = db.Column(db.String(255))
    last_login_at = db.Column(db.DateTime(timezone=False))
    last_login_ip = db.Column(db.String(255))
    login_count = db.Column(db.Integer())

    # additional
    username = db.Column(db.String(255), unique=True)
