import streamlit as st
from io import BytesIO
from moviepy.editor import VideoFileClip
from openai import OpenAI
import os
#from googletrans import Translator
#from openai import openai
#from gtts import gTTS
from translate import Translator
import time
from pathlib import Path


mp3_file = "audio.mp3"
#translator = Translator()

if 't_txt' not in st.session_state:
    st.session_state.t_txt = " "

if 'txt_tr' not in st.session_state:
    st.session_state.txt_tr = " "

#def text_to_speech(input_language, output_language, text, tld):
#        translation = translator.translate(text, src=input_language, dest=output_language)
#       trans_text = translation.text
#       #tts = gTTS(trans_text, lang=output_language, tld=tld, slow=False)
#        try:
#            my_file_name = text[0:20]
#        except:
#            my_file_name = "audio"
#        #tts.save(f"temp/{my_file_name}.mp3")
#        return my_file_name, trans_text



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
    st.session_state.t_txt=transcription.text
   
            
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
   
display_output_text = st.checkbox("Mostrar el texto")

if st.button("convertir con traductor"):
        
        #result, output_text = text_to_speech(input_language, output_language, text, tld)
        #audio_file = open(f"temp/{result}.mp3", "rb")
        #audio_bytes = audio_file.read()
        #st.markdown(f"## Tú audio:")
        #st.audio(audio_bytes, format="audio/mp3", start_time=0)
     translator = Translator(to_lang="es")
     input_text= st.session_state.t_txt
     max_section_length = 40
     sections = []
     ######sections = [input_text[i:i+40] for i in range(0, len(input_text), 40)]
     while input_text:
            if len(input_text) <= max_section_length:
                sections.append(input_text)
                break
            last_space_index = input_text[:max_section_length].rfind(" ")
            if last_space_index == -1:
                last_space_index = max_section_length
            sections.append(input_text[:last_space_index])
            input_text = input_text[last_space_index:].strip()

     translated_sections = []
     for section in sections:
            translated_text = translator.translate(section)
            translated_sections.append(translated_text)
            time.sleep(0.5)  # Retardo de medio segundo

        # Concatenar las secciones traducidas
     final_text = " ".join(translated_sections)

     st.subheader("Texto Traducido:")
     st.write(final_text)
     # Concatenar las secciones traducidas
     final_text = " ".join(translated_sections)
     st.subheader("Texto Traducido:")
     st.write(final_text)

     #translation = translator.translate(st.session_state.t_txt)
     #st.write(translation)	
     
     if display_output_text:
            st.markdown(f"## Texto de salida:")
            st.write(f" {output_text}")


if st.button("Traducir con IA",key=3):
       in_lang= "en"   
       out_lang="es"
     # Llama a la API de OpenAI para traducir el texto
       client = OpenAI(api_key=ke)  
       response = client.chat.completions.create(
         model="gpt-4o",
         messages=[
           {
             "role": "system",
             "content": f"You will be provided with a text in { in_lang }, and your task is to translate it into {out_lang}."
           },
           {
             "role": "user",
             "content": st.session_state.t_txt
           }
         ],
         temperature=0.7,
         max_tokens=300,
         top_p=1
       )
       texto_traducido = response.choices[0].message.content
       st.session_state.txt_tr=texto_traducido
       st.subheader("Texto traducido:")
       st.write(texto_traducido)
if st.button("Audio traducido",key=4):
  client = OpenAI(api_key=ke)
  #speech_file_path = Path(__file__).parent / "speech.mp3"
  response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input=st.session_state.txt_tr
  )
  response.stream_to_file("trad_text.mp3")
  st.audio("trad_text.mp3", format="audio/mp3") 
    
    
    
