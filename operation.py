# operations.py

# Add a new book
def add_book(books, isbn, title, author, genre, total_copies, genres):
    if isbn in books:
        return "ISBN already exists."
    if genre not in genres:
        return "Invalid genre."
    books[isbn] = {"title": title, "author": author, "genre": genre, "total_copies": total_copies}
    return "Book added successfully."

# Add a new member
def add_member(members, member_id, name, email):
    for m in members:
        if m["member_id"] == member_id:
            return "Member ID already exists."
    members.append({"member_id": member_id, "name": name, "email": email, "borrowed_books": []})
    return "Member added successfully."

# Search book by title or author
def search_books(books, keyword):
    return [b for b in books.values() if keyword.lower() in b["title"].lower() or keyword.lower() in b["author"].lower()]

# Update book details
def update_book(books, isbn, **kwargs):
    if isbn not in books:
        return "Book not found."
    books[isbn].update(kwargs)
    return "Book updated."

# Delete book
def delete_book(books, isbn):
    if isbn in books:
        del books[isbn]
        return "Book deleted."
    return "Book not found."

# Borrow book (max 3)
def borrow_book(members, books, member_id, isbn):
    for m in members:
        if m["member_id"] == member_id:
            if len(m["borrowed_books"]) >= 3:
                return "Borrowing limit reached."
            if isbn not in books:
                return "Book not found."
            if books[isbn]["total_copies"] == 0:
                return "No copies left."
            m["borrowed_books"].append(isbn)
            books[isbn]["total_copies"] -= 1
            return "Book borrowed."
    return "Member not found."

# Return book
def return_book(members, books, member_id, isbn):
    for m in members:
        if m["member_id"] == member_id:
            if isbn not in m["borrowed_books"]:
                return "Book not borrowed."
            m["borrowed_books"].remove(isbn)
            books[isbn]["total_copies"] += 1
            return "Book returned."
    return "Member not found."
