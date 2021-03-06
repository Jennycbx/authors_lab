from flask import Flask, render_template, redirect, request
from repositories import author_repository, book_repository

from models.book import Book

from flask import Blueprint

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/book.html", all_books = books)

@books_blueprint.route("/books/<id>/delete", methods=["POST"])
def delete_book(id):
    book_repository.delete(id)
    return redirect("/books")