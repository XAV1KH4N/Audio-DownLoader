from Manager import Manager

class Interface:
    def __init__(self):
        self.manager = Manager()

    def download(self, title):
        self.manager.download(title)

    def changeDownloadPath(self, path):
        self.manager.setPath(path)