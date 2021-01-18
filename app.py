import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image
from streamlit import caching

from neural_style_transfer import *
from data import *
from input import *

st.title("Neural Style Transfer")
st.sidebar.title('Options')

style_model_name = st.sidebar.selectbox("Choose the style model: ", style_models_name)
style_model_path = style_models_dict[style_model_name]

model = get_model_from_path(style_model_path)

image_input(style_model_path)
# webcam_input(model)
