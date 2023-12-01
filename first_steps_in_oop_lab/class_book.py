class Book:
    def __init__(self, name: str, autor: str, pages: int):
        self.name = name
        self.author = autor
        self.pages = pages


book = Book("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)