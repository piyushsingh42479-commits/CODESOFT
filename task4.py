import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data={"movie":["Thor","Spiderman","Captain America","Iron man","Deadpool",
               "Venom","hulk","doctor Strange"],
      "Genre":["Action fantacy","Action adventure Sci-Fi","Action adventure War",
               "Action adventure Sci-Fi","Action adventure War","Action adventure Sci-Fi",
               "Action adventure War","Action crime"]}
df=pd.DataFrame(data)

vectorizer=TfidfVectorizer(stop_words="english")
genre_matrix=vectorizer.fit_transform(df["Genre"])
similarity = cosine_similarity(genre_matrix, genre_matrix)

def recommendation_system(movie_title, top=3):
    if movie_title not in df["movie"].values:
        return "movie not found"

    index= df[df["movie"] == movie_title].index[0]
    Scores = list(enumerate(similarity[index]))
    Scores = sorted(Scores, key=lambda x: x[1], reverse=True)[1:top+1]
    recommendation = [df.iloc[i[0]]["movie"] for i in Scores]
    return recommendation
print("Recommendations for 'Venom':")
print(recommendation_system("Venom"))

print("\nRecommendations for 'doctor Strange':")
print(recommendation_system("doctor Strange"))
