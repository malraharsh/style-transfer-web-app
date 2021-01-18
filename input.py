import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image
from streamlit import caching
import cv2
from neural_style_transfer import *
from data import *

def image_input(model):
    
    if st.sidebar.checkbox('Upload'):
        content_file = st.sidebar.file_uploader("Choose a Content Image", type=["png", "jpg", "jpeg"])
    else:
        content_name = st.sidebar.selectbox("Choose the content images:", content_images_name)
        content_file = content_images_dict[content_name]

    if content_file is not None:
        content = Image.open(content_file)
        st.sidebar.image(content, width=300)
    else:
        st.header("Upload an Image OR Untick the Upload Button)")
        st.stop()
        
    # style_model_name = st.sidebar.selectbox("Choose the style model: ", style_models_name)
    # style_model_path = style_models_dict[style_model_name]
    generated = style_transfer(content, model)
    st.image(generated, width=500)


def webcam_input(model):
    st.title("Webcam Live Feed")
    run = st.checkbox('Run')
    FRAME_WINDOW = st.image([])
    SIDE_WINDOW = st.sidebar.image([])
    camera = cv2.VideoCapture(0)

    while run:
        _, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        frame = imutils.resize(frame, width=300)
        target = style_transfer(frame, model)
        FRAME_WINDOW.image(target)
        SIDE_WINDOW.image(frame)
    else:
        st.warning('Stopped')