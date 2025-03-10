# app.py

from flask import Flask, render_template, redirect, session, url_for, request
import config
from auth import login, callback, get_spotify_client, logout
from spotify_client import create_playlist, add_tracks_to_playlist


app = Flask(__name__)
app.secret_key = config.SECRET_KEY
app.config.from_object(config)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login")
def login_user():
    return login()


@app.route("/callback")
def callback_user():
    return callback()


@app.route("/recommend")
def recommend():
    sp = get_spotify_client()

    if not sp:
        return redirect('/login')

    # Pobieranie topowych artystów
    top_artists = sp.current_user_top_artists(limit=5)["items"]

    # Pobieranie najczęściej słuchanych utworów
    top_tracks = sp.current_user_top_tracks(limit=5)["items"]

    # Pobieranie albumów użytkownika
    albums = sp.current_user_saved_albums(limit=5)["items"]

    return render_template("recommendations.html", top_artists=top_artists, top_tracks=top_tracks, albums=albums)


@app.route('/logout')
def logout_user():
    return logout()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_playlist', methods=['POST'])
def create_playlist_route():
    """Tworzy playlistę i przekierowuje użytkownika po sukcesie."""
    if 'token_info' not in session:
        return redirect(url_for('login'))

    sp = get_spotify_client()

    playlist_name = request.form.get('playlist_name', 'Moja Nowa Playlista')
    playlist_id = create_playlist(sp, playlist_name)

    # Możemy dodać domyślnie kilka ulubionych utworów, jeśli są
    top_tracks = sp.current_user_top_tracks(limit=5)
    track_uris = [track["uri"] for track in top_tracks["items"]]
    if track_uris:
        add_tracks_to_playlist(sp, playlist_id, track_uris)

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)