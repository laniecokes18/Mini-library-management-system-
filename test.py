# test.py
from operation import *

books = {}
members = []
genres = ("Fiction", "Non-Fiction")

add_book(books, "111", "Book A", "Author X", "Fiction", 2, genres)
add_member(members, 1, "John", "john@mail.com")

assert add_book(books, "111", "Book A", "Author X", "Fiction", 2, genres) == "ISBN already exists."
assert borrow_book(members, books, 1, "111") == "Book borrowed."
assert borrow_book(members, books, 1, "111") == "Book borrowed."
assert borrow_book(members, books, 1, "111") == "No copies left."
assert return_book(members, books, 1, "111") == "Book returned."
print("All tests passed.")
