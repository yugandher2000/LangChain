import streamlit as st
import os
import time
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains.retrieval import create_retrieval_chain
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.embeddings import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from dotenv import load_dotenv

# Load .env from parent directory
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

groq_api_key = os.getenv("GROG_API_KEY")

if not groq_api_key:
    st.error("GROQ_API_KEY not found in environment variables. Please add it to your .env file.")
    st.stop()

llm=ChatGroq(
    api_key=groq_api_key,
    model="openai/gpt-oss-120b"
)
prompt = ChatPromptTemplate.from_template(
    """
    Answer the Questions based on the provided context .
    Please provide the most accurate response based on the question 
    <context>
        {context}
    </context>
    Question: {input}
    """
)
def create_vector_embeddings():
    if "vectors" not in st.session_state:
        st.session_state.embeddings = OllamaEmbeddings(model="llama3.1")
        st.session_state.loader = PyPDFDirectoryLoader("./research_papers") #data injection
        st.session_state.docs = st.session_state.loader.load() #loading the data
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        st.session_state.split_docs = st.session_state.text_splitter.split_documents(st.session_state.docs[:50]) #splitting the data into chunks
        st.session_state.vectors = FAISS.from_documents(st.session_state.split_docs, st.session_state.embeddings) #creating vector embeddings

user_prompt = st.text_input("Enter your query from the research papers")

if st.button("Document Embeddings"):
    create_vector_embeddings()
    st.success("Vector embeddings created successfully!")

if user_prompt:
    if "vectors" not in st.session_state:
        st.warning("Please create document embeddings first by clicking the 'Document Embeddings' button.")
    else:
        document_chain = create_stuff_documents_chain(llm,prompt)
        retriever =  st.session_state.vectors.as_retriever()
        retrieval_chain = create_retrieval_chain(retriever, document_chain)

        start_time = time.process_time()
        response = retrieval_chain.invoke({'input': user_prompt})
        end_time = time.process_time() - start_time
        print(f"Time taken for response: {end_time} seconds")
        st.write(response['answer'])

        ##with a streamlit expander
        with st.expander("Document similarity Search"):
            for i,doc in enumerate(response['context']):
                st.write(doc.page_content)
                st.write('--------------------------------------------------------------')
