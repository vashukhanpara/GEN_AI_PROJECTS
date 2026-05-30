# streamlit run main.py

# Step 1: Import Libraries and Load the Model
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model

# Load the IMDB dataset word index
word_index = imdb.get_word_index()
reverse_word_index = {value: key for key, value in word_index.items()}

# Load the pre-trained model with ReLU activation
model = load_model('simple_rnn_imdb.keras')

# Step 2: Helper Functions
# Function to decode reviews
def decode_review(encoded_review):
    return ' '.join([reverse_word_index.get(i - 3, '?') for i in encoded_review])

# Function to preprocess user input
def preprocess_text(text):
    words = text.lower().split()
    encoded_review = [word_index.get(word, 2) + 3 for word in words]
    padded_review = sequence.pad_sequences([encoded_review], maxlen=500)
    return padded_review


import streamlit as st
## streamlit app
# Streamlit app
st.title('IMDB Movie Review Sentiment Analysis')
st.write('Enter a movie review to classify it as positive or negative.')

# User input
user_input = st.text_area('Movie Review')

if st.button('Classify'):

    preprocessed_input=preprocess_text(user_input)

    ## MAke prediction
    prediction=model.predict(preprocessed_input)
    sentiment='Positive' if prediction[0][0] > 0.5 else 'Negative'

    # Display the result
    st.write(f'Sentiment: {sentiment}')
    st.write(f'Prediction Score: {prediction[0][0]}')
else:
    st.write('Please enter a movie review.')




# # main.py
# # streamlit run main.py

# import streamlit as st
# import tensorflow as tf
# from tensorflow.keras.datasets import imdb
# from tensorflow.keras.preprocessing.sequence import pad_sequences
# from tensorflow.keras.models import load_model

# # ===============================
# # App Config
# # ===============================
# st.set_page_config(
#     page_title="IMDB Sentiment Analysis",
#     layout="centered"
# )

# # ===============================
# # Load IMDB word index
# # ===============================
# word_index = imdb.get_word_index()

# # Reserve special tokens
# word_index = {k: (v + 3) for k, v in word_index.items()}
# word_index["<PAD>"] = 0
# word_index["<START>"] = 1
# word_index["<UNK>"] = 2
# word_index["<UNUSED>"] = 3

# reverse_word_index = {v: k for k, v in word_index.items()}

# # ===============================
# # Load trained model
# # ===============================
# @st.cache_resource
# def load_trained_model():
#     return load_model("simple_rnn_imdb.keras")

# model = load_trained_model()

# # ===============================
# # Helper functions
# # ===============================
# def preprocess_text(text, maxlen=500):
#     words = text.lower().split()
#     encoded = [
#         word_index.get(word, word_index["<UNK>"])
#         for word in words
#     ]
#     padded = pad_sequences([encoded], maxlen=maxlen)
#     return padded

# # ===============================
# # Streamlit UI
# # ===============================
# st.title("🎬 IMDB Movie Review Sentiment Analysis")
# st.write(
#     "Enter a movie review and the model will classify it as "
#     "**Positive** or **Negative**."
# )

# user_input = st.text_area(
#     "Movie Review",
#     placeholder="Type your movie review here..."
# )

# if st.button("Classify"):
#     if not user_input.strip():
#         st.warning("⚠️ Please enter a movie review.")
#     else:
#         processed_input = preprocess_text(user_input)
#         prediction = model.predict(processed_input)
#         score = float(prediction[0][0])

#         sentiment = "Positive 😊" if score > 0.5 else "Negative 😞"

#         st.subheader("Result")
#         st.write(f"**Sentiment:** {sentiment}")
#         st.write(f"**Prediction Score:** {score:.4f}")
