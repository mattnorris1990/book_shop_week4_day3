from models.author import Author
from models.book import Book
import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

author_repository.delete_all()
book_repository.delete_all()

author1 = Author("Bob Bobbles")
author_repository.save(author1)

author2 = Author("Jango Fett")
author_repository.save(author2)

book1 = Book("Christmas Baubles II", author1)
book_repository.save(book1)

book2 = Book("I Don't Believe In Santa", author1)
book_repository.save(book2)

book3 = Book("Star Wars is a Myth", author2)
book_repository.save(book3)

book4 = Book("I Am Not A Clone", author2)
book_repository.save(book4)