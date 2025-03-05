import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID", "twoje_client_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET", "twoje_secret_ID")
REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI", "http://localhost:5000/callback")

SCOPE = "user-top-read playlist-modify-public"
SECRET_KEY = "klucz"