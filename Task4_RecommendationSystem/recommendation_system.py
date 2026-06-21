import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
movies = pd.read_csv("movies.csv")

# Convert genres into vectors
cv = CountVectorizer()
matrix = cv.fit_transform(movies["genre"])

# Calculate similarity
similarity = cosine_similarity(matrix)

def recommend(movie_name):
    movie_name = movie_name.lower()

    movie_index = None

    for i in range(len(movies)):
        if movies.iloc[i]["title"].lower() == movie_name:
            movie_index = i
            break

    if movie_index is None:
        print("Movie not found!")
        return

    scores = list(enumerate(similarity[movie_index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print("\nRecommended Movies:\n")

    count = 0
    for movie in scores[1:]:
        print(movies.iloc[movie[0]]["title"])
        count += 1

        if count == 5:
            break

print("=" * 50)
print("MOVIE RECOMMENDATION SYSTEM")
print("=" * 50)

movie = input("\nEnter a movie name: ")

recommend(movie)