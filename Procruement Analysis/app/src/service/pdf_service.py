import os
from tempfile import NamedTemporaryFile
from langchain.agents import Tool
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores.faiss import FAISS
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from datetime import datetime


class PDFService:
    """
    Service to handle PDF-related operations.
    """

    def __init__(self):
        self.document_buffer = []
        self.max_documents = 2

    def save_uploaded_file(self, file):
        """
        Saves an uploaded PDF file and adds it to a circular buffer.
        """
        filename = f"doc{len(self.document_buffer) + 1}.pdf"
        with open(filename, "wb") as f:
            f.write(file.file.read())
        self.document_buffer.append({"name": filename, "path": filename})
        if len(self.document_buffer) > self.max_documents:
            self.document_buffer.pop(0)  # Remove the oldest file
        return {"name": filename, "path": filename}

    def compare_documents(self, question: str):
        """
        Compares the documents in the buffer based on the given question.
        """
        if not self.document_buffer:
            raise ValueError("No documents to compare.")

        tools, llm = self.create_tools(self.document_buffer)
        result = self.run_comparison(tools, llm, question)
        return result

    def create_tools(self, files):
        """
        Creates tools for document processing using LangChain.
        """
        tools = []
        for file in files:
            loader = PyPDFLoader(file["path"])
            pages = loader.load_and_split()
            text_splitter = CharacterTextSplitter(chunk_size=4000, chunk_overlap=0)
            docs = text_splitter.split_documents(pages)
            embeddings = HuggingFaceBgeEmbeddings(model_name="BAAI/bge-small-en", model_kwargs={"device": "cpu"})
            faiss_index = FAISS.from_documents(docs, embeddings)
            faiss_index_path = f"{file['name']}_faiss_index_{datetime.now().strftime('%Y%m%d%H%M%S')}"
            faiss_index.save_local(faiss_index_path)
            retriever = faiss_index.as_retriever()
            tools.append(Tool(name=file["name"], func=RetrievalQA.from_chain_type(llm=llm, retriever=retriever)))
        return tools

    def run_comparison(self, tools, llm, question):
        """
        Runs a comparison query on the provided documents.
        """
        from langchain.agents import AgentType, initialize_agent

        agent = initialize_agent(agent=AgentType.OPENAI_FUNCTIONS, tools=tools, llm=llm, verbose=True)
        result = agent({"input": question})
        return result["output"]
