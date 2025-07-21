contacts = {}

def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    contacts[name] = phone
    print("Contact added!✅\n")

def view_contacts():
    if len(contacts) == 0:
        print("❌No contacts found.\n")
    else:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

def search_contact():
    name = input("Enter name to search: ").strip()
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("❌Contact not found!\n")

def delete_contact():
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print("Deleted successfully!✅\n")
    else:
        print("❌Contact not found.\n")

while True:
    print("\n📇 Contact Book")
    print("1. Add Contact")
    print("2. View All")
    print("3. Search")
    print("4. Delete")
    print("5. Exit\n")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_contact()
        elif choice == 2:
            view_contacts()
        elif choice == 3:
            search_contact()
        elif choice == 4:
            delete_contact()
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("❌Invalid option, try again.\n")
    except ValueError:
        print("❌Invalid option, try again.\n")