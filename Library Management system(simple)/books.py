import json
import add_books
import view_all_books
import update_book
import delete_book
import lend_book

def restore_lend_data():
    
        with open("lend_data.json", 'r') as fp:
            return json.load(fp)
def restore_all_books():
    
        with open("booklist.json", 'r') as fp:
            return json.load(fp)
    

def save_books(all_books):
    with open("booklist.json", 'w') as fp:
        json.dump(all_books, fp, indent=4)

def main():
    
    all_books = restore_all_books()

    while True:
        print("\nWelcome to the Library Management System")
        print("0. Exit")
        print("1. Add books")
        print("2. View all books")
        print("3. Update a book")
        print("4. Remove a book")
        print("5. Lend Book")
        print("6. Return Book")

       
        menu = int(input("Select a number: "))
        

        if menu == 0:
            print("Thanks for using the Library Management System!")
            break
        elif menu == 1:
            all_books = add_books.add_books(all_books)
            save_books(all_books)
        elif menu == 2:
            view_all_books.view_books(all_books)
        elif menu == 3:
            all_books = update_book.update_books(all_books)
            save_books(all_books)
        elif menu == 4:
            all_books = delete_book.delete_book(all_books)
            save_books(all_books)
        elif menu == 5:
            all_books = lend_book.lend_book(all_books)
            save_books(all_books)
        

        else:
            print("Choose a valid number.")

if __name__ == "__main__":
    main()
