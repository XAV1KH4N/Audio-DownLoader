import threading
import time

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
        title = request.form['title']
        auth = request.form['by']
        if len(title) != 0:

            d = threading.Thread(target=thread_function, args=(1, title, auth))
            d.start()

            return render_template('loading.html', title=title, auth=auth)

    return render_template('index.html')

@app.route('/send/<string:title>/<string:auth>', methods=['POST','GET'])
def download_file(title, auth):
    title = "/" + title + " " + auth + ".mp4"
    d = Downloader()
    path = d.downloadPath + title
    return send_file(path, as_attachment=True)\

def thread_function(name, title, auth):
    interface = Interface()
    interface.download(title, auth)
    socketio.emit('ready', {'title': title, 'auth': auth})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    socketio.run(app)
