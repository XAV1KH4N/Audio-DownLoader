import ctypes
import threading
from flask_socketio import SocketIO

class Thread(threading.Thread):
    def __init__(self, name, manager, title, auth):
        threading.Thread.__init__(self)
        self.name = name
        self.manager = manager
        self.title = title
        self.auth = auth

    def addSocket(self, socket):
        self.socketio = socket

    def run(self):
        try:
            self.manager.download(self.title, self.auth)
            self.socketio.emit('ready', {'title': self.title, 'auth': self.auth})
            print("Emitted")
        except:
            self.socketio.emit('failed', {'title': self.title, 'auth': self.auth})
            print("failed")
        finally:
            print("final")

    def get_id(self):
        if hasattr(self, '_thread_id'):
            return self._thread_id

        for tid, thread in threading._active.items():
            if thread is self:
                return tid

    def raise_exception(self):
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
                                                         ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')



