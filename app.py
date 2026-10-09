import streamlit as st
import joblib

# Load the trained model and vectorizer
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Page settings
st.set_page_config(
    page_title="Spam SMS Classifier",
    page_icon="📩"
)

st.title("📩 Spam SMS Classifier")

st.write(
    "Enter an SMS message below to check whether "
    "it is Spam or Ham (legitimate)."
)

# Message input
message = st.text_area("Enter your SMS message:")

# Prediction button
if st.button("Check Message"):
    if message.strip():
        message_tfidf = vectorizer.transform([message])
        prediction = model.predict(message_tfidf)[0]

        if prediction == "spam":
            st.error("🚨 This message is SPAM!")
        else:
            st.success("✅ This message is HAM (Legitimate).")
    else:
        st.warning("Please enter an SMS message first.")
