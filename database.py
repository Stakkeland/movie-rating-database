import tkinter as tk
import sqlite3 as sql

con = sql.connect("movie_ratings.db")
cur = con.cursor()

def submit_action(event=None):
    movie_name = name_entry.get()
    movie_year = year_entry.get()
    movie_rating = rating_entry.get()
    update_db(movie_name, movie_year, movie_rating)

def update_db(name, year, rating):
    cur.execute("INSERT INTO movie VALUES (?, ?, ?)", (name, year, rating))
    con.commit()

def clear_entries():
    name_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)
    rating_entry.delete(0, tk.END)
    deleted_movie_entry.delete(0, tk.END)

def close_program():
    root.destroy()

def view_db():
    for row in cur.execute("SELECT * FROM movie"):
        print(f"{row[0]} | {row[1]} | {row[2]}")

def delete_column(event=None):
    movie_deleted = deleted_movie_entry.get()
    cur.execute("DELETE FROM movie WHERE title=(?)", (movie_deleted,))

root = tk.Tk()
root.title("Movie Input Form")

tk.Label(root, text="Movie Name:").grid(row=0, column=0)
tk.Label(root, text="Movie Year:").grid(row=1, column=0)
tk.Label(root, text="Rating (1-10):").grid(row=2, column=0)

name_entry = tk.Entry(root)
year_entry = tk.Entry(root)
rating_entry = tk.Entry(root)
deleted_movie_entry = tk.Entry(root)

name_entry.grid(row=0, column=1)
year_entry.grid(row=1, column=1)
rating_entry.grid(row=2, column=1)
deleted_movie_entry.grid(row=5, column=2)

submit_button = tk.Button(root, text="Submit", command=submit_action)
submit_button.grid(row=3, column=1)

clear_button = tk.Button(root, text="Clear", command=clear_entries)
clear_button.grid(row=3, column=0)

exit_button = tk.Button(root, text="Exit", command=close_program, bg='red')
exit_button.grid(row=4, column=1)

view_button = tk.Button(root, text="View db", command=view_db)
view_button.grid(row=3, column=2)

delete_button = tk.Button(root, text="Delete column", command=delete_column)
delete_button.grid(row=4, column=2)


root.bind('<Return>', submit_action)

root.mainloop()
