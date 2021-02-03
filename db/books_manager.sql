DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;

CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    books_written INT
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    year INT,
    author_id INT REFERENCES authors(id) ON DELETE CASCADE
);