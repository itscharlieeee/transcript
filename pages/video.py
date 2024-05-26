import streamlit as st

def video_to_transcript(video_file):
    # Step 1: Convert video to audio
    audio_file = "temp_audio.wav"
    audio = AudioSegment.from_file(video_file, format="mp4")
    audio.export(audio_file, format="wav")
    st.audio(temp_audio.wav, format="audio/wav")

st.title("Transcripción de Video")

st.write("Upload a video file and convert it to a transcript.")
video_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mkv"])
if video_file is not None:
        # Convert video to transcript
        #transcript = video_to_transcript(video_file)
        st.write("Cargado")
        st.video(video_file)
