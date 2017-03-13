from flask_wtf import FlaskForm 
from flask_wtf.file import FileRequired, FileField, FileAllowed
from wtforms import StringField, PasswordField, SelectField, TextAreaField, TextField
from wtforms.validators import InputRequired

#from flask_uploads import UploadSet, IMAGES

#images=UploadSet('images',IMAGES)

class UpForm(FlaskForm):
    fname = TextField('First Name', validators=[InputRequired()])
    lname = TextField('Last Name', validators=[InputRequired()])
    uname = TextField('Username', validators=[InputRequired()])
    age = TextField('Age', validators=[InputRequired()])
    gender = SelectField('Gender',choices=[('Male','Male'),('Female','Female'),('Other','Other')])
    photo= FileField("Upload your photo",validators=[FileRequired(),
           FileAllowed(['jpg','png','gif'],'images only')])
    biography = TextAreaField('Biography', validators=[InputRequired()])