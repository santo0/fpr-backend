from db import db


class Idea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    summary = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    image_uri = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Idea %r>' % self.name


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
