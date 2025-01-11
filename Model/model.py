# Building a RAG model as a QA bot for business related queries using transformers and pinecone databases for storing the data and vectorizing it.

import os
import openai
from pinecone import Pinecone  
from scrape import business_data
from sentence_tranformers import SentenceTransformer
from transformers import BertModel
import csv, json

pc = Pinecone(
    api_key = 'Enter your API key',
    environment = ''
)
index_name = ''
index = pc.Index(index_name)

openai.api_key = 'API_key'

def generate_embeds(text):
    model = SentenceTransformer('stsb-xlm-r-multilingual', trust_remote_code=True)
    embeddings = model.encode(text, batch_size = 32, convert_to_tensor=True)
    
    return embeddings['data'][0]['embedding']

embeds = [generate_embeds(doc) for doc in business_data]
print("Embeddings generated for all documents")


embedding_data = [(f"doc-{i}", embedding.tolist(), {"text": doc}) for i, (embedding, doc) in enumerate(zip(embeds, business_data))]
index.upsert(embedding_data)


model = SentenceTransformer('stsb-xlm-r-multilingual', trust_remote_code=True)

def retrieve_docs(query, top_k=5):
    query_embedding = model.encode(query).tolist()
    results = index.query(query_embedding, top_k = top_k, include_metadata=True)
    return [match['metadata']['text'] for match in results['matches']]

query = input("Enter the Query you have related to business: ")
results = retrieve_docs(query)


# import requests

# def generate_response_with_llama(context, query):
#     url = "http://localhost:5000/generate"
#     payload = {
#         "context": context,
#         "query": query
#     }
#     try:
#         response = requests.post(url, json=payload)
#         response.raise_for_status()
#         return response.json().get("response", "Sorry, no response generated.")
#     except requests.exceptions.RequestException as e:
#         return f"Error in Llama generation: {e}"


# formatted_context = "\n\n".join(results)  # Combine retrieved documents
# final_response = generate_response_with_llama(formatted_context, query)

# print("Final Response:")
# print(final_response)