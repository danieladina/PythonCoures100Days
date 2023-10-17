import requests
from bs4 import BeautifulSoup


URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
web_html=response.text

soup=BeautifulSoup(web_html,"html.parser")

all=soup.find_all(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")

movietitle=[movie.getText() for movie in all ]
movies = movietitle[::-1 ]
with open("movies.txt",mode="w",encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")