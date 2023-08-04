# Create a client instance
from elasticsearch import Elasticsearch
import openai

openai.api_key = ''

# Create a client instance with the necessary credentials
client = Elasticsearch(
    cloud_id='Elastic_DB:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvOjQ0MyQ0MzEwNjhmNjNlZGQ0MzE0YTgwZTE4NTMxNDUwMGQ0MCQxNjNiM2FkMTExMGQ0ODcwOWU4ZWJhMjkxOTQwMDU5Yw==',
    http_auth=('elastic', 'fUKkjx2bh80IlqzMGkT2kKXe')
)

# index name
index_name = 'search-amazon-document'

# search query
response = client.search(index=index_name, body={
    "query": {
        "match_all": {}
        }
})

# response
for hit in response['hits']['hits']:
    print(hit['_source'])

