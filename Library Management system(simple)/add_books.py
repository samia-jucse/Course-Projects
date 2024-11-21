from  save_all_books import save_books
def add_books(all_books):
    title = input("Enter Book Title:")
    author = input("Enter Author Name:")
    isbn = input("Enter ISBN Number:")
    year = int(input("Enter Publishing Year:"))
    price = int(input("Enter Book Price:"))
    quantity = int(input("Enter Book Quantity:"))

    book = {
        "title" : title,
        "author" : author,
        "isbn" : isbn,
        "year" : year,
        "price" : price,
        "quantity" : quantity,
    }
    
    all_books.append(book)
    save_books(all_books)
    print("Books added sucessfully!")
    return all_books
    
