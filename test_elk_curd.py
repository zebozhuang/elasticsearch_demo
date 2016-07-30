# coding: utf-8

import random
import time
from elasticsearch_client import ElasticsearchClient

HOST = '127.0.0.1'

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
