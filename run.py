import os
import json
# import flask class - capital letter indicates a class and is important to remember
from flask import Flask, render_template


app = Flask(__name__)
# create instance and store in variable called app.
# The first argument of the Flask class, is the name of the application's module - our package.
# Since we're just using a single module, we can use __name__ which is a built-in Python variable.
# Flask needs this so that it knows where to look for templates and static files.


@app.route("/") #  decorator starts with @ or pie notation.
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":  # name of default module in python
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),  # Using the os module from the python library to get the 'IP' environment variable if it exists, but set a default value if it's not found.
        port=int(os.environ.get("PORT", "5000")),  # It will be the same with 'PORT', but this time, we're casting it as an integer, and I will set that default to "5000", which is a common port used by Flask.
        debug=True)  # CHANGE TO FALSE BEFORE SUBMITTING PROJECT - IF NOT, IT CREATES A SECURITY FLAW
