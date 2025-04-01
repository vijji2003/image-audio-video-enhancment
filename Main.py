import streamlit as st
from streamlit_option_menu import option_menu
import base64
import Home,Services,About,Contact

class MultiApp:
    def __init__(self):
        self.apps=[]
    def add_app(self,title,function):
        self.apps.append({
            "title":title,
            "function":function
        })
    def run():
        def set_sidebar_background(image_file):
          with open(image_file, "rb") as file:
            encoded_string = base64.b64encode(file.read()).decode()

            css_code = f"""
            <style>
            [data-testid="stSidebar"] > div:first-child {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            }}
            </style>
            """
            st.markdown(css_code, unsafe_allow_html=True)

# Call the function to set the sidebar background image
        set_sidebar_background("image.jpg")

        def set_navbar_style(background_color, text_color="#FFFFFF"):
          css_code = f"""
          <style>
          .streamlit-topbar {{
          background-color: {background_color};
          color: {text_color};
          }}
          </style>
          """
          st.markdown(css_code, unsafe_allow_html=True)

# Call the function to set navbar background color
          set_navbar_style("#336699")  # Set background color to a shade of blue

        with st.sidebar:
            app = option_menu(
                menu_title='Main-Menu',
                options=['Home','Services','About','Contact'],
                icons=['house-fill','Services','info-circle-fill','person-lines-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    'container':{'padding':'5!important','background-color':'black'},
                    'nav-link':{'color':'white','font-size':'20px','text-align':'left','margin':'0px'},
                    'nav-link-selected':{"background-color":'#02ab21'},
                }            )
        if app=='Home':
            Home.app()
        if app=='Services':
            Services.app()
        if app=='About':
            About.app()
        if app=='Contact':
            Contact.app()
    run()

