# library_management.py

class Book:
    """A class to represent a book with a title, author, and checked-out status."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Marks the book as returned (available)."""
        self._is_checked_out = False

    def is_available(self):
        """Returns True if the book is available (not checked out)."""
        return not self._is_checked_out


class Library:
    """A class to represent a library containing books."""

    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Adds a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Checks out a book by title if it is available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        # Book not found or already checked out — silently ignore as per expected behavior

    def return_book(self, title):
        """Returns a book by title if it is currently checked out."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        # Book not found or already returned — silently ignore as per expected behavior

    def list_available_books(self):
        """Prints all available books in the library."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
