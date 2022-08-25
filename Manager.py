from Search import Search
from Downloader import Downloader

class Manager:
    def __init__(self):
        self.search = Search()
        self.down = Downloader()

    def download(self, title):
        sid = self.search.search(title)
        self.down.download(sid, False, True, title)

    def setPath(self, path):
        self.down.setPath(path)