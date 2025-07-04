from flask import Flask, render_template, redirect, url_for
from form import FeedbackForm

app = Flask(__name__)

app.secret_key = 'supersecretkey'  # Needed for CSRF protection

@app.route('/', methods=['GET', 'POST'])
def index():
    form = FeedbackForm()
    if form.validate_on_submit():
        name = form.name.data
        feedback = form.feedback.data
        return render_template('submitted.html', name=name, feedback=feedback)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
