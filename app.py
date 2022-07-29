from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def confirm_connect():
    print('Client connected')
    #emit('connections', {'data': 'Connected'}, broadcast=True)
@socketio.on('disconnect')
def confirm_disconnect():
    print('Client disconnected')
    emit('connections', {'data': 'Disconnected'}, broadcast=True)

@socketio.on('button press')
def buttonPressed(press):
    emit('pressed button', {'data': press['data']}, broadcast=True)

@socketio.on('others')
def misc(o):
    emit('other-cons', {'data': o['data']}, broadcast=True)



# @socketio.on('my event')
# def test_message(message):
#     emit('my response', {'data': message['data']})
#
# @socketio.on('my broadcast event')
# def test_message(message):
#     emit('my response', {'data': message['data']}, broadcast=True)



# @socketio.event()
# def my_event(message):
#     emit('my response', {'data': 'got it!'})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
