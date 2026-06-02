
import streamlit as st
import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from langchain.tools import Tool
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler

load_dotenv()

# SAFE TOOL FUNCTIONS 
def safe_wiki(query):
    try:
        return wiki.run(query)
    except Exception:
        return "Wikipedia not available"

def safe_arxiv(query):
    try:
        return arxiv.run(query)
    except Exception:
        return "Arxiv not available"

def safe_search(query):
    try:
        return search.run(query)
    except Exception:
        return "Search not available"

# TOOLS
arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)

wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
wiki = WikipediaQueryRun(api_wrapper=wiki_wrapper)

search = DuckDuckGoSearchRun()

tools = [
    Tool(name="Search", func=safe_search, description="Search the web"),
    Tool(name="Wikipedia", func=safe_wiki, description="Search Wikipedia"),
    Tool(name="Arxiv", func=safe_arxiv, description="Search research papers"),
]

# STREAMLIT UI
st.title("🔎 LangChain - Chat with search")

st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your Groq API Key:", type="password")

# CHAT HISTORY
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi, I'm a chatbot who can search the web. How can I help you?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# USER INPUT

if prompt := st.chat_input("Ask anything..."):

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    if not api_key:
        st.warning("Please enter Groq API key")
        st.stop()

    # LLM
    llm = ChatGroq(
        groq_api_key=api_key,
        model_name="llama-3.3-70b-versatile",
        temperature=0,
        streaming=True
    )

    # AGENT
    prompt_template = hub.pull("hwchase17/react")
    final_prompt = f"""
    Answer the question.
    
    IMPORTANT:
    - Follow EXACT format: Action + Action Input
    - Do NOT skip Action Input
    - Use tools at most 1-2 times
    - If simple question, answer directly
    
    Question: {prompt}
    """

    agent = create_react_agent(llm, tools, prompt_template)

    agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True,
    max_iterations=5,              # increase slightly
    early_stopping_method="force",
    return_intermediate_steps=False   

)

    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)

        response = agent_executor.invoke(
            {"input": prompt},
            {"callbacks": [st_cb]}
        )

        output = response["output"]

        st.session_state.messages.append({"role": "assistant", "content": output})
        st.write(output)