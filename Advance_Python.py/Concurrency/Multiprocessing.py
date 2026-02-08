from multiprocessing import Process
import os

def work():
    print("Process ID:", os.getpid())

p1 = Process(target=work)
p2 = Process(target=work)

p1.start()
p2.start()

p1.join()
p2.join()
