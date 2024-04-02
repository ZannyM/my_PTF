import streamlit as st
from PIL import Image
from information import *
import json
from streamlit_lottie import st_lottie
#https://github.com/ZannyM/Myportfolio.git
def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")

st.sidebar.markdown(info['Photo'],unsafe_allow_html=True)


st.title("Hobbies")

file_path_gym = '/home/zannymaholobela/Downloads/Animation - 1712058518157.json'
file_path_reading = '/home/zannymaholobela/Downloads/Animation - 1712058793497.json'
file_path_painting = '/home/zannymaholobela/Downloads/Animation - 1712059173535.json'
file_path_travel = '/home/zannymaholobela/Downloads/Animation - 1712059539579.json'

#read contents of local file
with open(file_path_gym, 'r') as file:
    animation_data1 = json.load(file)

with open(file_path_reading, 'r') as file:
    animation_data2 = json.load(file)

with open(file_path_painting, 'r') as file:
    animation_data3 = json.load(file)

with open(file_path_travel, 'r') as file:
    animation_data4 = json.load(file)

with st.container():
    
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        st_lottie(animation_data1, height=280, key="gym")

    with col2:
        st_lottie(animation_data2, height=280, key="reading")

    with col3:
        st_lottie(animation_data3, height=280, key="painting")

    with col4:
        st_lottie(animation_data4, height=280, key="travel")


 



