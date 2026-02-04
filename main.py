import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("API_KEY")
)
uploaded_file = st.file_uploader("upload an mp3 file", type=["mp3", "wav", "m4a"])
if uploaded_file:
    bytes_data = uploaded_file.getvalue()
    transcription = client.audio.transcriptions.create(
        file=("uploaded_file.mp3", bytes_data, "audio/mpeg"),
        model="whisper-large-v3-turbo",
        temperature=0,
        response_format="verbose_json",
    )
    for segment in transcription.segments:
        # covert the seconds to minutes:seconds format
        start_minutes = int(segment.get("start") // 60)
        start_seconds = int(segment.get("start") % 60)
        end_minutes = int(segment.get("end") // 60)
        end_seconds = int(segment.get("end") % 60)
        
        st.markdown(f"**[{start_minutes}:{start_seconds:02d} - {end_minutes}:{end_seconds:02d}]** {segment.get('text')}")