from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField, IntegerField, FileField
from wtforms.validators import DataRequired, Length

class BookForm(FlaskForm):
    title = StringField('What is the Title of the book?', validators=[DataRequired(), Length(10, 250)])
    cover = FileField('Add here the Cover image')
    description = StringField('Add a brief Description about the book ')
    pages = IntegerField ('How many Pages?', validators=[DataRequired()])
    submit = SubmitField('Submit')