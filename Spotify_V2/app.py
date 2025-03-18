from flask import Flask, render_template, redirect, session, url_for, request, jsonify
import config
from auth import login, callback, get_spotify_client, logout
from spotify_client import create_playlist, add_tracks_to_playlist
import spotipy

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
        return redirect("/login")

    # Pobieranie topowych artystów
    top_artists = sp.current_user_top_artists(limit=6)["items"]

    # Pobieranie najczęściej słuchanych utworów
    top_tracks = sp.current_user_top_tracks(limit=6)["items"]

    # Pobieranie albumów użytkownika
    albums = sp.current_user_saved_albums(limit=6)["items"]

    return render_template(
        "recommendations.html",
        top_artists=top_artists,
        top_tracks=top_tracks,
        albums=albums,
    )


@app.route("/logout")
def logout_user():
    return logout()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/currently_playing")
def currently_playing():
    token = session.get("token_info", {}).get("access_token")

    if not token:
        return jsonify({"error": "Brak tokena. Zaloguj się ponownie"}), 401

    sp = spotipy.Spotify(auth=token)

    current_track = sp.current_playback()

    if current_track and current_track["is_playing"]:
        track_info = {
            "name": current_track["item"]["name"],
            "artist": ", ".join(
                artist["name"] for artist in current_track["item"]["artists"]
            ),
            "album": current_track["item"]["album"]["name"],
            "image": current_track["item"]["album"]["images"][0]["url"],
            "progress_ms": current_track["progress_ms"],
            "duration_ms": current_track["item"]["duration_ms"],
        }
        return jsonify(track_info)

    return jsonify({"error": "Brak odtwarzanej muzyki"})


@app.route("/recently_played")
def recently_played():
    token = session.get("token_info", {}).get("access_token")

    if not token:
        return jsonify({"error": "Brak tokena. Zaloguj się ponownie"}), 401

    sp = spotipy.Spotify(auth=token)

    try:
        results = sp.current_user_recently_played(limit=10)

        if not results or "items" not in results or len(results["items"]) == 0:
            return jsonify(
                {"error": "Brak danych. Spotify może nie rejestrować historii."}
            )

        recently_played_tracks = []

        for item in results["items"]:
            track = item["track"]
            recently_played_tracks.append(
                {
                    "name": track["name"],
                    "artist": ", ".join(artist["name"] for artist in track["artists"]),
                    "album": track["album"]["name"],
                    "image": (
                        track["album"]["images"][0]["url"]
                        if track["album"]["images"]
                        else None
                    ),
                    "played_at": item["played_at"],
                }
            )

        return jsonify(recently_played_tracks)

    except spotipy.exceptions.SpotifyException as e:
        return jsonify({"error": f"Spotify API error: {str(e)}"})

    except Exception as e:
        return jsonify({"error": f"Nieznany błąd: {str(e)}"})


@app.route("/dashboard")
def dashboard():
    token = session.get("token_info", {}).get("access_token")

    if not token:
        return redirect(url_for("login_user"))

    sp = spotipy.Spotify(auth=token)

    # Pobranie ostatnio odtwarzanych utworów
    recently_played = sp.current_user_recently_played(limit=12).get("items", [])

    recently_played_tracks = []
    for item in recently_played:
        track = item["track"]
        recently_played_tracks.append(
            {
                "name": track["name"],
                "artist": ", ".join(artist["name"] for artist in track["artists"]),
                "album": track["album"]["name"],
                "image": (
                    track["album"]["images"][0]["url"]
                    if track["album"]["images"]
                    else None
                ),
                "played_at": item["played_at"],
            }
        )

    return render_template("dashboard.html", recently_played=recently_played_tracks)


@app.route("/create_playlist", methods=["POST"])
def create_playlist_route():
    """Tworzy playlistę i przekierowuje użytkownika"""
    if "token_info" not in session:
        return redirect(url_for("login"))

    sp = get_spotify_client()

    playlist_name = request.form.get("playlist_name", "Moja Nowa Playlista")
    playlist_id = create_playlist(sp, playlist_name)

    # Możemy dodać domyślnie kilka ulubionych utworów, jeśli są
    top_tracks = sp.current_user_top_tracks(limit=5)
    track_uris = [track["uri"] for track in top_tracks["items"]]
    if track_uris:
        add_tracks_to_playlist(sp, playlist_id, track_uris)

    return redirect(url_for("index"))


@app.route("/get_token")
def get_token():
    token_info = session.get("token_info", {})
    if "access_token" not in token_info:
        return jsonify({"error": "Token wygasł, zaloguj się ponownie"}), 401
    return jsonify({"access_token": token_info["access_token"]})


if __name__ == "__main__":
    app.run(debug=True)
