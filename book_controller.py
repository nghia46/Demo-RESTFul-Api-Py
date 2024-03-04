from flask import jsonify, request
from bson.objectid import ObjectId
from book import Book 

from app import app, book_service

# Route to retrieve all books
@app.route('/api/books', methods=['GET'])
def get_books():
    # Retrieve all books from the book service
    books = book_service.get_all_books()

    # Serialize books to JSON format and convert ObjectId to string
    serialized_books = [{**book, '_id': str(book['_id'])} for book in books]

    # Return JSON response with serialized books
    return jsonify(serialized_books)

# Route to retrieve a single book by its ID
@app.route('/api/books/<string:book_id>', methods=['GET'])
def get_book(book_id):
    # Retrieve the book by its ID from the book service
    book = book_service.get_book_by_id(ObjectId(book_id))

    if book:
        # Convert ObjectId to string for JSON serialization
        book['_id'] = str(book['_id'])

        # Return JSON response with the book data
        return jsonify(book)
    else:
        # Return JSON response with error message if book is not found
        return jsonify({'error': 'Book not found'}), 404

# Route to create a new book
@app.route('/api/books', methods=['POST'])
def create_book():
    # Get data from request body
    data = request.json

    # Check if required fields are present
    if not all(key in data for key in ['Title', 'Author']):
        return jsonify({'error': 'Title and author are required'}), 400

    # Create a Book instance from request data
    new_book = Book(title=data['Title'], author=data['Author'], genre=data.get('Genre'), published_year=data.get('Year'))

    # Add the book using the book service
    book_id = book_service.create_book(new_book.to_dict())

    # Return JSON response with the ID of the newly created book
    return jsonify({'_id': str(book_id)}), 201

# Route to add multiple books
@app.route('/api/books/batch', methods=['POST'])
def add_books():
    # Get data from request body
    data = request.json

    # Check if data is provided and is a list
    if not data or not isinstance(data, list):
        return jsonify({'error': 'Data must be a non-empty list of books'}), 400

    # List to store the IDs of the newly created books
    created_books_ids = []

    # Iterate over each book data in the list
    for book_data in data:
        # Create a Book instance from the book data
        new_book = Book(
            title=book_data.get('Title'),
            author=book_data.get('Author'),
            genre=book_data.get('Genre'),
            published_year=book_data.get('Year')
        )

        # Add the book using the book service
        book_id = book_service.create_book(new_book.to_dict())
        created_books_ids.append(str(book_id))

    # Return JSON response with the IDs of the newly created books
    return jsonify({'created_books_ids': created_books_ids}), 201

# Route to update an existing book
@app.route('/api/books/<string:book_id>', methods=['PUT'])
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

# Route to delete a book by its ID
@app.route('/api/books/<string:book_id>', methods=['DELETE'])
def delete_book(book_id):
    # Delete the book using the book service
    success = book_service.delete_book(ObjectId(book_id))

    if success:
        # Return JSON response with success message if book is deleted successfully
        return jsonify({'message': 'Book deleted successfully'})
    else:
        # Return JSON response with error message if book is not found
        return jsonify({'error': 'Book not found'}), 404
