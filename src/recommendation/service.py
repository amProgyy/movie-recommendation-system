from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

class MovieRecommender():
    def __init__(self):
        self.movies = pd.read_csv('data/processed_movies.csv')
        print(self.movies.columns.tolist())
        # self.movies = self.movies["tags"].fillna("")
        

        self.vectorizer = CountVectorizer(
            max_features=5000,
            stop_words="english"
        )

        self.vectors = self.vectorizer.fit_transform(
             self.movies["tags"]
        )

        self.similarity = cosine_similarity(self.vectors)

    def recommend(self, movie_title, no_of_movies = 5):
        movies_index = self.movies[
                self.movies['title'].str.lower() == movie_title.lower()
            ].index

        if len(movies_index) == 0:
            return []

        index = movies_index[0]

        similarity_score = list(enumerate(self.similarity[index]))

        similarity_score = sorted(similarity_score, key = lambda x : x[1], reverse=True)


        recommendations = []

        for movie_index, score in similarity_score[1:no_of_movies+1]:
            movie = self.movies.iloc[movie_index]

            recommendations.append(
                {
                    "id" : int(movie['id']),
                    "title" : movie['title'],
                    "similarity" : round(float(score), 3)
                }
            )

        return recommendations


