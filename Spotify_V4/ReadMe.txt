# 🎵 Spotify V4

Fullstack Spotify web application built with **FastAPI**, **JavaScript**, and the **Spotify Web API**.

The application allows users to log in with their Spotify account and control playback directly from a custom dashboard.

---

# 🚀 Live Demo

https://spotifyv4.onrender.com

---

# ✨ Features

## 🔐 Authentication

* Spotify OAuth 2.0 login
* User session handling

## 🎵 Playback Controls

* Play / Pause
* Next / Previous track
* Seek / Progress bar
* Real-time currently playing updates

## 🔍 Search

* Search Spotify tracks dynamically
* Play selected tracks instantly

## ❤️ User Content

* Recently played tracks
* User playlists
* Liked songs integration

## 🎨 Frontend

* Responsive Spotify-inspired UI
* Dynamic updates with JavaScript
* Real-time refresh without page reload

---

# 🛠️ Tech Stack

### Backend

* Python
* FastAPI
* Requests

### Frontend

* HTML
* CSS
* JavaScript

### APIs & Auth

* Spotify Web API
* OAuth 2.0

### Deployment

* Render

---


# ⚙️ Installation

## 1. Clone repository

```bash
git clone https://github.com/D4NTE-coder/Podstawy_Pycharm.git
```

## 2. Go to project directory

```bash
cd Spotify_V4
```

## 3. Create virtual environment

```bash
python -m venv .venv
```

## 4. Activate virtual environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

## 5. Install dependencies

```bash
pip install -r requirements.txt
```

## 6. Create `.env`

```env
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
REDIRECT_URI=http://127.0.0.1:8000/callback
SECRET_KEY=your_secret_key
```

## 7. Run application

```bash
uvicorn app.main:app --reload
```

---

# 🔑 Spotify Developer Setup

Create your Spotify app here:

https://developer.spotify.com/dashboard

Add redirect URI:

```text
http://127.0.0.1:8000/callback
```

For deployed version:

```text
https://spotifyv4.onrender.com/callback
```

---

# 📚 What I Learned

* OAuth 2.0 authentication flow
* REST API integration
* FastAPI backend architecture
* Dynamic frontend updates with JavaScript
* Real-world deployment workflow
* Working with external APIs and sessions

---

# 📌 Future Improvements

* Spotify Web Playback SDK
* Better responsive design
* User settings
* Queue management
* Improved recommendations system

---

# 👨‍💻 Author

Damian Rojek

GitHub:
https://github.com/D4NTE-coder
