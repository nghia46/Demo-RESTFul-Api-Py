from flask import Flask
from repository import Repository
from service import BookService
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

# Instantiate repository and book service
repository = Repository('books')
book_service = BookService(repository)

# Import and register the book controller
from book_controller import *

if __name__ == '__main__':
    app.run(debug=True)
