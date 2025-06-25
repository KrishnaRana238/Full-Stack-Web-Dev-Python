# # Design a library management system  using Object Oriented Programming concepts in Python`
# # Class: Book, Member, Library
# # 
# # Features: Add Books, register members, borrow books, return books, view available books
# # extend the library system with these are the features:
# # search book by title or author
# # limit the number of books a member can borrow (say max 3)
# # Handlev fines for late returns( we'll assume a fixed fine per day)
# # Track borrowed books and Calculate fines on return`

# from datetime import datetime, timedelta

# max_borrow_book=3
# fine_per_day = 10
# borrow_day=15

# class Books():
#     def __init__(self,book_id,title, author, ):
#         self.book_id = book_id
#         self.title = title
#         self.author = author
#         self.available_copies = True
#     def __str__(self):
#         return f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Available Copies: {self.available_copies}"

# class Member():
#     def __init__(self, member_id, name):
#         self.member_id = member_id
#         self.name = name
#         self.borrowed_books = []
    
#     def __str__(self):
#         return f"Member ID: {self.member_id}, Name: {self.name}, Borrowed Books: {len(self.borrowed_books)}"
    
# class Library():
#     def __init__(self):
#         self.books = {}
#         self.members = {}
    
#     def add_book(self, book_id,title, author):













from datetime import datetime, timedelta

MAX_BORROW_LIMIT = 3
FINE_PER_DAY = 10
BORROW_DAYS = 14

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True
    
    def __str__(self):
        return f"[{self.book_id}] {self.title} by {self.author} - {'Available' if self.available else 'Not Available'}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = {}  # book_id -> borrow_date

    def __str__(self):
        return f"Member {self.member_id}: {self.name}, Borrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}      # book_id -> Book
        self.members = {}    # member_id -> Member


    def add_book(self, book_id, title, author):
        if book_id in self.books:
            print(" Book ID already exists.")
            return
        self.books[book_id] = Book(book_id, title, author)
        print(" Book added successfully.")

    def view_available_books(self):
        print("\n📚 Available Books:")
        for book in self.books.values():
            if book.available:
                print(book)

    def search_books(self, keyword):
        print(f"\n Search results for '{keyword}':")
        found = False
        for book in self.books.values():
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                print(book)
                found = True
        if not found:
            print("No matching books found.")

    
    def register_member(self, member_id, name):
        if member_id in self.members:
            print(" Member ID already exists.")
            return
        self.members[member_id] = Member(member_id, name)
        print(" Member registered successfully.")

    
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print(" Member not found.")
            return
        if book_id not in self.books:
            print(" Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if not book.available:
            print(" Book is already borrowed.")
            return
        if len(member.borrowed_books) >= MAX_BORROW_LIMIT:
            print(" Borrowing limit reached (max 3 books).")
            return

        book.available = False
        member.borrowed_books[book_id] = datetime.now()
        print(f" Book '{book.title}' borrowed by {member.name}. Due in {BORROW_DAYS} days.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members or book_id not in self.books:
            print(" Invalid member or book ID.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book_id not in member.borrowed_books:
            print(" This member did not borrow the book.")
            return

        borrow_date = member.borrowed_books.pop(book_id)
        book.available = True

        due_date = borrow_date + timedelta(days=BORROW_DAYS)
        today = datetime.now()
        overdue_days = (today - due_date).days

        if overdue_days > 0:
            fine = overdue_days * FINE_PER_DAY
            print(f" Book returned late by {overdue_days} days. Fine = ₹{fine}")
        else:
            print(" Book returned on time. No fine.")

    def view_borrowed_books(self, member_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        print(f"\n Borrowed Books by {member.name}:")
        for book_id, date in member.borrowed_books.items():
            book = self.books[book_id]
            due_date = date + timedelta(days=BORROW_DAYS)
            print(f"{book} | Borrowed on: {date.strftime('%Y-%m-%d')} | Due: {due_date.strftime('%Y-%m-%d')}")



if __name__ == "__main__":
    lib = Library()

   
    lib.add_book("B001", "The Alchemist", "Paulo Coelho")
    lib.add_book("B002", "1984", "George Orwell")
    lib.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

   
    lib.register_member("M001", "Alice")
    lib.register_member("M002", "Bob")

    
    lib.search_books("alchemist")

    
    lib.borrow_book("M001", "B001")
    lib.borrow_book("M001", "B002")
    lib.borrow_book("M001", "B003")
    lib.borrow_book("M001", "B004")  
    lib.view_borrowed_books("M001")


    lib.view_available_books()


    lib.return_book("M001", "B001")
    lib.view_available_books()
