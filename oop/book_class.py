# Define the Book class
class Book:
    # Constructor method: initializes a new Book instance with title, author, and year
    def __init__(self, title, author, year):
        self.title = title       
        self.author = author     
        self.year = year         

    # Destructor method: called when the object is about to be destroyed
    def __del__(self):
        print(f"Deleting {self.title}")  # Message indicating the book is being deleted

    # String representation: used by print() and str()
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    # Official representation: used by repr(), debugging, or recreating the object
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
