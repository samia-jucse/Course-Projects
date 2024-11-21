import add_books
import view_all_books
all_books = []

while True:
    print("Welcome Library Management System")
    print(" 0 .Exit")
    print("1. Add books")
    print("2. View All books")
    
    menu =int(input("Select a number:"))
    
   
    
    if menu == 0:
        print("Thanks ")
        break
    elif menu == 1:
       all_books =add_books.add_books(all_books)
       
    elif menu == 2:
        view_all_books.view_books(all_books)
        
    else:print("Choose a valid number")
    