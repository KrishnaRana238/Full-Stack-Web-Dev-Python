from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm


app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def squarenumber():
    if request.method == 'POST':
        if request.form.get("num") == None:
            return render_template('squarenum.html', result="Please enter a number")
        elif request.form.get("num") == "":
            return f"Please enter a number"
        else:
            number = request.form.get('num')
            square = int(number) ** 2
            return render_template('result.html', num = number, square=square)
    return render_template('squarenum.html')

if __name__ == '__main__':
    app.run(debug=True)
