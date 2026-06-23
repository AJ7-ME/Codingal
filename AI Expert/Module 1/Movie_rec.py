import time, pandas as pd
from textblob import TextBlob
try: df = pd.read_csv("./movies.csv")
except FileNotFoundError:
    print("Error: 'movies.csv' file not found. Please ensure the file is in the correct directory."); raise SystemExit
genres = sorted({g.strip() for xs in df["Genre"].dropna().str.split(", ") for g in xs})
def dots():
    for _ in range(3): print(".", end="", flush=True); time.sleep(0.5)
def senti(p): return"Positive" if p>0 else "Negative" if p<0 else "Neutral"
def recommend(genre=None, mood=None, rating=None, n=5):
    d = df
    if genre: d = d[d["Genre"].str.contains(genre, case=False, na=False)]
    if rating is not None: d = d[d["IMDB_Rating"] >= rating]
    if d.empty: return "No movies found matching your criteria."
    d, need_nonneg, out = d.sample(frac=1).reset_index(drop=True), bool(mood), []
    for _, r in d.iterrows():
        ov = r.get("Overview")
        if pd.isna(ov): continue
        pol = TextBlob(ov).sentiment.polarity
        if need_nonneg and pol < 0:
            out.append((r["Series_Title"], pol))
            if len(out)==n: break
    if not out: return "No movies found matching your criteria."
def show(recs, name):
    print("\nRecommended Movies for {}:".format(name))
    for i, (t, p) in enumerate(recs, 1):
        print(f"{i}. {t} (Polarity: {p:.2f }, {senti(p)})")
def get_genre():
    print("Available Genres: ", end="")
    for i, g in enumerate(genres, 1): print(f"{i}. {g}")
    print()
    while True:
        x = input("Enter genre number: ").strip()
        if x.isdigit() and 1 <= int(x) <= len(genres):
            return genres[int(x)-1]
        x = x.title()
        if x in genres: return x
        print("Invalid input. Please try again.")
def get_rating():
    while True:
        x = input("Enter min IMDB rating (7.6 - 9.3) or skip: ").strip()
        if x.lower() == "skip": return None
        try:
            r = float(x)
            if 7.6 <= r <= 9.3: return r
        except ValueError: pass
        print("Invalid input. Please enter a number between 0 and 10.")
print("🎥 Welcome to your Personal Movie Recommendation Assistant! 🎥\n")
name = input("What's your name? ").strip()
print(f"\nGreat to meet you, {name}!\n")
print("\n🔍 Let's find the perfect movie for you!\n")
genre = get_genre()
mood = input("How do you feel today? (Describe your mood): ").strip()
print("\nAnalyzing mood", end="", flush=True); dots()
mp = TextBlob(mood).sentiment.polarity
md = "positive 😊" if mp > 0 else "negative 😞" if mp < 0 else "neutral 😐"
print(f"\nYour mood is {md} (Polarity: {mp:.2f}).\n")
rating = get_rating()
print(f"\nFinding movies for {name}", end="", flush=True); dots()
recs = recommend(genre=genre, mood=mood, rating=rating, n=5)
print(recs + "\n") if isinstance(recs, str) else show(recs, name)
while True:
    a = input("\nWould you like more recommendations? (yes/no): ").strip().lower()
    if a == "yes":
        print(f"\nEnjoy your movie picks, {name}! 🎬🍿\n"); break
    if a == "no":
        recs = recommend(genre=genre, mood=mood, rating=rating, n=5)
        print(recs + "\n") if isinstance(recs, str) else show(recs, name)
    else:
        print("Invalid choice. Try again.\n")