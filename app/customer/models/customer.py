from app import db


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    phone = db.Column(db.String(50))

    def __repr__(self):
        return '<Customer {}>'.format(self.id)
