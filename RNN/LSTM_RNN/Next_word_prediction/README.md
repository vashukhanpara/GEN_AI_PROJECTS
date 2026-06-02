# 🚀 Next Word Prediction using LSTM

A deep learning project that predicts the **next word in a sentence** using an LSTM-based neural network. The model is trained on custom text data and deployed with an interactive Streamlit interface.

---

## 📌 Overview

This project demonstrates how to build a **language model** capable of understanding context and predicting the next word in a sequence.

**Key Highlights:**

* LSTM-based sequence modeling
* Text preprocessing & tokenization
* Real-time prediction using Streamlit
* Trained on custom dataset

---

## 🧠 How It Works

1. Input text is converted into numeric sequences using a tokenizer
2. Sequences are padded to match model input length
3. The LSTM model predicts the most probable next word
4. The predicted index is mapped back to a word

---

## 📁 Project Structure

```
├── app.py                         # Streamlit app for prediction
├── another.txt                    # Training dataset
├── tokenizer.pickle               # Saved tokenizer
├── next_word_lstm.h5              # Trained model
├── experiments.ipynb              # Experiment notebook
├── requirements.txt               # Dependencies
```

---

## ⚙️ Setup & Installation

### 1️⃣ Create & Activate Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

After running, open the local URL shown in the terminal and start typing a sentence to get predictions.

---

## 💡 Example

**Input:**

```
Machine learning is
```

**Output:**

```
Machine learning is powerful
```

---

## 📊 Model Details

* Architecture: LSTM (Recurrent Neural Network)
* Type: Word-level prediction
* Framework: TensorFlow / Keras
* Input: Sequence of words
* Output: Next word probability

---

## 🚀 Future Improvements

* Use larger and more diverse datasets
* Implement BiLSTM or Transformer models
* Add temperature sampling for better predictions
* Improve UI/UX of the Streamlit app

---
