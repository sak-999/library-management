import tkinter as tk
from tkinter import messagebox
import sqlite3
conn = sqlite3.connect("library.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        genre TEXT,
        isbn TEXT
    )
""")
conn.commit()
app = tk.Tk()
app.title("Library Management System")
app.geometry("600x400")
app.config(bg="lightblue")
def add_book():
    title = entry_title.get()
    author = entry_author.get()
    genre = entry_genre.get()
    isbn = entry_isbn.get()
    if title and author and genre and isbn:
        cursor.execute("INSERT INTO books (title, author, genre, isbn) VALUES (?, ?, ?, ?)", (title, author, genre, isbn))
        conn.commit()
        messagebox.showinfo("Success", "Book added successfully!")
        clear_entries()
        show_books()
    else:
        messagebox.showwarning("Warning", "Please fill in all fields.")
def search_book():
    search_query = entry_search.get()
    cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ? OR genre LIKE ? OR isbn LIKE ?",
                   ('%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%'))
    records = cursor.fetchall()
    update_book_list(records)
def show_books():
    cursor.execute("SELECT * FROM books")
    records = cursor.fetchall()
    update_book_list(records)
def update_book_list(records):
    listbox_books.delete(0, tk.END)
    for record in records:
        listbox_books.insert(tk.END, f"ID: {record[0]}, Title: {record[1]}, Author: {record[2]}, Genre: {record[3]}, ISBN: {record[4]}")
def delete_book():
    selected_book = listbox_books.get(tk.ACTIVE)
    if selected_book:
        book_id = selected_book.split(",")[0].split(": ")[1]
        cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
        conn.commit()
        messagebox.showinfo("Success", "Book deleted successfully!")
        show_books()
    else:
        messagebox.showwarning("Warning", "Please select a book to delete.")
def update_book():
    selected_book = listbox_books.get(tk.ACTIVE)
    if selected_book:
        book_id = selected_book.split(",")[0].split(": ")[1]
        title = entry_title.get()
        author = entry_author.get()
        genre = entry_genre.get()
        isbn = entry_isbn.get()
        cursor.execute("UPDATE books SET title=?, author=?, genre=?, isbn=? WHERE id=?", (title, author, genre, isbn, book_id))
        conn.commit()
        messagebox.showinfo("Success", "Book updated successfully!")
        clear_entries()
        show_books()
    else:
        messagebox.showwarning("Warning", "Please select a book to update.")
def clear_entries():
    entry_title.delete(0, tk.END)
    entry_author.delete(0, tk.END)
    entry_genre.delete(0, tk.END)
    entry_isbn.delete(0, tk.END)
tk.Label(app, text="Title:", bg="lightblue").grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_title = tk.Entry(app, width=30)
entry_title.grid(row=0, column=1, padx=10, pady=10)
tk.Label(app, text="Author:", bg="lightblue").grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_author = tk.Entry(app, width=30)
entry_author.grid(row=1, column=1, padx=10, pady=10)
tk.Label(app, text="Genre:", bg="lightblue").grid(row=2, column=0, padx=10, pady=10, sticky="e")
entry_genre = tk.Entry(app, width=30)
entry_genre.grid(row=2, column=1, padx=10, pady=10)
tk.Label(app, text="ISBN:", bg="lightblue").grid(row=3, column=0, padx=10, pady=10, sticky="e")
entry_isbn = tk.Entry(app, width=30)
entry_isbn.grid(row=3, column=1, padx=10, pady=10)
tk.Button(app, text="Add Book", width=15, command=add_book).grid(row=4, column=0, padx=10, pady=10)
tk.Button(app, text="Update Book", width=15, command=update_book).grid(row=4, column=1, padx=10, pady=10)
tk.Button(app, text="Delete Book", width=15, command=delete_book).grid(row=5, column=0, padx=10, pady=10)
entry_search = tk.Entry(app, width=20)
entry_search.grid(row=5, column=1, padx=10, pady=10, sticky="w")
tk.Button(app, text="Search", width=10, command=search_book).grid(row=5, column=2, padx=10, pady=10)
listbox_books = tk.Listbox(app, width=80, height=10)
listbox_books.grid(row=6, column=0, columnspan=3, padx=10, pady=10)
show_books()
app.mainloop()
conn.close()
