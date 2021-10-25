import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image
import json
from tensorflow.keras.applications import EfficientNetB0, EfficientNetB1, EfficientNetB2, \
    EfficientNetB3, EfficientNetB4, EfficientNetB5, EfficientNetB6, EfficientNetB7

"""
# Image Classification
"""

networks = [EfficientNetB0, EfficientNetB1, EfficientNetB2, EfficientNetB3, EfficientNetB4, EfficientNetB5, EfficientNetB6, EfficientNetB7]
networks_string = [network.__name__ for idx, network in enumerate(networks)]
input_size = [224, 240, 260, 300, 380, 456, 528, 600]

network_dict = dict(zip(networks_string, networks))
shape_dict = dict(zip(networks_string, input_size))

network = st.select_slider(label='Network architecture', options=networks_string)


@st.cache
def load_network(network):
    return network_dict[network](weights='imagenet')

model = load_network(network)

with open('imagenet-simple-labels.json') as f:
    labels = json.load(f)

uploaded_file = st.file_uploader('', type="jpg")
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    image = img.resize((shape_dict[network], shape_dict[network]))
    image = np.expand_dims(image, axis=0)

    prediction = model.predict(image)
    prediction = labels[prediction.argmax()]

    caption = 'Model used: {N}\nPrediction: {P}'.format(N=network, P=prediction)
    st.image(img, caption=caption, use_column_width=True)

