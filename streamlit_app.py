import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()


col1, col2, col3 = st.columns(3)
col2.image(Image.open('nrsvg-clean.png'))

st.header('nae raste')

st.info('We are building simple yet unconventional products that support learning in the long term.')

icon_size = 20

st_button('youtube', 'https://youtube.com/@naeraste', 'Nae Raste YouTube channel', icon_size)
st_button('twitter', 'https://twitter.com/naeraste/', 'Follow me on Twitter', icon_size)
# st_button('whatsapp', 'https://sendfox.com/dataprofessor/', 'Sign up for my Newsletter', icon_size)
