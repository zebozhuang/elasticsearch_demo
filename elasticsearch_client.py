# coding: utf-8

import time
import random

from elasticsearch import Elasticsearch, helpers

HOST = '127.0.0.1'

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


if __name__ == '__main__':
    elk_client = ElasticsearchClient(HOST)


    index = 'myindex'
    doc_type = 'mytype'
    params = {
        "match": {
            "product": "Apples"
        }
    }

    #　search ...
    ret = elk_client.search(index=index, doc_type=doc_type, params=params)
    print "search ...\n", ret

    # create ...
    ret = elk_client.create(index='test', doc_type='user', body={'username': "t%s" % int(time.time()), 'age': random.randint(18, 30)})
    print "create ...\n", ret

    # update ...
    ret = elk_client.update(index='test', doc_type='user', id=ret['_id'], body={'doc': {'age': int(random.randint(14, 18))}})
    print "update ...\n", ret

    # update ...
    ret = elk_client.delete(index='test', doc_type='user', id=ret['_id'])
    print "delete ...\n", ret


    def bulk():
        '''批量写入'''
        num = 5*10**3 # 5000
        index = 'congyezhe'
        doc_type = 'user'

        i = 0
        actions = []
        while i < num:
            action = {
                '_index': index,
                '_type': doc_type,
                '_id': i + 1,
                '_source': {
                    'username': 'test_%d' % (i+1),
                    'age': random.randint(20, 30),
                    'gender': random.choice(['male', 'female']),
                }
            }

            actions.append(action)
            i += 1

            if len(actions) > 10000:
                elk_client.bulk(actions=actions)
                del actions[:]   #　不用重新申请内存

        elk_client.bulk(actions=actions)
        del actions[:]

    bulk()

    print "\n"

    def mget():
        '''批量获取'''
        index = 'congyezhe'
        doc_type = 'user'

        body = {
            'ids': [1, 2, 3]
        }

        users = elk_client.mget(body=body, index=index, doc_type=doc_type)

        for user in users.get('docs', []):
            print "user-->:", user

    mget()