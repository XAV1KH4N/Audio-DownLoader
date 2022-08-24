import os
from youtube_dl import YoutubeDL


class Downloader:
    def __init__(self):

        print('Youtube Downloader'.center(40, '_'))

        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        self.folderName = "Music_Downloads"
        self.downloadPath = desktop + "/" + self.folderName
        self.downloadPath = self.clean(self.downloadPath)

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
        self.dir = []
        self.cwd = os.getcwd()

    def download(self, url, full=True, rename=False, output="N/A"):

        self.snapshot()

        try:
            if not full:
                url = "https://www.youtube.com/watch?v=" + url
            self.audio_downloader.extract_info(url)

        except ValueError:
            return False

        new = self.findNew()
        new_path = self.cwd + "/" + new

        if rename:
            new_path = self.cwd + "/" + output + ".mp4"
            os.rename(self.cwd + "/" + new, new_path)

        self.move(output+".mp4", new_path)

        return True

    def snapshot(self):
        self.dir = [f for f in os.listdir(self.cwd) if os.path.isfile(os.path.join(self.cwd, f))]

    def findNew(self):
        temp = self.dir
        self.snapshot()

        new = list(set(self.dir) - set(temp))

        if len(new) != 1:
            raise DownloaderError("Downloaded file could not be found")

        return new[0]

    def move(self, file_name, path):
        dest = self.downloadPath + "/" + file_name

        dest = self.clean(dest)
        path = self.clean(path)

        try:
            os.mkdir(self.downloadPath)
        except FileExistsError:
            pass

        os.rename(path, dest)

    def clean(self, path):
        return path.replace("\\", "/")


class DownloaderError(Exception):
    def __init__(self, message):
        self.message = message


if __name__ == '__main__':
    down = Downloader()
    down.download("https://www.youtube.com/watch?v=BaW_jenozKc", rename=True, output="test")
