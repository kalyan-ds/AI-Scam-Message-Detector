import streamlit as st
import joblib

# Load saved model
model = joblib.load("spam_detector_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Text cleaning function
import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text

# Streamlit UI

st.title("📩 AI Scam Message Detector")

st.write(
    "Enter a message below to check whether it is Spam or Normal."
)

# Input box
message = st.text_area("Enter Message")

# Prediction button
if st.button("Predict"):

    cleaned_msg = clean_text(message)

    vectorized_msg = vectorizer.transform(
        [cleaned_msg]
    )

    prediction = model.predict(
        vectorized_msg
    )

    if prediction[0] == 1:
        st.error("⚠️ Spam Message Detected!")
    else:
        st.success("✅ Normal Message")