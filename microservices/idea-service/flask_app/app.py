from flask import Flask
from celery import Celery
import os
from api.route.idea_route import idea_api
from api.route.post_route import post_api
from api.route.comment_route import comment_api
from db import db

app = Flask(__name__)

if __name__ == '__main__':
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'SQLALCHEMY_DATABASE_URI')
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.register_blueprint(idea_api, url_prefix='/api')
    app.register_blueprint(comment_api, url_prefix='/api')
    app.register_blueprint(post_api, url_prefix='/api')
    backend_uri = 'db+postgresql://localhost:5433/postgres'

    simple_app = Celery('simple_worker',
                        broker='amqp://admin:mypass@rabbit:5672',
                        backend='mongodb://mongodb_container:27017/mydb')

    app.run(debug=True, host='0.0.0.0')
