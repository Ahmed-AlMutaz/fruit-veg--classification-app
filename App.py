import numpy as np 
import tensorflow as tf 
from tensorflow import keras
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
import streamlit as st

model = load_model("E:\AI\projects\MY PROJECTS\App\classify_Image3.keras")




img_hight = 224
img_width = 224
category= ['apple',
 'banana',
 'beetroot',
 'bell pepper',
 'cabbage',
 'capsicum',
 'carrot',
 'cauliflower',
 'chilli pepper',
 'corn',
 'cucumber',
 'eggplant',
 'garlic',
 'ginger',
 'grapes',
 'jalepeno',
 'kiwi',
 'lemon',
 'lettuce',
 'mango',
 'onion',
 'orange',
 'paprika',
 'pear',
 'peas',
 'pineapple',
 'pomegranate',
 'potato',
 'raddish',
 'soy beans',
 'spinach',
 'sweetcorn',
 'sweetpotato',
 'tomato',
 'turnip',
 'watermelon']


image = st.text_input("Enter Image name ", "Apple.jpg")
image_load = tf.keras.utils.load_img(image , target_size=(img_hight,img_width))
image_arr = tf.keras.utils.array_to_img(image_load)
image_batch = tf.expand_dims(image_arr,0)

pred = model.predict(image_batch)


predict_class = np.argmax(pred , axis=1)
score = np.max(pred)


st.image(image , width=150)
st.write(f"the type of veg/fruit is : {category[predict_class[0]]} and the accurecy = {score*100}")