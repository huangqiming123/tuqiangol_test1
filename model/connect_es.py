from elasticsearch import Elasticsearch


class ConnectEs():
    # 连接es
    def connect_es(self):
        es = Elasticsearch(
            ['172.16.0.115'],
            http_auth=('admin', 'jimijimi'),
            port=9200
        )
        return es
