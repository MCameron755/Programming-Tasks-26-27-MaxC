"""
TASK: 03 Contact Book

# Store contacts in a text file, each line containing
name,phone,email
Program must allow:
- Add contact
- Search contact (sequential search)
- Display all

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

filename = "contacts.txt"

def addcontact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    with open(filename, "a") as f:
        f.write(f"{name},{phone},{email}\n")
    print("Contact added successfully.")

def searchcontact():
    target = input("Enter name to search: ")
    found = False
    with open(filename, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) >= 3 and parts[0].strip().lower() == target:
                print(f"Found: Name: {parts[0]}, Phone: {parts[1]}, Email: {parts[2]}")
                found = True
                break
    if not found:
        print("Contact not found.")

def displaycontacts():
    with open(filename, "r") as f:
        print("Contacts:")
        for line in f:
            parts = line.strip().split(",")
            if len(parts) >= 3:
                print(f"Name: {parts[0]}, Phone: {parts[1]}, Email: {parts[2]}")

def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display All Contacts")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            addcontact()
        elif choice == "2":
            searchcontact()
        elif choice == "3":
            displaycontacts()
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
