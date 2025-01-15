from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (can be replaced with a database)
books = {
    1: {'id': 1, 'title': 'John Doe', 'author': 'johndoe'},
    2: {'id': 2, 'title': 'Jane Smith', 'author': 'janesmith'}
}

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return books

# Get a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    for book in books.values():  # Iterate over dictionary values
        if book['id'] == book_id:
            return book

    return {'error':'Book not found'}

# Create a book
@app.route('/books', methods=['POST'])
def create_book():
    new_book = {
        'id': len(books) + 1,
        'title': request.json['title'],
        'author': request.json['author']
    }
    # Add the new book to the dictionary
    books[new_book['id']] = new_book
    return new_book, 201  # Return 201 Created status

# Update a book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = books.get(book_id)
    if book:
        # Update book fields with provided data, or keep existing values if not provided
        book['title'] = request.json.get('title', book['title'])
        book['author'] = request.json.get('author', book['author'])
        return jsonify(book)
    return jsonify({'error': 'Book not found'}), 404

# Delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = books.pop(book_id, None)
    if book:
        return jsonify({'message': 'Book deleted'})
    return jsonify({'error': 'Book not found'}), 404


# Run the flask App
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
