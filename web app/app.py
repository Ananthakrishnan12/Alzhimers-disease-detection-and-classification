#!/usr/bin/env python
# coding: utf-8

# In[23]:


from flask import Flask,render_template, flash, redirect,url_for,request
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, Markup
import numpy as np
import pandas as pa
from tensorflow.keras.models import load_model
import cv2
from PIL import Image, ImageFont, ImageDraw
from PIL import Image
import PIL
import skimage
from tensorflow.keras.models import load_model
import os
import pywt
import glob  
import re
import pickle
import json
from skimage.io import imread
from PIL import Image, ImageFont, ImageDraw, ImageEnhance
from skimage import transform


# In[24]:


app=Flask(__name__)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
REGISTER_PATH="./Register/"
TEMP_PATH="./Temp"
app.config['SEND_FILE_MAX_AGE_DEFAULT']=1
def allowed_file(filename):
    return '.' in filename and            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# In[25]:


model = load_model(r'E:\Ak\2023 projects Ak Backup\Alzhimers disease detection and classification\M-02\Model/Alzhimers.h5',compile=False)


# In[26]:


@app.route('/register', methods=['GET', 'POST'])
def upload_register():
    # Check if a valid image file was uploaded
    if request.method == 'POST':
        if 'file' not in request.files:
            return json.dumps({"status": "Error", "msg": "Image cannot be empty "})
        name = request.form.get('name')
        email = request.form.get('email')
        
       
        if(name ==''):
            return json.dumps({"status": "Error", "msg": "Name cannot be empty "})

        file = request.files['file']
       # src = path.realpath(REGISTER_PATH+"/"+email+"/"+name+"/"+file.filename)
       
        print(name)
        print(file)
        
       

        if file.filename == '':
            return json.dumps({"status": "Error", "msg": "Image cannot be empty "})

        if file and allowed_file(file.filename):
            #if os.path.exists(REGISTER_PATH+email):

                #file.save(REGISTER_PATH+email+"/"+file.filename)
               #foo = Image.open(file)
                #foo = foo.rotate(90, PIL.Image.NEAREST, expand = 1)
                #foo.save(REGISTER_PATH+email+"/"+file.filename.strip(),optimize=True,quality=85)
               # os.rename(REGISTER_PATH+email+"/"+file.filename,REGISTER_PATH+email+"/"+name+".jpg")
                
                #return json.dumps({"status": "Error", "msg": "User Already Registered"})
            #else:
                #os.makedirs(REGISTER_PATH+email)
                #foo = Image.open(file)
                #file.save(REGISTER_PATH+email+"/"+file.filename)
                #foo = foo.rotate(90, PIL.Image.NEAREST, expand = 1)
               #foo.save(REGISTER_PATH+email+"/"+file.filename.strip(),optimize=True,quality=85)
                #os.rename(REGISTER_PATH+email+"/"+file.filename,REGISTER_PATH+email+"/"+name+".jpg")
                

            print(file)
            #return json.dumps(train(REGISTER_PATH))
        else:
            return json.dumps({"status": "Error", "msg": "Image Format not supported <png,jpg,jpeg> "})


# In[27]:


@app.route('/', methods=['GET', 'POST'])
def upload_image():
    # Check if a valid image file was uploaded

        return render_template('index.html')


# In[28]:


@app.route('/result', methods=['GET', 'POST'])
def result():
        
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
            

        file = request.files['file']
        print(file)

        if file.filename == '':
            return redirect(request.url)
        foo = Image.open(file)
        if file and allowed_file(file.filename):
            # The image file seems valid! Detect faces and return the result.
            print(file)
            print("cccccccccccccccccc*************************************")
            #foo = foo.rotate(90, PIL.Image.NEAREST, expand = 1) 
            foo.save(TEMP_PATH+"/"+file.filename.strip(),optimize=True,quality=85)
            
            test=imread(TEMP_PATH+"/"+file.filename.strip())
            print(test)
            image=np.array(test).astype('float32')/255
            image=transform.resize(image,(224,224,3))
            img=np.expand_dims(image,axis=0)
            prediction=model.predict(img)
            prediction=np.argmax(prediction)

            
            
            #prediction=np.argmax(prediction)
            #print(prediction)
            #if (prediction == 0):
                #print("Healthy")
            #else:
                #print("Non-Healthy")

            #return (tes_ft)
    return render_template("result.html",prediction=prediction)


# In[29]:


if __name__ == '__main__':
    app.run(debug=True)

