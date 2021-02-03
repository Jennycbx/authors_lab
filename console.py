import pdb
from models.author import Author

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

author_1 = Author("J.R.R. Tolkien", 5)
author_repository.save(author_1)

book_1 = Book("The Fellowship of the Rings", author_1, 1954)
book_repository.save(book_1)
book_2 = Book("The Two Towers", author_1, 1954)
book_repository.save(book_2)
book_3 = Book("The Return of the King", author_1, 1955)
book_repository.save(book_3)
book_4 Book("The Silmarillion", author_1, 1977)
book_repository.save(book_4)

print(author_repository.select_all())




pdb.set_trace()