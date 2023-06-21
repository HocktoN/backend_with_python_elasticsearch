from elasticsearch_dsl import Document, Text
from elasticsearch_dsl.connections import connections
from elasticsearch import Elasticsearch

ELASTICSEARCH_HOST = "172.17.0.3"
ELASTICSEARCH_PORT = '9200'
ELASTICSEARCH_CONNECTION_URL = '{host}:{port}'.format(
    host=ELASTICSEARCH_HOST, port=ELASTICSEARCH_PORT)
connections.create_connection(hosts=[ELASTICSEARCH_CONNECTION_URL], timeout=30)

client = Elasticsearch(hosts=['http://localhost:9200'])


class User(Document):
    username = Text()
    email = Text()
    password = Text(fields={'crypto': Text(analyzer='standard')})

    class Index:
        name = 'users'
