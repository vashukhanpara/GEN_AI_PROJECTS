# 🎵 AI Song Lyrics Generator

🚀 Generate creative song lyrics using Deep Learning (LSTM) + Streamlit UI

---

## ✨ Overview

This project is an **AI-powered lyrics generator** that creates song lyrics based on a given seed text.
It uses an **LSTM (Long Short-Term Memory)** neural network trained on song lyrics to predict the next word and generate sequences.

👉 You can also **choose artist style** and control creativity using temperature sampling.

---

## 🎯 Features

✅ LSTM-based deep learning model
✅ Artist-wise lyric generation
✅ Temperature-based creativity control
✅ Interactive **Streamlit UI**
✅ Real-time lyric generation
✅ Clean and modular project structure

---

## 🧠 How It Works

1. Lyrics dataset is **cleaned & tokenized**
2. Sequences are created using **n-grams**
3. Input is **padded** for equal length
4. LSTM model learns word patterns
5. During generation:

   * Model predicts next word
   * Sampling is applied using **temperature**
   * Words are generated sequentially

---

## 📂 Project Structure

```
Song_lyrics_generator/
│
├── app.py                     # Streamlit web app
├── README.md
├── requirements.txt
│
├── Data/
│   ├── archive/              # Artist-wise lyrics (.txt files)
│   ├── song_lyrics_lstm.h5   # Trained model
│   └── tokenizer.pickle      # Tokenizer
│
└── Notebooks/
    └── song_lyrics_generator.ipynb   # Training & experiments
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd Song_lyrics_generator
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

👉 Activate:

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

## ▶️ Run the App

```bash
python -m streamlit run app.py
```

👉 Open in browser:

```
http://localhost:8501
```

---

## 🎮 How to Use

1. Select an **Artist**
2. Enter a **Seed Text**
3. Choose number of words
4. Adjust **Creativity (Temperature)**
5. Click **Generate Lyrics**

---

## 🔥 Example Output

**Input:**

```
i knew you were
```

**Output:**

```
i knew you were the one that stayed tonight  
holding on to dreams we left behind  
```

---

## 🧪 Model Details

| Feature    | Value                |
| ---------- | -------------------- |
| Model Type | LSTM                 |
| Framework  | TensorFlow / Keras   |
| Input      | Tokenized sequences  |
| Output     | Next word prediction |
| Sampling   | Temperature-based    |

---

## 📦 Tech Stack

* 🧠 TensorFlow / Keras
* 📊 NumPy & Pandas
* 📈 Scikit-learn
* 🎨 Matplotlib
* 🌐 Streamlit
* 🔤 NLTK

---

## 📓 Notebook

Check full training process here:

```
Notebooks/song_lyrics_generator.ipynb
```

Includes:
✔ Data preprocessing
✔ Tokenization
✔ Model training
✔ Evaluation

---

## 🚧 Future Improvements

🔹 Better dataset (clean + large)
🔹 Add punctuation & grammar correction
🔹 Multi-language support
🔹 Genre-based generation
🔹 Download / save lyrics feature
🔹 Deploy on cloud (Streamlit Cloud / AWS)

---

## 💼 Resume Value

This project demonstrates:
✔ Deep Learning (LSTM)
✔ NLP (Text Generation)
✔ Model Deployment (Streamlit)
✔ End-to-End ML Pipeline

---

## 🤝 Contributing

Pull requests are welcome!
Feel free to improve UI, model, or dataset.

---


⭐ **Don’t forget to star the repo if you found it useful!**
