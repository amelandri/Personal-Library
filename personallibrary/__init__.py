import os

from flask import Flask, render_template, request, redirect, url_for

from personallibrary.db import get_db

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'personallibrary.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    @app.route('/')
    def index():
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

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import books
    app.register_blueprint(books.bp)

    from . import authors
    app.register_blueprint(authors.bp)

    return app

