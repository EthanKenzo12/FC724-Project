from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SelectField, TextAreaField, IntegerField, EmailField, SubmitField, \
    BooleanField
from wtforms.validators import DataRequired, Length, Email

# Creation of classes with their associated following attributes:
# first_name, last_name, Student number, gender, Intake year, Email, Course
# overall performance, individual grades, experience, reason for experience.
# also included T&C checkbox for validation before survey may be submitted
class SurveyForm(FlaskForm):
    FName = StringField('First Name', validators=[DataRequired()])
    LName = StringField('Last Name', validators=[DataRequired()])
    SNum = StringField('Student Number', validators=[DataRequired(), Length(max=7)])
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
    Overall = StringField('Overall, how did you perform academically?')
    Grade_1 = IntegerField('What was the grade of your 1st Module?')
    Grade_2 = IntegerField('What was the grade of your 2nd Module?')
    Grade_3 = IntegerField('What was the grade of your 3rd Module?')
    Grade_4 = IntegerField('What was the grade of your 4th Module?')
    Experience = RadioField('Did you enjoy your learning experience here?', choices=[
        ('Strongly Disagree', 'Strongly Disagree'),
        ('Disagree', 'Disagree'),
        ('Neutral', 'Neutral'),
        ('Agree', 'Agree'),
        ('Strongly Agree', 'Strongly Agree'),
    ])
    Why_1 = TextAreaField('Why or Why Not?')
    Suggestions = TextAreaField('Suggestions for improvement', validators=[Length(max=500)])
    T_and_C = BooleanField("I agree to have the following information shared with GIC", validators=[DataRequired()])
    Submit = SubmitField('Submit')
