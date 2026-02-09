import os

import streamlit as st
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

load_dotenv()

# LangSmith Tracking
if os.getenv("LANGCHAIN_API_KEY"):
    os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
    os.environ['LANGCHAIN_TRACING_V2'] = 'true'
    os.environ['LANGCHAIN_PROJECT'] = "Q&A Chatbot"

# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. please respond to the user queries."),
        ("user", "Question: {question}"),
    ]
)

# Available Groq models for free
GROQ_MODELS = {
    # OpenAI Models (Hosted on Groq - FREE)
    "OpenAI GPT OSS 120B": "openai/gpt-oss-120b",

    # Meta LLaMA Models
    "LLaMA 3.3 70B Versatile": "llama-3.3-70b-versatile",
    "LLaMA 3.1 8B Instant": "llama-3.1-8b-instant",
    "LLaMA 3.1 70B Versatile": "llama-3.1-70b-versatile",
    "LLaMA 3.2 1B Preview": "llama-3.2-1b-preview",
    "LLaMA 3.2 3B Preview": "llama-3.2-3b-preview",

    # Mixtral Models
    "Mixtral 8x7B": "mixtral-8x7b-32768",

    # Google Gemma Models
    "Gemma 2 9B": "gemma2-9b-it",
    "Gemma 7B": "gemma-7b-it",
}


def generate_response(question, api_key, model_name, temperature, max_tokens):
    """Generate response using the selected Groq model"""
    try:
        # Initializing ChatGroq with the selected model (works for all Groq-hosted models)
        llm = ChatGroq(
            api_key=api_key,
            model=model_name,
            temperature=temperature,
            max_tokens=max_tokens
        )

        # Create the chain
        output_parser = StrOutputParser()
        chain = prompt | llm | output_parser

        # Generate response
        response = chain.invoke({"question": question})
        return response
    except Exception as e:
        return f"Error: {str(e)}"


# Streamlit UI
st.set_page_config(page_title="Q&A Chatbot with Groq", page_icon="🤖")
st.title("🤖 Q&A Chatbot with Groq")
st.write("Ask me anything! All models are **FREE** via Groq API.")

# Sidebar for configuration
with st.sidebar:
    st.header("⚙️ Configuration")

    # API Key input
    st.subheader("🔑 API Key")
    st.info("💡 All models are FREE with Groq!")
    api_key_input = st.text_input(
        "Enter your Groq API Key:",
        type="password",
        help="Get your free API key from https://console.groq.com/keys"
    )

    # Model selection
    st.subheader("🤖 Model Selection")
    selected_model_display = st.selectbox(
        "Choose a model:",
        options=list(GROQ_MODELS.keys()),
        index=0,
        help="All models are hosted on Groq and are FREE to use"
    )
    selected_model = GROQ_MODELS[selected_model_display]

    # Show model info
    if "openai" in selected_model.lower():
        st.success("🎯 OpenAI-compatible model hosted on Groq (FREE)")
    elif "llama" in selected_model.lower():
        st.success("🦙 Meta LLaMA model (FREE)")
    elif "mixtral" in selected_model.lower():
        st.success("🔀 Mixtral model (FREE)")
    elif "gemma" in selected_model.lower():
        st.success("💎 Google Gemma model (FREE)")

    # Temperature slider
    st.subheader("Parameters")
    temperature = st.slider(
        "Temperature:",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1,
        help="Controls randomness. Lower = more focused, Higher = more creative"
    )

    # Max tokens slider
    max_tokens = st.slider(
        "Max Tokens:",
        min_value=100,
        max_value=4096,
        value=1024,
        step=100,
        help="Maximum length of the response"
    )

    st.divider()
    st.caption("💡 Tip: Higher temperature = more creative responses")

# Main chat interface
st.subheader("💬 Chat")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
user_question = st.chat_input("Type your question here...")

if user_question:
    # Check if API key is provided
    if not api_key_input:
        st.error("⚠️ Please enter your Groq API key in the sidebar to continue.")
    else:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_question})

        # Display user message
        with st.chat_message("user"):
            st.write(user_question)

        # Generate and display assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = generate_response(
                    question=user_question,
                    api_key=api_key_input,
                    model_name=selected_model,
                    temperature=temperature,
                    max_tokens=max_tokens
                )
                st.write(response)

        # Add assistant message to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

# Clear chat button
if st.session_state.messages:
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.rerun()
