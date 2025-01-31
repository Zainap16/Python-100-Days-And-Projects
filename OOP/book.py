class Book():
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
        
list_library = []       
class Library():
    def add_new_book(self):
        # add a new book to library
        list_library = [
            {"title": self.title,
             "author": self.author,
             "isbn": self.isbn,
             "available": self.available
             }
        ]
        
        
        
        
    def borrow_book():
        # borrow a book (mark it as unavailable)
        pass
    def return_book():
        # return a book (mark it as available)
        pass
    def display_books():
        # display all books in the library (including their availability)
        pass
       
        