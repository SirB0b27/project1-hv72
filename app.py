import requests
import base64
import os
import random
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def spotify_app():
    load_dotenv(find_dotenv())
    
    client_id = os.getenv("Client_ID")
    client_secret = os.getenv("Client_Secret")
    token_url = "https://accounts.spotify.com/api/token"
    
    token_response = requests.post(token_url,
        {
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
        }
    )
    
    token_response_data = token_response.json()
    
    # save the access token
    access_token = token_response_data["access_token"]
    
    headers = {
        "Authorization": "Bearer {}".format(access_token)
    }
    
    spotify_artists = ['3OKg7YbOIatODzkRIbLJR4',  # TheFatRat
                        '5ZbRDyTYX4HhXveONcZQn2', # Mystery Skills
                        '7p1fL0cAuCPDMG6oBswFhM', # Maretu
                        '6s22t5Y3prQHyaHWUN1R1C', # AJR
                        '3z97WMRi731dCvKklIf2X6', # NEFFEX
                        '3WrFJ7ztbogyGnTHbHJFl2', # The Beatles
                        '1dfeR4HaWDbWqFHLkxsg1d', # Queen
                        '1Xyo4u8uXC1ZmMpatF05PJ', # The Weeknd
                        '4gzpq5DPGxSnKTe4SA8HAU', # Coldplay
                        '0blbVefuxOGltDBa00dspv', # LiSA
                        '1XTqQwcJw9D1bo0cuO8Oq2', # Anna Tsychiya
                        '3iNL7rw7fpmysjZvhB8vi7', # MC Virgins
                        '04gDigrS5kc9YWfZHwBETP', # Maroon 5
                        '7vk5e3vY1uw9plTHJAMwjN', # Alan Walker
                        '6NgYKD0TKGjwtRFqTyyqKF', # Monsune
                        '0z7Yuv7DuDQ5SaVn4VSlLt', # Lisa Hannigan
                        '6udveWUgX4vu75FF0DTrXV', # Taeyang
                        '3Nrfpe0tUJi4K4DXYWgMUX', # BTS
                        '4XDi67ZENZcbfKnvMnTYsI', # Jay Park
                        '3HqSLMAZ3g3d5poNaI7GOU', # IU
                        ]
                        
    random_artist = random.randint(1, len(spotify_artists))
    
    url = 'https://api.spotify.com/v1/artists/{id}/top-tracks'.format(id = spotify_artists[random_artist-1])
    # print(url)
    # url = "https://api.spotify.com/v1/" + "browse/new-releases/"
    parameters = {
        "country" : "US",
        "limit" : 10,
        "offset" : 0
    }
    
    spotify_response = requests.get(url=url, headers = headers, params = parameters)
    return_data = spotify_response.json()
    
    # get random track
    random_track = random.randint(1, len(return_data['tracks']))
    
    # information to display on html
    song_list = []
    song_link_list = []
    for songs in return_data['tracks']:
        song_list.append(songs['name'])
        song_link_list.append(songs['external_urls']['spotify'])
    # print(song_link_list)
    num_songs = len(song_list)
    song_name = return_data['tracks'][random_track-1]['name']
    artists_name = []
    for artists in return_data['tracks'][random_track-1]['artists']:
        artists_name.append(artists['name'])
    image_link = return_data['tracks'][random_track-1]['album']['images'][1]['url']
    song_preview = return_data['tracks'][random_track-1]['preview_url']
    song_link = return_data['tracks'][random_track-1]['external_urls']['spotify']
    
    # print(song_preview)
    if(song_preview == None):
        # print(return_data)
        song_preview = "None"
        # print(song_name)
        
        
    #Genius Set up
    genius_base = "https://api.genius.com/"
    genius_token = os.getenv("Genius_Token")
    head = {
        "Authorization" : "Bearer {}".format(genius_token)
    }
    search_link = genius_base + "search"
    returned_data = requests.get(search_link, data={'q':song_name}, headers=head).json()
    lyric_link = "https://genius.com" + returned_data["response"]["hits"][0]["result"]["path"]
    # print(lyric_link)
        
        
    # render html file:
    return render_template(
        "index.html",
        songName=song_name,
        artistNames=artists_name,
        imageLink=image_link,
        songPreview=song_preview,
        songLink=song_link,
        lyricLink=lyric_link,
        songList=song_list,
        numSongs=num_songs,
        songLinkList=song_link_list)

# run the flask app
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)

