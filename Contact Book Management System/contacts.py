import os
from load_and_save import save_contacts_to_file

contacts = {}

def add_contact():
    name = (input("Enter Your Name: "))
    email = input("Enter Your Email: ")
    
    phone = int(input("Enter Your Phone: "))
    while not phone.isdigit() or len(phone) != 11:
        print("Invalid phone number. Please enter a valid 11-digit phone number.")
        phone = input("Enter Your Phone: ")
    
    if phone in contacts:
        print("This phone number already exists. Please enter a different number.")
        return
    
    address = input("Enter Your Address: ")
    contact = {'name': name, 'phone': phone, 'email': email, 'address': address}
    
    contacts[phone] = contact
    save_contacts_to_file(contacts)
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for phone, details in contacts.items():
            print(f"Name: {details['name']}, Email: {details['email']}, Phone: {phone}, Address: {details['address']}")

def search_contact():
    search_term = input("Enter name or phone to search: ")
    found = False
    for phone, details in contacts.items():
        if search_term.lower() in details['name'].lower() or search_term == phone:
            print(f"Name: {details['name']}, Email: {details['email']}, Phone: {phone}, Address: {details['address']}")
            found = True
    if not found:
        print("No contact found.")

def remove_contact():
    phone = input("Enter phone number to remove: ")
    if phone in contacts:
        del contacts[phone]
        save_contacts_to_file(contacts)
        print("Contact removed successfully!")
    else:
        print("Contact not found.")
