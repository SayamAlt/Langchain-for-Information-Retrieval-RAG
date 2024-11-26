from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chat_models.openai import ChatOpenAI
from langserve import add_routes
import os, uvicorn
from langchain_community.llms.ollama import Ollama
from dotenv import load_dotenv

load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

app = FastAPI(
    title="Langchain API",
    version="1.0",
    description="A simple API server"
)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)

model = ChatOpenAI()

llm = Ollama(model='llama2')

prompt1 = ChatPromptTemplate.from_template("Write an article on the topic {topic} in about 100 words.")
prompt2 = ChatPromptTemplate.from_template("Write a poem on the topic {topic} in about 100 words.")

add_routes(
    app,
    prompt1|model,
    path="/article"
)

add_routes(
    app,
    prompt2|llm,
    path="/poem"
)

if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=8000)