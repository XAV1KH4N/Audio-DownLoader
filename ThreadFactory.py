class ThreadFactory:
    def __init__(self, socket):
        self.threads = []
        self.socketio = socket

    def add(self, thread):
        self.threads.append(thread)
        thread.addSocket(self.socketio)
        thread.start()

    def check(self, title, auth):
        for t in self.threads:
            if t.equals(title, auth) and t.isAlive():
                return True
        return False
