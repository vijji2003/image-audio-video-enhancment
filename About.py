import streamlit as st
import base64

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
    st.title("About This Project")
    
    st.header("Project Overview")
    st.write("""
    This project focuses on enhancing the resolution of images, audio, and video files. By leveraging advanced machine learning techniques, we aim to improve the clarity and quality of various media types.
    """)
    
    st.header("Technology Stack")
    st.write("""
    - **Streamlit**: For building the web interface.
    - **OpenCV**: For image and video processing.
    - **Librosa**: For audio processing.
    - **TensorFlow/Keras**: For implementing deep learning models.
    """)
    
    st.header("Features")
    st.write("""
    - **Image Resolution Enhancement**: Upscale and improve the quality of low-resolution images.
    - **Audio Clarity Improvement**: Reduce noise and enhance the clarity of audio files.
    - **Video Resolution Enhancement**: Enhance the resolution of low-quality videos.
    """)
    
    st.header("How It Works")
    st.write("""
    1. **Image Enhancement**: Utilizes super-resolution techniques to upscale images. This involves using convolutional neural networks (CNNs) trained to predict high-resolution images from low-resolution inputs.
    2. **Audio Enhancement**: Uses noise reduction algorithms and deep learning to improve audio clarity. Techniques like spectral gating and deep neural networks (DNNs) are employed.
    3. **Video Enhancement**: Applies frame-by-frame enhancement using trained models to improve the overall quality of video content.
    """)
    
    st.header("Team/Contributors")
    st.write("""
    - **M.Bhanu Prakash**: Team Leader
    - **P.Thriveni**: Programmer
    - **K.vathsalya**: Programmer
    - **G.Venkateswarlu**: Documentation
    - **V.Manoj Naik**: Documentation
    """)
    