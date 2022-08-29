import threading

from Downloader import Downloader
from Interface import Interface
from flask import Flask, render_template, request, send_file
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST', 'GET'])
def download():
    if request.method == "POST":
        song = request.form['song']
        if len(song) != 0:

            d = threading.Thread(target=thread_function, args=(1,song))
            d.start()

            return render_template('loading.html', download=song)

    return render_template('index.html')

@app.route('/send', methods=['POST','GET'])
def download_file(song="/riptide.mp4"):
    d = Downloader()
    path = d.downloadPath + song
    return send_file(path, as_attachment=True)\

def thread_function(name, song):
    interface = Interface()
    interface.download(song)
    socketio.emit('ready', {'data': 'got it!'})


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    socketio.run(app)
