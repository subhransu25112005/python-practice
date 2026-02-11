# ===============================
# HOSPITAL PATIENT MANAGEMENT
# ===============================

# ❌ WRONG DESIGN (violates SRP)
# class Patient:
#     def __init__(self, name, diagnosis):
#         self.name = name
#         self.diagnosis = diagnosis
#
#     def save_to_database(self):
#         print("Saving patient to DB")
#
#     def generate_bill(self):
#         print("Generating bill")
#
#     def send_email(self):
#         print("Sending email")


# ✅ CORRECT DESIGN (SRP)

class Patient:
    def __init__(self, name, diagnosis):
        self.name = name
        self.diagnosis = diagnosis


class PatientRepository:
    def save(self, patient: Patient):
        print(f"Saving {patient.name} to database")


class BillingService:
    def generate_bill(self, patient: Patient):
        print(f"Generating bill for {patient.name}")


class NotificationService:
    def send_email(self, patient: Patient):
        print(f"Sending email to {patient.name}")


patient = Patient("Ramesh", "Flu")

repo = PatientRepository()
billing = BillingService()
notify = NotificationService()

repo.save(patient)
billing.generate_bill(patient)
notify.send_email(patient)
