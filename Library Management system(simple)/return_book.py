from lend_book import load_lend_data,save_lend_data
def return_book(all_books):
    
    lenders_list = load_lend_data()
    borrower_name = input("Enter the borrower's name: ")

    for lender in lenders_list:
        if lender["borrower_name"] == borrower_name:
            lenders_list.remove(lender)
            save_lend_data(lenders_list)

            for book in all_books:
                if book["title"] == lender["book_title"]:
                    book["quantity"] += 1
                    print(f"Book '{lender['book_title']}' successfully returned!")
                    return all_books

            print("Book data not found in the system.")
            return all_books

    print("No matching lend record found for this borrower.")
    return all_books
