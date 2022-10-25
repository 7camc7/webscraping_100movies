import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
movie_names = soup.find_all(name="h3", class_="title")
movies_for_txt = [movie.getText() for movie in movie_names]
# Reverse order of list:
movies = movies_for_txt[::-1]

with open("movies.txt", "w") as movie_list:
    # movie_list.truncate(0)
    for movie in movies:
        movie_list.write(f"{movie}\n")



