import streamlit as st
from PIL import Image
import cv2
from moviepy.editor import VideoFileClip
import librosa
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
import base64
import io

def app():
    def set_background(image_file):
        with open(image_file, "rb") as file:
          encoded_string = base64.b64encode(file.read()).decode()
    
        css_code = f"""
        <style>
       .stApp {{
           background-image: url("data:image/png;base64,{encoded_string}");
           background-size: cover;
           background-repeat: no-repeat;
           background-attachment: fixed;
        }}
        </style>
        """
        st.markdown(css_code, unsafe_allow_html=True)

# Call the function to set the background image
    set_background("images.jpeg")

    st.title("Resolution Enhancement for Images, Videos, and Audio")

    option = st.selectbox("Choose the type of media to enhance", ("Image", "Video", "Audio"))

    def enhance_image(input_image,scale_percent=200):
    # Read the input image
      image_np = np.array(image)
      original_width = image_np.shape[1]
      original_height = image_np.shape[0]
    
    # Calculate the new dimensions
      new_width = int(original_width * scale_percent / 100)
      new_height = int(original_height * scale_percent / 100)
    
    # Resize the image
      resized_image = cv2.resize(image_np, (new_width, new_height), interpolation=cv2.INTER_CUBIC)
    
    
    # Upscale the image by a factor of 2
     # enhanced_image_np = cv2.resize(image_np, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    
    # Convert back to PIL format
      enhanced_image = Image.fromarray(resized_image)
      return enhanced_image
    def enhance_video(video_path, scale_factor=2):
      clip = VideoFileClip(video_path)
      upscaled_clip = clip.resize(scale_factor)
      upscaled_clip.write_videofile("upscaled_video.mp4", codec='libx264')
      return "upscaled_video.mp4"
    def enhance_audio(audio_path):
      y, sr = librosa.load(audio_path)
      y_en = librosa.effects.preemphasis(y)
      sf.write("enhanced_audio.wav", y, sr)
      return "enhanced_audio.wav"

    if option == "Image":
       uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
       if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        st.write("")
        st.write("Enhancing...")
        enhance_image = enhance_image(image)
        st.image(enhance_image, caption='Enhanced Image', use_column_width=True)
        


    elif option == "Video":
       uploaded_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])
       if uploaded_file is not None:
         
         with open("temp_video.mp4", "wb") as f:
            f.write(uploaded_file.getbuffer())
         st.video(uploaded_file)
         st.write("")
         st.write("Enhancing...")
         result = enhance_video("temp_video.mp4")
         st.video(result)

    elif option == "Audio":
        uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])
        if uploaded_file is not None:
          with open("temp_audio.wav", "wb") as f:
            f.write(uploaded_file.getbuffer())
          st.audio(uploaded_file)
          st.write("")
          st.write("Enhancing...")
          result = enhance_audio(uploaded_file)
          st.audio(result)
