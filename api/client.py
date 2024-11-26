import requests
import streamlit as st

def get_openai_response(input_text):
    response = requests.post("http://localhost:8000/article/invoke",
                             json={'input':{'topic':input_text}})
    return response.json()['output']['content']

def get_ollama_response(input_text):
    response = requests.post(
        "http://localhost:8000/poem/invoke", 
        json={'input':{'topic':input_text}})
    return response.json()['output']

st.title("Langchain API with OpenAI and Ollama LLama2 Models")
input_text = st.text_input("Write an article on")
input_text2 = st.text_input("Write a poem on")

if input_text:
    st.write(get_openai_response(input_text))

if input_text2:
    st.write(get_ollama_response(input_text2))