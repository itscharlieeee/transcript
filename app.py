from pydub import AudioSegment
from pydub.playback import play
import streamlit as st

st.title("Reproductor de Audio")
# Cargar archivo de audio
uploaded_file = st.file_uploader("Cargar archivo de audio", type=["mp3", "wav"])
if uploaded_file:
        st.audio(uploaded_file, format="audio/mp3")

        # Convertir el archivo cargado a un objeto AudioSegment
        audio_data = AudioSegment.from_file(uploaded_file)

        # Reproducir el audio
st.subheader("Reproducir Audio")
if st.button("Reproducir"):
    play(audio_data)

          
