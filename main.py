import streamlit as st
import openai

# Configure page
st.set_page_config(page_title="Smart Notes Summarizer", layout="centered")

# Title
st.title("🧠 Smart Notes – AI Text Summarizer")
st.write("Paste your long text below and get a short summary instantly.")

# API key from Streamlit Secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Input area
text_input = st.text_area("Enter your text here:", height=300)

# Only run when button is clicked
if st.button("Summarize", use_container_width=True):
    if not text_input.strip():
        st.warning("Please enter some text to summarize.")
    else:
        try:
            with st.spinner("Summarizing..."):
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant that summarizes text."},
                        {"role": "user", "content": f"Summarize this:\n\n{text_input}"}
                    ]
                )
                summary = response.choices[0].message.content.strip()
            st.subheader("Summary:")
            st.success(summary)
        except Exception as e:
            st.error(f"Error: {str(e)}")
