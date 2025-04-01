import streamlit as st
import base64

def app():
    st.title('Home')
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
    st.markdown("""
    ## Overview

    This project leverages advanced machine learning algorithms to enhance the resolution and quality of images, audio, and videos. Whether you have a low-resolution image, an audio file with background noise, or a grainy video, our tools can help you improve their clarity and quality.

    ## Features

    - **Image Resolution Enhancement:** Improve the resolution of low-quality images using state-of-the-art deep learning models.
    - **Audio Enhancement:** Reduce noise and enhance the clarity of audio files.
    - **Video Resolution Enhancement:** Upscale and enhance the resolution of videos, making them clearer and more detailed.

    ## How It Works

    1. **Upload Your Media:** Use the upload buttons to select an image, audio, or video file from your device.
    2. **Enhance Media:** Our models will process your file to enhance its quality.
    3. **Download Enhanced Media:** Once the processing is complete, you can download the enhanced version of your file.

    ## Getting Started

    - To enhance an image, go to the **Image Resolution** page.
    - To enhance an audio file, go to the **Audio Enhancement** page.
    - To enhance a video, go to the **Video Resolution** page.

    Simply upload your file on the respective page and let our models do the work. The enhanced file will be available for download once the process is complete.

    ## Why Use Our Tool?

    - **User-Friendly:** Easy to use interface for uploading and downloading media files.
    - **Advanced Technology:** Utilizes cutting-edge machine learning models for high-quality enhancement.
    - **Versatile:** Supports a wide range of file formats for images, audio, and videos.

    """)
