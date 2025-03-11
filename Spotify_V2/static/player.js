const CLIENT_ID = 'db1bf149e0f141d0a20a52a5ed4a3fdb';
const REDIRECT_URI = 'http://localhost:5000/callback';
const SCOPES = 'user-read-playback-state user-modify-playback-state streaming';

let token = null;
let player = null;

const loginBtn = document.getElementById('login-btn');
const playBtn = document.getElementById('play-btn');

// Funkcja logowania do Spotify
if (loginBtn) {
    loginBtn.addEventListener('click', () => {
        const authUrl = `https://accounts.spotify.com/authorize?client_id=${CLIENT_ID}&response_type=token&redirect_uri=${REDIRECT_URI}&scope=${SCOPES}`;
        window.location.href = authUrl;
    });
}

// Funkcja do uzyskiwania tokenu z URL po przekierowaniu
window.onload = () => {
    const hash = window.location.hash.substring(1);
    const params = new URLSearchParams(hash);
    token = params.get('access_token');

    if (token) {
        if (loginBtn) loginBtn.style.display = 'none';  // Ukryj przycisk logowania
        if (playBtn) playBtn.style.display = 'block';  // Pokaż przycisk odtwarzania
        initializePlayer();  // Inicjalizuj odtwarzacz
    }
};

// Funkcja inicjalizująca Spotify Web Playback SDK
function initializePlayer() {
    if (!token) {
        console.error('Brak tokenu dostępu');
        return;
    }

    player = new Spotify.Player({
        name: 'My Spotify Player',
        getOAuthToken: (cb) => { cb(token); },
        volume: 0.5
    });

    player.addListener('initialization_error', ({ message }) => console.error(message));
    player.addListener('authentication_error', ({ message }) => console.error(message));
    player.addListener('account_error', ({ message }) => console.error(message));
    player.addListener('playback_error', ({ message }) => console.error(message));

    player.addListener('player_state_changed', state => {
        console.log(state);
    });

    player.addListener('ready', ({ device_id }) => {
        console.log('Player is ready with device ID', device_id);
        setActiveDevice(device_id);  // Ustaw aktywne urządzenie
    });

    player.addListener('not_ready', ({ device_id }) => {
        console.log('Player is not ready with device ID', device_id);
    });

    player.connect();
}

// Funkcja ustawiająca aktywne urządzenie
function setActiveDevice(device_id) {
    fetch('https://api.spotify.com/v1/me/player/devices', {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${token}`
        }
    })
    .then(response => response.json())
    .then(data => {
        const activeDevice = data.devices.find(device => device.id === device_id);
        if (activeDevice) {
            fetch(`https://api.spotify.com/v1/me/player`, {
                method: 'PUT',
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ device_ids: [device_id] })
            })
            .then(() => {
                console.log('Device set as active');
            })
            .catch(err => console.error('Error setting active device:', err));
        }
    });
}

// Funkcja do rozpoczęcia odtwarzania
if (playBtn) {
    playBtn.addEventListener('click', () => {
        fetch('https://api.spotify.com/v1/me/player/play', {
            method: 'PUT',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            }
        })
        .then(() => {
            console.log('Playback started');
        })
        .catch(err => console.error('Error starting playback:', err));
    });
}

// Spotify SDK initialization
window.onSpotifyWebPlaybackSDKReady = () => {
    // Initialize the player after the SDK is ready
    console.log("Spotify Web Playback SDK is ready!");
};
