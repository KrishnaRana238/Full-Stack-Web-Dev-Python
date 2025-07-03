from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# @app.route("/<username>")
# def index(username):
#     return f"Hello, {username}! Welcome to the Inventory Management System."
# # @app.route("/about") #decorator
# # def home():
# #     return "Welcome to the Inventory Management System!"


# # @app.route("/about")
# # def about():
# #     return "This is a simple inventory management system built with Flask."
# # @app.route("/about")
# # def home():
# #     return "Welcome to the Inventory Management System!"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/home")
def about():
    return render_template("home.html")

@app.route("/dashboard/<name>")
def dashboard(name):
    if name == 'admin':
        return redirect(url_for('home'))
    elif name == 'user':
        return redirect(url_for('about'))
    else:
        return "Invalid user type", 404
    
@app.route("/if")
def if_example():
    message = "This is an example route."
    return render_template("ifexample.html", message=message)

@app.route("/for")
def for_example():
    courses = ['Python', 'JavaScript', 'Java', 'C++']
    return render_template("forexample.html", courses=courses)

if __name__ == "__main__":
    app.run(debug=True)
    print("Invalid choice, please try again!")
    
