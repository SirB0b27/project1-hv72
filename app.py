import requests
import base64
import os
from dotenv import load_dotenv, find_dotenv
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

url = "https://api.spotify.com/v1/" + "browse/new-releases/"
parameters = {
    "country" : "US",
    "limit" : 10,
    "offset" : 0
}

spotify_response = requests.get(url=url, headers = headers, params = parameters)
return_data = spotify_response.json()

print("============================================")
print("\t10 Newest Songs On Spotify")
print("============================================")
for i in range(10):
    print(str(i+1) + ")\t" + return_data["albums"]["items"][i]["name"])
