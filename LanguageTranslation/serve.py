import uvicorn
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from langserve import add_routes  # add_routes help to create API's quickly
from dotenv import load_dotenv

load_dotenv()
groq_api_key = os.getenv("GROG_API_KEY")
model = ChatGroq(model="openai/gpt-oss-120b", api_key=groq_api_key)

# Create a prompt template
generic_temp = "Hay, translate the following english text to {language}"
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", generic_temp),
        ("human", "{text}"),
    ]
)

parser = StrOutputParser()
# prompt first, then model, then parser
base_chain = prompt | model | parser

# app definition
app = FastAPI(
    title="Langchain Serve with Groq Model",
    description="This is a simple API to demonstrate the integration of Langchain Serve with Groq Model",
    version="1.0.0",
)

add_routes(
    app,
    base_chain,
    path="/chain",
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
