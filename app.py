import os

from Downloader import Downloader
from Interface import Interface
from flask import Flask, render_template, request, send_file

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST', 'GET'])
def download():
    if request.method == "POST":
        song = request.form['song']
        if len(song) != 0:
            interface = Interface()
            interface.download(song)
            return render_template('index.html', download=song)

    return render_template('index.html')

@app.route('/send', methods=['POST','GET'])
def download_file():
    d = Downloader()
    path = d.downloadPath + "/riptide.mp4"
    return send_file(path, as_attachment=True)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
