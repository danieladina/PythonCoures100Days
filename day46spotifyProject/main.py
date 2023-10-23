# imports

from bs4 import BeautifulSoup
import spotipy
import requests
from spotipy.oauth2 import SpotifyOAuth

# scraping top 100 song to date given

data = input("enter date with that pattern yyyy-mm-dd")
response = requests.get(f"https://www.billboard.com/charts/hot-100/" + data)
soup=BeautifulSoup(response.text, 'html.parser')
song_names_spans=soup.select("li ul li h3")
song_names=[song.getText().strip() for song in song_names_spans]


#sporify authentication

##client id and clint secret you get from opening spotify developer account

sp=spotipy.spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist_modify_private",
        redirect_uri="http://example.com",
        client_id= "your client id",
        client_secret="your client secret",
        cache_path="token.txt",
        show_dialog=True

    )

)
user_id=sp.current_user()["id"]
print(user_id)


#search spoti for song by title

song_uris=[]
year= data.split("-")[0]
for song in song_names:
    result=sp.search(q=f"track:={song} year:={year}",type="track")
    print(result)
    try:
        uri=result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in spotify, skipped")





#Creating a new private playlist in spotify

playlist= sp.user_playlist_create(user=user_id, name=f"{data} billboard 100", public=False)
print(playlist)

#add song found into the playlist

sp.user_playlist_add_item(playlist_id=playlist["id"],item=song_uris)


