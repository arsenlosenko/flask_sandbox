#!/usr/bin/env python3
"""
To run this app do as follows:
1. Create virtualenv for this project
2. Install all of the dependencies (pip install -r requirements.txt)
3. Export name of this file as environmental variable (export FLASK_APP=app.py)
4. Run app by typing 'flask run' in the terminal
"""

from flask import Flask, render_template
from flask_socketio import SocketIO


# TODO: setup socket connection
# TODO: create default templates
# TODO: connect to DB
# TODO: setup tts

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_secured_password'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return "This is login page"


@socketio.on('my event')
def handle_my_event(json):
    print("Recieved json: ", str(json))

if __name__ == "__main__":
    print("Starting app...")
    socketio.run(app)