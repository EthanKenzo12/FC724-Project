from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SelectField, TextAreaField, IntegerField, EmailField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email


class SurveyForm(FlaskForm):
    FName = StringField('First Name', validators=[DataRequired])
    LName = StringField('Last Name', validators=[DataRequired])
    StuNum = StringField('Student Number', validators=[DataRequired, Length(max=7)])

