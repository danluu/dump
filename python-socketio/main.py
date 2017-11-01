from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

username_to_session = {}
session_to_username = {}

username_to_game = {}

class PresidentGame:
    def __init__(self):
        pass

class PreGame:
    def __init__(self, gamename):
        self.usernames = set()
        self.gamename = gamename
        
    def join(self, username):
        self.usernames.add(username)
    

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

@socketio.on('pingServer')
def test_message(message):
    print('got pingServer')
    emit('my response', {'data': 'got it!'})

@socketio.on('username')
def username_message(message):
    username = message
    print('got username: {} for session {}'.format(username, request.sid))
    
    if username in username_to_session:
        old_session = username_to_session[username]
        assert(old_session in session_to_username)
        print('deleting old session {} from {}'.format(
            old_session, username))

    username_to_session[username] = request.sid
    session_to_username[request.sid] = username
    emit('ack', {'username': username})

@socketio.on('gamename')
def gamename_message(message):
    print('got gamename: {}'.format(message, request.sid))
    username = session_to_username[request.sid]
    gamename = message
    assert(username in username_to_session)

    if username in username_to_game:
        print('ERROR: user already in game')
    else:
        username_to_game[username] = gamename
    
    
    emit('ack', {'gamename': gamename})

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    send('got message: ' + message)

if __name__ == '__main__':
    print('running socketio')
    socketio.run(app, port=4113)
    print('ran socketio')
