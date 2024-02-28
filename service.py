class BookService:
    def __init__(self, repository):
        self.repository = repository

    def get_all_books(self):
        return self.repository.find_all()

    def get_book_by_id(self, book_id):
        return self.repository.find_by_id(book_id)

    def create_book(self, data):
        return self.repository.create(data)

    def update_book(self, book_id, data):
        return self.repository.update(book_id, data)

    def delete_book(self, book_id):
        return self.repository.delete(book_id)