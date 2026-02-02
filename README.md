# LangChain + LangServe Translation API

This project exposes a simple translation API using LangChain, LangServe, and a Groq-hosted large language model.

The main FastAPI app is defined in `Data-Ingestion/serve.py` and serves a single runnable chain at the path `/chain`.

---

## 1. What the API does

- Uses a Groq LLM via `langchain_groq.ChatGroq`.
- Wraps it in a LangChain pipeline:
  - `ChatPromptTemplate` with variables `language` and `text`.
  - The model.
  - `StrOutputParser` to return a plain string.
- Exposes this chain as an HTTP API using LangServe.
- Endpoint: `POST /chain/invoke`.
- You send English text and a target language, and it returns the translated text.

The core chain (from `Data-Ingestion/serve.py`):

```python
generic_temp = "Hay, translate the following english text to {language}"
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", generic_temp),
        ("human", "{text}"),
    ]
)

parser = StrOutputParser()
base_chain = prompt | model | parser

add_routes(
    app,
    base_chain,
    path="/chain",
)
```

---

## 2. Prerequisites

1. **Python environment**
   - Python 3.10+ recommended.
   - A virtual environment is strongly recommended.

2. **Dependencies**
   - Install from `requirements.txt` in the repo root:

     ```powershell
     cd "C:\Users\ybalasaraswa\OneDrive - OpenText\Desktop\deep learning\LangChain"
     python -m venv .myvenv
     .\.myvenv\Scripts\activate
     pip install -r requirements.txt
     ```

3. **Groq API key**
   - Sign up at Groq and obtain an API key.
   - Create a `.env` file in the project root (same folder as `requirements.txt`) with:

     ```env
     GROG_API_KEY=your_groq_api_key_here
     ```

   - `serve.py` loads this via `dotenv.load_dotenv()` and uses it to configure `ChatGroq`:

     ```python
     load_dotenv()
     groq_api_key = os.getenv("GROG_API_KEY")
     model = ChatGroq(model="openai/gpt-oss-120b", api_key=groq_api_key)
     ```

---

## 3. Running the server

From the project root, run the FastAPI/LangServe app defined in `Data-Ingestion/serve.py`:

```powershell
cd "C:\Users\ybalasaraswa\OneDrive - OpenText\Desktop\deep learning\LangChain"
.\.myvenv\Scripts\activate
python .\Data-Ingestion\serve.py
```

By default, the app starts on `http://localhost:8000`.

You should see logs similar to:

- Uvicorn starting
- Application startup complete

---

## 4. Using the interactive docs (`/docs`)

1. Open your browser and go to:

   - `http://localhost:8000/docs`

2. You will see the automatically generated Swagger UI.

3. Expand the **POST** endpoint:

   - `/chain/invoke`

4. Click **Try it out**.

5. Replace the default request body with something like:

   ```json
   {
     "input": {
       "language": "French",
       "text": "Artificial intelligence is changing many industries."
     },
     "config": {},
     "kwargs": {}
   }
   ```

6. Click **Execute**.

7. The response body will contain the translated text returned by the chain.

> Note: The Swagger UI may show `"input": "string"` in the schema, but `input` is actually a JSON object. You can safely pass a dict containing `language` and `text` as shown above.

---

## 5. Calling the API from PowerShell

You can also test the API from PowerShell using `Invoke-WebRequest`:

```powershell
$body = @{
  input = @{
    language = "Spanish"
    text     = "Good morning! How are you today?"
  }
  config = @{}
  kwargs = @{}
} | ConvertTo-Json -Depth 5

Invoke-WebRequest `
  -Uri "http://localhost:8000/chain/invoke" `
  -Method POST `
  -ContentType "application/json" `
  -Body $body | Select-Object -ExpandProperty Content
```

Or with `curl` on Windows:

```powershell
curl -X POST "http://localhost:8000/chain/invoke" `
  -H "Content-Type: application/json" `
  -d "{""input"": {""language"": ""German"", ""text"": ""Nice to meet you""}, ""config"": {}, ""kwargs"": {}}"
```

---

## 6. Sample document to translate

You can use this sample English paragraph as a test input for `text`:

> Artificial intelligence (AI) is the field of computer science focused on building systems that can perform tasks that normally require human intelligence. Common applications of AI include language translation, image recognition, virtual assistants, and recommendation engines. Modern AI systems often rely on large datasets and powerful models that learn patterns from data instead of being explicitly programmed for every possible situation. As AI continues to improve, it is becoming an important tool in healthcare, finance, education, and many other industries.

Example request body for translating this to French:

```json
{
  "input": {
    "language": "French",
    "text": "Artificial intelligence (AI) is the field of computer science focused on building systems that can perform tasks that normally require human intelligence. Common applications of AI include language translation, image recognition, virtual assistants, and recommendation engines. Modern AI systems often rely on large datasets and powerful models that learn patterns from data instead of being explicitly programmed for every possible situation. As AI continues to improve, it is becoming an important tool in healthcare, finance, education, and many other industries."
  },
  "config": {},
  "kwargs": {}
}
```

---

## 7. Implementation details (quick reference)

- **Entry point**: `Data-Ingestion/serve.py`
- **Frameworks**:
  - FastAPI
  - LangChain + LangServe
- **Model provider**: Groq via `langchain_groq.ChatGroq`
- **Main chain**: `ChatPromptTemplate` → `ChatGroq` → `StrOutputParser`
- **Exposed route**: `/chain` (invoke via `/chain/invoke`)

If you later add more chains or routes, you can follow the same pattern:

```python
add_routes(app, some_other_chain, path="/another-path")
```

and call them via `POST /another-path/invoke` with the appropriate `input` structure.

