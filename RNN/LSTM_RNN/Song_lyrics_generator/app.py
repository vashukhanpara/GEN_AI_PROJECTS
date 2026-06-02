import streamlit as st
import numpy as np
import pickle
import os
import re

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# -------------------------------
# Load model + tokenizer
# -------------------------------
model = load_model('song_lyrics_lstm.h5')

with open('lyrics_tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

max_sequence_len = model.input_shape[1] + 1

# -------------------------------
# Artist folder path
# -------------------------------
DATASET_PATH = r"D:\generative AI\RNN\LSTM+RNN\LSTM RNN\archive"

# Get list of artists from filenames
artists = [file.replace(".txt", "") for file in os.listdir(DATASET_PATH) if file.endswith(".txt")]

# -------------------------------
# Sampling function
# -------------------------------
def sample_with_temperature(preds, temperature=1.0):
    preds = np.log(preds + 1e-10) / temperature
    preds = np.exp(preds)
    preds = preds / np.sum(preds)
    return np.random.choice(len(preds), p=preds)

# -------------------------------
# Generate lyrics
# -------------------------------
def generate_lyrics(seed_text, next_words, temperature):
    result = seed_text.lower()

    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([result])[0]

        token_list = pad_sequences(
            [token_list],
            maxlen=max_sequence_len - 1,
            padding='pre'
        )

        preds = model.predict(token_list, verbose=0)[0]
        predicted_index = sample_with_temperature(preds, temperature)

        # Fast lookup (optimized)
        output_word = tokenizer.index_word.get(predicted_index, '')

        if output_word == '':
            continue

        result += ' ' + output_word

    return result

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("🎵 AI Lyrics Generator")

st.write("Generate song lyrics using LSTM")

# Artist selection
selected_artist = st.selectbox("Select Artist", artists)

# Seed text
seed_text = st.text_input("Enter starting words", "i love you")

# Number of words
num_words = st.slider("Number of words", 10, 100, 40)

# Temperature
temperature = st.slider("Creativity (Temperature)", 0.5, 1.5, 1.0)

# Generate button
if st.button("Generate Lyrics"):
    
    # Load selected artist text
    file_path = os.path.join(DATASET_PATH, selected_artist + ".txt")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        artist_text = f.read().lower()
    
    # Clean text (important)
    artist_text = re.sub(r'[^a-zA-Z\s]', '', artist_text)
    
    st.write(f"🎤 Style: {selected_artist}")
    
    output = generate_lyrics(seed_text, num_words, temperature)
    
    st.success(output)