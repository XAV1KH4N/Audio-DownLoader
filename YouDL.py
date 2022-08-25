from youtube_dl import YoutubeDL

class YouDL:
    def __init__(self):
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

    def extract_info(self, url):
        self.audio_downloader.extract_info(url)