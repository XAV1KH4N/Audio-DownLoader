import threading
import time

from Downloader import Downloader
from Interface import Interface
from flask import Flask, render_template, request, send_file
from flask_socketio import SocketIO, emit
from flask import Flask
from flask import render_template, redirect, url_for
from flask import request
from flask import Response

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
            #interface = Interface()
            #interface.download(song)

            d = threading.Thread(target=thread_function, args=(1,))
            d.start()
            return render_template('loading.html', download=song)

    return render_template('index.html')

@app.route('/send', methods=['POST','GET'])
def download_file():
    d = Downloader()
    path = d.downloadPath + "/riptide.mp4"
    return send_file(path, as_attachment=True)\

def thread_function(name):
    time.sleep(5)
    print("Emitting")
    socketio.emit('ready', {'data': 'got it!'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    socketio.run(app)
