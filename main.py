import streamlit as st
from PIL import Image

img1 = Image.open('images/Job.png')
img1.resize((400,400))

st.image(img1)

#streamlit run main.py
