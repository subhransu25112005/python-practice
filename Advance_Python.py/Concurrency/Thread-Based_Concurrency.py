import threading
import time

def task(name):
    for i in range(3):
        print(f"{name} working...")
        time.sleep(1)

t1 = threading.Thread(target=task, args=("Task A",))
t2 = threading.Thread(target=task, args=("Task B",))

t1.start()
t2.start()

t1.join()
t2.join()

print("All tasks finished")
