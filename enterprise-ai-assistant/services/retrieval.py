from services.embedding import model
from services.vectordb import collection

def search_documents(question):

    question_embedding = (
        model.encode(question)
        .tolist()
    )

    results = collection.query(
        query_embeddings=[
            question_embedding
        ],
        n_results=3
    )

    return results["documents"][0]