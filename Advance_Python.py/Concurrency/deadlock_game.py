import threading
import time

# Two dungeon keys (resources)
key_1 = threading.Lock()
key_2 = threading.Lock()

def player_a():
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
            print("🧝 Player B escaped the dungeon!")

# Create threads (players)
t1 = threading.Thread(target=player_a)
t2 = threading.Thread(target=player_b)

t1.start()
t2.start()

t1.join()
t2.join()

print("🏁 Game Over")
