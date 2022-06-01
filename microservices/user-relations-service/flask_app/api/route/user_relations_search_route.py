import json
from flask import Blueprint
from flask import request, jsonify
from ..service.user_relations_service import UserRelationsService

idea_search_api = Blueprint('user_relations_api', __name__)


@idea_search_api.route('/idea/create', methods=['POST'])
def create_idea():
    #return list of possible users given keyword
    raise NotImplementedError

@idea_search_api.route('/idea', methods=['PUT'])
def update_idea():
    #return list of possible users given keyword
    raise NotImplementedError

@idea_search_api.route('/idea', methods=['DELETE'])
def delete_idea():
    #return list of possible users given keyword
    raise NotImplementedError

