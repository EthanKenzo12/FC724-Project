from flask import render_template, redirect, url_for, flash, Flask
from survey import SurveyForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'GIC'


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

        flash('Survey submitted successfully!')
        return redirect(url_for('form'))
    return render_template("survey.html", form=form)


@app.route('/')
@app.route('/home')
def home():
    return render_template('Homepage.html')


@app.route('/about')
def about():
    return render_template('About.html')


if __name__ == '__main__':
    app.run(debug=True)