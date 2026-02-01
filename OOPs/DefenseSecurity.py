class DefenseSystem:                      #ENCAPSULATION
    def __init__(self, system_name, security_code):
        self.system_name = system_name
        self.__security_code = security_code  
        self.__armed = False                   

    def __verify_code(self, code):
        return self.__security_code == code

    def arm_system(self, code):
        if self.__verify_code(code):
            self.__armed = True
            print("System armed successfully.")
        else:
            print("Access denied: Invalid security code.")

    def launch_missile(self, code):
        if not self.__armed:
            print("System not armed. Cannot launch missile.")
            return

        if self.__verify_code(code):
            print("🚀 Missile launched successfully!")
        else:
            print("Launch aborted: Invalid security code.")

    def system_status(self):
        status = "ARMED" if self.__armed else "DISARMED"
        print(f"System Status: {status}")


def main():
    print("=== DEFENSE SECURITY SYSTEM ===")

    system = DefenseSystem("Missile Defense Unit", "DEF123")

    while True:
        print("\n1. Arm System")
        print("2. Launch Missile")
        print("3. Check System Status")
        print("4. Exit")

        choice = input("Enter choice: ")
        code = input("Enter security code: ")

        if choice == "1":
            system.arm_system(code)

        elif choice == "2":
            system.launch_missile(code)

        elif choice == "3":
            system.system_status()

        elif choice == "4":
            print("System shutting down.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
