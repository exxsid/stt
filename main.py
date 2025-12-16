import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("API_KEY"))
client = Groq(
    api_key=os.getenv("API_KEY")
)
uploaded_file = st.file_uploader("upload an mp3 file", type=["mp3", "wav"])
if uploaded_file:
    bytes_data = uploaded_file.getvalue()
    transcription = client.audio.transcriptions.create(
        file=("uploaded_file.mp3", bytes_data, "audio/mpeg"),
        model="whisper-large-v3-turbo",
        temperature=0,
        response_format="verbose_json",
    )
    st.write(transcription.text)
