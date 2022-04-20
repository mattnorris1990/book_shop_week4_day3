from flask import Flask, render_template, Blueprint, request, redirect

from repositories import book_repository, author_repository
from models.author import Author
from models.book import Book

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/")
def books():
    books = book_repository.select_all()
    return render_template("index.html", books = books)

@books_blueprint.route("/<id>/delete", methods = ['POST'])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/')

@books_blueprint.route("/addbook")
def add_book_form():
    authors = author_repository.select_all()
    return render_template('books/new-book.html', authors=authors)

@books_blueprint.route("/addbook", methods=['POST'])
def add_book():
    title = request.form['book_name']
    author = request.form['author_id']
    author_object = author_repository.select(author)

    book_object = Book(title, author_object)

    book_repository.save(book_object)

    return redirect('/')

@books_blueprint.route('/<id>')
def show_book(id):
    book = book_repository.select(id)
    return render_template('books/show-book.html', book = book)

# BELOW DOES NOT WORK

@books_blueprint.route('/<id>/edit')
def edit_book(id):
    book = book_repository.select(id)
    author_list = author_repository.select_all()
    return render_template('/books/edit.html', book = book, authors = author_list)

@books_blueprint.route('/<id>', methods = ["POST"])
def edit_book_form(id):
    title = request.form['book_title']
    author = request.form['author_id']
    author_object = author_repository.select(author)

    book_object = Book(title, author_object, id)

    book_repository.update(book_object)

    return redirect('/')


