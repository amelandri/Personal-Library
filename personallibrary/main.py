import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from personallibrary.db import get_db

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/', methods=('GET','POST'))
def register():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books inner join authors on books.author_id = authors.author_id")
    books = cursor.fetchall()

    cursor.execute("SELECT count(*) as num FROM books")
    booknum = cursor.fetchall()

    cursor.execute("SELECT count(*) as num FROM authors")
    authornum = cursor.fetchall()

    conn.close()
    return render_template('main.html', books=books, booknum=booknum, authornum=authornum )