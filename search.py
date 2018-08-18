import json
import requests
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


def search_tags(term):
    query = {
        "query": {
            "match": {
                "source": "{}".format(term)
            }
        }
    }
    return es.search(index='testbulk2', body=query)

res = search_tags('VietnamNet')
print(res)
