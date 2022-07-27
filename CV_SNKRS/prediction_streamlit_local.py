#py -m streamlit run .\prediction_streamlit.py

import streamlit as st
import time

import urllib.request
import numpy as np

# my_bar = st.progress(0)

# for percent_complete in range(100):
#      time.sleep(0.02)
#      my_bar.progress(percent_complete + 1)


# with st.spinner('Wait for it...'):
#     time.sleep(5)
# st.success('Done!')
tabs1, tabs2 = st.tabs(["Project", "Test it"])

tabs1.title("Nike Sneakers prediction")
tabs1.header("By computer vision")
tabs1.write("Created by [axelooc59(Github link)](https://github.com/axelooc59)")
tabs1.write("In this page you can predict what is the type of the Nike sneakers you want.")
tabs1.write("This is possible with a neural Network which was trained over 700 pictures.")
tabs1.write("This model has an accurancy of 82%, namely it predict correctly 82 times in mean every 100 pictures.")
tabs1.write("Find detail of this project in my github at this  [link](https://github.com/axelooc59/Detecting-type-of-sneakers-shoes-by-ML-).")





tabs1.warning("You must provide a picture with a white background pointing to the left (see below)")
from PIL import Image

urllib.request.urlretrieve(
  'https://media.restocks.net/products/555088-105/air-jordan-1-retro-high-dark-mocha-1-400.png',
   "image.png")
image = Image.open('image.png')
tabs1.image(image,caption="Expected picture format")

pic=None

from PIL import Image



with st.spinner('Loading...'):

   #pic= st.file_uploader('',type=['png','jpeg'])
   import cv2
   from tkinter import filedialog as fd
   from tensorflow.keras.models import Model
   from tensorflow import keras
   import matplotlib.pyplot as plt
   #download model in a temp file
   
   model = keras.models.load_model('model_CNN')
   if tabs2.button('Upload a picture'):
      filename = fd.askopenfilename()

     
      if filename is not None:
         image2 = Image.open(filename)
         tabs2.image(image2,caption="Picture to predict")
         # image = Image.open(pic)
         # img_array = np.array(image)
         type= ['Dunk high', 'Dunk low', 'Jordan 1 high', 'Jordan 1 low', 'Jordan 1 mid', 'Jordan 3', 'Jordan 4']

         
         ##prediction 
         

         #st.write(pic)
         

         image_to_predict = cv2.imread(filename,cv2.IMREAD_COLOR)
         
         
         img_to_predict = np.expand_dims(cv2.resize(image_to_predict,(200,200)), axis=0)
         
         res1 = model.predict(img_to_predict)
         res=np.argmax(res1) 
         tabs2.success("Result : "+ type[res])

   



