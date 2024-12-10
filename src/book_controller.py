import os
from flask import jsonify, request
from bson.objectid import ObjectId
from app import app, book_service
from flasgger import swag_from

# Đường dẫn tuyệt đối tới thư mục swagger
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Lấy thư mục chứa file controller
SWAGGER_DIR = os.path.join(BASE_DIR, '../swagger')  # Lùi lại 2 cấp tới thư mục gốc

# Route to retrieve all books
@app.route('/api/books', methods=['GET'])
@swag_from(os.path.join(SWAGGER_DIR, 'book/get_books.yml'))
def get_books():
    books = book_service.get_all_books()
    serialized_books = [{**book, '_id': str(book['_id'])} for book in books]
    return jsonify(serialized_books)

# Route to retrieve a single book by its ID
@app.route('/api/book/<string:book_id>', methods=['GET'])
@swag_from(os.path.join(SWAGGER_DIR, 'book/get_book.yml'))
def get_book(book_id):
    book = book_service.get_book_by_id(ObjectId(book_id))
    if book:
        book['_id'] = str(book['_id'])
        return jsonify(book)
    else:
        return jsonify({'error': 'Book not found'}), 404

# Route to create a new book
@app.route('/api/books', methods=['POST'])
@swag_from(os.path.join(SWAGGER_DIR, 'book/create_book.yml'))
def create_book():
    data = request.json
    book_id = book_service.create_book(data)
    return jsonify({'_id': str(book_id)}), 201

# Route to update book
@app.route('/api/books/<string:book_id>', methods=['PUT'])
@swag_from(os.path.join(SWAGGER_DIR, 'book/update_book.yml'))

def update_book(book_id):
    # Get data from request body
    data = request.json

    # Update the book using the book service
    success = book_service.update_book(ObjectId(book_id), data)

    if success:
        # Return JSON response with success message if book is updated successfully
        return jsonify({'message': 'Book updated successfully'})
    else:
        # Return JSON response with error message if book is not found
        return jsonify({'error': 'Book not found'}), 404
    
# Route to delete book
@app.route('/api/books/<string:book_id>', methods=['DELETE'])
@swag_from(os.path.join(SWAGGER_DIR, 'book/delete_book.yml'))
def delete_book(book_id):
    success = book_service.delete_book(ObjectId(book_id))
    if success:
        return jsonify({'message': 'Book deleted successfully'})
    else:
        return jsonify({'error': 'Book not found'}), 404
    