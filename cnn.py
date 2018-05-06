#coding:utf-8
from captcha.image import ImageCaptcha  # pip install captcha
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import random,time,os

from __future__ import print_function
import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
import os


x_train_list=[]
y_train_list=[]
x_test_list=[]
y_test_list=[]
def get_data():
    x = np.load("x.npy")[1:10000]
    y = np.load("y.npy")[1:10000]
    for cnt in range(x.shape[0]):
        if(cnt % 10 == 1):
            x_test_list.append(x[cnt])
            y_test_list.append(y[cnt])
        x_train_list.append(x[cnt])
        y_train_list.append(y[cnt]) 
    return np.array(x_train_list), np.array(y_train_list), np.array(x_test_list), np.array(y_test_list)
    
    
def main():    
    #get data
    x_train, y_train, x_test, y_test = get_data()
    #set the model
    model = Sequential()
    model.add(Conv2D(32, (3, 3), padding='same',
                     input_shape=x_train.shape[1:]))
    model.add(Activation('relu'))
    model.add(Conv2D(32, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(64, (3, 3), padding='same'))
    model.add(Activation('relu'))
    model.add(Conv2D(64, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(512))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    # the 36 is number of class, and the 4 is capture's length
    model.add(Dense(4*36))
    model.add(Activation('softmax'))

    # initiate RMSprop optimizer
    opt = keras.optimizers.rmsprop(lr=0.0001, decay=1e-6)
    # Let's train the model using RMSprop
    model.compile(loss='categorical_crossentropy',
                  optimizer=opt,
                  metrics=['accuracy'])
    # x_train = x_train.astype('float32')
    # x_test = x_test.astype('float32')
    x_train =  x_train/ 255
    x_test = x_test/ 255
    ##  there need to add the checkpoints, need to be done
    model.fit(x_train, y_train,
                  batch_size=32,
                  epochs=20,
                  validation_data=(x_test, y_test),
                  shuffle=True)
    ##  to save the models
    
    
main()
