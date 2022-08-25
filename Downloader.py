import os
from YouDL import YouDL


class Downloader:
    def __init__(self):

        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

        self.folderName = "Music_Downloads"
        self.downloadPath = desktop + "/" + self.folderName
        self.downloadPath = self.clean(self.downloadPath)

        self.audio_downloader = YouDL()

        self.dir = []
        self.cwd = os.getcwd()

    def setPath(self):
        self.downloadPath = path

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