import os
from youtube_dl import YoutubeDL


class Downloader:
    def __init__(self):
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        self.folderName = "Music_Downloads"

        self.downloadPath = desktop + self.folderName
        self.ffmpegPath = "c:/Users/Xavi/Downloads/ffmpeg-5.1-essentials_build/bin"
        self.options = {
            "format": "bestaudio/best",
            "output": "test.mp3",
            "ffmpeg_location": self.ffmpegPath,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
            }],
        }

        self.audio_downloader = YoutubeDL(self.options)

    def download(self, url, full=True):

        try:
            print('Youtube Downloader'.center(40, '_'))

            # URL = input('Enter youtube url :  ')
            URL = "https://www.youtube.com/watch?v=BaW_jenozKc"

            self.audio_downloader.extract_info(URL)

        except:

            print("Couldn\'t download the audio")
