from app import db
from datetime import datetime

class Shopping(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    createddate = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Shopping {}>'.format(self.name)