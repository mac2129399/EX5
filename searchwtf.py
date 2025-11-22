from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired
from booksdb import BooksDB

class SearchWTF(FlaskForm):
    myoptions = [
        (None, "Choose your Search Type"),
        ('byAuthor','By Author'),
        ('byTitle','By Title'),
        ('byPublisher','By Publisher')
    ]
    search_choice = SelectField("SearchChoice", choices=myoptions,validators=[DataRequired()] )

class ByAuthorIdWTF(FlaskForm):
    mydb = BooksDB()
    authors = mydb.getauthors()
    author_choice = SelectField("AuthorChoice", choices=authors)


class ByPublisherIdWTF(FlaskForm):
    mydb = BooksDB()
    publishers = mydb.getpublishers()
    publisher_choice = SelectField("Publisher", choices=publishers)

class ByTitleWTF(FlaskForm):
    title_choice = StringField("Enter Title", validators=[DataRequired()])
    submit = SubmitField("Search")
