import streamlit as st
import numpy as np
import pandas as pd

"""
# Here's a pointless slider

"""

x = st.slider('x')
st.write(x, 'squared is', x * x)

"""
# Next is a pointless dataframe
"""

df = pd.read_csv('DB.csv')

st.dataframe(df)

"""
Everything is better with Rick, or is it?
"""

st.image('rick.jpg')