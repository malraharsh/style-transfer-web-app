import numpy as np
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
from PIL import Image
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
    WIDTH = st.sidebar.select_slider('QUALITY (May reduce the speed)', list(range(150, 501, 50)))

    class NeuralStyleTransferTransformer(VideoTransformerBase):
        def transform(self, frame):
            image = frame.to_ndarray(format="bgr24")
            orig_h, orig_w = image.shape[0:2]

            input = imutils.resize(image, width=WIDTH)

            transferred = style_transfer(input, model)

            result = cv2.resize((transferred * 255).astype(np.uint8), (orig_w, orig_h))
            return result

    webrtc_streamer(key="neural-style-transfer", video_transformer_factory=NeuralStyleTransferTransformer)
