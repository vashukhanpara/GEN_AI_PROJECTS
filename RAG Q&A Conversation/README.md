# 💬📄 RAG Q&A Conversation

> A powerful **Conversational AI chatbot** that answers questions from your PDFs using **Retrieval-Augmented Generation (RAG)** with memory.

---

## 🚀 Overview

This project combines **LLMs + Vector Search + Chat Memory** to create a **ChatGPT-like experience for your documents**.

Upload PDFs, ask questions, and get **context-aware answers** — even across multiple turns of conversation.

---

## ✨ Features

🔍 **PDF-based Q&A** — Ask questions from your own documents
🧠 **Conversational Memory** — Remembers previous interactions
⚡ **Fast LLM Responses** — Powered by Groq
📚 **Smart Retrieval** — Uses semantic search (Chroma DB)
📂 **Multi-file Upload** — Supports multiple PDFs
🖥️ **Interactive UI** — Built with Streamlit

---

## 🛠️ Tech Stack

| Layer      | Technology                       |
| ---------- | -------------------------------- |
| UI         | Streamlit                        |
| LLM        | Groq (LLaMA 3.3)                 |
| Embeddings | HuggingFace (`all-MiniLM-L6-v2`) |
| Vector DB  | Chroma                           |
| Framework  | LangChain                        |

---

## 📦 Installation

### 1️⃣ Clone Repo

```bash
git clone <your-repo-url>
cd "RAG Q&A Conversation"
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install streamlit langchain-core langchain-chroma langchain-groq langchain-huggingface langchain-text-splitters langchain-community python-dotenv
```

---

## ⚙️ Configuration

Create `.env` file (optional):

```env
# Example
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

📍 Open in browser:

```
http://localhost:8501
```

---

## 🧑‍💻 How to Use

1. 🔑 Enter your **Groq API Key**
2. 🆔 Provide a **Session ID** (for memory tracking)
3. 📂 Upload one or more **PDF files**
4. 💬 Ask questions related to documents
5. 🧠 View answers + conversation history

---

## 🧠 How It Works

```text
PDF → Text Split → Embeddings → Chroma DB
                         ↓
                  User Question
                         ↓
            Retrieve Relevant Chunks
                         ↓
        + Chat History (Memory)
                         ↓
                  LLM (Groq)
                         ↓
                    Response
```

---

## ⚡ Key Highlights

* 🔄 **Context-aware responses** (not just one-shot Q&A)
* 📊 **Semantic search instead of keyword search**
* 🧠 **Memory-enabled conversations**
* 🚫 No need for OpenAI / paid APIs (uses Groq)

---

## ⚠️ Notes

* PDFs are temporarily stored before processing
* Works best with **text-based PDFs (not scanned images)**
* Ensure **valid Groq API key** is provided

---

## 🔮 Future Enhancements

* 📌 Chat UI (like ChatGPT bubbles)
* 📊 Source citation display
* 📁 Persistent vector DB
* 🌐 Deployment (Streamlit Cloud / Docker)

---

## 📄 License

This project is open-source and free to use.
Modify and build your own AI apps 🚀

---

## ⭐ Support

If you found this useful, give it a ⭐ on GitHub!
