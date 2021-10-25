import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""
# Here's a pointless slider
"""

@st.cache
def squared(x):
    return x * x

x = st.slider('x')
st.write(x, 'squared is', squared(x))

"""
# Next is a pointless dataframe
"""

df = pd.read_csv('DB.csv')

st.dataframe(df)

"""
# A pointless plot to go with
"""

fig_1 = plt.figure(figsize=(9, 5))
plt.plot(df['Col1'], df['Col2'])
st.pyplot(fig_1)


"""
Everything is better with Rick, or is it?
"""

st.image('rick.jpg')

filename = st.text_input(label='Enter a file path:', value='C:/Users/danie/Documents/DW/Scheduler/text_simple.txt')
try:
    with open(filename) as input:
        st.text(input.read())
except FileNotFoundError:
    st.error('File not found.')
