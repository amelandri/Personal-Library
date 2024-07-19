-- authors definition

CREATE TABLE authors (
    author_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    notes TEXT
);

CREATE INDEX idx_authors_last_name ON authors(last_name);


-- borrowers definition

CREATE TABLE borrowers (
    borrower_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);

CREATE INDEX idx_borrowers_last_name ON borrowers(last_name);


-- editors definition

CREATE TABLE editors (
    editor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);


-- genres definition

CREATE TABLE genres (
    genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE INDEX idx_genres_name ON genres(name);


-- locations definition

CREATE TABLE locations (
    location_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT
);

CREATE INDEX idx_locations_name ON locations(name);


-- books definition

CREATE TABLE books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    isbn TEXT,
    publication_year INTEGER,
    edition TEXT,
    lang TEXT,
    notes TEXT,
    author_id INTEGER,
    editor_id INTEGER,
    genre_id INTEGER,
    location_id INTEGER, status TEXT CHECK(status IN ('A', 'O', 'L', 'D')) DEFAULT 'A',
    FOREIGN KEY (author_id) REFERENCES authors(author_id),
    FOREIGN KEY (editor_id) REFERENCES editors(editor_id),
    FOREIGN KEY (genre_id) REFERENCES genres(genre_id),
    FOREIGN KEY (location_id) REFERENCES locations(location_id)
);

CREATE INDEX idx_books_title ON books(title);


-- loans definition

CREATE TABLE loans (
    loan_id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER NOT NULL,
    borrower_id INTEGER NOT NULL,
    loan_date DATE NOT NULL,
    due_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (book_id) REFERENCES books(book_id),
    FOREIGN KEY (borrower_id) REFERENCES borrowers(borrower_id)
);

CREATE INDEX idx_loans_book_id ON loans(book_id);
CREATE INDEX idx_loans_borrower_id ON loans(borrower_id);
CREATE INDEX idx_loans_due_date ON loans(due_date);


-- book_authors definition

CREATE TABLE book_authors (
    book_id INTEGER,
    author_id INTEGER,
    PRIMARY KEY (book_id, author_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id),
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);