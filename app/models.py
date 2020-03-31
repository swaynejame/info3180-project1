from . import db
from datetime import date

class UserProfile(db.Model):
    __tablename__ = 'user_profile'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    email = db.Column(db.String(120))
    location = db.Column(db.String(80))
    biography = db.Column(db.String(500))
    photo = db.Column(db.String(80))
    current = date.today()
    # created_on = db.Column(db.DateTime, server_default=db.func.now())
    created_on = current.strftime("%B %d, %Y")

    def __init__(self, firstname, lastname,gender, email, location, biography, photo):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.email = email
        self.location = location
        self.biography = biography
        self.photo = photo

    def __repr__(self):
        return '<User %r>' % self.id