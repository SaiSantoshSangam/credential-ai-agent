from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

def create_vector_store(text_chunks):
    embeddings = OpenAIEmbeddings()
    db = Chroma.from_texts(text_chunks, embedding=embeddings)
    return db
 