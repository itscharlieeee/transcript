import streamlit as st
from tempfile import NamedTemporaryFile
from openai import OpenAI
import os
import whisper
from PIL import Image

if 't_txt' not in st.session_state:
    st.session_state.t_txt = " "

if 'txt_tr' not in st.session_state:
    st.session_state.txt_tr = " "


st.title("Transcriptor de Audio")
image = Image.open('OIG3.jpg')
st.image(image,width=350)


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
    st.write(transcription.text)
    st.session_state.t_txt= transcription.text
if st.button("Traducir con IA",key=3):
       in_lang= "English"   
       out_lang="Spanish"
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
       st.session_state.txt_tr= texto_traducido
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

          
