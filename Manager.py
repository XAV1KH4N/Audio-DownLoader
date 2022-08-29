from Search import Search
from Downloader import Downloader

class Manager:
    def __init__(self):
        self.search = Search()
        self.down = Downloader()

    def download(self, title, auth=None):
        if auth == None or len(auth) == 0 or auth == "":
            pass
        else:
            title = title + " " + auth

        sid = self.search.search(title)
        self.down.download(sid, False, True, title)

    def setPath(self, path):
        self.down.setPath(path)

    def purge(self):
        self.down.purge()