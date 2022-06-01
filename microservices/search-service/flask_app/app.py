from flask import Flask
import os
from api.route.search_route import search_api

app = Flask(__name__)

if __name__ == '__main__':
    app.config.from_pyfile('config.py')
    app.register_blueprint(search_api, url_prefix='/api')

    app.run(debug=True, host='0.0.0.0')
