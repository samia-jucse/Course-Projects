import save_all_books
def delete_book(all_books):
    search_book=input("Enter the title of the book:")
    for book in all_books:
     if search_book == book["title"]:
         all_books.remove(book)
         save_all_books.save_books(all_books)
         print("Book delete successfully!")
    return all_books
