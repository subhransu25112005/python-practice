from abc import ABC, abstractmethod

# ❌ WRONG DESIGN (tight coupling)
# class EmailService:
#     def send(self, msg):
#         print("Email sent")
#
# class BankApp:
#     def __init__(self):
#         self.notification = EmailService()


# ✅ CORRECT DESIGN

class NotificationService(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(NotificationService):
    def send(self, message):
        print(f"Email sent: {message}")


class SMSNotification(NotificationService):
    def send(self, message):
        print(f"SMS sent: {message}")


class BankApp:
    def __init__(self, notification_service: NotificationService):
        self.notification_service = notification_service

    def transfer_money(self, amount):
        print(f"Transferred ₹{amount}")
        self.notification_service.send("Transaction Successful")


app = BankApp(EmailNotification())
app.transfer_money(10000)
