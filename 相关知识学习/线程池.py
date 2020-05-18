import sys, os, time
from concurrent.futures import ThreadPoolExecutor


def task(i):
    time.sleep(1)
    print("I am %s" % str(i))

start_time = time.time()
for i in range(100):
    # pool = ThreadPoolExecutor(10)
    # pool.submit(task, i)
    task(i)
print("cost time is:",(time.time()-start_time))