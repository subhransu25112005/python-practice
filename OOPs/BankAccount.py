class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def show_details(self):
        print("\n----- Account Details -----")
        print(f"Name           : {self.name}")
        print(f"Account Number : {self.account_number}")
        print(f"Balance        : ₹{self.balance}")
        print("----------------------------")


def main():
    print("=== Welcome to Bank Account System ===")

    name = input("Enter account holder name: ")
    acc_no = input("Enter account number: ")

    account = BankAccount(name, acc_no)

    while True:
        print("\nChoose an option:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Show Account Details")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)

        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)

        elif choice == "3":
            account.show_details()

        elif choice == "4":
            print("Thank you for using the Bank Account System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
