#!/usr/bin/env python3
"""
To run this app do as follows:
1. Create virtualenv for this project
2. Install all of the dependencies (pip install -r requirements.txt)
3. Export name of this file as environmental variable (export FLASK_APP=app.py)
4. Run app by typing 'flask run' in the terminal
"""

import os
from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
from tts import text_to_speech

# TODO: create default templates
# TODO: connect to DB
# TODO: create bash deploy script


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


@app.route('/')
def index():
    return render_template('index.html',
                           title="RapBattlaChatReboot")


@app.route('/login')
def login():
    return "This is login page"


@socketio.on('connect_event')
def handle_my_event(data):
    print("Connection message:", data)
    socketio.emit('response_event', data)


@socketio.on('send_message')
def handle_message(data):
    audio_dir = '/static/audio/'
    print("Message sent:", data)
    audio_file = text_to_speech(data)
    if audio_file == "ready":
        res = {
            "msg": data,
            "audio_file": audio_dir + "audio.mp3"
        }
        send(res, broadcast=True)


@socketio.on('del_audio')
def handle_del_audio(data):
    current_dir = os.getcwd()
    os.remove(current_dir + data)
    print('file_removed: ', current_dir + data)


if __name__ == "__main__":
    print("Starting app...")
    socketio.run(app)
