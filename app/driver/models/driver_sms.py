from app import db
from datetime import datetime


class DriverSms(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(20))
    code = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return '< DriverSms {}>'.format(self.id)
