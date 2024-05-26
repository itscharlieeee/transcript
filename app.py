import streamlit as st
from tempfile import NamedTemporaryFile
import whisper

st.title("Reproductor de Audio")
# Cargar archivo de audio
uploaded_file = st.file_uploader("Cargar archivo de audio", type=["mp3", "wav"])
if uploaded_file:
        st.audio(uploaded_file, format="audio/mp3")

if uploaded_file is not None:
    with NamedTemporaryFile(suffix="mp3") as temp:
        temp.write(uploaded_file.getvalue())
        temp.seek(0)
        model = whisper.load_model("base")
        result = model.transcribe(temp.name)
        st.write(result["text"])

          
