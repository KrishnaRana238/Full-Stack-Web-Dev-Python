# #Scenario
# # A library wants to track of books it has, how many copies of each book are available,
# # and which books are borrowed by which books. Implements a simple system that allows
# # Adding new books to the library inventory
# # borrowig a book
# # returning a book
# # chech which book a member has borrowed

library = {
    "books": {"The Great Gatsby": 5, "1984": 3, "To Kill a Mockingbird": 4 , 
              "Pride and Prejudice": 2, "How to invest time": 7},
    "borrowed_books": {},
    "returned_books": {},   
}
# print(library)  
# library["books"].update({"The Catcher in the Rye": 8, "Brave New World": 9})
# print("Updated Library Inventory:", library["books"])
# available_books = library["books"]
# print("Available Books:", available_books)
# # boorrowing a book
# book = "Brave New World"
# copy = library["books"].get(book, 0)

# library["borrowed_books"][book] = copy - (copy > 0)

# print("Borrowed Books:", library["borrowed_books"])

# # returning a book
# def return_book(book):
#     if book in library["borrowed_books"]:
#         library["returned_books"][book] = library["borrowed_books"].pop(book)
#         library["books"][book] += 1
#         print(f"Book '{book}' returned successfully.")
#     else:
#         print(f"Book '{book}' was not borrowed.")
# return_book("Brave New World")

# # Check which book a member has borrowed
# def check_borrowed_books():
#     if library["borrowed_books"]:
#         print("Borrowed Books:")
#         for book, copies in library["borrowed_books"].items():
#             print(f"{book}: {copies} copies")
#     else:
#         print("No books are currently borrowed.")
# check_borrowed_books()


books = {}
members = {}

def add_book(title, count =1):
    if title in books:
        books[title]['total'] += count
        books[title]['available'] += count
    else:
        books[title] = {'total': count, 'available': count}
    print(f"Added {count} copy/copies of '{title}' to the library.")
add_book("The Great Gatsby", 5)
add_book("1984", 3)
add_book("To Kill a Mockingbird", 4)  


def borrow_book(member, title):
    if title not in books:
        print(f"Sorry, '{title}' is not available in the library.")
        return
    if books[title]['available'] <= 0:
        print(f"Sorry, '{title}' is currently not available for borrowing.")
        return
    if member not in members:
        members[member] = []
    members[member].append(title)
    books[title]['available'] -= 1
    print(f"{member} borrowed '{title}'.")
borrow_book("Alice", "1984")
borrow_book("Bob", "The Great Gatsby")
        
    

# def borrow_book(member_name, title):
#     if title not in books or books[title]['available'] <= 0:
#         print(f"Sorry, '{title}' is not available for borrowing.")
#         return
#     if member_name not in members:
#         members[member_name] = []
#     members[member_name].append(title)
#     books[title]['available'] -= 1
#     print(f"{member_name} borrowed '{title}'.")
# borrow_book("Alice", "1984")
# borrow_book("Bob", "The Great Gatsby")    

# def available_books():
#     print("Available books in the library:")
#     for title, info in books.items():
#         print(f"{title}: {info['available']} copies available out of {info['total']} total copies.")
# available_books()


