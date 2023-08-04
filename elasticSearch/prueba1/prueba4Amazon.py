import os
import openai
from elasticsearch import Elasticsearch

# Required Environment Variables
# openai_api - OpenAI API Key
# cloud_id - Elastic Cloud Deployment ID
# cloud_user - Elasticsearch Cluster User
# cloud_pass - Elasticsearch User Password

openai.api_key = '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'
model = "gpt-3.5-turbo-0301"

# Connect to Elastic Cloud cluster
def es_connect(cid, user, passwd):
    es = Elasticsearch(cloud_id=cid, http_auth=(user, passwd))
    return es

# Search ElasticSearch index and return body and URL of the result
def search(query_text):
    cid = 'ElasticChat_GPT:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvOjQ0MyRmZmIxNmFlM2EyODY0YTRkYjg4N2ViODExM2VhMDFjOCQ2YTlmNDkwODc2ZDY0OGQ5YjA5M2Q0ZWUxNjg0ZTYyYw=='
    cp = 'vH1jyVgDrKuMDreUJkzwCjh7'
    cu = 'elastic'
    es = es_connect(cid, cu, cp)

    # Elasticsearch query (BM25) and kNN configuration for hybrid search
    query = {
        "bool": {
            "must": [{
                "match": {
                    "title": {
                        "query": query_text,
                        "boost": 1
                    }
                }
            }],
            "filter": [{
                "exists": {
                    "field": "description-vector"
                }
            }]
        }
    }

    knn = {
        "field": "description-vector",
        "k": 1,
        "num_candidates": 20,
        "query_vector_builder": {
            "text_embedding": {
                "model_id": "sentence-transformers__all-distilroberta-v1",
                "model_text": query_text
            }
        },
        "boost": 24
    }

    fields = ["description", "body_content", "url"]
    index = 'amazon-document'
    resp = es.search(index=index,
                     query=query,
                     knn=knn,
                     fields=fields,
                     size=1,
                     source=False)

    print("resp: ", resp)

    body = resp['hits']['hits'][0]['fields']['body_content'][0]
    url = resp['hits']['hits'][0]['fields']['url'][0]

    return body, url

def truncate_text(text, max_tokens):
    tokens = text.split()
    if len(tokens) <= max_tokens:
        return text

    return ' '.join(tokens[:max_tokens])

# Generate a response from ChatGPT based on the given prompt
def chat_gpt(prompt, model="gpt-3.5-turbo", max_tokens=1024, max_context_tokens=4000, safety_margin=5):
    # Truncate the prompt content to fit within the model's context length
    truncated_prompt = truncate_text(prompt, max_context_tokens - max_tokens - safety_margin)

    response = openai.ChatCompletion.create(model=model,
                                            messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": truncated_prompt}])

    return response["choices"][0]["message"]["content"]

query = input("Question: ")
resp, url = search(query)
negResponse = "I'm unable to answer the question based on the information I have from Elastic Docs."
prompt = f"Answer this question: {query}\nUsing only the information from this Elastic Doc: {resp}\nIf the answer is not contained in the supplied doc reply '{negResponse}' and nothing else"
answer = chat_gpt(prompt)

if negResponse in answer:
    print(f"ChatGPT: {answer.strip()}")
else:
    print(f"ChatGPT: {answer.strip()}\n\nDocs: {url}")
