import pandas as pd

movies = pd.read_csv("data/tmdb_5000_movies.csv")

movies = movies[['id', 'title', 'genres', 'keywords', 'overview']]

movies = movies.dropna(subset=['title', 'overview']).reset_index(drop=True)

movies['genres'] = movies['genres'].fillna('')
movies['keywords'] = movies['keywords'].fillna('')

movies['tags'] = (
    movies['genres'] + " "
    + movies['keywords'] + " "
    + movies['overview'] 
    )

movies['tags'] = movies['tags'].str.lower()

movies = movies[['id', 'title', 'tags']]

movies.to_csv('data/processed_movies.csv', index=False)
print(movies.head())
print(len(movies))