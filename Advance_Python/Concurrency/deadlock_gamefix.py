import threading
import time

# Two dungeon keys (resources)
key_1 = threading.Lock()
key_2 = threading.Lock()

'''def player_a():
    print("🧙 Player A enters dungeon and grabs Key-1")
    with key_1:
        time.sleep(1)
        print("🧙 Player A tries to grab Key-2...")
        with key_2:   # waits forever
            print("🧙 Player A escaped the dungeon!")

def player_b():
    print("🧝 Player B enters dungeon and grabs Key-2")
    with key_2:
        time.sleep(1)
        print("🧝 Player B tries to grab Key-1...")
        with key_1:   # waits forever
            print("🧝 Player B escaped the dungeon!")'''
def player_safe(name):
    print(f"{name} tries to escape safely")
    with key_1:
        time.sleep(1)
        with key_2:
            print(f"{name} escaped the dungeon safely!")

t1 = threading.Thread(target=player_safe, args=("🧙 Player A",))
t2 = threading.Thread(target=player_safe, args=("🧝 Player B",))

t1.start()
t2.start()

t1.join()
t2.join()

print("🏆 All players escaped safely!")


