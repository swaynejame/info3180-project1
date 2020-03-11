from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Email

class ProfileForm(FlaskForm):
    name = StringField('Name',validators = [DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    subject = StringField('Subject',validators = [DataRequired()])
    message = TextField('Message',validators = [DataRequired()])
    send = SubmitField('Send')