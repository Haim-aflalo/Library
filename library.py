from book import Book
from user import User


class Library:
    """Library"""
    max_borrows_day = 14
    def __init__(self,books,users):
        self.users = users
        self.books = books

    def register_user(self,user:User):
        self.users[user.user_id] = user

    def add_book(self,book:Book):
        self.books[book.isbn] = book


