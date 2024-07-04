DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS songs;
DROP TABLE IF EXISTS playlists;
DROP TABLE IF EXISTS playlist_songs;


CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE songs(
    id integer PRIMARY KEY AUTOINCREMENT,
    title TEXT  NOT NULL,
    artist TEXT NOT NULL,
    album TEXT,
    url TEXT
);

CREATE TABLE playlists(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE playlist_songs (
    playlist_id INTEGER NOT NULL,
    song_id INTEGER NOT NULL,
    FOREIGN KEY (playlist_id) REFERENCES playlists (id),
    FOREIGN KEY (song_id) REFERENCES songs (id),
    PRIMARY KEY (playlist_id, song_id)
);
