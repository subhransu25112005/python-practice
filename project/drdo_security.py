class DRDOSecurityZone:
    def __init__(self, officer_id, clearance_level):
        self.officer_id = officer_id
        self.clearance_level = clearance_level

    def __enter__(self):
        print("🔐 Initializing DRDO Secure Zone...")
        if self.clearance_level < 5:
            raise PermissionError("❌ Clearance level too low!")

        print(f"✅ Access Granted to Officer ID: {self.officer_id}")
        print("🟢 Secure systems unlocked")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("🔴 Secure systems locked")
        print("🚨 Session terminated")

        if exc_type:
            print("⚠️ SECURITY ALERT: Abnormal termination detected")
            return False   # propagate exception

        print("✅ Operation completed safely")
        return True


# ---------- MAIN PROGRAM ----------
print("\n🇮🇳 DRDO CLASSIFIED OPERATION SYSTEM 🇮🇳\n")

try:
    officer_id = input("Enter Officer ID: ")
    clearance = int(input("Enter Clearance Level (1-10): "))

    with DRDOSecurityZone(officer_id, clearance):
        print("\n🚀 Launching classified defense operation...")
        print("📡 Accessing missile guidance system...")
        print("🧠 Processing encrypted data...")

except PermissionError as p:
    print(p)

except Exception as e:
    print("System Error:", e)
