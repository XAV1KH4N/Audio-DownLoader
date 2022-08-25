import ctypes
import threading


class Thread(threading.Thread):
    def __init__(self, name, manager, title):
        threading.Thread.__init__(self)
        self.name = name
        self.manager = manager
        self.title = title

    def run(self):
        try:
            self.manager.download(self.title)
        finally:
            print('\n**Ended - Hit Enter')

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



