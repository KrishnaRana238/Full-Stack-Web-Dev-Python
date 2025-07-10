from flask import Flask, render_template, request, session, redirect, url_for
import pymysql
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


app = Flask(__name__)
app.secret_key = "12345678"

# class RegisterForm(FlaskForm):
  
#      regUsername = StringField('Username', validators=[DataRequired()])
#      regEmail = StringField('Email', validators=[DataRequired(), Email()])
#      regUsername = StringField('Username', validators=[DataRequired()])
#      submit = SubmitField('Create Account')

class RegisterForm(FlaskForm):
    regUsername = StringField('Username', validators=[DataRequired()])
    regEmail = StringField('Email', validators=[DataRequired(), Email()])
    regPassword = PasswordField('Password', validators=[DataRequired()])  
    submit = SubmitField('Create Account')
    
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
    
# Database connection function
def get_db_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="login4321",
        database="login",
        port=3306,
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route("/", methods=['GET', 'POST'])
# def register():
#     register_form = RegisterForm()
#     if request.method == "POST":
#         # details = request.form
#         # username = details["name"]
#         # email = details["email"]
#         # password = details["pass"]
#         if register_form.validate_on_submit():
#             username = register_form.regUsername.data
#             email = register_form.regEmail.data
#             password = register_form.regUsername.data
#             conn = get_db_connection()
#             with conn.cursor() as cur:
#                 cur.execute("INSERT INTO tb(username, email, password) VALUES (%s, %s, %s)", (username, email, password))
#                 conn.commit()
#         conn.close()
        
#         return redirect(url_for("index"))
#     return render_template("register.html")
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        username = register_form.regUsername.data
        email = register_form.regEmail.data
        password = register_form.regPassword.data

        conn = get_db_connection()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO tb(username, email, password) VALUES (%s, %s, %s)", (username, email, password))
            conn.commit()
        conn.close()

        return redirect(url_for("login"))
    return render_template("register.html", register_form=register_form)

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/login", methods=['GET', 'POST'])
# def login():
#     if request.method == "POST":
#         details = request.form
#         username = details["name"]
#         password = details["pass"]
#         conn = get_db_connection()
#         with conn.cursor() as cur:
#             cur.execute("SELECT * FROM tb WHERE username=% s AND password=% s", (username, password))
#             account = cur.fetchone()
#         conn.close()
#         if account:
#             session["loggedin"] = True
#             return render_template("index.html", msg="Login successfully")
#         else:
#             return "Invalid credentials"
#     return render_template("login.html")
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data

        conn = get_db_connection()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM tb WHERE username=%s AND password=%s", (username, password))
            account = cur.fetchone()
        conn.close()

        if account:
            session["loggedin"] = True
            return render_template("index.html", msg="Login successful")
        else:
            return "Invalid credentials"

    return render_template("login.html", login_form=login_form)

if __name__ == "__main__":
    app.run(debug=True)
