from bs4 import BeautifulSoup
import requests


#scripting from URL     -     https://news.ycombinator.com/


response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage , "html.parser")

art=soup.find_all(name="a",rel="noreferrer")
artical_text=[]
artical_list=[]



for artical in art:
    text=artical.getText()
    artlink=artical.get("href")
    artical_text.append(text)
    artical_list.append(artlink)


upvoids=[int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
#print(artical_text)
#print(artical_list)
#print(upvoids)
m=max(upvoids)
index=upvoids.index(m)
print(index)
print(artical_list[index])
print(artical_text[index])

