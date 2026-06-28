from tkinter import *
import random
import pandas as pd

movies = pd.read_csv("movies.csv")

def sentiment(text):
    text = str(text).lower()
    if "good" in text or "great" in text or "love" in text:
        return "Positive"
    elif "bad" in text or "boring" in text:
        return "Negative"
    return "Neutral"

def show_movie(movie):
    output.config(text=
        "Title: " + movie['title'] + "\n" +
        "Genre: " + movie['genre'] + "\n" +
        "IMDB: " + str(movie['imdb_rating']) + "\n" +
        "Overview: " + movie['overview'] + "\n" +
        "Sentiment: " + sentiment(movie['overview'])
    )

def submit_name():
    output.config(text="Welcome " + name.get() + "! Choose AI or Random.")

def random_rec():
    movie = movies.sample().iloc[0]
    show_movie(movie)

def ai_rec():
    genre = genre_entry.get().lower()
    rating = rating_entry.get()

    filtered = movies

    if genre:
        filtered = filtered[filtered["genre"].str.lower().str.contains(genre)]

    if rating:
        filtered = filtered[filtered["imdb_rating"] >= float(rating)]

    if len(filtered) > 0:
        show_movie(filtered.sample().iloc[0])
    else:
        output.config(text="No movies found")

root = Tk()
root.title("Movie Recommendation App")
root.geometry("400x500")

Label(root, text="Name").pack()
name = Entry(root)
name.pack()

Button(root, text="Submit Name", command=submit_name).pack()

Button(root, text="AI Recommendation", command=ai_rec).pack()
Button(root, text="Random Recommendation", command=random_rec).pack()

Label(root, text="Genre").pack()
genre_entry = Entry(root)
genre_entry.pack()

Label(root, text="Min IMDB Rating").pack()
rating_entry = Entry(root)
rating_entry.pack()

output = Label(root, text="", justify=LEFT)
output.pack()

root.mainloop()