class Book:
    def __init__(self, title, author, genre=None, published_year=None):
        self.title = title
        self.author = author
        self.genre = genre
        self.published_year = published_year

    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'genre': self.genre,
            'published_year': self.published_year
        }
