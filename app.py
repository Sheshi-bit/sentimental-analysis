
import streamlit as st
from textblob import TextBlob

st.title("🎭 Sentiment Analysis App (TextBlob)")
st.subheader("Enter text and get sentiment instantly")

user_input = st.text_area("Type your review or sentence here...", height=150)

if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        blob = TextBlob(user_input)
        polarity = blob.sentiment.polarity
        sentiment = "Positive 😊" if polarity > 0 else "Negative 😞" if polarity < 0 else "Neutral 😐"
        st.info(f"Polarity Score: {polarity:.2f}")
        st.success(f"Predicted Sentiment: {sentiment}")
