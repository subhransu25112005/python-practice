import threading
import time
import random

def task1():
    time.sleep(random.random())
    print("Task 1 proceeds")

def task2():
    time.sleep(random.random())
    print("Task 2 proceeds")


'''def task1():
    while True:
        print("Task 1: Trying to proceed")
        time.sleep(0)

def task2():
    while True:
        print("Task 2: Trying to proceed")
        time.sleep(1)'''

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()
