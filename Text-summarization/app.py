import os
from dotenv import load_dotenv
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_groq import ChatGroq
import validators
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load environment variables if they exist
load_dotenv()

# Configure the Streamlit page
st.set_page_config(
    page_title="Content Summarizer",
    page_icon="📝",
    layout="wide"
)

st.title("📝 Web Page Content Summarizer")
st.markdown("Summarize content from web pages using AI")

# Sidebar configuration
with st.sidebar:
    st.header("⚙️ Settings")

    # Check if API key exists in environment, otherwise let user input it
    groq_api_key = os.getenv("GROQ_API_KEY", "")
    user_api_key = st.text_input(
        "Enter Groq API Key",
        value=groq_api_key,
        type="password",
        help="Get your API key from https://console.groq.com"
    )

    st.markdown("---")
    st.markdown("### About")
    st.markdown("This app uses **ChatGroq** to summarize content from:")
    st.markdown("- 🌐 Web pages")

    st.markdown("---")
    st.markdown("### Instructions")
    st.markdown("1. Enter your Groq API key")
    st.markdown("2. Paste a webpage URL")
    st.markdown("3. Click 'Summarize'")

# Main input area
webpage_url = st.text_input("Enter URL (Webpage)", placeholder="https://example.com")
summarize_button = st.button("🚀 Summarize", type="primary")


def check_valid_url(url):
    """Check if the provided URL is valid"""
    return validators.url(url)


def fetch_webpage_content(url):
    """
    Fetch and extract content from a webpage
    Returns the document content or None if it fails
    """
    try:
        st.info("🔄 Loading content from webpage...")
        st.write(f"📎 URL: {url}")

        # Set up the loader with proper headers to avoid being blocked
        content_loader = UnstructuredURLLoader(
            urls=[url],
            ssl_verify=False,
            headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        )

        st.write("🔄 Extracting content...")
        documents = content_loader.load()

        # Check if we actually got content
        if documents and len(documents) > 0:
            page_content = documents[0].page_content if documents[0].page_content else ""
            content_length = len(page_content)
            st.write(f"📏 Content length: {content_length} characters")

            if content_length > 0:
                st.success("✅ Successfully loaded content!")
                return documents
            else:
                st.error("❌ Empty content received from webpage")
                return None
        else:
            st.error("❌ Failed to load content from webpage")
            st.info("💡 Troubleshooting tips:")
            st.info("• Make sure the URL is accessible and public")
            st.info("• Some websites may block automated content extraction")
            st.info("• Try a different webpage")
            return None

    except Exception as error:
        st.error(f"Error loading content: {str(error)}")
        st.info("💡 Troubleshooting tips:")
        st.info("• Verify the URL is correct and accessible")
        st.info("• Some websites have anti-scraping protection")
        st.info("• Try a different webpage (news sites, blogs usually work well)")
        return None


def generate_summary(documents, api_key):
    """
    Generate a summary of the document content using ChatGroq
    Handles large content by chunking if necessary
    """
    try:
        # Set up the language model
        chat_model = ChatGroq(
            api_key=api_key,
            model="llama-3.3-70b-versatile",
            temperature=0
        )

        # Combine all the content from documents
        full_content = "\n\n".join([doc.page_content for doc in documents])

        # Rough estimate: 1 token is about 4 characters
        estimated_token_count = len(full_content) // 4

        st.info(f"📊 Content size: ~{estimated_token_count:,} tokens (~{len(full_content):,} characters)")

        # Check if we need to chunk the content due to rate limits
        # Groq free tier has a 12K tokens per minute limit
        # So we chunk at 8K to be safe and leave room for the prompt
        needs_chunking = estimated_token_count > 8000

        if needs_chunking:
            st.warning("⚠️ Content is large. Using chunked summarization strategy...")

            # Split the content into manageable chunks
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=24000,  # About 6K tokens per chunk
                chunk_overlap=1000,
                length_function=len
            )

            content_chunks = text_splitter.split_text(full_content)
            total_chunks = len(content_chunks)
            st.info(f"📄 Split into {total_chunks} chunks for processing")

            # Process each chunk and collect summaries
            chunk_summaries = []
            progress_bar = st.progress(0)

            for index, chunk in enumerate(content_chunks, start=1):
                st.write(f"Processing chunk {index}/{total_chunks}...")

                # Create a prompt for this chunk
                chunk_summary_prompt = """Summarize the following section of content. Focus on main points and key information:

{chunk_text}

SUMMARY:"""

                prompt = ChatPromptTemplate.from_template(chunk_summary_prompt)
                chain = prompt | chat_model
                response = chain.invoke({"chunk_text": chunk})
                chunk_summaries.append(response.content)

                # Update progress
                progress_bar.progress(index / total_chunks)

            # Now combine all chunk summaries into a final comprehensive summary
            st.write("Creating final comprehensive summary...")
            combined_summaries = "\n\n".join(chunk_summaries)

            final_summary_prompt = """Below are summaries of different sections of a document. 
Please create a cohesive, comprehensive summary that combines all these points:

{summary_text}

FINAL COMPREHENSIVE SUMMARY:"""

            prompt = ChatPromptTemplate.from_template(final_summary_prompt)
            chain = prompt | chat_model
            final_response = chain.invoke({"summary_text": combined_summaries})

            return final_response.content

        else:
            # Content is small enough to summarize in one go
            summary_prompt = """Please provide a comprehensive summary of the following content.
Include the main points, key insights, and important details.
Content:
{text}
SUMMARY:"""

            prompt = ChatPromptTemplate.from_template(summary_prompt)
            chain = prompt | chat_model
            response = chain.invoke({"text": full_content})

            return response.content

    except Exception as error:
        st.error(f"Error during summarization: {str(error)}")

        # Give helpful tips for common errors
        error_message = str(error)
        if "rate_limit_exceeded" in error_message or "413" in error_message:
            st.info("💡 The content is too large. Try:")
            st.info("• A shorter article")
            st.info("• Wait a moment and try again")
            st.info("• The app will automatically chunk large content")

        return None


# Main application flow
if summarize_button:
    # Validation checks
    if not user_api_key:
        st.error("⚠️ Please enter your Groq API key in the sidebar")
    elif not webpage_url:
        st.error("⚠️ Please enter a URL")
    else:
        # Validate the URL format
        if not check_valid_url(webpage_url):
            st.error("⚠️ Invalid URL. Please enter a valid webpage URL")
        else:
            # Start the process
            with st.spinner("Loading content from webpage..."):
                # Try to fetch the webpage content
                page_documents = fetch_webpage_content(webpage_url)

                if page_documents:
                    st.success("✅ Content loaded successfully!")

                    # Show a preview of the content
                    with st.expander("📄 View Original Content Preview"):
                        content = page_documents[0].page_content
                        preview = content[:1000] + "..." if len(content) > 1000 else content
                        st.text(preview)

                    # Generate the summary
                    with st.spinner("Generating summary..."):
                        summary_text = generate_summary(page_documents, user_api_key)

                        if summary_text:
                            st.success("✅ Summary generated!")

                            # Display the summary
                            st.markdown("### 📋 Summary")
                            st.markdown(summary_text)

                            # Show metadata if available
                            if page_documents[0].metadata:
                                st.markdown("---")
                                st.markdown("### 📊 Metadata")
                                for key, value in page_documents[0].metadata.items():
                                    st.markdown(f"**{key.capitalize()}:** {value}")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>Built with ❤️ using LangChain, ChatGroq, and Streamlit</p>
    </div>
    """,
    unsafe_allow_html=True
)

