from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

class rag_vecdb:
    def __init__(self):
        pass

    def load_data(self, data_file):
        self.load_docs = TextLoader("data_file").load()
        self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.vectorstore = Chroma.from_documents(self.load_docs, self.embeddings)
        retriever = self.vectorstore.as_retriever()
        return retriever
