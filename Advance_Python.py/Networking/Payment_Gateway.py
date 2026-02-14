import random
import time
from datetime import datetime
from pathlib import Path


# -------------------------------------------------
# 1️⃣ Transaction Logger
# -------------------------------------------------
LOG_FILE = Path("transactions.txt")

def log_transaction(data: str):
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(data + "\n")


# -------------------------------------------------
# 2️⃣ Generate Transaction ID
# -------------------------------------------------
def generate_txn_id():
    return "TXN" + str(random.randint(100000, 999999))


# -------------------------------------------------
# 3️⃣ Base Payment Class
# -------------------------------------------------
class PaymentMethod:
    def pay(self, amount):
        raise NotImplementedError


# -------------------------------------------------
# 4️⃣ Card Payment
# -------------------------------------------------
class CardPayment(PaymentMethod):
    def pay(self, amount):
        card = input("Enter card number (16 digits): ")

        if len(card) != 16 or not card.isdigit():
            print("❌ Invalid card number")
            return False

        cvv = input("Enter CVV: ")
        if len(cvv) != 3:
            print("❌ Invalid CVV")
            return False

        print("Processing card payment...")
        time.sleep(2)
        return True


# -------------------------------------------------
# 5️⃣ UPI Payment
# -------------------------------------------------
class UPIPayment(PaymentMethod):
    def pay(self, amount):
        upi = input("Enter UPI ID (example@upi): ")

        if "@" not in upi:
            print("❌ Invalid UPI ID")
            return False

        print("Waiting for UPI approval...")
        time.sleep(2)
        return True


# -------------------------------------------------
# 6️⃣ Wallet Payment
# -------------------------------------------------
class WalletPayment(PaymentMethod):
    wallet_balance = 5000  # demo balance

    def pay(self, amount):
        print(f"Wallet Balance: ₹{self.wallet_balance}")

        if amount > self.wallet_balance:
            print("❌ Insufficient wallet balance")
            return False

        WalletPayment.wallet_balance -= amount
        print("Wallet payment successful")
        return True


# -------------------------------------------------
# 7️⃣ Payment Gateway Controller
# -------------------------------------------------
class PaymentGateway:

    def process_payment(self, method: PaymentMethod, amount, user):

        print(f"\nInitiating payment of ₹{amount}...")

        success = method.pay(amount)

        txn_id = generate_txn_id()
        timestamp = datetime.now()

        if success:
            print("✅ Payment Successful")
            status = "SUCCESS"
        else:
            print("❌ Payment Failed")
            status = "FAILED"

        # Log transaction
        log_transaction(
            f"{timestamp} | {txn_id} | {user} | ₹{amount} | {status}"
        )

        print("Transaction ID:", txn_id)
        return success


# -------------------------------------------------
# 8️⃣ Simple Login Simulation
# -------------------------------------------------
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    # demo check
    if username == "admin" and password == "1234":
        print("Login successful\n")
        return username
    else:
        print("Invalid login")
        return None


# -------------------------------------------------
# 9️⃣ Main Application
# -------------------------------------------------
def main():

    print("===== PAYMENT GATEWAY SYSTEM =====\n")

    user = login()
    if not user:
        return

    amount = int(input("Enter amount to pay: ₹"))

    print("\nChoose payment method:")
    print("1. Card")
    print("2. UPI")
    print("3. Wallet")

    choice = input("Select: ")

    if choice == "1":
        method = CardPayment()
    elif choice == "2":
        method = UPIPayment()
    elif choice == "3":
        method = WalletPayment()
    else:
        print("Invalid choice")
        return

    gateway = PaymentGateway()
    gateway.process_payment(method, amount, user)


# -------------------------------------------------
if __name__ == "__main__":
    main()
