from app import db


class Driver(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.Integer)
    phone = db.Column(db.String)
    email = db.Column(db.String)

    def __repr__(self):
        return "Driver: {}".format(self.id)
