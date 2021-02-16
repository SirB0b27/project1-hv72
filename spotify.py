import requests
import base64
import os
import random
from dotenv import load_dotenv, find_dotenv

def get_token():
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
    return token_response_data["access_token"]

def random_artist():
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
                        
    random_num = random.randint(1, len(spotify_artists))
    return spotify_artists[random_num-1]
  
def get_spotify_response():
    headers = {
        "Authorization": "Bearer {}".format(get_token())
    }
    url = 'https://api.spotify.com/v1/artists/{id}/top-tracks'.format(id = random_artist())
    parameters = {
        "country" : "US",
        "limit" : 10,
        "offset" : 0
    }
    
    spotify_response = requests.get(url=url, headers = headers, params = parameters)
    return spotify_response.json()
    
