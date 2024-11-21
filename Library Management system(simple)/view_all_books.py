def view_books(all_books):
    if all_books:
        for book in all_books:
            print(f"Title: {book['title']}, "
                  f"Author: {book['author']}, "
                  f"ISBN: {book['isbn']}, "
                  f"Year: {book['year']}, "
                  f"Price: {book['price']}, "
                  f"Quantity: {book['quantity']}\n")
    else:
        print("No Book Found in All Books")
