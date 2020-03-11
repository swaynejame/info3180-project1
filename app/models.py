from . import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    email = db.Column(db.String(120))
    location = db.Column(db.String(80))
    biography = db.Column(db.String(500))
    photo = db.Column(db.String(80))

def __init__(self, firstname, lastname,gender, email, location, biography, photo):
    self.firstname = firstname
    self.lastname = lastname
    self.gender = gender
    self.email = email
    self.location = location
    self.biography = biography
    self.photo = picture

def __repr__(self):
    return '<User %r>' % self.username