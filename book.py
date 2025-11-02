class Book:
    """
    Book
    """
    def __init__(self,title,author,isbn,is_available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

    def get_details(self):
        return f" the book:{self.title}, by:{self.author}, number:{self.isbn} , available: {self.is_available}"