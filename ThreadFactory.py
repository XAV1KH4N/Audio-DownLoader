class ThreadFactory:
    def __init__(self, socket):
        self.threads = []
        self.socketio = socket

    def add(self, thread):
        self.threads.append(thread)
        thread.addSocket(self.socketio)
        thread.start()

    def view(self):
        for t in self.threads:
            print(t.name)