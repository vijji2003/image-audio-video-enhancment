import streamlit as st
import base64

def app():
# Custom CSS to style the contact page
    def add_custom_css():
        st.markdown(
           """
           <style>
           body {
              background-color: #f0f2f6;
            }
           .contact-form {
               background-color: #ffffff;
               padding: 20px;
               border-radius: 10px;
               box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);
            }
           .contact-form input, .contact-form textarea {
              width: 100%;
              padding: 10px;
              margin: 10px 0;
              border: 1px solid #ccc;
              border-radius: 5px;
            }
           .contact-form button {
              background-color: #4CAF50;
              color: black;
              padding: 10px 20px;
              border: none;
              border-radius: 5px;
              cursor: pointer;
            }
           .contact-form button:hover {
              background-color: #45a049;
            }
           </style>
           """,
           unsafe_allow_html=True
        )

    # Add custom CSS to the page
    add_custom_css()
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
    
    st.write("""
    ### Welcome to the Image, Audio, and Video Resolution Project
    This project aims to enhance the resolution of images, audio, and video files using advanced machine learning techniques.
    If you have any questions or need support, please fill out the form below or contact us directly at support@resolutionproject.com.
    """)

    st.write("## Contact Form")
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    
    st.write("### Upload Your Files")
    image_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])
    audio_file = st.file_uploader("Upload an Audio File", type=["wav", "mp3"])
    video_file = st.file_uploader("Upload a Video File", type=["mp4", "mov", "avi"])

    if st.button("Submit"):
        if not name or not email or not message:
            st.error("Please fill out all required fields.")
        else:
            st.success("Thank you for your message! We will get back to you soon.")
            # Process the uploaded files and message here

    st.write("## Contact Information")
    st.write("""
    **Email:** support@resolutionproject.com  
    **Phone:** +1 (123) 456-7890  
    **Address:** 123 Resolution St, Imaginary City, IM 12345
    """)