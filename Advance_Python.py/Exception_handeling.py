balance = 10000
PIN = 6965

print("=== Welcome to ATM ===")

try:
    user_pin = int(input("Enter your 4-digit PIN: "))

    if user_pin != PIN:
        raise ValueError("Incorrect PIN")

    while True:
        print("\n1. Check Balance")
        print("2. Withdraw Money")
        print("3. Exit")

        try:
            choice = int(input("Choose an option: "))

            if choice == 1:
                print("Current Balance:", balance)

            elif choice == 2:
                amount = int(input("Enter amount to withdraw: "))

                if amount <= 0:
                    raise ValueError("Amount must be positive")

                if amount > balance:
                    raise RuntimeError("Insufficient balance")

                balance -= amount
                print("Withdrawal successful!")
                print("Remaining Balance:", balance)

            elif choice == 3:
                print("Thank you for using ATM.")
                break

            else:
                print("Invalid menu choice!")

        except ValueError as ve:
            print("Input Error:", ve)

        except RuntimeError as re:
            print("Transaction Error:", re)

except ValueError as e:
    print("Access Denied:", e)

except Exception as e:
    print("Unexpected Error:", e)

finally:
    print("\nATM session closed.")
