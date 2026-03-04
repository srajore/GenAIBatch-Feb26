import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
#from langchain_ollama import ChatOllama

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

#Page configuration
st.set_page_config(
    page_title="Chatbot with Streamlit and Ollama",
    page_icon="🤖",
)

st.title("Famous Personalities Achievements Chatbot")

st.write("Enter a person's name to get their key achievements in 3 bullet points.")

# Prompt template for the chatbot
prompt = ChatPromptTemplate.from_messages([
('system','You are a helpful AI assistant that provides information about the achievements of famous personalities.'),
('human','Tell me the key achievements of {name} in 3 bullet points.'),
])


#Load LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

chain = prompt | llm


name= st.text_input("Enter the name of a famous personality:")


#Generate button

if st.button("Generate Achievements"):
    if name:
        response = chain.invoke({"name": name})
        st.write(response.content)
    else:
        st.warning("Please enter a name to generate achievements.")

