from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), index=True, unique=True, nullable=False)
    encrypted_password = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    postcode = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.name)

    def setPassword(self, encrypted_password):
        self.encrypted_password = generate_password_hash(encrypted_password)

    def checkPassword(self, encrypted_password):
        return check_password_hash(self.encrypted_password, encrypted_password)