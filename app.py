import pickle
import string
import streamlit as st
from PIL import Image
import webbrowser

global Lrdetect_Model

LrdetectFile = open('model.pckl','rb')
Lrdetect_Model = pickle.load(LrdetectFile)
LrdetectFile.close()
st.title("Language Detection Tool")
input_test = st.text_input("provide your text input here", 'Hello my name is Vishal Lazrus... ')

res = Lrdetect_Model.predict([input_test])

button_clicked = st.button("Get Language Name")
if button_clicked:
	st.text(f'The language "{input_test}" is {res[0]}')
	

st.write(f'This application supports given 17 languages.')


#opening the image
image = Image.open('NLP.png')
#displaying the image on streamlit app
st.image(image, caption='Languages')