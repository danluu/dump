from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

class PresidentGame:
    def __init__(self):
        pass

class PreGame:
    def __init__(self, gamename):
        self.usernames = set()
        self.gamename = gamename
        
    def join(self, username):
        self.usernames.add(username)

    def start(self):

class PlayerRouter:
    def __init__(self):
        username_to_sid = {}
        sid_to_username = {}

        username_to_gamename = {}
        games = {}

    def attach_username_sid(self, username, sid):
        if username in username_to_sid:
            old_sid = username_to_sid[username]
            assert(old_sid in sid_to_username)
            print('deleting old sid {} from {}'.format(
                old_sid, username))

        username_to_sid[username] = request.sid
        sid_to_username[request.sid] = username

    def attach_sid_gamename(self, sid, game):
        username = sid_to_username[request.sid]
        assert(username in username_to_sid)
        attach_username_game(username, game)

    def attach_username_gamename(self, username, gamename):
        if username in username_to_gamename:
            print('ERROR: user already in game')
        else:
            username_to_gamename[username] = gamename

        if not gamename in games:
            games[gamename] = PreGame(gamename)

        games[gamename].join(username)
        # TODO: need to return something to client if we failed to join the game.

    def start_sid_gamename(self, sid, gamename):
        # TODO: make sure the sid is allowed to start the game.
        

    def username_to_sid(self, username):
        pass

    def sid_to_username(self, sid):
        pass

    def username_to_gamename(self, username):
        pass

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
    print('got username: {} for sid {}'.format(username, request.sid))
    router.attach_username_sid(username, request.sid)

    emit('ack', {'username': username})

@socketio.on('gamename')
def gamename_message(message):
    print('got gamename: {}'.format(message, request.sid))
    gamename = message
    attach_sid_gamename(request.sid, gamename)

    router.attach_sid_game(request.sid, gamename)
    emit('ack', {'gamename': gamename})

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    send('got message: ' + message)

if __name__ == '__main__':
    router = PlayerRouter()

    print('running socketio')
    socketio.run(app, port=4113)
    print('ran socketio')
