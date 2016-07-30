# coding: utf-8

import time
import random

from elasticsearch import Elasticsearch, helpers


class ElasticsearchClient(object):

    def __init__(self, host=''):
        self.elasticsearch = Elasticsearch(host)

    def search(self, index, doc_type, body=None, params={}):
        return self.elasticsearch.search(index=index, doc_type=doc_type, body=body, params=params)

    def create(self, index, doc_type, body, id=None, params={}):
        return self.elasticsearch.create(index=index, doc_type=doc_type, body=body, id=id, params=params)

    def update(self, index, doc_type, id, body=None, params={}):
        return self.elasticsearch.update(index=index, doc_type=doc_type, id=id, body=body, params=params)

    def delete(self, index, doc_type, id, params={}):
        return self.elasticsearch.delete(index=index, doc_type=doc_type, id=id, params=params)

    def bulk(self, actions, stats_only=False, **kwargs):
        return helpers.bulk(self.elasticsearch, actions=actions, stats_only=stats_only, **kwargs)

    def mget(self, body, index=None, doc_type=None, params={}):
        return self.elasticsearch.mget(body=body, index=index, doc_type=doc_type, params=params)
