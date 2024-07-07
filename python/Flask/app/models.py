from . import db

class UserInput(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"UserInput('{self.content}')"

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    authors = db.Column(db.String(200), nullable=False)
    publisher = db.Column(db.String(200), nullable=False)
    published_date = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=False)
    page_count = db.Column(db.Integer, nullable=False)
    main_category = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f"<Book {self.title}>"
