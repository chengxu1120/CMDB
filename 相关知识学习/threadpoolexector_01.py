import sys, os, time
import threading
from concurrent.futures import ThreadPoolExecutor

def add(n1,n2):
    v = n1 + n2
    print("add:",v,", tid:",threading.get_ident())
    time.sleep(1)
    return v

ex = ThreadPoolExecutor(5)
f1 = ex.submit(add,2,3)
f2 = ex.submit(add,5,8)
print("main thread running")
print(f1.done)
print(f2.result)
