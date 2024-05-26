import streamlit as st
import whisper
from tempfile import NamedTemporaryFile

audio = st.file_uploader("Upload an audio file", type=["mp3"])

if audio is not None:
    with NamedTemporaryFile(suffix="mp3") as temp:
        temp.write(audio.getvalue())
        temp.seek(0)
        model = whisper.load_model("base")
        result = model.transcribe(temp.name)
        st.write(result["text"])
