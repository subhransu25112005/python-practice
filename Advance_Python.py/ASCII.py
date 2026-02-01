while True:
    print("\n--- ASCII Converter Menu ---")
    print("1. Character to ASCII")
    print("2. ASCII to Character")
    print("3. String to ASCII")
    print("4. ASCII to String")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    # 1. Character to ASCII
    if choice == 1:
        ch = input("Enter a character: ")
        print("ASCII value:", ord(ch))

    # 2. ASCII to Character
    elif choice == 2:
        num = int(input("Enter ASCII value: "))
        print("Character:", chr(num))

    # 3. String to ASCII
    elif choice == 3:
        text = input("Enter a string: ")
        ascii_values = list(map(lambda c: ord(c), text))
        print("ASCII values:", ascii_values)

    # 4. ASCII to String
    elif choice == 4:
        nums = list(map(int, input("Enter ASCII values separated by space: ").split()))
        text = "".join(map(lambda n: chr(n), nums))
        print("String:", text)

    # 5. Exit
    elif choice == 5:
        print("Program exited.")
        break

    else:
        print("Invalid choice!")
