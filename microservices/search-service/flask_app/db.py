from elasticsearch import Elasticsearch
from time import sleep

def connect_elasticsearch(**kwargs):
    sleep(5)
    es = None
    while 1:
        try:
            es = Elasticsearch(
                "http://elasticsearch.search-service_default:9200")
        except Exception as e:
            print("Can't connect to Elasticsearch: ", e)
            continue
        else:
            print("Connected to Elasticsearch", es.ping())
        break
    return es

es = connect_elasticsearch()