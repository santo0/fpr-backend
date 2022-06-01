import json
from flask import Blueprint
from flask import request, jsonify
from ..service.search_service import SearchService
from db import es

search_api = Blueprint('search_api', __name__)


@search_api.route('/search', methods=['GET'])
def get_results_by_keyword():
    # return list of possible users given keyword
    raise NotImplementedError


@search_api.route('/search-idea', methods=['GET'])
def get_ideas_by_keyword():
    # return list of possible ideas given keyword
    data = request.json
    searchService = SearchService(es)
    resp = searchService.get_ideas_by_keyword(data['query'])
    print(resp)
    ideas = [{'id': hit['_id'], 'idea_name': hit['_source']["idea_name"]}
             for hit in resp['hits']['hits']]
    return jsonify(ideas)


@search_api.route('/search-user', methods=['GET'])
def get_users_by_keyword():
    # return list of possible users given keyword
    raise NotImplementedError
