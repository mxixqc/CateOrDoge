from PIL import Image
from flask import Flask, render_template, request
import sys 
import os
import tensorflow as tf 
from tensorflow import keras
import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.applications.resnet_v2 import preprocess_input,decode_predictions,ResNet50V2

print("Python version")
print (sys.version)

print(tf.version.VERSION)
print(tf.keras.__version__)
app = Flask(__name__)

model=ResNet50V2()
@app.route('/',methods=['GET'])
def index_view():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    imagefile = request.files['image']
    imagepath = './static/' + 'download.jpg'
    imagefile.save(imagepath)
    if request.form.get('ResNet50V2', False):
        try:
            image = load_img(imagepath, target_size=(224,224))
        except:
            return render_template('index.html',prediction = "Please input an image:)",result = False)
 
        image = img_to_array(image)
        image = image.reshape((1,image.shape[0],image.shape[1],image.shape[2]))
        image = preprocess_input(image)

        yhat = model.predict(image)
        label = decode_predictions(yhat)
        label = label[0][0]
        classification = '%s(%2f%%)' % (label[1],label[2]*100)
        return render_template('index.html',prediction="This is a "+classification, result=True) 

    # if not, then
    elif request.form.get('MobileNetV2', False):
        try:
            image = load_img(imagepath, target_size=(32,32))
        except:
            return render_template('index.html',prediction = "Please input an image:)")

        image = img_to_array(image)
        image = image.reshape((1,image.shape[0],image.shape[1],image.shape[2]))
        image = image/127.5 -1 
        cnn = tf.keras.models.load_model('./model/my_model.h5')
        l = cnn.predict(image).tolist()
        # print(l)
        pred = l[0].index(max(l[0]))
        classnames = ['airplane', 'automobile', 'bird', 'cat', 'deer','dog', 'frog', 'horse', 'ship', 'truck']
        return render_template('index.html', prediction= "This is a " + classnames[pred], result=True) 

if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=5000, debug=True)
    app.debug=True
