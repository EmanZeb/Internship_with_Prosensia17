def add_contact(contact_list, name, phone):  #Function to add contact
    for contact in contact_list:
        if contact[0].lower() == name.lower():
            print("Contact already exists.")
            return
    contact_list.append((name, phone))
    print("Contact added successfully.")
def search_contact(contact_list, name):   #Function to search contact
    for contact in contact_list:
        if contact[0].lower() == name.lower():
            print(f"Found contact: {contact[0]} - {contact[1]}")
            return
    print("Contact not found.")
def display_contacts(contact_list):#Function to display contacts
    if not contact_list:
        print("No contacts available.")
    else:
        print("Contact List:")
        for contact in contact_list:
            print(f"{contact[0]} - {contact[1]}")
def main():
    contact_list = []
    
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display All Contacts")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            add_contact(contact_list, name, phone)
        
        elif choice == '2':
            name = input("Enter name to search: ")
            search_contact(contact_list, name)
        
        elif choice == '3':
            display_contacts(contact_list)
        
        elif choice == '4':
            print("Exiting the contact book.")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
main()