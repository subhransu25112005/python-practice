import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

'''def task1():
    with lock1:
        print("Task 1 acquired lock1")
        time.sleep(1)
        with lock2:
            print("Task 1 acquired lock2")

def task2():
    with lock2:
        print("Task 2 acquired lock2")
        time.sleep(1)
        with lock1:
            print("Task 2 acquired lock1")'''

def task1():
    with lock1:
        with lock2:
            print("Task 1 done")

def task2():
    with lock1:
        with lock2:
            print("Task 2 done")


t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()
