# 🏥 Hospital Chatbot – AI Healthcare Assistant

<p align="center">
  <img src="https://img.shields.io/badge/Model-GPT--2-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/PEFT-LoRA-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/TRL-Fine--Tuning-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Streamlit-UI-red?style=for-the-badge&logo=streamlit">
</p>

---

## ✨ Overview

**Hospital Chatbot** is an AI-powered assistant designed to answer **hospital and healthcare-related queries** using a fine-tuned **GPT-2 model**.

Built with modern LLM tooling, this project demonstrates how to efficiently fine-tune models using **LoRA (Low-Rank Adaptation)** and deploy them with a **Streamlit-based chat interface**.

---

## 🚀 Key Features

* 💬 **Conversational AI for hospital queries**
* 🧠 **Fine-tuned GPT-2 model**
* ⚡ **LoRA (PEFT) for efficient training**
* 🔧 **TRL-based supervised fine-tuning**
* 🌐 **Interactive Streamlit UI**
* 📦 **Pre-trained model checkpoints included**
* 🧪 **Custom healthcare dataset support**

---

## 🏗️ Project Structure

```id="a8k2n1"
Hospital-Chatbot/
│
├── app.py                        # 🚀 Streamlit chatbot UI
├── requirements.txt             # 📦 Dependencies
│
├── data/
│   └── train.json               # 🧪 Training dataset
│
├── models/
│   ├── hospital-chatbot/        # 🔁 Training checkpoints
│   │   ├── checkpoint-2/
│   │   ├── checkpoint-4/
│   │   ├── checkpoint-6/
│   │   ├── checkpoint-40/
│   │   ├── checkpoint-80/
│   │   └── checkpoint-120/
│   │
│   └── hospital-chatbot-model/  # ✅ Final fine-tuned model
│
├── scripts/
│   ├── finetune.py              # 🧠 Training script
│   ├── test.py                  # 🧪 Model testing
│   └── models/                  # (Optional duplicate storage)
│
└── README.md                    # 📘 Documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash id="b3u91k"
git clone https://github.com/your-username/Hospital-Chatbot.git
cd Hospital-Chatbot
```

---

### 2️⃣ Create Virtual Environment

```bash id="n92kqp"
python -m venv venv
```

#### ▶ Activate

**Windows**

```bash id="h29dk2"
venv\Scripts\activate
```

**Mac/Linux**

```bash id="s8xk21"
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash id="p0z92k"
pip install -r requirements.txt
```

> ⚠️ For GPU users: install CUDA-compatible PyTorch

---

## 🧠 Model Training

### 📌 Training Pipeline

* Loads **GPT-2 base model**
* Applies **LoRA (PEFT)** for efficient fine-tuning
* Uses **TRL SFT Trainer**
* Trains on `data/train.json`
* Saves final adapter to `models/hospital-chatbot-model`

---

### ▶ Run Training

```bash id="z19dks"
python scripts/finetune.py
```

---

## 🚀 Usage

### ▶ Run Streamlit App

```bash id="q1mx82"
streamlit run app.py
```

---

### 💡 How It Works

```id="m8c91s"
User Query → GPT-2 + LoRA → Response → Streamlit UI
```

---

### 🧪 Test Model (CLI)

```bash id="w8dn12"
python scripts/test.py
```

---

## 📊 Dataset Format

Your `train.json` should follow this structure:

```json id="t6sk29"
{
  "question": "What are OPD timings?",
  "answer": "OPD is open from 9 AM to 5 PM."
}
```

Training uses formatted prompts:

```id="v72ksl"
### Question:
<question>

### Answer:
<answer>
```

---

## ⚠️ Important Notes

* Ensure model exists in:

  ```
  models/hospital-chatbot-model/
  ```
* LoRA adapters are merged during inference
* Add your own dataset if `train.json` is missing
* GPT-2 has limitations for complex medical reasoning

---

## 🛠️ Future Improvements

* 🧬 Upgrade to LLaMA / Mistral models
* 🌍 Multi-language support
* 🔐 User authentication
* 📊 Admin dashboard for queries
* 🏥 Integration with real hospital APIs

---

## 🧑‍💻 Tech Stack

* **Model:** GPT-2
* **Fine-tuning:** PEFT (LoRA), TRL
* **Framework:** HuggingFace Transformers
* **UI:** Streamlit

---

## 📄 License

This project is currently **unlicensed**.

👉 Recommended: Add **MIT License** before publishing.

---

## 🤝 Contributing

Contributions are welcome!

```bash id="k29d82"
# Fork the repo
# Create a new branch
# Make changes
# Submit a PR 🚀
```

---

## ⭐ Support

If you like this project:

👉 Star ⭐ the repo
👉 Share with others
👉 Build impactful AI apps

---

<p align="center">
  Built with ❤️ for AI in Healthcare
</p>
