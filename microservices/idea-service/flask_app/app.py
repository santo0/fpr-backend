from flask import Flask
from celery import Celery
from api.route.idea_route import idea_api
from api.route.post_route import post_api
from api.route.comment_route import comment_api

if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(idea_api, url_prefix='/api')
    app.register_blueprint(comment_api, url_prefix='/api')
    app.register_blueprint(post_api, url_prefix='/api')
    backend_uri = 'db+postgresql://localhost:5433/postgres'

    simple_app = Celery('simple_worker',
                        broker='amqp://admin:mypass@rabbit:5672',
                        backend='mongodb://mongodb_container:27017/mydb')

    app.run()
