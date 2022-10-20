from flask import Flask, render_template, request
import random
import json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")
        attributes = (username, email, subject, message)
        correct = False

        # Checking if everything is entered
        if all(attributes):
            correct = True
        
        return render_template('submitted_contact.html', correct = correct)

    with open("information.json", "r") as information_file:
        # This file contains all the information about me
        information = json.load(information_file)

    greetings = ("Hi there", "Hello there", "Hi", "Hello")
    greeting = random.choice(greetings)
    return render_template("index.html", greeting = greeting, information = information)

if __name__ == "__main__":
    app.run(debug=True)