# 🚀 Chat_SQL – Talk to Your Database using AI

<p align="center">
  <img src="https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit">
  <img src="https://img.shields.io/badge/LangChain-Agent-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Groq-LLM-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/SQLite-Database-lightgrey?style=for-the-badge">
</p>

---

## ✨ Overview

**Chat_SQL** is an AI-powered Streamlit application that allows you to **interact with SQL databases using natural language**.

Instead of writing SQL queries manually, you can simply **ask questions in plain English**, and the app will generate and execute queries for you.

---

## 🔥 Key Features

* 💬 **Chat-based SQL interaction**
* ⚡ **Powered by LangChain SQL Agent**
* 🧠 **Groq LLM (LLaMA 3.3) for fast responses**
* 🗃️ **Supports SQLite (default)**
* 🔌 **Optional MySQL database connection**
* 📡 **Streaming responses for real-time experience**
* 🧪 **Prebuilt sample database (`students` table)**

---

## 🏗️ Project Structure

```
Chat_SQL/
│
├── app.py            # 🚀 Main Streamlit application
├── sqlite.py         # 🗄️ Script to create & populate SQLite DB
├── india.db          # 📊 Sample database
├── requirements.txt  # 📦 Dependencies
└── README.md         # 📘 Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Chat_SQL.git
cd Chat_SQL
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

#### ▶ Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Setup Database

```bash
python sqlite.py
```

This will create:

* `india.db`
* `students` table with sample data

---

## 🚀 Usage

### Run the App

```bash
streamlit run app.py
```

---

### 💡 How to Use

1. Open browser → `http://localhost:8501`
2. Enter your **Groq API Key** in sidebar
3. Start asking questions like:

```
👉 Show all students
👉 Who scored more than 80?
👉 Count students by city
👉 Average marks of students
```

---

## 🔌 Database Support

| Database | Status                  |
| -------- | ----------------------- |
| SQLite   | ✅ Default               |
| MySQL    | ✅ Supported via sidebar |

### MySQL Setup

Provide:

* Host
* Username
* Password
* Database Name

---

## 🧠 Tech Stack

* **Frontend:** Streamlit
* **LLM:** Groq (`llama-3.3-70b-versatile`)
* **Framework:** LangChain
* **Database:** SQLite / MySQL

---

## 📸 Demo Flow

```
User Question → LLM → SQL Query → Database → Result → Chat Response
```

---

## ⚠️ Notes

* Default database: `india.db`
* Make sure your **Groq API key is valid**
* MySQL requires proper credentials and network access

---

## 🛠️ Future Improvements

* ✅ PostgreSQL support
* ✅ Query history
* ✅ Download results as CSV
* ✅ Authentication system
* ✅ Dashboard analytics

---

## 📄 License

This project is currently **unlicensed**.

Feel free to add an MIT License if you plan to open-source it.

---

## 🤝 Contributing

Contributions are welcome!

```bash
# Fork the repo
# Create a new branch
# Make changes
# Submit a PR 🚀
```

---

## ⭐ Support

If you like this project:

👉 Star ⭐ the repository
👉 Share with others
👉 Build cool AI apps 🚀

---

<p align="center">
  Made with ❤️ using AI + SQL
</p>
