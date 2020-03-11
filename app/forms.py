from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email

class ProfileForm(FlaskForm):
    firstname = StringField('First Name',validators = [DataRequired()])
    lastname = StringField('Last Name',validators = [DataRequired()])
    gender = SelectField('Title', [DataRequired()],choices=[('Male', 'male'),('Female', 'female')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    location = StringField('Location',validators = [DataRequired()])
    biography = TextField('Biography',validators = [DataRequired()])