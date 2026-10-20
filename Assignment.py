# ============================================================
# git remote add origin https://github.com/joshuajonathankaridbangura-collab/PROGAMMING-HEALTH-PAITENT-RECORD-SYSTEM.git
# git branch -M main
# git push -u origin main+
# ============================================================


# ------------------------------------------------------------
# CLASS 1: Person
# ------------------------------------------------------------
class Person:
    total_people = 0

    def __init__(self, name, person_id, age, phone):
        self.name = name
        self.person_id = person_id
        self.age = age
        self.phone = phone

        Person.total_people += 1

    # Instance method
    def display_basic_info(self):
        print("Patient ID :", self.person_id)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Phone      :", self.phone)

    # Class method
    @classmethod
    def get_total_people(cls):
        return cls.total_people


# ------------------------------------------------------------
# CLASS 2: Patient
# Patient inherits from Person
# ------------------------------------------------------------
class Patient(Person):

    def __init__(
        self,
        name,
        patient_id,
        age,
        phone,
        diagnosis,
        blood_group,
        emergency_contact
    ):
        # Call the parent class constructor
        super().__init__(name, patient_id, age, phone)

        self.diagnosis = diagnosis
        self.blood_group = blood_group
        self.emergency_contact = emergency_contact
        self.visit_count = 0

    # Instance method
    def display_record(self):
        print("\n----------------------------------------")
        print("         PATIENT RECORD")
        print("----------------------------------------")
        print("Patient ID        :", self.person_id)
        print("Name              :", self.name)
        print("Age               :", self.age)
        print("Phone             :", self.phone)
        print("Diagnosis         :", self.diagnosis)
        print("Blood Group       :", self.blood_group)
        print("Emergency Contact :", self.emergency_contact)
        print("Number of Visits  :", self.visit_count)
        print("----------------------------------------")

    # Instance method
    def update_diagnosis(self, new_diagnosis):
        self.diagnosis = new_diagnosis

    # Instance method
    def record_visit(self):
        self.visit_count += 1


# ------------------------------------------------------------
# CLASS 3: PatientRecordSystem
# ------------------------------------------------------------
class PatientRecordSystem:

    def __init__(self):
        # One main data structure: LIST
        self.patients = []

    # Add patient
    def add_patient(self, patient):

        # Check if patient ID already exists
        if self.search_patient(patient.person_id) is not None:
            print("\nPatient ID already exists.")
            return False

        self.patients.append(patient)

        print("\nPatient added successfully.")
        return True

    # Search patient
    def search_patient(self, patient_id):

        for patient in self.patients:

            if patient.person_id.lower() == patient_id.lower():
                return patient

        return None

    # Display all patients
    def display_all_patients(self):

        if len(self.patients) == 0:
            print("\nNo patient records available.")
            return

        print("\n========================================")
        print("        ALL PATIENT RECORDS")
        print("========================================")

        for patient in self.patients:
            patient.display_record()

    # Update diagnosis
    def update_diagnosis(self, patient_id, new_diagnosis):

        patient = self.search_patient(patient_id)

        if patient is not None:
            patient.update_diagnosis(new_diagnosis)
            print("\nDiagnosis updated successfully.")
            return

        print("\nPatient not found.")

    # Record patient visit
    def record_patient_visit(self, patient_id):

        patient = self.search_patient(patient_id)

        if patient is not None:
            patient.record_visit()
            print("\nPatient visit recorded successfully.")
            return

        print("\nPatient not found.")


# ------------------------------------------------------------
# FUNCTION: Load Sample Patients
# ------------------------------------------------------------
def load_sample_patients(system):

    patients = [

        Patient(
            "Abdul Rahman",
            "P001",
            22,
            "076000001",
            "Malaria",
            "O+",
            "076901011"
        ),

        Patient(
            "Joshua Jonathan",
            "P002",
            21,
            "076000002",
            "Hypertension",
            "A+",
            "076174002"
        ),

        Patient(
            "Thomas Turay",
            "P003",
            21,
            "076000003",
            "Asthma",
            "B+",
            "076103043"
        ),

        Patient(
            "Joseph Davies",
            "P004",
            35,
            "076000004",
            "Cold",
            "AB+",
            "076900004"
        ),

        Patient(
            "Andrew Conteh",
            "P005",
            42,
            "076000005",
            "Arthritis",
            "O-",
            "076912015"
        ),

        Patient(
            "Moses Fullah",
            "P006",
            22,
            "076000006",
            "Typhoid",
            "B-",
            "078704016"
        )
    ]

    # Add all patients to the system
    for patient in patients:
        system.add_patient(patient)


# ------------------------------------------------------------
# FUNCTION: Add New Patient
# ------------------------------------------------------------
def add_new_patient(system):

    print("\n========================================")
    print("          ADD NEW PATIENT")
    print("========================================")

    patient_id = input("Enter Patient ID: ")

    # Check duplicate ID
    if system.search_patient(patient_id) is not None:
        print("\nPatient ID already exists.")
        return

    name = input("Enter Full Name: ")

    while True:
        try:
            age = int(input("Enter Age: "))

            if age <= 0:
                print("Age must be greater than zero.")
            else:
                break

        except ValueError:
            print("Please enter a valid number.")

    phone = input("Enter Phone Number: ")
    diagnosis = input("Enter Diagnosis: ")
    blood_group = input("Enter Blood Group: ")
    emergency_contact = input("Enter Emergency Contact: ")

    patient = Patient(
        name,
        patient_id,
        age,
        phone,
        diagnosis,
        blood_group,
        emergency_contact
    )

    system.add_patient(patient)


# ------------------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------------------
def main():

    # Create PatientRecordSystem object
    system = PatientRecordSystem()

    # Load more than five patient records
    load_sample_patients(system)

    print("\n============================================")
    print("     HEALTH PATIENT RECORD SYSTEM")
    print("============================================")
    print("Object-Oriented Programming Project")

    while True:

        print("\n")
        print("============= MAIN MENU =============")
        print("1. Display All Patients")
        print("2. Search Patient")
        print("3. Add New Patient")
        print("4. Update Diagnosis")
        print("5. Record Patient Visit")
        print("6. Display Total People")
        print("7. Exit")
        print("=====================================")

        choice = input("Enter your choice (1-7): ")

        # ----------------------------------------------------
        # OPTION 1
        # ----------------------------------------------------
        if choice == "1":

            system.display_all_patients()

        # ----------------------------------------------------
        # OPTION 2
        # ----------------------------------------------------
        elif choice == "2":

            patient_id = input("Enter Patient ID: ")

            patient = system.search_patient(patient_id)

            if patient is not None:
                patient.display_record()
            else:
                print("\nPatient not found.")

        # ----------------------------------------------------
        # OPTION 3
        # ----------------------------------------------------
        elif choice == "3":

            add_new_patient(system)

        # ----------------------------------------------------
        # OPTION 4
        # ----------------------------------------------------
        elif choice == "4":

            patient_id = input("Enter Patient ID: ")
            new_diagnosis = input("Enter New Diagnosis: ")

            system.update_diagnosis(
                patient_id,
                new_diagnosis
            )

        # ----------------------------------------------------
        # OPTION 5
        # ----------------------------------------------------
        elif choice == "5":

            patient_id = input("Enter Patient ID: ")

            system.record_patient_visit(
                patient_id
            )

        # ----------------------------------------------------
        # OPTION 6
        # ----------------------------------------------------
        elif choice == "6":

            total = Person.get_total_people()

            print("\nTotal Person objects created:", total)

        # ----------------------------------------------------
        # OPTION 7
        # ----------------------------------------------------
        elif choice == "7":

            print("\nThank you for using the")
            print("Health Patient Record System.")
            print("Goodbye!")

            break

        # ----------------------------------------------------
        # INVALID OPTION
        # ----------------------------------------------------
        else:

            print("\nInvalid choice.")
            print("Please select a number from 1 to 7.")


# ------------------------------------------------------------
# PROGRAM START
# ------------------------------------------------------------
if __name__ == "__main__":
    main()