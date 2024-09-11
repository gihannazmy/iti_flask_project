from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from flask import url_for

db = SQLAlchemy()

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    pages = db.Column(db.Integer,  nullable=True)
    title = db.Column(db.String(250))
    description = db.Column(db.String(1000), nullable=True)
    cover = db.Column(db.String(250), nullable=True)

    def __str__(self):
        return f"{self.name}"

    @property
    def cover_url(self):
        return url_for('static', filename=f'books/images/{self.cover}')

    @property
    def show_url(self):
        return url_for('books.show', id=self.id)

    @property
    def delete_url(self):
        return url_for('books.delete', id=self.id)

    @property
    def edit_url(self):
        return url_for('books.edit', id=self.id)