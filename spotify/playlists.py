from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

from spotify.auth import login_required
from spotify.db import get_db

bp = Blueprint('playlists', __name__)

@bp.route('/playlists')
@login_required
def index():
    db = get_db()
    playlists = db.execute(
        'SELECT * FROM playlists WHERE user_id = ?',
        (g.user['id'],)
    ).fetchall()
    return render_template('playlists/index.html', playlists=playlists)


@bp.route('/<int:id>/details')
@login_required
def details(id):
    db = get_db()
    playlistsongs = db.execute(
        "SELECT s.* FROM songs s JOIN playlist_songs ps ON s.id = ps.song_id WHERE ps.playlist_id = ?",
        (id,)
    )
    return render_template('playlists/details.html', playlistsongs= playlistsongs)
