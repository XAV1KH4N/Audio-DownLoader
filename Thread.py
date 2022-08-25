import threading


class Thread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name


