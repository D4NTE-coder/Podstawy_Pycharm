import os
from dotenv import load_dotenv

load_dotenv()  # Ładowanie zmiennych środowiskowych z pliku .env

class Config:
    SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
    SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
    SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")
    SECRET_KEY = os.getenv("SECRET_KEY")
