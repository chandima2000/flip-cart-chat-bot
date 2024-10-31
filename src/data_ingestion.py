import os
from dotenv import load_dotenv
from langchain_astradb import AstraDBVectorStore
from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings
from src.data_converter import data_converter


load_dotenv()

# Load API keys

ASTRA_DB_API_ENDPOINT=os.getenv("ASTRA_DB_API_ENDPOINT")
ASTRA_DB_APPLICATION_TOKEN=os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_KEYSPACE=os.getenv("ASTRA_DB_KEYSPACE")
HUGGING_FACE_TOKEN = os.getenv("HUGGING_FACE_TOKEN")


# Initialize embedding model
embedding = HuggingFaceInferenceAPIEmbeddings(api_key= HUGGING_FACE_TOKEN, model_name="BAAI/bge-base-en-v1.5")


# Initialize the AstraDB vector store with embedding and connection settings.
def initialize_vector_store():
    
    return AstraDBVectorStore(
        embedding=embedding,
        collection_name="flipcart",
        api_endpoint=ASTRA_DB_API_ENDPOINT,
        token=ASTRA_DB_APPLICATION_TOKEN,
        namespace=ASTRA_DB_KEYSPACE
    )


# Ingest the data into the vector store
def data_ingestion(status=None):

    vector_store = initialize_vector_store()

    storage = status

    if storage == None:

        ## Load the document and insert it into the vector store
        docs = data_converter()
        insert_ids = vector_store.add_documents(docs)
    
    else:
        return vector_store
    return vector_store, insert_ids



# similarity search on the vector store.
def search_query(vector_store, query):
    
    results = vector_store.similarity_search(query)
    for result in results:
        print(f"\nResult: {result.page_content} [Metadata: {result.metadata}]")


if __name__ == "__main__":

    vector_store, insert_ids = data_ingestion(None)
    query = "Can you tell me the low-budget sound bass head?"
    search_query(vector_store, query)