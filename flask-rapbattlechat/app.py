
import os
from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, send


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


@socketio.on('message')
def handle_my_event(data):
    print("Comment: ", data)
    socketio.emit('response', data)


@socketio.on('connect')
def handle_connect():
    print("Connected")

if __name__ == "__main__":
    print("Starting app...")
    socketio.run(app)
