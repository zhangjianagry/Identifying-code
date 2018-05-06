#coding:utf-8
from captcha.image import ImageCaptcha  # pip install captcha
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import random,time,os

def pic2list():
    filenames = os.listdir("pic/")
    paths = ['pic/'+filename for filename in filenames]
    imdatas=[]
    labels=[]
    cnt = 1
    for p in paths:
        cnt+=1
        if(cnt % 5000 == 0):
            print(cnt)
        imdata = np.array(Image.open(p))
        label = p.split("/")[1][0:4]
        imdatas.append(imdata)
        labels.append(label)
    #     print(imdata.shape, label)
    #list to array
    return imdatas, labels

# text to class
def text2vec(text):
	text_len = len(text)

	vector = np.zeros(4*CHAR_SET_LEN)
	def char2pos(c):
		k = ord(c)-48
		if k > 9:
			k = ord(c) - 87
		return k
	for i, c in enumerate(text):
		idx = i * CHAR_SET_LEN + char2pos(c)
		vector[idx] = 1
	return vector
    
    
def list2numpy(imdatas, labels):
    CHAR_SET_LEN = 36
    y = [text2vec(text) for text in labels]
    x = np.array(imdatas)
    y = np.array(y)
    print("x.shape:", x.shape)
    print("y.shape:", y.shape)
    np.save("x.npy",x)
    np.save("y.npy",y)
    
    
def main():
    imdatas, labels = pic2list()
    list2numpy(imdatas, labels)

main()
    
    
    
    
    
    
    
    
    
    
    
    