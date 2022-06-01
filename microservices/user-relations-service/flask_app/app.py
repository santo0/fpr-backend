from flask import Flask
import os
#from api.route.idea_search_route import idea_search_api
#from api.route.user_search_route import user_search_api

app = Flask(__name__)

if __name__ == '__main__':
    app.config.from_pyfile('config.py')
    #app.register_blueprint(idea_search_api, url_prefix='/api')
    #app.register_blueprint(user_search_api, url_prefix='/api')

    app.run(debug=True, host='0.0.0.0')
