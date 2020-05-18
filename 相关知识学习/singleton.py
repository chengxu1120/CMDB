import sys, os, time
import threading


class Singleton(object):
    instance = None
    lock = threading.RLock()

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        if cls.instance:
            return cls.instance
        with cls.lock:
            if not cls.instance:
                # time.sleep(0.2)
                cls.instance = object.__new__(cls)
            return cls.instance


def func():
    obj1 = Singleton('alex')
    print(obj1)


for i in range(10):
    t = threading.Thread(target=func)
    t.start()
time.sleep(5)
obj2 = Singleton('david')