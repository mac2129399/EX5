from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired
from booksdb import BooksDB

class SearchWTF(FlaskForm):
    """
    Main search selection form.
    Options include: author, title and publisher.
    """
    myoptions = [
        (None, "Choose your Search Type"),
        ('byAuthor','By Author'),
        ('byTitle','By Title'),
        ('byPublisher','By Publisher')
    ]
    search_choice = SelectField("SearchChoice", choices=myoptions,validators=[DataRequired()] )

class ByAuthorIdWTF(FlaskForm):
    """Form to search books by author."""
    mydb = BooksDB()
    authors = mydb.getauthors()
    author_choice = SelectField("AuthorChoice", choices=[], coerce=int)
    submit = SubmitField("Search")

class ByPublisherIdWTF(FlaskForm):
    """Form to search books by publisher."""
    mydb = BooksDB()
    publishers = mydb.getpublishers()
    publisher_choice = SelectField("PublisherChoice", choices=[], coerce=int)
    submit = SubmitField("Search")

class ByTitleWTF(FlaskForm):
    """Form to search books by title."""
    title_input = StringField("Enter Title", validators=[DataRequired()])
    submit = SubmitField("Search")
