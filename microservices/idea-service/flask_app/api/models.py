from db import db


class Idea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ownerId = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(80), unique=True, nullable=False)
    summary = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    image_uri = db.Column(db.String(200), nullable=True)
    category = db.Column(db.String(200), nullable=False)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __repr__(self):
        return '<Idea %r>' % self.name

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    authorId = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(30), nullable=False)
    text = db.Column(db.Text, nullable=False)
    image_uri = db.Column(db.Text, nullable=True)
    created_on = db.Column(db.DateTime, server_default=db.func.now())


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    authorId = db.Column(db.Integer, nullable=False)
    message = db.Column(db.Text, nullable=False)
    parentCommentId = db.Column(db.Integer, nullable=True)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
