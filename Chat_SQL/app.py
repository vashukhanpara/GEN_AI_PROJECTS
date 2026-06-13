from urllib.parse import quote_plus
import streamlit as st

# Path handling for SQLite DB file
from pathlib import Path

# LangChain components for SQL agent
from langchain_community.agent_toolkits import create_sql_agent
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_types import AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain.agents.agent_toolkits import SQLDatabaseToolkit

# SQLAlchemy for database engine
from sqlalchemy import create_engine

# SQLite driver
import sqlite3
from langchain_groq import ChatGroq


st.set_page_config(page_title="LangChain: Chat with SQL DB", page_icon="🦜")
st.title("🦜 LangChain: Chat with SQL DB")

LOCALDB = "USE_LOCALDB"
MYSQL = "USE_MYSQL"

# Options for user to choose which database to connect in streamlit sidebar
radio_opt = ["Use SQLLite 3 Database- india.db", "Connect to you MySQL Database"]
selected_opt = st.sidebar.radio(label="Choose the DB which you want to chat", options=radio_opt)

# Collect DB connection info from sidebar
if radio_opt.index(selected_opt) == 1:
    # User wants MySQL
    db_uri = MYSQL
    mysql_host = st.sidebar.text_input("Provide MySQL Host")
    mysql_user = st.sidebar.text_input("MYSQL User")
    mysql_password = st.sidebar.text_input("MYSQL password", type="password")
    mysql_db = st.sidebar.text_input("MySQL database")
else:
    # Default: use local SQLite
    db_uri = LOCALDB

# Get Groq API Key
api_key = st.sidebar.text_input(label="Groq API Key", type="password")

# Basic input validations
if not db_uri:
    st.info("Please enter the database information and URI")

if not api_key:
    st.warning("Please enter your Groq API key in the sidebar.")
    st.stop()

# Initialize Groq LLM with streaming output
llm = ChatGroq(
    groq_api_key=api_key,
    model_name="llama-3.3-70b-versatile",
    streaming=True
)

# Configure the database connection
@st.cache_resource(ttl="2h")  # Cache for 2 hours to avoid reconnecting
def configure_db(db_uri, mysql_host=None, mysql_user=None, mysql_password=None, mysql_db=None):
    if db_uri == LOCALDB:
        # Absolute path to local SQLite database
        dbfilepath = (Path(__file__).parent / "india.db").absolute()
        print("Using SQLite DB at:", dbfilepath)
        # SQLite connection creator
        creator = lambda: sqlite3.connect(f"file:{dbfilepath}?mode=ro", uri=True)
        # Return LangChain SQLDatabase object
        return SQLDatabase(create_engine("sqlite:///", creator=creator))    

    elif db_uri == MYSQL:
        # Clean input strings
        mysql_host = mysql_host.strip()
        mysql_user = mysql_user.strip()
        mysql_password = mysql_password.strip()
        mysql_db = mysql_db.strip()

        if not (mysql_host and mysql_user and mysql_password and mysql_db):
            st.error("Please provide all MySQL connection details.")
            st.stop()

        # URL-encode password to handle special characters
        password_encoded = quote_plus(mysql_password)

        # Construct SQLAlchemy connection URL for MySQL
        engine_url = f"mysql+mysqlconnector://{mysql_user}:{password_encoded}@{mysql_host}/{mysql_db}"
        print("Connecting to MySQL with URL:", engine_url)
        return SQLDatabase(create_engine(engine_url))

# Connect to DB based on user selection
if db_uri == MYSQL:
    db = configure_db(db_uri, mysql_host, mysql_user, mysql_password, mysql_db)
else:
    db = configure_db(db_uri)

# Create LangChain SQL Toolkit
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

# Create LangChain SQL Agent
agent = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

# Initialize chat session
if "messages" not in st.session_state or st.sidebar.button("Clear message history"):
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# Display previous messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Chat input for user queries
user_query = st.chat_input(placeholder="Ask anything from the database")

if user_query:
    # Append user message
    st.session_state.messages.append({"role": "user", "content": user_query})
    st.chat_message("user").write(user_query)

    # Run agent and stream assistant's response
    with st.chat_message("assistant"):
        streamlit_callback = StreamlitCallbackHandler(st.container())
        response = agent.run(user_query, callbacks=[streamlit_callback])
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)


# credentials for mysql connection:localhost:3306, root, password, student_db