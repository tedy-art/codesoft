class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"\nContact '{contact.name}' added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("\nContact book is empty.")
        else:
            print("\nContact List:")
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone_number}")

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts
                   if search_term.lower() in contact.name.lower() or
                   search_term in contact.phone_number]
        if results:
            print("\nSearch Results:")
            for result in results:
                print(f"Name: {result.name}, Phone: {result.phone_number}")
        else:
            print("\nNo matching contacts found.")

    def update_contact(self, name, new_phone_number, new_email, new_address):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.phone_number = new_phone_number
                contact.email = new_email
                contact.address = new_address
                print(f"\nContact '{contact.name}' updated successfully!")
                return
        print("\nContact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"\nContact '{contact.name}' deleted successfully!")
                return
        print("\nContact not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter the contact's name: ")
            phone_number = input("Enter the contact's phone number: ")
            email = input("Enter the contact's email: ")
            address = input("Enter the contact's address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(new_contact)
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            search_term = input("Enter the name or phone number to search: ")
            contact_book.search_contact(search_term)
        elif choice == "4":
            name = input("Enter the name of the contact to update: ")
            new_phone_number = input("Enter the new phone number: ")
            new_email = input("Enter the new email: ")
            new_address = input("Enter the new address: ")
            contact_book.update_contact(name, new_phone_number, new_email, new_address)
        elif choice == "5":
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)
        elif choice == "6":
            print("Exiting the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
