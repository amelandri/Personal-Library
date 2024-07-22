import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from personallibrary.db import get_db

bp = Blueprint('authors', __name__, url_prefix='/authors')


@bp.route('/list', methods=('GET', 'POST'))
def list():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT authors.author_id, first_name, last_name, count(books.book_id) as book_num FROM authors left outer join books on books.author_id = authors.author_id group by authors.author_id, first_name, last_name ORDER BY first_name, last_name")
    authors = cursor.fetchall()
    db.close()
    
    return render_template('authors.html', authors=authors)


@bp.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO authors (first_name, last_name) VALUES (?, ?)", (first_name, last_name))
        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))
    
    return render_template('authors_add.html')