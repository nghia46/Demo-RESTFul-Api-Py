from flask import jsonify, request
from bson.objectid import ObjectId
from book import Book
from app import app, book_service
from flasgger import swag_from

# Route to retrieve all books
@app.route('/api/books', methods=['GET'])
@swag_from('swagger/book/get_books.yml', methods=['GET'], endpoint='get_books')
def get_books():
    books = book_service.get_all_books()
    serialized_books = [{**book, '_id': str(book['_id'])} for book in books]
    return jsonify(serialized_books)

# Route to retrieve a single book by its ID
@app.route('/api/books/<string:book_id>', methods=['GET'])
@swag_from('swagger/book/get_book.yml', methods=['GET'], endpoint='get_book')
def get_book(book_id):
    book = book_service.get_book_by_id(ObjectId(book_id))
    if book:
        book['_id'] = str(book['_id'])
        return jsonify(book)
    else:
        return jsonify({'error': 'Book not found'}), 404

# Route to create a new book
@app.route('/api/books', methods=['POST'])
@swag_from('swagger/book/create_book.yml', methods=['POST'], endpoint='create_book')
def create_book():
    data = request.json
    book_id = book_service.create_book(data)
    return jsonify({'_id': str(book_id)}), 201

# Route to update book
@app.route('/api/books/<string:book_id>', methods=['PUT'])
@swag_from('swagger/book/update_book.yml', methods=['PUT'], endpoint='update_book')
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
@swag_from('swagger/book/delete_book.yml', methods=['DELETE'], endpoint='delete_book')
def delete_book(book_id):
    success = book_service.delete_book(ObjectId(book_id))
    if success:
        return jsonify({'message': 'Book deleted successfully'})
    else:
        return jsonify({'error': 'Book not found'}), 404
    