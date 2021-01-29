import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image
from streamlit import caching
import cv2
import imutils
from neural_style_transfer import style_transfer
from data import *

def image_input(model):
    
    if st.sidebar.checkbox('Upload'):
        content_file = st.sidebar.file_uploader("Choose a Content Image", type=["png", "jpg", "jpeg"])
    else:
        content_name = st.sidebar.selectbox("Choose the content images:", content_images_name)
        content_file = content_images_dict[content_name]

    if content_file is not None:
        content = Image.open(content_file)
        content = np.array(content) #pil to cv
        content = cv2.cvtColor(content, cv2.COLOR_RGB2BGR) 
    else:
        st.warning("Upload an Image OR Untick the Upload Button)")
        st.stop()
     
    WIDTH = st.sidebar.select_slider('QUALITY (May reduce the speed)', list(range(150, 501, 50)), value=200) 
    content = imutils.resize(content, width=WIDTH)
    generated = style_transfer(content, model)
    st.sidebar.image(content, width=300, channels='BGR')
    st.image(generated, channels='BGR', clamp=True)


def webcam_input(model):
    st.header("Webcam Live Feed")
    run = st.checkbox('Run')
    FRAME_WINDOW = st.image([], channels='BGR')
    SIDE_WINDOW = st.sidebar.image([], width=100, channels='BGR')
    camera = cv2.VideoCapture(0)
    WIDTH = st.sidebar.select_slider('QUALITY (May reduce the speed)', list(range(150, 501, 50))) 

    while run:
        _, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        # orig = frame.copy()
        orig = imutils.resize(frame, width=300)
        frame = imutils.resize(frame, width=WIDTH)
        target = style_transfer(frame, model)
        FRAME_WINDOW.image(target)
        SIDE_WINDOW.image(orig)
    else:
        st.warning('Stopped')