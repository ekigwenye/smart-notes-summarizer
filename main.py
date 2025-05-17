import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="Smart Notes Summarizer", layout="centered")
st.title("🧠 Smart Notes – AI Text Summarizer")
st.write("Paste your long text below and get a short summary instantly.")

text_input = st.text_area("Enter your text here:", height=300)

if st.button("Summarize"):
    if text_input.strip() == "":
        st.warning("Please enter some text to summarize.")
    else:
        with st.spinner("Summarizing..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant that summarizes text."},
                        {"role": "user", "content": f"Summarize this:\n\n{text_input}"}
                    ]
                )
                summary = response.choices[0].message.content
                st.subheader("Summary:")
                st.success(summary)
            except Exception as e:
                st.error(f"Error: {e}")
