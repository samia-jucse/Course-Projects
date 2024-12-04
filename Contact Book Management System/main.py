from contacts import add_contact, view_contacts, search_contact, remove_contact
from load_and_save import save_contacts_to_file

def main():
    
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Remove Contact")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue
        
        if choice == 1:
            add_contact()
        elif choice == 2:
            view_contacts()
        elif choice == 3:
            search_contact()
        elif choice == 4:
            remove_contact()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 5.")

