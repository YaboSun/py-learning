from elasticsearch import Elasticsearch

es = Elasticsearch(hosts='localhost:9200', http_auth='elastic:123456')
print(es.cluster.client.info())
print(es.index(index='py2', id=1, body={'name': "张三", "age": 18}))
print(es.get(index='py2', id=1))

