import streamlit as st
from tempfile import NamedTemporaryFile
import whisper
from openai import OpenAI


st.title("Reproductor de Audio")
ke = st.text_input('Ingresa tu Clave')
os.environ['OPENAI_API_KEY'] = ke

# Cargar archivo de audio
uploaded_file = st.file_uploader("Cargar archivo de audio", type=["mp3", "wav"])
if uploaded_file:
        st.audio(uploaded_file, format="audio/mp3")

if uploaded_file is not None:
    client = OpenAI(api_key=ke)    
    transcription = client.audio.transcriptions.create(
       model="whisper-1", 
       file=uploaded_file
     )
     st.writre(transcription.text)

          
