# RAG Document Q&A Application

A Retrieval-Augmented Generation (RAG) application built with Streamlit and LangChain that allows users to ask questions about PDF documents using AI-powered search and question answering.

## Features

- 📄 **PDF Document Processing**: Automatically loads and processes PDF files from a directory
- 🔍 **Semantic Search**: Uses FAISS vector store for efficient similarity search
- 🤖 **AI-Powered Answers**: Leverages Groq's ChatGroq model for intelligent responses
- 💾 **Vector Embeddings**: Uses Ollama embeddings for document vectorization
- 📊 **Context Display**: Shows relevant document chunks that were used to answer questions
- ⚡ **Fast Response Time**: Optimized retrieval chain for quick answers

## Prerequisites

Before running this application, ensure you have:

1. **Python 3.8+** installed
2. **Ollama** installed and running locally
   - Download from: https://ollama.ai
   - Pull the required model: `ollama pull llama3.1`
3. **Groq API Key**
   - Sign up at: https://console.groq.com
   - Get your API key from the dashboard

## Installation

1. **Clone the repository** (or navigate to the project directory)
   ```bash
   cd "C:\Users\LangChain\RAG_document_QA"
   ```

2. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   Required packages:
   - streamlit
   - langchain-classic
   - langchain-community
   - langchain-core
   - langchain-groq
   - langchain-text-splitters
   - pypdf
   - faiss-cpu
   - python-dotenv

3. **Set up environment variables**
   
   Create or update the `.env` file in the parent directory (`LangChain/.env`):
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Add PDF documents**
   
   Place your PDF files in the `research_papers` folder:
   ```
   RAG_document_QA/
   ├── app.py
   └── research_papers/
       ├── document1.pdf
       ├── document2.pdf
       └── ...
   ```

## Usage

1. **Start Ollama** (if not already running)
   ```bash
   ollama serve
   ```

2. **Run the Streamlit application**
   ```bash
   streamlit run app.py
   ```

3. **Using the application**
   
   a. **Create Document Embeddings**:
      - Click the "Document Embeddings" button to process your PDF documents
      - This creates vector embeddings for semantic search
      - Wait for the success message
   
   b. **Ask Questions**:
      - Enter your question in the text input field
      - Press Enter or click outside the input box
      - The AI will retrieve relevant context and provide an answer
   
   c. **View Source Context**:
      - Expand the "Document similarity Search" section
      - See the actual document chunks used to answer your question

## Configuration

### Chunk Settings
In `app.py`, you can modify text splitting parameters:
```python
RecursiveCharacterTextSplitter(
    chunk_size=1000,      # Size of each text chunk
    chunk_overlap=200     # Overlap between chunks
)
```

### Document Limit
Currently processes the first 50 document chunks. Modify in `create_vector_embeddings()`:
```python
st.session_state.split_docs = st.session_state.text_splitter.split_documents(
    st.session_state.docs[:50]  # Change this number
)
```

### Ollama Model
Change the embedding model in `create_vector_embeddings()`:
```python
OllamaEmbeddings(model="llama3.1")  # Try: gemma3, llama2, etc.
```

### Groq Model
Change the chat model:
```python
ChatGroq(
    api_key=groq_api_key,
    model="openai/gpt-oss-120b"  # Or other Groq models
)
```

## Architecture

```
User Query → Vector Store (FAISS) → Retriever → LangChain Chain → Groq LLM → Answer
                    ↑
            PDF Documents → Text Splitter → Ollama Embeddings
```

## Troubleshooting

### Issue: "GROQ_API_KEY not found"
**Solution**: Ensure the `.env` file exists in the parent directory and contains:
```
GROQ_API_KEY=your_actual_api_key
```

### Issue: "model 'llama3.1' not found"
**Solution**: Pull the model using Ollama:
```bash
ollama pull llama3.1
```
Or change to an installed model (check with `ollama list`)

### Issue: "research_papers directory not found"
**Solution**: Create the directory and add PDF files:
```bash
mkdir research_papers
```

### Issue: Slow embedding creation
**Solution**: 
- Reduce the number of documents processed (change `[:50]` to a smaller number)
- Use a smaller embedding model
- Ensure Ollama is running locally

## Performance Tips

1. **First-time setup**: Creating embeddings takes time. It only needs to be done once per session.
2. **Session persistence**: Vector embeddings are stored in `st.session_state` and persist during the session.
3. **Restart required**: If you add new documents, restart the app and recreate embeddings.

## File Structure

```
RAG_document_QA/
├── app.py                  # Main application file
├── README.md               # This file
└── research_papers/        # PDF documents directory
    ├── AOYN.pdf
    └── LLMS.pdf
```

## Technologies Used

- **Streamlit**: Web application framework
- **LangChain**: LLM orchestration framework
- **FAISS**: Vector similarity search
- **Groq**: Fast LLM inference
- **Ollama**: Local embedding generation
- **PyPDF**: PDF document loading

## License

This project is for educational and research purposes.

## Contributing

Feel free to submit issues and enhancement requests!

---

**Note**: Make sure Ollama is running before starting the application, and ensure you have a valid Groq API key in your `.env` file.

