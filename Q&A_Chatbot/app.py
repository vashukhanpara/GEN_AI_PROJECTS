
import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

# Load environment variables if you need them (e.g., LangChain API keys)
load_dotenv()

# LangChain tracing / logging (like OpenAI Langsmith)
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Combined Chatbot with Ollama"


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries."),
        ("user", "Question:{question}")
    ]
)

# Response generation function
def generate_response(question, model_name, temperature):
    
    llm = Ollama(
        model=model_name,
        temperature=temperature
    )
    
    # Output parser converts model output → string
    output_parser = StrOutputParser()
    
    # Chain = Prompt → Model → Output parser
    chain = prompt | llm | output_parser
    
    # Invoke chain with question
    answer = chain.invoke({'question': question})

    return answer



st.title("Combined Chatbot Learning (OpenAI & Ollama Logic)")

st.sidebar.title("Settings")

model_name = st.sidebar.selectbox(
    "Select Open Source Model",
    ["llama3.2:1b",
     "gemma3:1b" ]
)
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)

max_tokens = st.sidebar.slider("Max Tokens (not used for Ollama)", 50, 300, 150)

# Main input
st.write("Go ahead and ask any question:")
user_input = st.text_input("You:")

if user_input:
    response = generate_response(user_input, model_name, temperature)
    st.write(response)
else:
    st.write("Please provide the user input")