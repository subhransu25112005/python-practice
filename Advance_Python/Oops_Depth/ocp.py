from abc import ABC, abstractmethod

# ❌ WRONG DESIGN (modification required every time)
# class PaymentProcessor:
#     def process(self, method, amount):
#         if method == "card":
#             print("Card payment")
#         elif method == "upi":
#             print("UPI payment")


# ✅ CORRECT DESIGN (OCP)

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Card")


class UPIPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class CryptoPayment(PaymentMethod):  # New feature without modifying old code
    def pay(self, amount):
        print(f"Paid ₹{amount} using Crypto")


class Checkout:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def complete_order(self, amount):
        self.payment_method.pay(amount)


checkout = Checkout(CardPayment())
checkout.complete_order(5000)
