

import requests
from urllib.parse import urlencode
from app.config import (
    SPOTIFY_CLIENT_ID,
    SPOTIFY_CLIENT_SECRET,
    SPOTIFY_REDIRECT_URI
)


def get_auth_url():
    scope = (
        "user-top-read "
        "user-read-recently-played "
        "user-read-playback-state "
        "user-read-currently-playing "
        "user-modify-playback-state "
        "streaming "
        "user-library-read "
    )

    params = {
        "client_id": SPOTIFY_CLIENT_ID,
        "response_type": "code",
        "redirect_uri": SPOTIFY_REDIRECT_URI,
        "scope": scope,
        "show_dialog": "true"
    }

    auth_url = "https://accounts.spotify.com/authorize?" + urlencode(params)

    return {
        "auth_url": auth_url
    }

def get_access_token(code):
    url = "https://accounts.spotify.com/api/token"

    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": SPOTIFY_REDIRECT_URI,
        "client_id": SPOTIFY_CLIENT_ID,
        "client_secret": SPOTIFY_CLIENT_SECRET
    }

    response = requests.post(url, data=data)

    return response.json()

def get_user_top_tracks(access_token):
    url = "https://api.spotify.com/v1/me/top/tracks"

    headers = {"Authorization": f"Bearer {access_token}"

               }
    response = requests.get(url, headers=headers)
    return response.json()
