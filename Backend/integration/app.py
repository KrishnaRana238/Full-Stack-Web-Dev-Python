from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField, DateField, TelField
from wtforms.validators import DataRequired, Email, Length
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a strong secret key
csrf = CSRFProtect(app)

# WTForm for login
class LoginForm(FlaskForm):
    username = StringField('Username or Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

# WTForm for registration
class RegisterForm(FlaskForm):
    regUsername = StringField('Username', validators=[DataRequired(), Length(min=3)])
    regEmail = StringField('Email', validators=[DataRequired(), Email()])
    gender = RadioField('Gender', choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], validators=[DataRequired()])
    dob = DateField('Date of Birth', validators=[DataRequired()])
    phone = TelField('Phone', validators=[DataRequired(), Length(min=10, max=10)])
    regPassword = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Create Account')

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    register_form = RegisterForm()

    if login_form.validate_on_submit() and login_form.submit.data:
        flash(f"Logged in as {login_form.username.data}", "info")
        return redirect(url_for('login'))

    if register_form.validate_on_submit() and register_form.submit.data:
        flash(f"Registered user {register_form.regUsername.data}", "success")
        return redirect(url_for('login'))

    return render_template('login.html', login_form=login_form, register_form=register_form)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/courses')
def courses():
    return render_template("courses.html")

@app.route('/applied')
def applied():
    return render_template("applied.html")

@app.route('/setting')
def setting():
    return render_template("settings.html")

if __name__ == '__main__':
    app.run(debug=True)
