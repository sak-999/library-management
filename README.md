# library-management
![I1 (2)](https://github.com/user-attachments/assets/595a59b1-43d7-4a76-8700-e32b374eb552)

This Python code creates a Library Management System using Tkinter for the graphical user interface (GUI) and SQLite for database management. This application allows users to add, search, update, and delete book records, making it a useful tool for managing a library’s book inventory.

Key Components: Database Setup:

The code connects to an SQLite database named library.db and creates a table books (if it doesn’t already exist) to store book details like title, author, genre, and isbn. Each book record is assigned a unique id as the primary key. Adding a Book:

The add_book function retrieves the book details entered by the user (title, author, genre, and ISBN) and inserts this data into the database. It validates that all fields are filled, commits the data to the database, and then displays a success message. The show_books function is called to update the list of books, and fields are cleared after each entry. Searching for a Book:

The search_book function allows users to search for books based on partial matches in any field (title, author, genre, or ISBN). It executes a query to retrieve matching records and updates the displayed book list with the results. Updating Book Records:

The update_book function lets users modify details of a selected book. After the user selects a book from the list and updates the fields, this function retrieves the id of the selected book and updates the database entry with the new values. Deleting a Book:

The delete_book function allows users to delete a selected book record from the database. It prompts the user to select a book from the displayed list, retrieves the book id, and deletes the entry from the database. Displaying Book Records:

The show_books function displays all book records in a list box widget, refreshing whenever a new entry is added, updated, or deleted. The update_book_list function manages how records are displayed in the list box, formatting each entry for readability. Search Functionality:

A search entry field and a “Search” button allow users to filter and view specific books based on keywords, enhancing the user experience by allowing easy access to specific records. GUI Layout:

The GUI is organized using Tkinter widgets. Labels, entries, and buttons are used for input and actions, while a list box displays the list of books. Buttons for "Add Book," "Update Book," and "Delete Book" are provided, as well as a search field and button. App Lifecycle:

The program opens a connection to the database at the start and closes it automatically when the app is closed (conn.close()), ensuring data integrity. Summary: This Library Management System is a beginner-friendly, straightforward application for managing a library's inventory, offering essential functions for adding, viewing, updating, and deleting book records. The app’s use of SQLite ensures persistent data storage, and Tkinter provides a user-friendly interface for interacting with the
