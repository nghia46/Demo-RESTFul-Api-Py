from flask import Flask
from repository import Repository
from service import BookService

app = Flask(__name__)

# Instantiate repository and book service
repository = Repository('books')
book_service = BookService(repository)

# Import and register the book controller
from book_controller import *

if __name__ == '__main__':
    app.run(debug=True)
