# app.py
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database/personallibrary.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books inner join authors on books.author_id = authors.author_id")
    books = cursor.fetchall()

    cursor.execute("SELECT count(*) as num FROM books")
    booknum = cursor.fetchall()

    cursor.execute("SELECT count(*) as num FROM authors")
    authornum = cursor.fetchall()

    conn.close()
    return render_template('bookslist.html', books=books, booknum=booknum, authornum=authornum )

@app.route('/authors')
def authorslist():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT authors.author_id, first_name, last_name, count(books.book_id) as book_num FROM authors inner join books on books.author_id = authors.author_id group by authors.author_id, first_name, last_name ORDER BY first_name, last_name")
    authors = cursor.fetchall()

    conn.close()
    return render_template('authorslist.html', authors=authors )

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author_id']
        isbn = request.form['isbn']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (title, author_id, isbn) VALUES (?, ?, ?)", (title, author, isbn))
        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM authors order by first_name")
    authors = cursor.fetchall()
    conn.close()
    
    return render_template('add_book.html', authors=authors)

@app.route('/addAuthor', methods=['GET', 'POST'])
def add_author():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO authors (first_name, last_name ) VALUES (?, ?)", (first_name, last_name))
        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))
    
    return render_template('add_author.html')

if __name__ == '__main__':
    app.run(debug=True)

