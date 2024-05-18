import tkinter as tk
import sqlite3 as sql

'''
    This program is a movie rating database. It uses sqlite3 and contains
    the following: 
    1 table -> movie
    3 rows -> title, year, score
'''

# Connects to db.
con = sql.connect("movie_ratings.db")
cur = con.cursor()

# Functions.
def submit_action(event=None):
    '''Get input for name, year, and rating in 3 main entry boxes'''
    movie_name = name_entry.get()
    movie_year = year_entry.get()
    movie_rating = rating_entry.get()
    update_db(movie_name, movie_year, movie_rating)

def update_db(name, year, rating):
    '''When user presses submit the info is pushed to the db'''
    cur.execute("INSERT INTO movie VALUES (?, ?, ?)", (name, year, rating))
    con.commit()

def clear_entries():
    '''When clear is pressed all entry boxes are cleared'''
    name_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)
    rating_entry.delete(0, tk.END)
    deleted_movie_entry.delete(0, tk.END)
    db_search_entry.delete(0,tk.END)

def close_program():
    '''When End button is pressed program closes'''
    root.destroy()

def view_db():
    '''When view button is pressed, the console displays the db info in a neat format'''
    rating = db_search_entry.get()

    if rating == "": # If empty entry box.
        for row in cur.execute("SELECT * FROM movie"):
            print(f"{row[0]} | {row[1]} | {row[2]}")
    else:
        for row in cur.execute("SELECT * FROM movie WHERE score > (?)", (rating,)):
            print(f"{row[0]} | {row[1]} | {row[2]}")

def delete_column(event=None):
    '''When the user enters the name of a title and submits, the row is deleted from the db.'''
    movie_deleted = deleted_movie_entry.get()
    cur.execute("DELETE FROM movie WHERE title=(?)", (movie_deleted,))
    con.commit()

# GUI.
root = tk.Tk()
root.title("Movie Input Form")

# Words.
tk.Label(root, text="Movie Name:").grid(row=1, column=0)
tk.Label(root, text="Movie Year:").grid(row=2, column=0)
tk.Label(root, text="Rating (1-10):").grid(row=3, column=0)
tk.Label(root, text="Empty = all | score = all > score: ").grid(row=1, column=2)
tk.Label(root, text="Movie title to remove from database: ").grid(row=3, column=2)

# Entry boxes.
name_entry = tk.Entry(root)
year_entry = tk.Entry(root)
rating_entry = tk.Entry(root)
deleted_movie_entry = tk.Entry(root)
db_search_entry = tk.Entry(root)

name_entry.grid(row=1, column=1)
year_entry.grid(row=2, column=1)
rating_entry.grid(row=3, column=1)
deleted_movie_entry.grid(row=3, column=3)
db_search_entry.grid(row=1, column=3)

# Buttons.
submit_button = tk.Button(root, text="Submit", command=submit_action)
submit_button.grid(row=4, column=1)

clear_button = tk.Button(root, text="Clear", command=clear_entries)
clear_button.grid(row=4, column=0)

exit_button = tk.Button(root, text="Exit", command=close_program, bg='red')
exit_button.grid(row=7, column=2)

view_button = tk.Button(root, text="View db", command=view_db)
view_button.grid(row=2, column=3)

delete_button = tk.Button(root, text="Delete column", command=delete_column)
delete_button.grid(row=4, column=3)


root.bind('<Return>', submit_action)

root.mainloop()
