# 🎬 Simple RNN for IMDB Sentiment Analysis

A clean and beginner-friendly deep learning project that classifies IMDB movie reviews as **positive** or **negative** using a `SimpleRNN` model built with Keras.

---

## 🚀 Overview

This project demonstrates an **end-to-end NLP pipeline**, including:

* Data preprocessing
* Model building
* Training & evaluation
* Deployment with Streamlit

It’s designed for **learning purposes** and helps you understand how Recurrent Neural Networks work on text data.

---

## 🧠 Model Architecture

The model is built using Keras `Sequential` API:

```
Embedding → SimpleRNN → Dense (Sigmoid)
```

* **Embedding Layer** → Converts words into dense vectors
* **SimpleRNN Layer** → Learns sequential patterns in text
* **Dense Layer** → Outputs sentiment (positive/negative)

---

## 📂 Project Structure

```
📁 project-root/
│
├── train_model.py        # Train & save the RNN model
├── main.py               # Streamlit app for predictions
│
├── notebooks/
│   ├── simplernn.ipynb  # Full training walkthrough
│   ├── embedding.ipynb  # Embedding + preprocessing
│   └── prediction.ipynb # Inference examples
│
├── models/
│   ├── simple_rnn_imdb.keras
│   └── simple_rnn_imdb.h5
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🏋️ Train the Model

```bash
python train_model.py
```

This will:

* Load IMDB dataset
* Train the RNN model
* Save the trained model

---

## 💻 Run the Web App

```bash
streamlit run main.py
```

Then:

* Open the local URL in your browser
* Enter a movie review
* Get instant sentiment prediction 🎯

---

## 📊 Dataset Details

* Dataset: IMDB Movie Reviews
* Vocabulary size: **10,000 words**
* Sequence length: **500 tokens (padded)**

---

## ⚠️ Limitations

* `SimpleRNN` struggles with long-term dependencies
* Not suitable for production-grade NLP tasks
* Better alternatives:

  * LSTM
  * GRU
  * Transformer-based models (BERT, etc.)

---

## 🎯 Goal

> Predict whether a movie review expresses a **positive** or **negative** sentiment.

---

