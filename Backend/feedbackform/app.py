# Practice Task: Simple Feedback Form
# You will build a Flask app with a page showing a form (name + feedback message).
#Post method to handle form submission and display the submitted data on a new page.

#file Structure:
#Feedback_app/
#|
#|-- app.py
#|-- templates/
#    |-- index.html (input name and feedback and submit button)
#    |-- submitted.html (display the submitted name and feedback)


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def feedbackform():
    if request.method == 'POST':
        if request.form.get("name") == None or request.form.get("feedback") == None:
            return render_template('index.html', result="Please fill in all fields")
        elif request.form.get("name") == "" or request.form.get("feedback") == "":
            return render_template('index.html', result="Please fill in all fields")
        else:
            name = request.form.get('name')
            feedback = request.form.get('feedback')
            return render_template('submit.html', name=name, feedback=feedback)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)