# 🔎 AI Search Engine – Smart Research Assistant

<p align="center">
  <img src="https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit">
  <img src="https://img.shields.io/badge/LangChain-ReAct-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Groq-LLM-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Search-Web%20%7C%20Wiki%20%7C%20arXiv-lightgrey?style=for-the-badge">
</p>

---

## ✨ Overview

**AI Search Engine** is an intelligent research assistant that combines:

* 🌐 Web search (DuckDuckGo)
* 📚 Wikipedia knowledge
* 📄 arXiv research papers

Powered by a **LangChain ReAct agent** and **Groq LLM**, it dynamically decides **when to search, where to search, and how to respond** — just like a real AI researcher.

---

## 🚀 Key Features

* 💬 **Chat-based search interface**
* 🧠 **ReAct-style reasoning agent**
* 🌐 **DuckDuckGo web search integration**
* 📚 **Wikipedia lookup tool**
* 📄 **arXiv research paper search**
* ⚡ **Fast responses using Groq models**
* 🛡️ **Safe fallback handling for tool failures**

---

## 🏗️ Project Structure

```id="p82kx1"
Search_Engine/
│
├── app.py                # 🚀 Main Streamlit application
├── requirements.txt     # 📦 Dependencies
├── .env                 # 🔐 API keys (optional)
└── README.md            # 📘 Documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash id="x91k2m"
git clone https://github.com/your-username/Search_Engine.git
cd Search_Engine
```

---

### 2️⃣ Create Virtual Environment

```bash id="k82mqp"
python -m venv .venv
```

#### ▶ Activate

**Windows**

```bash id="v1k29d"
.venv\Scripts\activate
```

**Mac/Linux**

```bash id="n9k21s"
source .venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash id="z19kqp"
pip install -r requirements.txt
```

---

### 4️⃣ Setup API Key

Create a `.env` file:

```env id="m82kq1"
GROQ_API_KEY=your_api_key_here
```

---

## 🚀 Usage

### ▶ Run the App

```bash id="p92kx8"
streamlit run app.py
```

---

### 💡 Example Queries

```id="l2k91x"
👉 Latest AI research papers on LLMs
👉 Who is Alan Turing?
👉 Current trends in machine learning
👉 Explain quantum computing simply
```

---

## 🧠 How It Works

```id="c29k1x"
User Query
   ↓
LangChain ReAct Agent
   ↓
[ DuckDuckGo | Wikipedia | arXiv ]
   ↓
Groq LLM (ChatGroq)
   ↓
Final Answer
```

---

## ⚙️ Configuration

* Enter your **Groq API key** in sidebar (or `.env`)
* Default model:

  ```
  llama-3.3-70b-versatile
  ```
* Modify tools, prompts, or model inside `app.py`

---

## 🔍 Search Capabilities

### 🌐 Web Search

* Retrieves real-time information using DuckDuckGo

### 📚 Wikipedia

* Provides structured knowledge and explanations

### 📄 arXiv

* Fetches academic papers and research insights

---

## ⚠️ Notes

* Requires a **valid Groq API key**
* Tool failures return safe fallback responses
* Accuracy depends on external search sources

---

## 🛠️ Future Improvements

* 📊 Source citation display
* 🧾 Search history tracking
* 🧠 Multi-step reasoning visualization
* 🌍 Multi-language support
* 📱 Mobile-friendly UI

---

## 🧑‍💻 Tech Stack

* **Frontend:** Streamlit
* **Backend:** LangChain (ReAct Agent)
* **LLM:** Groq (`ChatGroq`)
* **Tools:** DuckDuckGo, Wikipedia, arXiv

---

## 📄 License

No license included by default.

👉 Recommended: Add **MIT License**

---

## 🤝 Contributing

Contributions are welcome!

```bash id="x92k1q"
# Fork the repo
# Create a branch
# Make changes
# Submit PR 🚀
```

---

## ⭐ Support

If you like this project:

👉 Star ⭐ the repo
👉 Share with others
👉 Build smarter AI tools 🚀

---

<p align="center">
  Built with ❤️ for AI-powered research
</p>
