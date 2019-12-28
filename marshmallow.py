from marshmallow import Schema, fields, INCLUDE, EXCLUDE

class BookSchema(Schema):
    title = fields.Str(required=True)
    author = fields.Str(requeire=True)
    description = fields.Str()

class Book:
    def __init__(self, title, author, description=None):
        self.title = title
        self.author = author
        self.description = description

book = Book("title", "author", "desc")

incoming_book = {
    "title": "bla bla",
    "author": "Mr bla",
}

book_schema = BookSchema()
book_dict = book_schema.dump(book)

book2 = book_schema.load(incoming_book)
book_obj = Book(**book2)

print(book_dict)
print(book_obj.title)