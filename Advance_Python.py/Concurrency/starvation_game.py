import threading
import time

counter_lock = threading.Lock()

def vip_player():
    while True:
        with counter_lock:
            print("👑 VIP got the ticket")
            time.sleep(0.1)   # VIP uses counter quickly

def normal_player():
    while True:
        acquired = counter_lock.acquire(timeout=1)
        if acquired:
            print("🙍 Normal player finally got the ticket")
            counter_lock.release()
            break
        else:
            print("🙍 Normal player waiting...")

vip = threading.Thread(target=vip_player)
normal = threading.Thread(target=normal_player)

vip.start()
normal.start()
