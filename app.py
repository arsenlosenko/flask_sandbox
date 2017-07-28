#!/usr/bin/env python3
"""
To run this app do as follows:
1. Create virtualenv for this project
2. Install all of the dependencies (pip install -r requirements.txt)
3. Export name of this file as environmental variable (export FLASK_APP=app.py)
4. Run app by typing 'flask run' in the terminal
"""


from flask import Flask

app = Flask(__name__)

# TODO: setup socket connection
# TODO: create default templates
# TODO: connect to DB
# TODO: setup tts


@app.route('/')
def index():
    return "This is index page"


@app.route('/login')
def login():
    return "This is login page"
