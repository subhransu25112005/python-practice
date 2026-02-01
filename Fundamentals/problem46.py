from random import randint

class Train:
    def __init__(self, train_no):
        self.train_no = train_no

    def book(self, frm, to):
        print(f"Ticket is booked in train no {self.train_no} from {frm} to {to}")

    def getstatus(self):
        print(f"{self.train_no} is Running Time")

    def getfare(self, fro, to):
        print(f"Ticket fare in train no: {self.train_no} from {fro} to {to} is {randint(212, 555)}")

t = Train(12399)
t.book("Rampur", "Delhi")
t.getstatus()
t.getfare("Rampur", "Delhi")
