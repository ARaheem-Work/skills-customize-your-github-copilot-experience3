# 📘 Assignment: SQLite Mini Library API

## 🎯 Objective

Build a small Python program that uses SQLite to store and manage library books. Students will practice creating tables, inserting records, and querying data with SQL in a real workflow.

## 📝 Tasks

### 🛠️	Create the Database and Seed Data

#### Description
Set up a local SQLite database for a mini library and add starter book records using Python.

#### Requirements
Completed program should:

- Create a SQLite database file named `library.db`
- Create a `books` table with columns: `id`, `title`, `author`, `year_published`, and `is_borrowed`
- Insert at least 5 sample books into the table
- Print all inserted rows to confirm setup worked


### 🛠️	Implement Borrowing and Search Features

#### Description
Add functions that allow users to borrow a book and view books based on availability.

#### Requirements
Completed program should:

- Implement a function to mark a book as borrowed by `id`
- Implement a function to list only available books (`is_borrowed = 0`)
- Implement a function to search books by author name
- Display clear output that can be used for quick grading in class pairs
