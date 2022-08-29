from Manager import Manager

class Interface:
    def __init__(self):
        self.manager = Manager()

    def download(self, title, auth=None):
        self.manager.download(title, auth)

    def changeDownloadPath(self, path):
        self.manager.setPath(path)


class InterfaceError(Exception):
    def __init__(self, message):
        self.message = message