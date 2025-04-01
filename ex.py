import streamlit as st

def main():
    st.title("Contact Us")
    
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

if __name__ == '__main__':
    main()
