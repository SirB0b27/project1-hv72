import requests
import base64
import os
from dotenv import load_dotenv, find_dotenv

def get_lyric_link(song_name):
    #Genius Set up
    genius_base = "https://api.genius.com/"
    genius_token = os.getenv("Genius_Token")
    head = {
        "Authorization" : "Bearer {}".format(genius_token)
    }
    search_link = genius_base + "search"
    returned_data = requests.get(search_link, data={'q':song_name}, headers=head).json()
    lyric_link = "https://genius.com" + returned_data["response"]["hits"][0]["result"]["path"]
    
    return lyric_link
