import threading
import time

# Shared state
player_a_ready = True
player_b_ready = True

'''def player_a():
    global player_a_ready, player_b_ready
    while True:
        if player_b_ready:
            print("🤵 Player A: You go first!")
            time.sleep(0.5)
        else:
            print("🤵 Player A passed through coridor")
            break

def player_b():
    global player_a_ready, player_b_ready
    while True:
        if player_a_ready:
            print("🧍 Player B: No no, you go first!")
            time.sleep(0.5)
        else:
            print("🧍 Player B passed through corridor")
            break

# Start players
t1 = threading.Thread(target=player_a)
t2 = threading.Thread(target=player_b)

t1.start()
t2.start()'''
import random

def player_a_fixed():
    time.sleep(random.random())
    print("🤵 Player A passed through corridor")

def player_b_fixed():
    time.sleep(random.random())
    print("🧍 Player B passed through corridor")

t1 = threading.Thread(target=player_a_fixed)
t2 = threading.Thread(target=player_b_fixed)

t1.start()
t2.start()

t1.join()
t2.join()

print("🏁 Both players moved forward!")

