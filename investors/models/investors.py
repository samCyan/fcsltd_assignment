

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Investor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(120), unique=True, nullable=False)
    location = db.Column(db.String(120), unique=True, nullable=False)
    latitude = db.Column(db.Numeric, nullable=False)
    longitude = db.Column(db.Numeric, nullable=False)

    def __repr__(self):
        return "<Investor %r>" % self.fullname
