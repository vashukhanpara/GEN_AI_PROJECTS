# 🤖 Q&A Chatbot

A simple yet powerful **Streamlit-based chatbot** built using **LangChain** and **Ollama** for local, open-source LLM inference.

---

## 🚀 Features

✨ Interactive chatbot UI with Streamlit
🧠 Supports multiple Ollama models
🎛️ Adjustable temperature for response control
🔗 Built with LangChain prompt templates
⚡ Fast, local inference (no API required)

---

## 🛠️ Tech Stack

* **Python 3.10+**
* **Streamlit**
* **LangChain**
* **Ollama (Local LLMs)**
* **python-dotenv**

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone <your-repo-url>
cd Q-A-Chatbot
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
```

Activate:

* Windows:

```bash
venv\Scripts\activate
```

* Mac/Linux:

```bash
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install streamlit langchain-core langchain-community python-dotenv
```

---

## ⚙️ Configuration

Create a `.env` file (optional):

```env
# Add environment variables if needed
```

The app internally sets:

```python
LANGCHAIN_TRACING_V2 = true
LANGCHAIN_PROJECT = "Ollama Chatbot"
```

---

## ▶️ Usage

Run the app:

```bash
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## 🧠 Supported Models

Select from sidebar:

* `llama3.2:1b`
* `gemma3:1b`

💡 Make sure models are pulled via Ollama:

```bash
ollama pull llama3.2:1b
ollama pull gemma3:1b
```

---

## 🎛️ Controls

* **Temperature** → Controls creativity
* **Model Selector** → Switch between LLMs
* **Max Tokens** → (UI only, not active yet)

---

## ⚠️ Notes

* Requires **Ollama running locally**
* No external API calls (fully local)
* `max_tokens` is currently not used

---

## 📌 Future Improvements

* Add chat history memory
* Streaming responses
* File/document Q&A
* API integration

---

## 📄 License

This project is open-source and free to use.
Feel free to modify and build upon it 🚀

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
