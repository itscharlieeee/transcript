import streamlit as st
from io import BytesIO
from moviepy.editor import VideoFileClip
from openai import OpenAI
import os

mp3_file = "audio.mp3"
def video_to_transcript(video_file):
    client = OpenAI(api_key=ke)   
    # Step 1: Convert video to audio
    video_clip = VideoFileClip("myarchivo.mp4")
    audio_clip = video_clip.audio
    # Write the audio to a separate file
    audio_clip.write_audiofile(mp3_file) 
    st.audio("audio.mp3", format="audio/mp3")
    #client = OpenAI(api_key=ke) 
    audio_file= open("audio.mp3", "rb")
    transcription = client.audio.transcriptions.create(
       model="whisper-1", 
       file= audio_file
    )
    st.write(transcription.text)
    in_lang = st.selectbox(
        "Selecciona el lenguaje de Entrada",
        ("Inglés", "Español", "Bengali", "Coreano", "Mandarín", "Japonés"),
    )
    if in_lang == "Inglés":
        input_language = "en"
    elif in_lang == "Español":
        input_language = "es"
    elif in_lang == "Bengali":
        input_language = "bn"
    elif in_lang == "Coreano":
        input_language = "ko"
    elif in_lang == "Mandarín":
        input_language = "zh-cn"
    elif in_lang == "Japonés":
        input_language = "ja"
      
    out_lang = st.selectbox(
        "Selecciona el lenguaje de salida",
        ("Inglés", "Español", "Bengali", "Coreano", "Mandarín", "Japonés"),
    )
    if out_lang == "Inglés":
        output_language = "en"
    elif out_lang == "Español":
        output_language = "es"
    elif out_lang == "Bengali":
        output_language = "bn"
    elif out_lang == "Coreano":
        output_language = "ko"
    elif out_lang == "Mandarín":
        output_language = "zh-cn"
    elif out_lang == "Japonés":  
        output_language = "ja"

    english_accent = st.selectbox(
        "Selecciona el acento",
        (
            "Defecto",
            "Español",
            "Reino Unido",
            "Estados Unidos",
            "Canada",
            "Australia",
            "Irlanda",
            "Sudáfrica",
        ),
    )
  
    # Close the video and audio clips
    audio_clip.close()
    


st.title("Transcripción de Video")

ke = st.text_input('Ingresa tu Clave')
os.environ['OPENAI_API_KEY'] = ke

st.write("Carga el video que quieres transcribir.")

video_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mkv"])
if video_file is not None:
        file_path = "myarchivo.mp4"
        with open(file_path, "wb") as f:
            f.write(video_file.read())
        st.write("Cargado")
        st.video(video_file)
    
if st.button("Transcribir", type="primary"):
    video_to_transcript(video_file)
   
