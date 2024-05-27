import streamlit as st
from io import BytesIO
from moviepy.editor import VideoFileClip

mp3_file = "audio.mp3"
def video_to_transcript(video_file):
    # Step 1: Convert video to audio
    video_clip = VideoFileClip("myarchivo.mp4")
    c = video_clip.audio
    # Write the audio to a separate file
    audio_clip.write_audiofile(mp3_file) 
    st.audio("audio.mp3", format="audio/mp3")
    client = OpenAI(api_key=ke)    
    transcription = client.audio.transcriptions.create(
       model="whisper-1", 
       file=audio_clip
    )
    st.write(transcription.text)
    # Close the video and audio clips
    audio_clip.close()
    
    #buffer = BytesIO()
    #audio =video_file.get_audio_only()
    #default_filename = audio.default_filename
    #audio.stream_to_buffer(buffer)
    #st.audio(buffer, format="audio/mpeg")

st.title("Transcripción de Video")

st.write("Upload a video file and convert it to a transcript.")
video_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mkv"])
if video_file is not None:
        file_path = "myarchivo.mp4"
        with open(file_path, "wb") as f:
            f.write(video_file.read())
        st.write("Cargado")
        st.video(video_file)
    
if st.button("Transcribir", type="primary"):
    video_to_transcript(video_file)
   
