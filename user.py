from book import Book


class User:
    """user"""
    def __init__(self,user_id:str,name:str,borrowed_books:list[Book]):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = borrowed_books

    def borrow_book(self,book:Book):
        if book.is_available:
            self.borrowed_books.append(book)


    def return_book(self,book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)




