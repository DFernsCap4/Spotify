from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

from spotify.auth import login_required
from spotify.db import get_db

bp = Blueprint('songs', __name__)

@bp.route('/')
def index():
    db = get_db()
    songs = db.execute(
        'SELECT * FROM songs'
    ).fetchall()
    playlists = db.execute(
        'SELECT * FROM playlists WHERE user_id = ?',
        (g.user['id'],)
    )
    content=[songs,playlists]
    return render_template('songs/index.html', content=content)

@bp.route('/addSong', methods=('GET', 'POST'))
@login_required
def add():
    if request.method == 'POST':
        title = request.form['title']
        artist = request.form['artist']
        album = request.form['album']
        url = request.form['url']

        error = None

        if not title:
            error = "Title is required"
        elif not artist:
            error = "artist is required"
        
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO songs (title, artist, album, url) VALUES (?,?,?,?)',
                (title, artist, album, url)
            )
            db.commit()
            return redirect(url_for('songs.index'))
    return render_template('songs/add.html')

