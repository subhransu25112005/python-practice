import threading
import time

# Shared treasure chest
treasure = 100

'''def player(name):
    global treasure
    for _ in range(50):
        if treasure > 0:
            current = treasure      # read
            time.sleep(0.01)         # context switch
            treasure = current - 1   # write
            print(f"{name} collected a coin. Remaining: {treasure}")

# Two players
p1 = threading.Thread(target=player, args=("🏴 Player A",))
p2 = threading.Thread(target=player, args=("🏴 Player B",))

p1.start()
p2.start()

p1.join()
p2.join()

print("\n🏁 Game Over")
print("Final treasure count:", treasure)'''

lock = threading.Lock()

def safe_player(name):
    global treasure
    for _ in range(50):
        with lock:
            if treasure > 0:
                treasure -= 1
                print(f"{name} safely collected a coin. Remaining: {treasure}")

treasure = 100

p1 = threading.Thread(target=safe_player, args=("🟢 Player A",))
p2 = threading.Thread(target=safe_player, args=("🟢 Player B",))

p1.start()
p2.start()

p1.join()
p2.join()

print("\n🏆 Game Over (Safe)")
print("Final treasure count:", treasure)

