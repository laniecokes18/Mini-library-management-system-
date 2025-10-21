# demo.py
from operation import *

books = {}
members = []
genres = ("Fiction", "Non-Fiction", "Sci-Fi")

print(add_book(books, "1234", "The Martian", "Andy Weir", "Sci-Fi", 3, genres))
print(add_member(members, 1, "Jane Doe", "jane@mail.com"))
print(borrow_book(members, books, 1, "1234"))
print(return_book(members, books, 1, "1234"))
