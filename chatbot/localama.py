from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms.ollama import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')
# Langsmith Tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv('LANGCHAIN_API_KEY')

# Prompt Template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the user queries."),
        ("user","Question:{question}")
    ]
)

# Streamlit App
st.title("Langchain API")
text_input = st.text_input("Enter your desired topic:")

llm = Ollama(model='llama2')
output_parser = StrOutputParser()

chain = prompt|llm|output_parser

if text_input:
    st.write(chain.invoke({'question': text_input}))