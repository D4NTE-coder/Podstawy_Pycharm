# auth.py

import os
from flask import redirect, request, session, current_app
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from flask import current_app

# Funkcja do uzyskiwania dostępu do Spotify OAuth
def get_spotify_client():
    """
    Funkcja zwracająca klienta Spotify, jeśli użytkownik jest zalogowany.
    """
    token_info = session.get("token_info")
    if not token_info:
        return None

    sp = Spotify(auth=token_info["access_token"])
    return sp

def login():
    """
    Funkcja przekierowująca użytkownika do strony logowania Spotify.
    """
    sp_oauth = SpotifyOAuth(client_id=current_app.config["SPOTIPY_CLIENT_ID"],
                             client_secret=current_app.config["SPOTIPY_CLIENT_SECRET"],
                             redirect_uri=current_app.config["SPOTIPY_REDIRECT_URI"],
                             scope="user-top-read user-library-read playlist-modify-public playlist-modify-private user-read-currently-playing user-read-playback-state user-read-recently-played user-read-playback-state user-modify-playback-state streaming")
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

def callback():
    """
    Funkcja obsługująca callback po autoryzacji użytkownika w Spotify.
    """
    sp_oauth = SpotifyOAuth(client_id=current_app.config["SPOTIPY_CLIENT_ID"],
                             client_secret=current_app.config["SPOTIPY_CLIENT_SECRET"],
                             redirect_uri=current_app.config["SPOTIPY_REDIRECT_URI"],
                             scope="user-top-read user-library-read playlist-modify-public playlist-modify-private user-read-currently-playing user-read-playback-state user-read-recently-played user-read-playback-state user-modify-playback-state streaming ")
    token_info = sp_oauth.get_access_token(request.args['code'])
    session['token_info'] = token_info
    return redirect('/recommend')

def logout():
    """
    Funkcja wylogowująca
"""
