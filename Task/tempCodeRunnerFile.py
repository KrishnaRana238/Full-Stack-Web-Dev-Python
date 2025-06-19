
# returnning a book
def return_book(book):
    if book in library["borrowed_books"]:
        library["books"][book] += 1
        del library["borrowed_books"][book]
        print(f"Book '{book}' returned successfully.")
    else:
        print(f"Book '{book}' was not borrowed.")
print(return_book("Brave New World"))
    