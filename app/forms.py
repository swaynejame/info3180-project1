from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email

class ProfileForm(FlaskForm):
    firstname = StringField('First Name',validators = [DataRequired()])
    lastname = StringField('Last Name',validators = [DataRequired()])
    gender = SelectField('Title', [DataRequired()],choices=[('', 'Select Gender'),('male', 'Male'),('female', 'Female')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    location = StringField('Location',validators = [DataRequired()])
    biography = TextField('Biography',validators = [DataRequired()])
    photo = FileField('Profile Picture', validators=[FileRequired(),FileAllowed(['jpg', 'png', 'Images only!'])])