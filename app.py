from flask import Flask, redirect
from repository import Repository
from service import BookService
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

# Instantiate repository and book service
repository = Repository('books')
book_service = BookService(repository)

# Redirect root URL to /apidocs
@app.route('/')
def redirect_to_apidocs():
    return redirect('/apidocs')

# Import and register the book controller
from book_controller import *

def run_app():
    app.run(debug=True, use_reloader=False)

if __name__ == '__main__':
    app.run(debug=True)
