import streamlit as st

from data import *
from input import image_input, webcam_input

st.title("Neural Style Transfer")
st.sidebar.title('Navigation')
method = st.sidebar.radio('Go To ->', options=['Webcam', 'Image'])
st.sidebar.header('Options')

style_model_name = st.sidebar.selectbox("Choose the style model: ", style_models_name)

if method == 'Image':
    image_input(style_model_name)
else:
    webcam_input(style_model_name)
