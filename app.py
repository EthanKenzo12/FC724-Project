from flask import render_template, redirect, url_for, flash, Flask, jsonify
from survey import SurveyForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'some-random-secret-key'


@app.route('/form', methods=['GET', 'POST'])
def form():
    form = SurveyForm()
    if form.validate_on_submit():
        # Process the data
        flash('Survey submitted successfully!')
        return redirect(url_for('survey'))
    return render_template("survey.html", form=form)


@app.route('/home')
def home():
    return render_template('Homepage.html')


@app.route('/about')
def about():
    return render_template('About.html')


if __name__ == '__main__':
    app.run(debug=True)