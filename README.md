# 🤖 GENAI Projects – End-to-End AI Portfolio

<p align="center">
  <img src="https://img.shields.io/badge/Streamlit-Apps-red?style=for-the-badge&logo=streamlit">
  <img src="https://img.shields.io/badge/LangChain-LLM%20Framework-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Groq-LLM-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/TensorFlow-Deep%20Learning-orange?style=for-the-badge&logo=tensorflow">
  <img src="https://img.shields.io/badge/Ollama-Local%20LLMs-grey?style=for-the-badge">
</p>

---

## ✨ Overview

**GENAI Projects** is a curated collection of **Generative AI and Machine Learning applications** built using modern AI tools and frameworks.

This repository demonstrates:

* 🧠 LLM-powered applications (Groq, LangChain)
* 📊 Deep Learning models (ANN, RNN, LSTM)
* 🔎 AI-powered search & retrieval systems
* 💬 Chatbots (local + cloud-based)
* 📄 Document understanding (RAG)

---

## 🚀 Featured Projects

### 🧠 Machine Learning

* 📉 **Churn Prediction** → Predict customer churn using ANN
* 💰 **Salary Prediction** → Regression model for salary estimation

---

### 💬 Chatbots & Assistants

* 🏥 **Hospital Chatbot** → GPT-2 + LoRA fine-tuned healthcare assistant
* 🤖 **Q&A Chatbot** → Local chatbot using Ollama
* 🧮 **MathsGPT** → AI-powered math reasoning assistant

---

### 🔎 AI Search & Data Apps

* 🌐 **AI Search Engine**

  * Web + Wikipedia + arXiv search
  * LangChain ReAct agent

* 🗄️ **Chat SQL**

  * Query databases using natural language

---

### 📄 RAG & Document AI

* 📚 **RAG Q&A Chatbot**

  * Ask questions from PDFs
  * Uses embeddings + semantic search

---

### 🔁 Deep Learning (RNN/LSTM)

* 🎬 **IMDB Sentiment Analysis**
* ✍️ **Next Word Prediction (LSTM)**
* 🎵 **Song Lyrics Generator**

---

### 📝 Utility AI Apps

* 📄 **Text Summarization**

  * Summarize YouTube videos & websites

---

## 🏗️ Project Structure

```id="3ps9k1"
GENAI_Projects/
│
├── ANN/
│   ├── Churn_prediction/
│   └── Salary_prediction/
│
├── Chat_SQL/
├── Hospital_chatbot/
├── MathsGPT/
├── Q&A_Chatbot/
├── RAG Q&A Conversation/
├── RNN/
│   ├── Simple_RNN/
│   └── LSTM_RNN/
│
├── Search_Engine/
├── Text_Summarization/
└── README.md
```

---

## ⚙️ Getting Started

Each project is **independent** and has its own setup.

### 🔧 General Steps

```bash id="gen1"
# Navigate to any project
cd project_folder

# Create virtual environment
python -m venv .venv

# Activate
.venv\Scripts\activate   # Windows
source .venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py
```

---

## 🧠 How It Works (Overall Architecture)

```id="arch91"
User
  ↓
Streamlit UI
  ↓
LangChain / Custom Logic
  ↓
[ Groq LLM | Ollama | ML Models ]
  ↓
[ APIs | PDFs | Database | Web ]
  ↓
Final Output
```

---

## ⚙️ Technologies Used

### 🧠 AI / ML

* LangChain
* Groq (LLM)
* TensorFlow / Keras
* Scikit-learn

### 💬 LLM Tools

* Ollama (local models)
* ReAct Agents
* RAG pipelines

### 🌐 Data Sources

* DuckDuckGo
* Wikipedia
* arXiv
* PDFs
* YouTube transcripts

### 🖥️ Frontend

* Streamlit

---

## ⚠️ Notes

* Some projects require:

  * 🔑 Groq API key
  * 🧠 Local LLM setup (Ollama)
* Model files may increase repository size
* Performance depends on API & hardware

---

## 🛠️ Future Improvements

* 🌐 Deploy all apps (Streamlit Cloud / AWS)
* 📊 Add dashboards & analytics
* 🔗 Integrate vector databases (FAISS, Pinecone)
* 🧠 Multi-agent workflows
* 📱 Mobile-friendly UI

---

## 📄 License

No global license included.

👉 Recommended: **MIT License**

---

## 🤝 Contributing

Want to contribute?

```bash id="contri91"
# Fork repo
# Create new branch
# Add your project
# Submit PR 🚀
```

---

## ⭐ Support

If you like this repository:

👉 Star ⭐ the repo
👉 Share with others
👉 Build amazing AI projects 🚀

---

<p align="center">
  Built with ❤️ for Generative AI learning
</p>
