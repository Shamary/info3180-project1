from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, TextAreaField
from wtforms.validators import InputRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class UpForm(FlaskForm):
    fname = StringField('First Name', validators=[InputRequired()])
    lname = StringField('Last Name', validators=[InputRequired()])
    uname = StringField('Username', validators=[InputRequired()])
    age = StringField('Age', validators=[InputRequired()])
    gender = SelectField('Gender',choices=[('Male','Male'),('Female','Female'),('Other','Other')])
    biography = TextAreaField('Biography', validators=[InputRequired()])