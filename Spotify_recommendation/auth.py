import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from flask import Flask, redirect, session, request, url_for
from dotenv import load_dotenv

# Wczytujemy zmienne środowiskowe z pliku .env
load_dotenv()

app = Flask(__name__)
app.secret_key = "some_secret_key"  # Klucz do sesji
app.config["SESSION_COOKIE_NAME"] = "Spotify Cookie"

# Ustawienia autoryzacji
sp_oauth = SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope="user-top-read playlist-read-private"
)


def login():
    """Przekierowuje użytkownika do logowania przez Spotify."""
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)


def callback():
    """Obsługuje przekierowanie po logowaniu i zapisuje token."""
    session.clear()
    code = request.args.get("code")

    if not code:
        return "Błąd autoryzacji: brak kodu", 400

    token_info = sp_oauth.get_access_token(code)
    session["token_info"] = token_info
    return redirect("/recommend")


def get_token():
    """Pobiera aktualny token i odświeża go, jeśli wygasł."""
    token_info = session.get("token_info")

    if not token_info:
        return None  # Brak tokena w sesji

    if sp_oauth.is_token_expired(token_info):
        token_info = sp_oauth.refresh_access_token(token_info["refresh_token"])
        session["token_info"] = token_info  # Aktualizacja tokena w sesji

    return token_info["access_token"]


def get_spotify_client():
    """Zwraca klienta Spotify z aktualnym tokenem."""
    access_token = get_token()

    if not access_token:
        return None  # Brak dostępu, użytkownik musi się zalogować

    return spotipy.Spotify(auth=access_token)

def logout():
    """Wylogowuje użytkownika ze Spotify."""
    session.clear()  # Usuwa wszystkie dane sesji
    return redirect(url_for("login"))  # Przekierowanie na stronę główną
