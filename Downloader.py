import os
from YouDL import YouDL


class Downloader:
    def __init__(self):

        #desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

        #self.folderName = "Music_Downloads"
        #self.downloadPath = desktop + "/" + self.folderName

        self.cwd = os.getcwd()

        self.folderName = "downloads"
        self.downloadPath = self.cwd + "/" + self.folderName

        self.downloadPath = self.clean(self.downloadPath)

        self.audio_downloader = YouDL()

        self.dir = []

    def setPath(self, path):
        self.downloadPath = path

    def download(self, url, full=True, rename=False, output="N/A"):

        self.snapshot()

        try:
            if not full:
                url = "https://www.youtube.com/watch?v=" + url
            self.audio_downloader.extract_info(url)

        except:
            return False

        new = self.findNew()
        new_path = self.cwd + "/" + new

        if rename:
            new_path = self.cwd + "/" + output + ".mp4"
            os.rename(self.cwd + "/" + new, new_path)

        self.move(output+".mp4", new_path)

        self.purge()
        return True

    def purge(self):
        files = self.getFiles()
        for file in files:
            ext = file.split(".")[-1]
            if ext != "py":
                del_path = self.cwd + "/" + file
                os.remove(del_path)
                print("Deleting ", del_path)

    def snapshot(self):
        self.dir = self.getFiles()

    def getFiles(self):
        return [f for f in os.listdir(self.cwd) if os.path.isfile(os.path.join(self.cwd, f))]

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

        try:
            os.rename(path, dest)
        except FileExistsError:
            os.remove(path)

    def clean(self, path):
        return path.replace("\\", "/")


class DownloaderError(Exception):
    def __init__(self, message):
        self.message = message