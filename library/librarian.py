# librarian.py

def add_book(library, title, author, isbn):
    """Add a new book to the library if ISBN doesn't exist."""
    if isbn in library:
        print(f"Book with ISBN {isbn} already exists.")
    else:
        library[isbn] = {
            'title': title,
            'author': author,
            'isbn': isbn,
            'available': True
        }

def remove_book(library, isbn):
    """Remove a book from the library by ISBN."""
    if isbn in library:
        del library[isbn]
    else:
        print(f"No book found with ISBN {isbn}.")

def check_out_book(library, isbn):
    """Mark a book as checked out if available."""
    if isbn in library:
        if library[isbn]['available']:
            library[isbn]['available'] = False
        else:
            print(f"Book '{library[isbn]['title']}' is already checked out.")
    else:
        print(f"No book found with ISBN {isbn}.")

def return_book(library, isbn):
    """Return a book and mark it available again."""
    if isbn in library:
        library[isbn]['available'] = True
    else:
        print(f"No book found with ISBN {isbn}.")

def display_books(library):
    """Display all books in the library."""
    for book in library.values():
        status = "Available" if book['available'] else "Checked Out"
        print(f"{book['title']} by {book['author']} (ISBN: {book['isbn']}) - {status}")
    print()  # newline for readability
