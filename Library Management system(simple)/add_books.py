from  save_all_books import save_books
import random
from datetime import datetime

def add_books(all_books):
    title = input("Enter Book Title:")
    author = input("Enter Author Name:")
    #isbn = input("Enter ISBN Number:")
    isbn= random.randint(10000,99999)
    
    year = int(input("Enter Publishing Year:"))
    price = int(input("Enter Book Price:"))
    quantity = int(input("Enter Book Quantity:"))
    bookAddedAt=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    book = {
        "title" : title,
        "author" : author,
        "isbn" : isbn,
        "year" : year,
        "price" : price,
        "quantity" : quantity,
        "bookAddedAt": bookAddedAt,
    }
    
    all_books.append(book)
    save_books(all_books)
    print("Books added sucessfully!")
    return all_books
    
