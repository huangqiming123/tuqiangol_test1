from elasticsearch import Elasticsearch

es = Elasticsearch(
    ['http://tuqianges.jimicloud.com'],
    http_auth=('admin', 'jimijimi'),
    port=9200
)
