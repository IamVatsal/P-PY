from threading import Thread
import time


class th(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        for i in range(5):
            print("Thread " + self.name + ": " + time.ctime(time.time()))


t1 = th("1")
t2 = th("2")
t1.start()
t2.start()
t1.join()
t2.join()