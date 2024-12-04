import os
import contacts
def save_contacts_to_file(contacts):
    with open("contacts_list.txt", "w") as file:
        for phone, contact in contacts.items():
            file.write(f"{contact['name']},{contact['email']},{phone},{contact['address']}\n")



def load_contacts():
    if os.path.exists("contacts_list.txt"):
        with open("contacts_list.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                name, email, phone, address = line.strip().split(",")
                contacts[phone] = {'name': name, 'email': email, 'address': address}
