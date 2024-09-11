

from flask import request, render_template, url_for, redirect
from werkzeug.utils import secure_filename

from app.books import book_blueprint
from app.models import Book, db
import os



@book_blueprint.route('', endpoint='index')
def index():
    books = Book.query.all()
    return render_template("books/index.html", books=books)



@book_blueprint.route('<int:id>/show', endpoint='show')
def show (id):
    book = db.get_or_404(Book, id)
    return render_template("books/show.html", book=book)

@book_blueprint.route('/<int:id>/delete', endpoint='delete')
def delete(id):
    book = db.get_or_404(Book, id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('books.index'))

# forms
from app.books.forms import BookForm
@book_blueprint.route("/create", endpoint='create', methods=["GET", "POST"])
def create():
    form = BookForm()
    if request.method=="POST":
        if form.validate_on_submit():
            cover_name = None
            if request.files.get('cover'):
                cover = form.cover.data
                cover_name = secure_filename(cover.filename)
                cover.save(os.path.join('static/books/images', cover_name))
            data= dict(request.form)
            del data['csrf_token']
            del data['submit']
            data['cover'] = cover_name
            book = Book(**data)
            db.session.add(book)
            db.session.commit()
            return redirect(book.show_url)
    return render_template('books/forms/create.html', form=form)

@book_blueprint.route('/<int:id>/edit', endpoint='edit', methods=['GET', 'POST'])
def edit(id):
    # get all books first
    book = Book.query.get_or_404(id)
    form = BookForm(obj=book)
    if request.method == "POST":
        if form.validate_on_submit():
            book.title = form.title.data
            book.description = form.description.data
            book.pages = form.pages.data
            if request.files.get('cover'):
                cover = form.cover.data
                cover_name = secure_filename(cover.filename)
                cover.save(os.path.join('static/books/images', cover_name))
                book.cover = cover_name
            db.session.commit()
            return redirect(book.show_url)

    return render_template('books/forms/edit.html', form=form, book=book)
