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

def run_app():
    app.run(debug=True, use_reloader=False)

if __name__ == '__main__':
    print(" * Running on http://127.0.0.1:5000/apidocs (Press CTRL+C to quit)")
    app.run(debug=True)
