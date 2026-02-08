import threading
import time
import random

# ==================================================
# 1️⃣ RACE CONDITION GAME – Treasure Chest
# ==================================================
def race_condition_game():
    print("\n🎮 RACE CONDITION GAME: Treasure Chest\n")

    global treasure
    treasure = 50

    def player(name):
        global treasure
        for _ in range(25):
            if treasure > 0:
                temp = treasure
                time.sleep(0.01)
                treasure = temp - 1
                print(f"{name} took a coin. Remaining: {treasure}")

    t1 = threading.Thread(target=player, args=("🏴 Player A",))
    t2 = threading.Thread(target=player, args=("🏴 Player B",))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("🏁 Game Over | Final Treasure:", treasure)


# ==================================================
# 2️⃣ DEADLOCK GAME – Dungeon Keys
# ==================================================
def deadlock_game():
    print("\n🎮 DEADLOCK GAME: Dungeon Key Quest\n")

    key1 = threading.Lock()
    key2 = threading.Lock()

    def player_a():
        with key1:
            print("🧙 Player A got Key-1")
            time.sleep(1)
            print("🧙 Player A waiting for Key-2")
            with key2:
                print("🧙 Player A escaped")

    def player_b():
        with key2:
            print("🧝 Player B got Key-2")
            time.sleep(1)
            print("🧝 Player B waiting for Key-1")
            with key1:
                print("🧝 Player B escaped")

    t1 = threading.Thread(target=player_a)
    t2 = threading.Thread(target=player_b)

    t1.start()
    t2.start()


# ==================================================
# 3️⃣ STARVATION GAME – VIP Ticket Counter
# ==================================================
def starvation_game():
    print("\n🎮 STARVATION GAME: VIP Ticket Counter\n")

    lock = threading.Lock()

    def vip():
        while True:
            with lock:
                print("👑 VIP served")
                time.sleep(0.1)

    def normal():
        while True:
            acquired = lock.acquire(timeout=1)
            if acquired:
                print("🙍 Normal user finally served")
                lock.release()
                break
            else:
                print("🙍 Normal user waiting...")

    t1 = threading.Thread(target=vip)
    t2 = threading.Thread(target=normal)

    t1.start()
    t2.start()


# ==================================================
# 4️⃣ LIVELOCK GAME – Polite Corridor
# ==================================================
def livelock_game():
    print("\n🎮 LIVELOCK GAME: Polite Corridor\n")

    def player_a():
        while True:
            print("🤵 Player A: You go first!")
            time.sleep(0.5)

    def player_b():
        while True:
            print("🧍 Player B: No, you go first!")
            time.sleep(0.5)

    t1 = threading.Thread(target=player_a)
    t2 = threading.Thread(target=player_b)

    t1.start()
    t2.start()


# ==================================================
# MAIN MENU
# ==================================================
while True:
    print("\n🔥 CONCURRENCY CHAOS ARENA 🔥")
    print("1️⃣ Race Condition Game")
    print("2️⃣ Deadlock Game")
    print("3️⃣ Starvation Game")
    print("4️⃣ Livelock Game")
    print("5️⃣ Exit")

    choice = input("Select a game (1-5): ")

    if choice == "1":
        race_condition_game()
    elif choice == "2":
        deadlock_game()
    elif choice == "3":
        starvation_game()
    elif choice == "4":
        livelock_game()
    elif choice == "5":
        print("👋 Exiting game arena")
        break
    else:
        print("❌ Invalid choice")
