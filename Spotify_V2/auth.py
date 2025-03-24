# auth.py

from flask import current_app, redirect, request, session, url_for
from spotipy.oauth2 import SpotifyOAuth
import spotipy
import os

from flask import current_app
from spotipy.oauth2 import SpotifyOAuth

def create_sp_oauth():
    """Funkcja tworząca instancję SpotifyOAuth w kontekście aplikacji"""
    with current_app.app_context():  # Dodanie kontekstu aplikacji
        return SpotifyOAuth(
            client_id=current_app.config["SPOTIPY_CLIENT_ID"],
            client_secret=current_app.config["SPOTIPY_CLIENT_SECRET"],
            redirect_uri=current_app.config["SPOTIPY_REDIRECT_URI"],
            scope="user-top-read user-library-read playlist-modify-public playlist-modify-private user-read-currently-playing user-read-playback-state user-read-recently-played user-read-playback-state user-modify-playback-state streaming",
            show_dialog=True  # Wymusza ponowne logowanie
        )


def login():
    sp_oauth = create_sp_oauth()  # Utwórz instancję sp_oauth w kontekście aplikacji
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

def callback():
    sp_oauth = create_sp_oauth()  # Utwórz instancję sp_oauth w kontekście aplikacji
    token_info = sp_oauth.get_access_token(request.args['code'])
    session['token_info'] = token_info
    return redirect('/recommend')

def get_spotify_client():
    token_info = session.get("token_info")
    if not token_info:
        return None

    sp_oauth = create_sp_oauth()  # Utwórz instancję sp_oauth w kontekście aplikacji
    if sp_oauth.is_token_expired(token_info):
        token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])
        session['token_info'] = token_info
    sp = spotipy.Spotify(auth=token_info["access_token"])
    return sp


def logout():
    """Wylogowanie użytkownika i całkowite usunięcie sesji"""
    session.pop('token_info', None)  # Usuń token ze zmiennych sesji
    session.clear()  # Wyczyść całą sesję

    # Dodatkowo usuń zapisany token OAuth2, jeśli istnieje
    if os.path.exists(".cache"):
        os.remove(".cache")

    return redirect(url_for('home'))
