from flask import Blueprint

post_api = Blueprint('post_api', __name__)


@post_api.route('/posts/<idea_id>', methods=['GET'])
def get_posts(idea_id):
    # read database
    # notify user logging service
    raise NotImplementedError()


@post_api.route('/post/<post_id>', methods=['GET'])
def get_post(post_id):
    # read database
    # notify user logging service
    raise NotImplementedError()


@post_api.route('/post/<idea_id>', methods=['POST'])
def create_post(idea_id):
    # write database
    # notify user service
    # notify feed service
    raise NotImplementedError()


@post_api.route('/post/<post_id>', methods=['DELETE'])
def delete_post(post_id):
    # write database
    # notify user service
    raise NotImplementedError()


@post_api.route('/post/<post_id>/like', methods=['PUT'])
def like_post():
    # write database
    # notify user service
    # notify notification service
    # notify feed service
    raise NotImplementedError()


@post_api.route('/post/<post_id>/like', methods=['DELETE'])
def unlike_post(post_id):
    # write database
    # notify user service
    # notify feed service
    raise NotImplementedError()
