# Text Summarization

A Streamlit app that summarizes text content from a YouTube video or a website URL using Groq and LangChain.

## Features
- Summarizes content from Y# 📝 AI Text Summarizer – YouTube & Website Content

<p align="center">
  <img src="https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit">
  <img src="https://img.shields.io/badge/LangChain-LLM-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Groq-LLM-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Input-YouTube%20%7C%20Website-lightgrey?style=for-the-badge">
</p>

---

## ✨ Overview

**AI Text Summarizer** is a smart application that converts long-form content into concise summaries.

It supports:

* 📺 YouTube videos (via transcript)
* 🌐 Website URLs (via content extraction)

Powered by **LangChain** and **Groq LLM**, it generates a **clean ~300-word summary** in seconds.

---

## 🚀 Key Features

* 📄 **Summarize YouTube videos using transcripts**
* 🌐 **Summarize any website content**
* 🧠 **LLM-powered summarization (Groq)**
* ⚡ **Fast and efficient responses**
* ✅ **URL validation with error handling**
* 🎯 **Clean and structured output**

---

## 🏗️ Project Structure

```
Text_Summarization/
│
├── app.py                # 🚀 Main Streamlit application
├── requirements.txt     # 📦 Dependencies
└── README.md            # 📘 Documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

#### ▶ Activate

**Windows**

```bash
.venv\Scripts\activate
```

**Mac/Linux**

```bash
source .venv/bin/activate
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Add API Key

Enter your **Groq API key** directly in the Streamlit sidebar when running the app.

---

## 🚀 Usage

### ▶ Run the App

```bash
streamlit run app.py
```

---

### 💡 Example Inputs

```
👉 https://www.youtube.com/watch?v=example
👉 https://example.com/blog-post
👉 Any article or documentation URL
```

---

## 🧠 How It Works

```
User Input (URL)
      ↓
URL Validation
      ↓
[ YouTube Transcript | Website Loader ]
      ↓
LangChain Processing
      ↓
Groq LLM (llama-3.3-70b-versatile)
      ↓
300-word Summary
      ↓
Displayed in Streamlit UI
```

---

## ⚙️ Configuration

* Enter API key in sidebar
* Default model:

  ```
  llama-3.3-70b-versatile
  ```
* Modify behavior in `app.py`:

  * Prompt template
  * Summary length
  * Error handling

---

## 🔍 Supported Inputs

### 📺 YouTube

* Extracts transcript using `youtube_transcript_api`
* Works best with videos that have captions

### 🌐 Websites

* Uses `UnstructuredURLLoader`
* Extracts readable content from webpages

---

## ⚠️ Notes

* Requires a valid **Groq API key**
* Some websites may block scraping
* YouTube must have available transcripts
* Errors are handled with user-friendly messages

---

## 🛠️ Future Improvements

* 📊 Bullet-point summaries
* 🌍 Multi-language summarization
* 🧾 Download summary as PDF
* 📱 Mobile-friendly UI
* 🧠 Adjustable summary length

---

## 🧑‍💻 Tech Stack

* **Frontend:** Streamlit
* **Backend:** LangChain
* **LLM:** Groq (`llama-3.3-70b-versatile`)
* **Tools:**

  * youtube_transcript_api
  * UnstructuredURLLoader
  * validators

---

## 📄 License

No license included.

👉 Recommended: **MIT License**

---

## 🤝 Contributing

Contributions are welcome!

```bash
# Fork the repo
# Create a new branch
# Make changes
# Submit PR 🚀
```

---

## ⭐ Support

If you like this project:

👉 Star ⭐ the repo
👉 Share with others
👉 Build more AI tools 🚀

---

<p align="center">
  Built with ❤️ using LLMs
</p>
YouTube transcripts or webpage text
- Uses `langchain_groq` with the `llama-3.3-70b-versatile` model
- Validates URL input and displays user-friendly warnings
- Loads website content with `UnstructuredURLLoader`
- Converts text into a 300-word summary

## Files
- `app.py` - main Streamlit application
- `requirements.txt` - Python dependencies for the project

## Setup
1. Create and activate a Python virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add your Groq API key in the Streamlit sidebar when you run the app.

## Run
From the `Text_Summarization` folder, start the app:
```bash
streamlit run app.py
```

Then open the local URL shown in the terminal.

## Usage
1. Enter a valid Groq API key in the sidebar.
2. Paste a YouTube or website URL into the input field.
3. Click the `Summarize the Content from YT or Website` button.
4. The app fetches the content, summarizes it, and displays the result.

## Notes
- The app supports both YouTube links and general website URLs.
- YouTube content is summarized using transcript data.
- Website pages are loaded via `UnstructuredURLLoader`.
- If content extraction or summarization fails, an error message is shown.

## Requirements
The app relies on the following packages (also listed in `requirements.txt`):
- `streamlit`
- `langchain`
- `langchain_groq`
- `langchain_community`
- `validators`
- `youtube_transcript_api`
- `unstructured`
- `pytube`

Adjust `app.py` if you want to change the model, prompt template, or output handling.
