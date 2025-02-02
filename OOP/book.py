class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        # self.isbn = isbn
        self.is_borrowed = False
        
     
class Library():
    books = []
    # contains all the books
    def add_new_book(self):
        # add a new book to library
        list_library = [
            {"title": self.title,
             "author": self.author,
            #  "isbn": self.isbn,
             "available": self.is_borrowed
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
       
class Borrower():
    def __init__(self,ame_of_borrower):
        borrowed_books = []
        self.name_of_borrower = ame_of_borrower