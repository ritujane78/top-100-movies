import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
empire_webpage = response.text
soup=BeautifulSoup(empire_webpage, 'html.parser')
movie_names = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")
all_movies = [movie.getText() for movie in movie_names]
all_movies_formatted = all_movies[::-1]

with open("best-100-movies.txt", mode="w") as file:
    for movie in all_movies_formatted:
        print(movie)
        file.write(f"{movie}\n")

