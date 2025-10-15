import dataOP 

from library import librarian

def main():
    # Library database (dictionary)
    my_library = {}

    # Add some books
    librarian.add_book(my_library, "The Catcher in the Rye", "J.D. Salinger", "9780316769174")
    librarian.add_book(my_library, "To Kill a Mockingbird", "Harper Lee", "9780446310789")
    librarian.add_book(my_library, "1984", "George Orwell", "9780451524935")

    # Display all books
    librarian.display_books(my_library)

    # Checkout a book
    librarian.check_out_book(my_library, "9780316769174")
    librarian.display_books(my_library)

    # Return the book
    librarian.return_book(my_library, "9780316769174")
    librarian.display_books(my_library)

if __name__ == "__main__":
    main()

print("__"*44)
print("Solve the first question")
dataOP.print_current_date()