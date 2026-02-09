# LangChain Projects Repository

A comprehensive collection of LangChain-based applications demonstrating various AI-powered use cases including chatbots, document Q&A, language translation, and more.

---

## 📁 Repository Structure

This repository contains multiple independent projects, each showcasing different LangChain capabilities:

```
LangChain/
├── IntroSection/              # LangChain basics and middleware concepts
├── Building-chatBot/          # Basic chatbot implementation
├── E2E_QA_ChatBot/           # End-to-end Q&A chatbot with multiple models
├── LanguageTranslation/      # Translation API with LangServe
└── RAG_document_QA/          # RAG-based document question answering
```

---

## 🚀 Projects Overview

### 1. **IntroSection** - LangChain Fundamentals
Introduction to LangChain concepts, basic chains, and middleware patterns.

**Contents:**
- `LangchainIntro.ipynb` - Getting started with LangChain
- `Middlewares.ipynb` - Understanding LangChain middlewares

---

### 2. **Building-chatBot** - Basic ChatBot
Simple chatbot implementation demonstrating core LangChain chat functionality.

**Contents:**
- `ChatBot.ipynb` - Basic chatbot notebook

---

### 3. **E2E_QA_ChatBot** - Multi-Model Q&A Chatbot
A fully-featured Streamlit chatbot supporting multiple AI models from Groq - all 100% FREE!

**Features:**
- ✅ **9 Different Models**: OpenAI-compatible, LLaMA, Mixtral, Gemma
- ✅ **Runtime API Key Input**: No .env file needed
- ✅ **Configurable Parameters**: Temperature, max tokens
- ✅ **Persistent Chat History**: Session-based conversations

**Quick Start:**
```powershell
cd E2E_QA_ChatBot
streamlit run app.py
```

**Models Available:**
- OpenAI GPT OSS 120B (OpenAI-compatible)
- Meta LLaMA 3.3 70B, 3.1 8B/70B, 3.2 1B/3B
- Mixtral 8x7B
- Google Gemma 2 9B, 7B

📖 **[Full Documentation](E2E_QA_ChatBot/README.md)**

---

### 4. **LanguageTranslation** - Translation API
A FastAPI-based translation service using LangChain and LangServe.

**Features:**
- 🌐 **Multi-language Translation**: English to any language
- ⚡ **REST API**: FastAPI with automatic Swagger docs
- 🔗 **LangServe Integration**: Easy-to-use API routes

**Quick Start:**
```powershell
cd LanguageTranslation
python serve.py
```

**API Endpoint:**
- `POST http://localhost:8000/chain/invoke`

**Example Request:**
```json
{
  "input": {
    "language": "French",
    "text": "Hello, how are you?"
  },
  "config": {},
  "kwargs": {}
}
```

**Interactive Docs:** `http://localhost:8000/docs`

---

### 5. **RAG_document_QA** - Document Q&A with RAG
Retrieval-Augmented Generation application for asking questions about PDF documents.

**Features:**
- 📄 **PDF Processing**: Automatic document loading and chunking
- 🔍 **Semantic Search**: FAISS vector store for similarity search
- 🤖 **AI-Powered Answers**: Groq ChatGroq model with context
- 💾 **Ollama Embeddings**: Local embeddings generation
- 📊 **Context Display**: View source chunks used for answers

**Quick Start:**
```powershell
cd RAG_document_QA
# Make sure Ollama is running: ollama serve
streamlit run app.py
```

**Prerequisites:**
- Ollama installed and running
- PDF documents in `research_papers/` folder
- Groq API key

📖 **[Full Documentation](RAG_document_QA/README.md)**

---

## 🛠️ Setup & Installation

### Prerequisites
- **Python 3.8+** (3.10+ recommended)
- **Ollama** (for RAG_document_QA project)
- **Groq API Key** (get it FREE at [console.groq.com](https://console.groq.com))

### Installation Steps

1. **Clone or navigate to the repository:**
   ```powershell
   cd "C:\Users\LangChain"
   ```

2. **Create and activate a virtual environment:**
   ```powershell
   python -m venv .myvenv
   .\.myvenv\Scripts\activate
   ```

3. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   
   Create a `.env` file in the project root:
   ```env
   GROG_API_KEY=your_groq_api_key_here
   GROQ_API_KEY=your_groq_api_key_here
   ```
   
   > Note: Some projects use `GROG_API_KEY` and others use `GROQ_API_KEY`

5. **Install Ollama (for RAG project):**
   - Download from [ollama.ai](https://ollama.ai)
   - Pull required model: `ollama pull llama3.1`

---

## 📦 Dependencies

Core packages used across projects:
- **LangChain** - Framework for LLM applications
- **LangServe** - API deployment for LangChain
- **LangChain-Groq** - Groq model integration
- **Streamlit** - Web UI framework
- **FastAPI** - REST API framework
- **FAISS** - Vector similarity search
- **Ollama** - Local embeddings
- **PyPDF** - PDF processing

Install all dependencies:
```powershell
pip install -r requirements.txt
```

---

## 🎯 Quick Start Guide

### For Chatbots (E2E_QA_ChatBot):
```powershell
cd E2E_QA_ChatBot
streamlit run app.py
# Enter Groq API key in UI
```

### For Translation API (LanguageTranslation):
```powershell
cd LanguageTranslation
python serve.py
# Visit http://localhost:8000/docs
```

### For Document Q&A (RAG_document_QA):
```powershell
# Start Ollama first
ollama serve

# In another terminal
cd RAG_document_QA
streamlit run app.py
```

---

## 🔑 API Keys

All projects use **Groq** models, which are:
- ✅ **100% FREE** - No credit card required
- ⚡ **Lightning Fast** - Extremely fast inference
- 🔄 **Generous Limits** - Suitable for development and production

Get your free API key: [console.groq.com/keys](https://console.groq.com/keys)

---

## 📖 Documentation

Each project has its own detailed README:
- [E2E_QA_ChatBot Documentation](E2E_QA_ChatBot/README.md)
- [RAG_document_QA Documentation](RAG_document_QA/README.md)

---

## 🤝 Contributing

Feel free to explore, modify, and extend these projects for your own use cases.

---

## 📝 Notes

- Projects are independent and can be run separately
- Shared dependencies are in the root `requirements.txt`
- Environment variables can be set globally in root `.env`
- Each project may have specific setup requirements (see individual READMEs)

---

## 🐛 Troubleshooting

**Common Issues:**

1. **Import errors:** Make sure virtual environment is activated and dependencies are installed
2. **API key errors:** Check `.env` file exists with correct key names
3. **Ollama errors:** Ensure Ollama is running with `ollama serve`
4. **Port conflicts:** Change ports in respective app files if 8000/8501 are in use

---

