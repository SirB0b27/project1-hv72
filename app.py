import requests
import base64
import os
import random
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template
from genius import get_lyric_link
from spotify import get_spotify_response

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def spotify_app():
    #get the return data from spotify.py
    return_data = get_spotify_response()
    
    # information to display on html
    # list of songs and links to their spotify page
    song_list = []
    song_link_list = []
    for songs in return_data['tracks']:
        song_list.append(songs['name'])
        song_link_list.append(songs['external_urls']['spotify'])
    num_songs = len(song_list)
    
    # get random track
    random_track_num = random.randint(1, len(return_data['tracks']))
    random_track = return_data['tracks'][random_track_num-1]
    
    # get the song name
    song_name = random_track['name']
    
    # get all the artists related to this song
    artists_name = []
    for artists in random_track['artists']:
        artists_name.append(artists['name'])
        
    # get the link to the album image
    image_link = random_track['album']['images'][1]['url']
    
    #get the song preview url
    song_preview = random_track['preview_url']
    
    #get the link of the song chosen to be previewed
    song_link = random_track['external_urls']['spotify']
    
    # if there is no preview, then give the song_preview variable a string to compare in jinja
    if(song_preview == None):
        song_preview = "None"
        
    # get the link to the lyrics using Genius API
    lyric_link = get_lyric_link(song_name)
        
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

