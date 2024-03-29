from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
load_dotenv()
spotify_client_id=os.getenv("spotify_client_id")
spotify_client_secret=os.getenv("spotify_client_secret")


# Scraping Billboard 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

#Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=spotify_client_id,
        client_secret=spotify_client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

#Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)














# import requests
# from bs4 import BeautifulSoup
# from dotenv import load_dotenv
# import os
# load_dotenv()
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth






# user_in=input("which year do you wasnt to travel to? type thje data in this format YYYY-MM-DD: ")


# website=requests.get("https://www.billboard.com/charts/hot-100/"+user_in)

# # print(website.status_code)
# print(website.cookies)
# # print(website.headers)
# soup=BeautifulSoup(website.text,"html.parser")

# titles=soup.select(selector="li ul li h3")

# # a=soup.find_all(name="li",class_="o-chart-results-list__item")

# with open("songs_title.txt","w") as file:
#     for title in titles:
#         file.write(title.text.strip()+"\n")
#     # # this wont work with write because write expect an str not list 
#     # all_title=[title.text.strip() for title in titles]
#     # file.write(all_title)



