import threading
import time

lock = threading.Lock()

'''def greedy_task():
    while True:
        with lock:
            print("Greedy task running")
            time.sleep(0.1)'''
def greedy_task():
    while True:
        with lock:
            print("Greedy task running")
        time.sleep(0.2)


def poor_task():
    while True:
        acquired = lock.acquire(timeout=1)
        if acquired:
            print("Poor task finally running")
            lock.release()
            break
        else:
            print("Poor task waiting...")

t1 = threading.Thread(target=greedy_task)
t2 = threading.Thread(target=poor_task)

t1.start()
t2.start()
