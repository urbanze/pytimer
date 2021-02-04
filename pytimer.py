import time
from threading import Thread

class software_timer(Thread):
    def __init__(self, time_sec, autoreload, function, compensation=1):
        Thread.__init__(self)
        self.time_sec = time_sec
        self.autoreload = autoreload
        self.function = function
        self.compensation = compensation

    def stop(self):
        self.function = self.stop
        self.autoreload = 0

    def run(self):
        t = self.time_sec

        while 1:
            time.sleep(t)
            
            t1 = time.time()
            self.function()
            t2 = time.time()

            if self.compensation:
                t = self.time_sec - (t2-t1)
                if (t < 0): t = 0

            if self.autoreload == 0: break

