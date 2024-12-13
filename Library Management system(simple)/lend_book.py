import json
from datetime import datetime, timedelta


def load_lend_data():
    try:
        with open("lend_data.json", 'r') as fp:
            data = fp.read().strip()
            if not data:
                return []
            return json.loads(data)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Invalid JSON data in lend_data.json.")
        return []
def save_lend_data(lenders_list):
    with open("lend_data.json", 'w') as fp:
        json.dump(lenders_list, fp, indent=4)

def lend_book(all_books):
    lenders_list = load_lend_data()
    lend_book_name = input("Enter the name of the book to lend: ")

    for book in all_books:
        if lend_book_name == book["title"]:
            if book["quantity"] > 0:
                borrower_name = input("Enter borrower's name: ")
                borrower_phone = input("Enter borrower's phone number: ")
                due_date = datetime.now() + timedelta(days=7)
                due_date = due_date.strftime("%Y-%m-%d")

                lender_info = {
                    "book_title": lend_book_name,
                    "borrower_name": borrower_name,
                    "borrower_phone": borrower_phone,
                    "due_date": due_date
                }

                lenders_list.append(lender_info)
                save_lend_data(lenders_list)

                book["quantity"] -= 1 
                print("Book lending successful!")
                return all_books
            else:
                print("There are not enough books available to lend.")
                return all_books

    print(f"Book '{lend_book_name}' not found in the library.")
    return all_books
