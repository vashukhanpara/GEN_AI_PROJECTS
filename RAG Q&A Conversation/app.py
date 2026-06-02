
import streamlit as st
import os
import tempfile

from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# ------------------ ENV ------------------
load_dotenv()

# ------------------ EMBEDDINGS ------------------
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# ------------------ STREAMLIT UI ------------------
st.title("Conversational RAG with Memory 📄💬")

api_key = st.text_input("Enter Groq API Key", type="password")

if api_key:

    llm = ChatGroq(
        groq_api_key=api_key,
        model_name="llama-3.3-70b-versatile"
    )

    session_id = st.text_input("Session ID", value="default_session")

    if "store" not in st.session_state:
        st.session_state.store = {}

    # ------------------ MEMORY FUNCTION ------------------
    def get_session_history(session: str) -> BaseChatMessageHistory:
        if session not in st.session_state.store:
            st.session_state.store[session] = ChatMessageHistory()
        return st.session_state.store[session]

    # ------------------ FILE UPLOAD ------------------
    uploaded_files = st.file_uploader(
        "Upload PDFs",
        type="pdf",
        accept_multiple_files=True
    )

    if uploaded_files:

        documents = []

        for uploaded_file in uploaded_files:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(uploaded_file.getvalue())
                temp_path = tmp.name
   
            loader = PyPDFLoader(temp_path)
            docs = loader.load()
            documents.extend(docs)

        if len(documents) == 0:
            st.error("No text found in PDF ❌")
            st.stop()

        # ------------------ SPLITTING ------------------
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        splits = text_splitter.split_documents(documents)

        if len(splits) == 0:
            st.error("Splitting failed ❌")
            st.stop()

        # ------------------ VECTOR STORE ------------------
        vectorstore = Chroma.from_documents(
            documents=splits,
            embedding=embeddings
        )

        retriever = vectorstore.as_retriever(search_kwargs={"k": 6})

        # ------------------ PROMPT ------------------
        qa_prompt = ChatPromptTemplate.from_messages([
            ("system",
             "You are a helpful assistant.\n\n"
             "Rules:\n"
             "- If user asks to summarize conversation, summarize chat history.\n"
             "- If question is about previous messages, use chat history.\n"
             "- Otherwise use document context.\n"
             "- Give clear and concise answers.\n\n"
             "Document Context:\n{context}"
            ),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}")
        ])

        # ------------------ FORMAT DOCS ------------------
        def format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)

        # ------------------ RAG CHAIN ------------------
        rag_chain = (
            RunnablePassthrough.assign(
                context=lambda x: format_docs(
                    retriever.invoke(x["input"])
                )
            )
            | qa_prompt
            | llm
        )
                          
        # ------------------ MEMORY CHAIN ------------------
        conversational_rag_chain = RunnableWithMessageHistory(
            rag_chain,
            get_session_history,
            input_messages_key="input",
            history_messages_key="chat_history"
        )

        # ------------------ USER INPUT ------------------
        user_input = st.text_input("Ask something:")

        if user_input:

            response = conversational_rag_chain.invoke(
                {"input": user_input},
                config={"configurable": {"session_id": session_id}}
            )

            session_history = get_session_history(session_id)

            st.write("### 🤖 Assistant")
            st.write(response.content)

            st.write("### 🧠 Chat History")
            st.write(session_history.messages)

else:
    st.warning("Enter Groq API Key to continue")