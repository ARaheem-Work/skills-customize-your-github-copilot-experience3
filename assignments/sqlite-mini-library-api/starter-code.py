"""Starter code for the SQLite Mini Library API assignment."""

import sqlite3

DB_NAME = "library.db"


# Task 1: Create the table and seed at least 5 books.
def setup_database() -> None:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # TODO: Create books table if it does not exist.
    # Columns: id (INTEGER PRIMARY KEY), title (TEXT), author (TEXT),
    # year_published (INTEGER), is_borrowed (INTEGER default 0).

    # TODO: Insert at least 5 sample books.

    conn.commit()
    conn.close()


# Task 1: Print all books so setup can be validated quickly.
def list_all_books() -> None:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # TODO: SELECT all rows from books and print each one.

    conn.close()


# Task 2: Mark a book as borrowed by id.
def borrow_book(book_id: int) -> None:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # TODO: Update the selected book so is_borrowed becomes 1.

    conn.commit()
    conn.close()


# Task 2: Show only books that are not borrowed.
def list_available_books() -> None:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # TODO: SELECT rows where is_borrowed = 0 and print them.

    conn.close()


# Task 2: Search books by author name.
def search_by_author(author_name: str) -> None:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # TODO: SELECT rows where author matches the provided name.
    # Tip: use parameterized SQL to avoid SQL injection.

    conn.close()


if __name__ == "__main__":
    # Suggested demo flow for class check-ins and rubric scoring.
    setup_database()
    print("\nAll Books:")
    list_all_books()

    print("\nBorrowing Book with id=1...")
    borrow_book(1)

    print("\nAvailable Books:")
    list_available_books()

    print("\nBooks by 'Octavia Butler':")
    search_by_author("Octavia Butler")
