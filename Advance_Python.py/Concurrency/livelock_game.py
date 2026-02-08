#Polite Corridor Dance
'''Two players meet in a narrow corridor 🚶‍♂️🚶‍♀️

Both are too polite:

Player A steps aside to let Player B go

Player B also steps aside to let Player A go

They keep reacting to each other

➡️ They are active, but nobody moves forward'''
import threading
import time

# Shared state
player_a_ready = True
player_b_ready = True

def player_a():
    global player_a_ready, player_b_ready
    while True:
        if player_b_ready:
            print("🤵 Player A: You go first!")
            time.sleep(0.4)
        else:
            print("🤵 Player A passed through corridor")
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
t2.start()
