from enum import unique
from ..utils import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    """User model"""

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(30), unique = True, nullable = False)
    password = db.Column(db.String(150), nullable = False)