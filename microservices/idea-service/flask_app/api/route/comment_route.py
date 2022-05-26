from flask import Blueprint

comment_api = Blueprint('comment_api', __name__)


@comment_api.route('/comments/<post_id>', methods=['GET'])
def get_comments(post_id):
    raise NotImplementedError()


@comment_api.route('/comment/<comment_id>', methods=['GET'])
def get_comment(comment_id):
    raise NotImplementedError()


@comment_api.route('/comment/<comment_id>/conversation', methods=['GET'])
def get_comment_conversation(comment_id):
    raise NotImplementedError()


@comment_api.route('/comment/<post_id>', methods=['POST'])
def create_comment():
    raise NotImplementedError()
