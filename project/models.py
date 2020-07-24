# from sqlalchemy.dialects.postgresql import UUID

from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# import uuid
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    # id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True)
    password_hash = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    balance = db.Column(db.Integer, nullable=False)

    def __init__(self, username, password, balance, created_at):
        self.username = username
        self.balance = balance
        self.created_at = created_at
        self.set_password(password)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<username {}, created_at {}>'.format(self.username, self.created_at)

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'balance': self.balance
        }
