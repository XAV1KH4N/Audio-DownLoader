import threading


class Thread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

        self.name = name


    def run(self):
        try:
            pass
            #func goes here
        finally:
            print('ended')



