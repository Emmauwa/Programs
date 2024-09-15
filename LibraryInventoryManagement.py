# Create a Book class with attributes for title, author, and availability.
class Book():
    def __init__(self, title, author, availability = True):
        self.title = title
        self.author = author
        self.availability = availability

class Library():
    # Use an array to store the library's collection of books.
    def __init__(self):
        self.books = []
    # Implement methods to add books, search for books by title or author, and update book availability using lambdas.
    def addBook(self, book):
        self.books.append(book)
    def searchByTitle(self, title):
        searchTitle = lambda book: book.title.lower() == title.lower()
        return list(filter(searchTitle, self.books))
    def searchByAuthor(self, author):
        searchAuthor = lambda book: book.author.lower() == author.lower()
        return list(filter(searchAuthor, self.books))          
    def updateBookAvailability(self, title, availability):
        for book in self.books:
            if book.title.lower() == title.lower():
               book.availability = availability
               return
        print(f"Book with title '{title}' not found.")
   
# Create instances of the Book class and test the functionality.
book1 = Book("The Hunger Games", "Suzanne Collins")
book2 = Book("Kaguya-sama: Love Is War", "Aka Akasaka")
book3 = Book("The Fragrant Flower Blooms with Dignity", "Deng Xiaohan")

library = Library()

library.addBook(book1)
library.addBook(book2)
library.addBook(book3)

# Search for books by title
print("Books with title 'The Fragrant Flower Blooms with Dignity':")
for book in library.searchByTitle("The Fragrant Flower Blooms with Dignity"):
    print(f"""Title: {book.title} 
Author: {book.author}""")
    
# Search for books by author
print("\nBooks with author 'Aka Akasaka':")
for book in library.searchByAuthor("Aka Akasaka"):
    print(f"""Title: {book.title} 
Author: {book.author}""")

# Print availability before update
print("\nAvailability of 'The Hunger Games':", book1.availability)

# Update the availability of 'The Hunger Games'
library.updateBookAvailability("The Hunger Games", False)

# Print availability after update
print("Updated availability of 'The Hunger Games':", book1.availability)


        
    
