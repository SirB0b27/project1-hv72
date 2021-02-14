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
    
    spotify_artists = ['3OKg7YbOIatODzkRIbLJR4', '5ZbRDyTYX4HhXveONcZQn2', '7p1fL0cAuCPDMG6oBswFhM', '6s22t5Y3prQHyaHWUN1R1C', '3z97WMRi731dCvKklIf2X6']
    random_number = random.randint(1, len(spotify_artists))
    
    url = 'https://api.spotify.com/v1/artists/{id}/top-tracks'.format(id = spotify_artists[random_number-1])
    # print(url)
    # url = "https://api.spotify.com/v1/" + "browse/new-releases/"
    parameters = {
        "country" : "US",
        "limit" : 20,
        "offset" : 0
    }
    
    spotify_response = requests.get(url=url, headers = headers, params = parameters)
    return_data = spotify_response.json()
    
    # information to display on html
    song_name = return_data['tracks'][0]['name']
    artists_name = []
    for artists in return_data['tracks'][0]['artists']:
        artists_name.append(artists['name'])
    num_artists = len(artists_name)
    image_link = return_data['tracks'][0]['album']['images'][1]['url']
    song_preview = return_data['tracks'][0]['preview_url']
    song_link = return_data['tracks'][0]['external_urls']['spotify']
    
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
        length=num_artists,
        imageLink=image_link,
        songPreview=song_preview,
        songLink=song_link,
        lyricLink = lyric_link)

# run the flask app
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)

