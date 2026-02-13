# 📝 Web Page Content Summarizer

A powerful content summarization application that uses ChatGroq AI to summarize content from web pages through simple URL inputs.

## 🌟 Features

- **Web Page Summarization**: Summarize content from any web page URL
- **AI-Powered**: Leverages ChatGroq's LLaMA 3.3 70B model for intelligent summarization
- **User-Friendly Interface**: Built with Streamlit for an intuitive web interface
- **Content Preview**: View original content before summarization
- **Metadata Display**: Shows additional information about the source (for YouTube videos)

## 🛠️ Technologies Used

- **LangChain**: Framework for building LLM applications
- **ChatGroq**: Fast AI inference using Groq's LPU
- **Streamlit**: Web application framework
- **Python-dotenv**: Environment variable management
- **Validators**: URL validation
- **UnstructuredURLLoader**: Extract web page content

## 📋 Prerequisites

- Python 3.8 or higher
- Groq API Key (get it from [Groq Console](https://console.groq.com))

## 🚀 Installation

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd Text-summarization
   ```

2. **Install required dependencies**:
   ```bash
   pip install -r ../requirements.txt
   ```

3. **Get your Groq API Key**:
   - Visit [Groq Console](https://console.groq.com)
   - Sign up or log in
   - Create a new API key
   - Keep it ready for the next step

## 💻 Usage

1. **Run the Streamlit application**:
   ```bash
   streamlit run app.py
   ```

2. **Access the application**:
   Open your browser and navigate to `http://localhost:8501`

3. **Enter your Groq API Key**:
   - **Required**: Enter your API key in the sidebar input field
   - The key is used at runtime and not stored permanently
   - Alternatively, you can set it in a `.env` file (optional):
     ```
     GROQ_API_KEY=your_groq_api_key_here
     ```

4. **Summarize content**:
   - Paste a web page URL
   - Click the "🚀 Summarize" button
   - View the generated summary

## 📝 Example URLs to Try

### Web Pages:
- Any valid web page URL (e.g., `https://example.com/article`)
- News articles from CNN, BBC, etc.
- Blog posts
- Technical documentation

## 🏗️ Project Structure

```
Text-summarization/
│
├── app.py              # Main Streamlit application
├── README.md           # Project documentation
└── .env               # Environment variables (not tracked by git)
```

## 🔑 Key Functions

### `is_valid_url(url)`
Validates URL format.

### `load_content(url)`
Loads content from the provided web page URL.

### `summarize_content(docs, api_key)`
Generates a comprehensive summary using ChatGroq AI.

## ⚙️ Configuration

The app uses the following ChatGroq configuration:
- **Model**: `llama-3.3-70b-versatile` (Meta's LLaMA 3.3 70B)
- **Context Window**: 128,000 tokens (massive context!)
- **Temperature**: `0` (for consistent, deterministic outputs)
- **Auto-chunking**: Enabled for content > 30,000 tokens (rare with 128K context!)

You can modify these settings in the `summarize_content()` function.

## 🔒 Security Notes

- **API keys are entered at runtime** through the Streamlit UI for maximum security
- Keys are stored only in the browser session and never saved to disk
- Optionally, you can use a `.env` file for development (already in `.gitignore`)
- Never commit your `.env` file or expose your API keys in code
- The UI input field is password-protected (hidden text)

## 🐛 Troubleshooting

### Common Issues:

1. **"Invalid API Key" error**:
   - Verify your Groq API key is correct
   - Check that the key is properly set in .env or entered in the sidebar

2. **Web page not loading**:
   - Some websites may block automated content extraction
   - Try a different URL or check your internet connection
   - News sites and blogs usually work well

3. **Module not found errors**:
   - Ensure all dependencies are installed: `pip install -r ../requirements.txt`

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements.

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Built with [LangChain](https://www.langchain.com/)
- Powered by [Groq](https://groq.com/)
- UI created with [Streamlit](https://streamlit.io/)

## 📧 Support

For issues or questions, please open an issue in the repository or contact the maintainer.

---

**Built with ❤️ using LangChain, ChatGroq, and Streamlit**

