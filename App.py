from flask import render_template, redirect, url_for, flash, Flask
from Survey import SurveyForm

app = Flask(__name__)


@app.route('/survey', methods=['GET', 'POST'])
def survey():
    form = SurveyForm()
    if form.validate_on_submit():
        # Process the data
        flash('Survey submitted successfully!')
        return redirect(url_for('some_function'))
    return render_template('Page%3%(Survey).html', form=form)
