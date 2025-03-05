import spotipy
from flask import redirect, sessions, request
from spotipy.oauth2 import SpotifyOAuth
import config

sp_oauth = SpotifyOAuth(
    client_id = config.CLIENT_ID,
    client_secret=config.CLIENT_SECRET,
    redirect_uri=config.REDIRECT_URI,
    scope=config.SCOPE
)

def login():
    """Przekierowuje użytkownika do logowania Spotify."""
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

def callback():
    """OBsluguje przekierowanie po logowaniu i zapisuje token."""
    sessions.clear()
    code = requests.args.get("code")
    token_info = sp_oauth.get_access_token(code)
    sessions["token_info"] = token_info
    return redirect("/recommend")

def get_spotify_client():
    """Zwraca klienta Spotify z aktualbym tokenem"""
    token_info = sessions.get("token_info")
    if not token_info:
        return None
    return spotipy.Spotify(auth=token_info["access_token"])