# app.py
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('personallibrary.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books inner join authors on books.author_id = authors.author_id")
    books = cursor.fetchall()
    conn.close()
    return render_template('bookslist.html', books=books)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author_id']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (title, author_id) VALUES (?, ?)", (title, author))
        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))
    
    return render_template('add_book.html')

if __name__ == '__main__':
    app.run(debug=True)

