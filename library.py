from book import Book
from user import User


class Library:
    """Library"""
    max_borrows_day = 14
    def __init__(self):
        self.users = {}
        self.books = {}

    def register_user(self,user:User):
        self.users[user.user_id] = user

    def add_book(self,book:Book):
        self.books[book.isbn] = book

    def perform_borrow(self,user_id,isbn):
        if user_id not in self.users:
            print("the user doesn't exist")
        if isbn not in self.books:
            print("the book doesn't exist")
        if not self.books[isbn].is_available:
            print("this book is already borrowed ")
        else:
            self.users[user_id].borrow_book(self.books[isbn])
            self.books[isbn].is_available = False



    def perform_return(self, user_id, isbn):
        if user_id not in self.users:
            print("the user doesn't exist")
        if isbn not in self.books:
            print("the book doesn't exist")
        if self.books[isbn].is_available:
            print("this book is already returned ")
        else:
            self.users[user_id].return_book(self.books[isbn])
            self.books[isbn].is_available = True