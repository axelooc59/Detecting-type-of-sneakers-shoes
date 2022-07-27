import streamlit as st
import time

import urllib.request
import numpy as np


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



from PIL import Image



with st.spinner('Loading...'):

   
   import cv2
   
   from tensorflow.keras.models import Model
   from tensorflow import keras
   
   
   
   
   model = keras.models.load_model('CV_SNKRS/model_CNN')
   
   filename=tabs2.file_uploader("Upload a picture",type=["png","jpg"])
   if tabs2.button('Predict'):
      
      if filename is not None:
         image2 = Image.open(filename)
         image2.save("pic_pred.png")
         tabs2.image(image2,caption="Picture to predict")
         import os
         
         
         type= ['Dunk high', 'Dunk low', 'Jordan 1 high', 'Jordan 1 low', 'Jordan 1 mid', 'Jordan 3', 'Jordan 4']

         
         ##prediction 
         

         
         image_to_predict = cv2.imread("pic_pred.png",cv2.IMREAD_COLOR)
         
         
         img_to_predict = np.expand_dims(cv2.resize(image_to_predict,(200,200)), axis=0)
         st.write(img_to_predict.shape)

         
         
         #img_to_predict = np.expand_dims(cv2.resize(image_to_predict,(200,200)), axis=0)
         
         
         
         

         
         
         
         
         
         
         
         res1 = model.predict(img_to_predict)
         res=np.argmax(res1) 
         tabs2.success("Result : "+ type[res])
