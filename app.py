import streamlit as st

from neural_style_transfer import get_model_from_path
from data import *
from input import image_input, webcam_input

st.title("Neural Style Transfer")
st.sidebar.title('Navigation')
method = st.sidebar.radio('Go To ->', options=['Image', 'Webcam'])
st.sidebar.header('Options')

style_model_name = st.sidebar.selectbox("Choose the style model: ", style_models_name)
style_model_path = style_models_dict[style_model_name]

model = get_model_from_path(style_model_path)

if method == 'Image':
    image_input(model)
else:
    webcam_input(model)
