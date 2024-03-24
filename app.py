from flask import render_template, redirect, url_for, flash, Flask
from survey import SurveyForm

# creation of secret key for session security and CSRF protection
app = Flask(__name__)
app.config['SECRET_KEY'] = 'GIC'

# routed app to /form when url: http://127.0.0.1:5000/form is accessed, associated html page is accessed
# user will be directed to the survey for directly
# creation of form function,
# use of with open such that data input on the server-side survey is saved as text in Data.txt
@app.route('/form', methods=['GET', 'POST'])
def form():
    form = SurveyForm()
    if form.validate_on_submit():
        with open("Data.txt", "a") as l:
            l.write(f'FName: {form.FName.data}\n')
            l.write(f'LName: {form.LName.data}\n')
            l.write(f'SNum: {form.SNum.data}\n')
            l.write(f'Gender: {form.Gender.data}\n')
            l.write(f'Intake: {form.Intake.data}\n')
            l.write(f'Email: {form.Email.data}\n')
            l.write(f'Course: {form.Course.data}\n')
            l.write(f'Overall: {form.Overall.data}\n')
            l.write(f'Grade_1:{form.Grade_1.data}\n')
            l.write(f'Grade_2:{form.Grade_2.data}\n')
            l.write(f'Grade_3:{form.Grade_3.data}\n')
            l.write(f'Grade_4:{form.Grade_4.data}\n')
            l.write(f'Experience: {form.Experience.data}\n')
            l.write(f'Why_1:{form.Why_1.data}\n')
            l.write(f'Suggestions:{form.Suggestions.data}\n')
            l.write(f'--------line break--------\n')

        # use of flash to create flash message to inform user of successful survey submission
        flash('Survey submitted successfully!')
        # use of redirect to redirect user to the survey page after survey is submitted
        return redirect(url_for('form'))
    # use of render template to access survey.html, HTML page
    return render_template("survey.html", form=form)


# routed app to /home when url: http://127.0.0.1:5000 is accessed, associated html page is accessed
# as the default page is the home page default localhost website will be http://127.0.0.1:5000
@app.route('/')
def home():
    # use of render template to access Homepage.html, HTML page
    return render_template('Homepage.html')

# routed app to /about when url: http://127.0.0.1:5000/about is accessed, associated html page is accessed
@app.route('/about')
def about():
    # use of render template to access About.html, HTML page
    return render_template('About.html')


if __name__ == '__main__':
    app.run(debug=True)