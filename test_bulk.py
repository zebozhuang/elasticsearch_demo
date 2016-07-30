# coding: utf-8

import random
from elasticsearch_client import ElasticsearchClient

HOST = '127.0.0.1'

elk_client = ElasticsearchClient(HOST)


def bulk():
    '''批量写入'''
    num = 5 * 10 ** 3  # 5000
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
                'username': 'test_%d' % (i + 1),
                'age': random.randint(20, 30),
                'gender': random.choice(['male', 'female']),
            }
        }

        actions.append(action)
        i += 1

        if len(actions) > 10000:
            elk_client.bulk(actions=actions)
            del actions[:]  # 不用重新申请内存

    elk_client.bulk(actions=actions)
    del actions[:]


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


bulk()
mget()
