from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
username_to_session = {}
session_to_username = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def test_connect():
    print('got connection from {}'.format(request.sid))
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect')
def test_disconnect():
    print('got disconnection')

@socketio.on('my event')
def test_message(message):
    emit('my response', {'data': 'got it!'})

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    send('got message: ' + message)

if __name__ == '__main__':
    print('running socketio')
    socketio.run(app, port=4113)
    print('ran socketio')
