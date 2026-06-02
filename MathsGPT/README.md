# 🧮 MathsGPT – AI Math & Reasoning Assistant

<p align="center">
  <img src="https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit">
  <img src="https://img.shields.io/badge/LangChain-Agent-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Groq-LLM-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Wikipedia-Tool-lightgrey?style=for-the-badge">
</p>

---

## ✨ Overview

**MathsGPT** is an AI-powered chatbot that can:

* 🧮 Solve mathematical problems
* 🧠 Answer reasoning questions
* 🌍 Fetch knowledge from Wikipedia

Built using **LangChain + Groq models**, this app provides an interactive **Streamlit chat interface** for real-time problem solving and learning.

---

## 🚀 Key Features

* 💬 **Conversational math solver**
* 🔢 **Accurate numeric answer extraction**
* 🧠 **Logical reasoning assistant**
* 🌍 **Wikipedia integration for knowledge queries**
* ⚡ **Fast inference using Groq LLMs**
* 🎯 **Multi-tool agent using LangChain**

---

## 🏗️ Project Structure

```id="m1k29x"
MathsGPT/
│
├── app.py                # 🚀 Main Streamlit app
├── requirements.txt     # 📦 Dependencies
├── .env                 # 🔐 API keys (optional)
└── README.md            # 📘 Documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash id="k2m91z"
git clone https://github.com/your-username/MathsGPT.git
cd MathsGPT
```

---

### 2️⃣ Create Virtual Environment

```bash id="v8xk12"
python -m venv venv
```

#### ▶ Activate

**Windows**

```bash id="c2k91q"
venv\Scripts\activate
```

**Mac/Linux**

```bash id="p9x2kl"
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash id="z81nq2"
pip install -r requirements.txt
```

---

### 4️⃣ Setup API Key

Create a `.env` file:

```env id="f7k29s"
GROQ_API_KEY=your_api_key_here
```

---

## 🚀 Usage

### ▶ Run the App

```bash id="u29sk1"
streamlit run app.py
```

---

### 💡 Example Queries

```id="x8k21m"
👉 Solve: 25 * 48 + 120
👉 What is the square root of 144?
👉 If a train travels 60 km in 1 hour, what is its speed?
👉 Who is Isaac Newton?
```

---

## ⚙️ Configuration

* Enter your **Groq API key** in sidebar (if not using `.env`)
* Choose a model:

| Model                 | Description      |
| --------------------- | ---------------- |
| `openai/gpt-oss-120b` | Strong reasoning |
| `groq/compound`       | Faster responses |

---

## 🧠 How It Works

```id="l29dk3"
User Input 
   ↓
LangChain Agent
   ↓
[ Math Tool | Reasoning Tool | Wikipedia Tool ]
   ↓
Groq LLM
   ↓
Final Answer (Numeric / Text)
```

---

## 🔍 Core Capabilities

### 🧮 Math Solver

* Extracts and returns **clean numeric answers**
* Avoids unnecessary explanations (optimized output)

### 🧠 Reasoning Engine

* Handles logic, puzzles, and conceptual questions

### 🌍 Wikipedia Tool

* Fetches real-world knowledge dynamically

---

## ⚠️ Notes

* App **requires a valid Groq API key**
* Numeric extraction may simplify complex outputs
* Wikipedia responses depend on internet availability

---

## 🛠️ Future Improvements

* 📊 Step-by-step solution explanations
* 🧾 History of solved problems
* 🎤 Voice input support
* 📱 Mobile-friendly UI enhancements
* 📚 Support for advanced math (calculus, algebra)

---

## 🧑‍💻 Tech Stack

* **Frontend:** Streamlit
* **Backend:** LangChain
* **LLM:** Groq Models
* **Tools:** Wikipedia API, Custom Math Parser

---

## 📄 License

No license included by default.

👉 Recommended: Add **MIT License** for open-source use.

---

## 🤝 Contributing

Contributions are welcome!

```bash id="p82k1x"
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
👉 Build more AI tools 🚀

---

<p align="center">
  Built with ❤️ for learning & problem solving
</p>
