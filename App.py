from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SelectField, TextAreaField, IntegerField, EmailField, SubmitField, \
    BooleanField
from wtforms.validators import DataRequired, Length, Email


class SurveyForm(FlaskForm):
    FName = StringField('First Name', validators=[DataRequired()])
    LName = StringField('Last Name', validators=[DataRequired()])
    StuNum = StringField('Student Number', validators=[DataRequired(), Length(max=7)])
    Gender = RadioField('Gender', choices=[('Male', 'Male'), ('Female', 'Female'), ('Non-Binary', 'Non-Binary')],
                        validators=[DataRequired()])
    Intake = SelectField('Intake', choices=[('September 2023', 'September 2023'), ('January 2024', 'January 2024')],
                         validators=[DataRequired()])
    Email = EmailField('Email', validators=[DataRequired(), Email()])
    Course = SelectField('Programme of Study', choices=[
        ('FC Business & Social Science', 'FC Business & Social Science'),
        ('FC Arts & Humanities', 'FC Arts & Humanities'),
        ('FC Science & Engineering', 'FC Science & Engineering'),
        ('PM Business, Economics & Finance', 'PM Business, Economics & Finance'),
        ('PM Law & Social Sciences', 'PM Law & Social Sciences'),
        ('PM Arts & Humanities', 'PM Arts & Humanities'),
        ('PM Science & Engineering', 'PM Science & Engineering'),
        ('PM Science & Engineering 2', 'PM Science & Engineering 2')
    ], validators=[DataRequired()])
