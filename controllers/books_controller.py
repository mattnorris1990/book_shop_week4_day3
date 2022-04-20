from flask import Flask, render_template, Blueprint, request, redirect

from repositories import book_repository, author_repository
from models.author import Author
from models.book import Book

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/")
def books():
    books = book_repository.select_all()
    return render_template("index.html", books = books)