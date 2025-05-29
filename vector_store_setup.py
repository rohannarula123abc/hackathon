from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone

embeddings = OpenAIEmbeddings()
vectorstore = Pinecone.from_documents(
    documents=knowledge_base_docs,
    embedding=embeddings,
    index_name="securegpt-knowledge"
)