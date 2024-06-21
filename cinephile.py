import tkinter as tk
from tkinter import messagebox

# List to store movies
movies = []

# Function to add a new movie
def add_movie():
    title = entry_title.get()
    genre = entry_genre.get()
    try:
        rating = float(entry_rating.get())
        movie = {'title': title, 'genre': genre, 'rating': rating}
        movies.append(movie)
        messagebox.showinfo("Success", f"Movie '{title}' added successfully!")
    except ValueError:
        messagebox.showerror("Error", "Invalid rating. Please enter a number.")
    entry_title.delete(0, tk.END)
    entry_genre.delete(0, tk.END)
    entry_rating.delete(0, tk.END)

# Function to search for movies
def search_movies():
    search_term = entry_search.get()
    search_type = search_var.get()
    results = [movie for movie in movies if search_term.lower() in movie[search_type].lower()]
    result_text = "\n".join([f"Title: {movie['title']}, Genre: {movie['genre']}, Rating: {movie['rating']}" for movie in results])
    if not results:
        result_text = "No movies found."
    messagebox.showinfo("Search Results", result_text)

# Function to recommend top N movies
def recommend_top_movies():
    try:
        n = int(entry_top_n.get())
        sorted_movies = sorted(movies, key=lambda x: x['rating'], reverse=True)[:n]
        result_text = "\n".join([f"Title: {movie['title']}, Genre: {movie['genre']}, Rating: {movie['rating']}" for movie in sorted_movies])
        if not sorted_movies:
            result_text = "No movies to recommend."
        messagebox.showinfo("Top Movies", result_text)
    except ValueError:
        messagebox.showerror("Error", "Invalid number. Please enter an integer.")
    entry_top_n.delete(0, tk.END)

# Function to delete a movie
def delete_movie():
    global movies
    title = entry_delete.get()
    movies = [movie for movie in movies if movie['title'].lower() != title.lower()]
    messagebox.showinfo("Success", f"Movie '{title}' deleted successfully!")
    entry_delete.delete(0, tk.END)

# Creating the main window
root = tk.Tk()
root.title("Cinephile")

# Adding Movie
tk.Label(root, text="Add Movie").grid(row=0, column=0, columnspan=2)
tk.Label(root, text="Title:").grid(row=1, column=0)
entry_title = tk.Entry(root)
entry_title.grid(row=1, column=1)
tk.Label(root, text="Genre:").grid(row=2, column=0)
entry_genre = tk.Entry(root)
entry_genre.grid(row=2, column=1)
tk.Label(root, text="Rating:").grid(row=3, column=0)
entry_rating = tk.Entry(root)
entry_rating.grid(row=3, column=1)
tk.Button(root, text="Add Movie", command=add_movie).grid(row=4, column=0, columnspan=2)

# Searching Movie
tk.Label(root, text="Search Movie").grid(row=5, column=0, columnspan=2)
search_var = tk.StringVar(value="title")
tk.Radiobutton(root, text="Title", variable=search_var, value="title").grid(row=6, column=0)
tk.Radiobutton(root, text="Genre", variable=search_var, value="genre").grid(row=6, column=1)
entry_search = tk.Entry(root)
entry_search.grid(row=7, column=0, columnspan=2)
tk.Button(root, text="Search", command=search_movies).grid(row=8, column=0, columnspan=2)

# Recommending Movies
tk.Label(root, text="Recommend Top N Movies").grid(row=9, column=0, columnspan=2)
tk.Label(root, text="N:").grid(row=10, column=0)
entry_top_n = tk.Entry(root)
entry_top_n.grid(row=10, column=1)
tk.Button(root, text="Recommend", command=recommend_top_movies).grid(row=11, column=0, columnspan=2)

# Deleting Movie
tk.Label(root, text="Delete Movie").grid(row=12, column=0, columnspan=2)
tk.Label(root, text="Title:").grid(row=13, column=0)
entry_delete = tk.Entry(root)
entry_delete.grid(row=13, column=1)
tk.Button(root, text="Delete", command=delete_movie).grid(row=14, column=0, columnspan=2)

# Start the main event loop
root.mainloop()






















