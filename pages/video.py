import streamlit as st
from io import BytesIO


def video_to_transcript(video_file):
    # Step 1: Convert video to audio
    buffer = BytesIO()
    audio =video_file.get_audio_only()
    default_filename = audio.default_filename
    audio.stream_to_buffer(buffer)
    st.audio(buffer, format="audio/mpeg")

st.title("Transcripción de Video")

st.write("Upload a video file and convert it to a transcript.")
video_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mkv"])
if video_file is not None:
        # Convert video to transcript
        #transcript = video_to_transcript(video_file)
        #video_to_transcript(video_file)
        st.write("Cargado")
        st.video(video_file)
