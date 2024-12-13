import json
def save_books(all_books):
    # with open("all_books.cvs","w") as fp:
    #     for book in all_books :
    #          line = f"{book['title']}, 
    #          {book['author']},
    #          {book['isbn']},
    #          {book['year']}, {book['price']},
    #          {book['quantity']},
    #          {book['bookAddedAt']}\n"
    #          fp.write(line)
    # just save in a cvs file 
    with open("booklist.json","w") as fp:
        json.dump(all_books,fp,indent=4)
        
        