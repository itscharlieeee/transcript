import streamlit as st
import whisper
from tempfile import NamedTemporaryFile
import ffmpeg
from openai import OpenAI
client OpenAI()

audio = st.file_uploader("Upload an audio file", type=["mp3"])

if audio is not None:
    with NamedTemporaryFile(suffix="mp3") as temp:
        temp.write(audio.getvalue())
        temp.seek(0)
        model = whisper.load_model("base")   
        audio_file= open("Bienvenida.mp3", "rb")
        transcription = client.audio.transcriptions.create(
           model="whisper-1", 
           file=audio_file
        )

        
        #result = model.transcribe("Bienvenida.mp3")
        #st.write(result["text"])
        st.write(transcription.text)
