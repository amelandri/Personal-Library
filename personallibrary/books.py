import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from personallibrary.db import get_db

bp = Blueprint('books', __name__, url_prefix='/books')


@bp.route('/list', methods=('GET', 'POST'))
def list():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM books inner join authors on books.author_id = authors.author_id")
    books = cursor.fetchall()
    db.close()
    
    return render_template('books.html', books=books)


@bp.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author_id']
        isbn = request.form['isbn']
        
        db = get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO books (title, author_id, isbn) VALUES (?, ?, ?)", (title, author, isbn))
        db.commit()
        db.close()
        
        return redirect(url_for('main'))
    
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM authors order by first_name")
    authors = cursor.fetchall()
    db.close()
    
    return render_template('books_add.html', authors=authors)