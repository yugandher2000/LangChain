# Q&A Chatbot with Groq - Tools & Agents Integration

A Streamlit-based chatbot that allows users to interact with various LLM models from Groq, including OpenAI-compatible models, with integrated tools and agents for real-time information retrieval.

## Features

✨ **Runtime API Key Input**: Enter your Groq API key directly in the UI (no need to store in .env file)

🆓 **100% FREE**: All models are hosted on Groq with free API access

🤖 **Multiple Model Selection**: 

### OpenAI Models (Hosted on Groq - FREE):
- **OpenAI GPT OSS 120B** - OpenAI-compatible model with reasoning capabilities

### Meta LLaMA Models (FREE):
- LLaMA 3.3 70B (Versatile - Best all-around)
- LLaMA 3.1 8B (Instant - Fastest responses)
- LLaMA 3.1 70B (Versatile)
- LLaMA 3.2 1B (Preview - Ultra compact)
- LLaMA 3.2 3B (Preview - Compact)

### Mixtral Models (FREE):
- Mixtral 8x7B (32K context window)

### Google Gemma Models (FREE):
- Gemma 2 9B (Instruction-tuned)
- Gemma 7B (Compact)

⚙️ **Configurable Parameters**:
- **Temperature**: Control response randomness (0.0 - 1.0)
- **Max Tokens**: Set maximum response length (100 - 4096)

💬 **Chat Interface**:
- Persistent chat history during session
- Clear chat history option
- User-friendly chat interface
- Model-specific status indicators

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. **Enter your Groq API Key** in the sidebar
   - Get your free API key from: https://console.groq.com/keys
   - No credit card required!

3. Select your preferred model from the dropdown
   - Try the **OpenAI GPT OSS 120B** for OpenAI-compatible experience
   - Or choose LLaMA, Mixtral, or Gemma models

4. Adjust temperature and max tokens as needed

5. Start chatting!

## Configuration

### Sidebar Options

- **API Key**: Enter your Groq API key (required, but FREE)
- **Model Selection**: Choose from 9 different models:
  - OpenAI-compatible: GPT OSS 120B
  - Meta LLaMA: 3.3 70B, 3.1 8B/70B, 3.2 1B/3B
  - Mixtral: 8x7B
  - Google Gemma: 2 9B, 7B
- **Temperature**: Controls creativity (lower = more focused, higher = more creative)
- **Max Tokens**: Maximum length of the response

## Why Groq?

✅ **Completely FREE** - No credit card required
⚡ **Lightning Fast** - Extremely fast inference speeds
🎯 **OpenAI-Compatible Models** - Use `openai/gpt-oss-120b` for OpenAI-like experience
🔄 **Generous Rate Limits** - Suitable for development and testing
🚀 **Production Ready** - Reliable API with good uptime

## Security

- API keys are entered at runtime and not stored in files
- API key input field is password-protected (hidden input)
- No API keys are persisted between sessions

## Requirements

- Python 3.8+
- streamlit
- langchain
- langchain-groq
- langchain-core
- langchain-community
- langchain-classic
- python-dotenv
- arxiv
- wikipedia
- langsmith (optional, for tracing)

## Notes

- The app uses LangChain's ChatGroq integration
- All models (including OpenAI-compatible ones) are accessed through Groq's API
- Optional LangSmith tracking (if LANGCHAIN_API_KEY is set in environment)
- Chat history is maintained during the session but cleared when app is restarted
- **100% FREE** - No payment or credit card required
- OpenAI-compatible models like `openai/gpt-oss-120b` are hosted on Groq infrastructure

