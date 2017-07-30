#!/usr/bin/env python3
"""
To run this app do as follows:
1. Create virtualenv for this project
2. Install all of the dependencies (pip install -r requirements.txt)
3. Export name of this file as environmental variable (export FLASK_APP=app.py)
4. Run app by typing 'flask run' in the terminal
"""

import os
from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, send
from tts import text_to_speech

# TODO: create default templates
# TODO: connect to DB


def before_request():
    app.jinja_env.cache = {}

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_secured_password'
app.config["DEBUG"] = True
socketio = SocketIO(app)
app.before_request(before_request)
app.config.update(
    DEBUG=True,
    TEST=True,
    TEMPLATES_AUTO_RELOAD=True
)

page_title = "RapBattlaChatReboot"


@app.route('/')
def index():
    return render_template('index.html', title=page_title)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin':
            error = "Invalid Creadentials. Please try again."
        else:
            return redirect(url_for('index'))
    return render_template('login.html', title=page_title, error=error)


@socketio.on('connect_event')
def handle_my_event(data):
    print("Connection message:", data)
    socketio.emit('response_event', data)


@socketio.on('send_message')
def handle_message(data):
    audio_dir = '/static/audio/'
    print("Message sent:", data)
    audio_file = text_to_speech(data)
    if audio_file:
        res = {
            "msg": data,
            "audio_file": audio_file
        }
        send(res, broadcast=True)


@socketio.on('del_audio')
def handle_del_audio(data):
    files = os.listdir("static/audio")
    if data[13:] in files:
        current_dir = os.getcwd()
        os.remove(current_dir + "/" + data)
        print('file_removed: ', current_dir + "/" + data)


if __name__ == "__main__":
    print("Starting app...")
    socketio.run(app)
