import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

st.title('Create short video')

topic = st.text_input("Topic", "Yoga")
#st.write("The topic is", title)

def click_button():
    print("Button clicked")
    url = os.getenv("BACKEND_ENDPOINT") + "/create_video"
    params = {
        "topic": topic
    }

    response = requests.get(url, params=params)
    print(response.text)
    video_file = open('../text-to-video-azure/video.mp4', 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)

st.button("Generate video", type="primary", on_click=click_button)


