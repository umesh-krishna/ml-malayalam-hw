import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Dropout, Flatten
from sklearn.preprocessing import LabelEncoder
from sklearn.cross_validation import train_test_split
from keras.utils import np_utils
from keras.constraints import maxnorm
from keras.optimizers import SGD
from matplotlib import pyplot as plt
from keras.layers import Convolution2D, MaxPooling2D
import cv2
import csv
import webbrowser
from scipy import ndimage
import segmentation as s
import sys

def openImage(path):
	img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
	ret,img = cv2.threshold(img,130,255,cv2.THRESH_BINARY)
	return img

def showImage(img1):
	cv2.imshow('image',img1)
	cv2.waitKey()
	cv2.destroyAllWindows()
	
def resize(img, x, y):
	height, width = img.shape
	try:
		res = cv2.resize(img, None, fx = x/width, fy = y/height, interpolation=cv2.INTER_CUBIC)
		return res
	except:
		print('error resizing...')

def main():
	sys.setrecursionlimit(9999)


	dataset = pd.read_csv('dataset-1.csv')
	X = dataset.iloc[:, 0:784].values
	y = dataset.iloc[:, 784].values

	data = X
	labels = y
	dataset = []
	print(data.shape)
	for i in range(len(data)):
		temp = np.reshape(data[i],(28,28))
		dataset.append(temp)
		#print(data[i])
	dataset = np.array(dataset)
	data = dataset
	
	le = LabelEncoder()
	labels = le.fit_transform(labels)
	#data = np.array(data) / 255.0
	print("[INFO] constructing training/testing split...")
	(X_train, X_test, y_train, y_test) = train_test_split(data, labels, test_size=0.25, random_state=42)
	
	X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)
	X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)
	
	X_train = X_train.astype('float32')
	X_test = X_test.astype('float32')
	X_train /= 255
	X_test /= 255
		
	Y_train = np_utils.to_categorical(y_train, 29)#change this number to total no. of labels
	Y_test = np_utils.to_categorical(y_test, 29)#here also
		
	#neural net
	model = Sequential()
	model.add(Convolution2D(32, 3, 3, activation='relu', input_shape=(28,28,1)))
	
	model.add(Convolution2D(32, 3, 3, activation='relu'))
	model.add(MaxPooling2D(pool_size=(2,2)))
	model.add(Dropout(0.25))
	
	model.add(Flatten())
	model.add(Dense(128, activation='relu'))
	model.add(Dropout(0.5))
	model.add(Dense(29, activation='softmax'))#change this number to total no. of labels

	model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
	model.fit(X_train, Y_train, batch_size=32, nb_epoch=10, verbose=1)
	
	score = model.evaluate(X_test, Y_test, verbose=0)
	print(score)
	

	def predict_images(model):
		img_path=sys.argv[1]
		#img_path = input('image path: ')
		img = openImage(img_path)
		ret,img = cv2.threshold(img,130,255,cv2.THRESH_BINARY_INV)
		img = ndimage.median_filter(img, 3)
		showImage(img)
		list_img = s._main(img)
		for i in range(len(list_img)):
			h,w = list_img[i].shape
			if h+w <= 5:
				continue
			img = list_img[i]
			showImage(img)
			img = resize(img,28,28)
			img = np.array(img)
			#print(img)
			img = img/255
			#print(img)
			img = np.reshape(img,(1,28,28,1))
			result = model.predict_classes(img)
			#print('res: ',result)
			#print(labels)
			kio=le.inverse_transform(result)
			print(kio[0])
			with open('dataaa.csv') as csvfile:
				readCSV = csv.reader(csvfile, delimiter=',')
				filee= open("file.txt","a")
				for row in readCSV:
					if row[0]==kio[0]:
							nee=row[1]
							filee.write(nee)
							print('UNICODE Value:',nee)
							break
						

			
				filee.close()
	while(True):
		predict_images(model)
		#ch = input('0. Quit')
		#if ch == 0 or ch == '0':
		webbrowser.open('http://localhost/FINALS/final.html')
		return
	
main()