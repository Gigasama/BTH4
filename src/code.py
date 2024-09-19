class Citizen:
    def __init__(self, id_number, name, age, address):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return f"ID: {self.id_number}, Name: {self.name}, Age: {self.age}, Address: {self.address}"

class CitizenManagement:
    def __init__(self):
        self.citizen_list = []

    def add_citizen(self, id_number, name, age, address):
        citizen = Citizen(id_number, name, age, address)
        self.citizen_list.append(citizen)
        print(f"Added citizen: {name}")

    def remove_citizen(self, id_number):
        for citizen in self.citizen_list:
            if citizen.id_number == id_number:
                self.citizen_list.remove(citizen)
                print(f"Removed citizen with ID: {id_number}")
                return
        print("Citizen not found.")

    def update_citizen(self, id_number, name=None, age=None, address=None):
        for citizen in self.citizen_list:
            if citizen.id_number == id_number:
                if name:
                    citizen.name = name
                if age:
                    citizen.age = age
                if address:
                    citizen.address = address
                print(f"Updated citizen with ID: {id_number}")
                return
        print("Citizen not found.")

    def search_citizen(self, id_number):
        for citizen in self.citizen_list:
            if citizen.id_number == id_number:
                print("Citizen found:")
                print(citizen)
                return
        print("Citizen not found.")

    def list_citizens(self):
        if not self.citizen_list:
            print("No citizens in the list.")
        else:
            print("List of citizens:")
            for citizen in self.citizen_list:
                print(citizen)

def menu():
    cm = CitizenManagement()
    while True:
        print("\n--- Citizen Management ---")
        print("1. Add citizen")
        print("2. Remove citizen")
        print("3. Update citizen")
        print("4. Search citizen")
        print("5. List all citizens")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            id_number = input("Enter ID number: ")
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            address = input("Enter address: ")
            cm.add_citizen(id_number, name, age, address)
        elif choice == '2':
            id_number = input("Enter ID number to remove: ")
            cm.remove_citizen(id_number)
        elif choice == '3':
            id_number = input("Enter ID number to update: ")
            name = input("Enter new name (or leave empty): ")
            age = input("Enter new age (or leave empty): ")
            age = int(age) if age else None
            address = input("Enter new address (or leave empty): ")
            cm.update_citizen(id_number, name, age, address)
        elif choice == '4':
            id_number = input("Enter ID number to search: ")
            cm.search_citizen(id_number)
        elif choice == '5':
            cm.list_citizens()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
