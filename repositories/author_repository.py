from db.run_sql import run_sql

from models.book import Book
from models.author import Author

def save(author):
    sql = "INSERT INTO authors (name, books_written) VALUES (%s, %s) RETURNING *"
    values = [author.name, author.books_written]
    results = run_sql(sql, values)
    id = results[0]['id']
    author.id = id
    return author

def select_all():
    authors = []

    sql = "SELECT * FROM authors"
    results = run_sql(sql)

    for row in results:
        author = Author(row["name"], row["books_written"], row["id"])
        authors.append(author)
    return authors

def select(id):
    user = None
    sql = "SELECT * FROM authors WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        author = Author(result['name'], result['books_written'], result['id'])
    return author

def delete_all():
    sql = "DELETE FROM authors"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM authors WHERE id = %s"
    values = [id]
    run_sql(sql, values)