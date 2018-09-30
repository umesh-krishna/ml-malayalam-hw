#import knn
import cv2
import segmentation as s
import numpy as np
import csv
import random
import math
import operator
import sys
import webbrowser
from scipy import ndimage
import skeletonize as ske
import line_segmentation as ls

def openImage(path):
	img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
	#ret,thresh = cv2.threshold(img,130,255,cv2.THRESH_BINARY_INV)
	return img
def showImage(img1):
	cv2.imshow('image',img1)
	cv2.waitKey()
	cv2.destroyAllWindows()
	
def resize(img, x, y):
	height, width = img.shape
	try:
		res = cv2.resize(img, None, fx = x/width, fy = y/height, interpolation=cv2.INTER_CUBIC)
	except:
		return None
	return res
def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)

def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors

def loadDataset(filename, split, trainingSet =[], testSet = []):
	with open(filename,'r') as csvfile:
		lines = csv.reader(csvfile)
		dataset = list(lines)
		for x in range(len(dataset)-1):
			for y in range(28*28):
				dataset[x][y] = float(dataset[x][y])
			#if random.random()<split:
			trainingSet.append(dataset[x])
			#else:
				#testSet.append(dataset[x])
				
def getResponse(neighbors):
	classVotes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]

def main():
	sys.setrecursionlimit(9999)
	from sklearn.neighbors import KNeighborsClassifier

	#img_name = input('Input the image name to predict: ')
	img_name=sys.argv[1]
	img = openImage(img_name)
	#showImage(img)
	#gaussian filtering
	#img = cv2.blur(img,(5,5))
	ret,img = cv2.threshold(img,130,255,cv2.THRESH_BINARY)
	#showImage(img)
	img = ndimage.median_filter(img, 3)
	#print('background noise removed...')
	#showImage(img)
	
	
	trainingSet =[]
	testSet=[]
	split=0.99
	loadDataset('dataset-1.csv',split,trainingSet,testSet)
	#print('Train set: '+repr(len(trainingSet)))
	#print('Test set: '+repr(len(testSet)))
	predictions =[]
	k=3
	#print('test: ',testSet)
	
	#.....preprocessing....
	
	
	#....line_segmentation.......
	lines = ls.segment(img)
	for u in range(len(lines)):
		#showImage(lines[u])
		#.....character segmentation.....
		list_img = s._main(lines[u])
		for i in range(len(list_img)):
			h,w = list_img[i].shape
			if h+w <= 5:
				continue
			list_img[i] = resize(list_img[i],28,28)
			#showImage(list_img[i])
			try:
				ret,list_img[i] = cv2.threshold(list_img[i],130,255,cv2.THRESH_BINARY)
			except:
				print('')
			img = np.array(list_img[i])
			#showImage(img)
			array = np.array(img)


			array = np.reshape(array, (1,np.product(array.shape)))
			#showImage(list_img[i])
			
			#trainingSet = np.array(trainingSet)
			#print(trainingSet,'\n')

			knn = KNeighborsClassifier()
			
			trainingSet = np.array(trainingSet)
			
			length = len(trainingSet)
			#print('len: ',length)
			X = trainingSet[0:length, 0:784]
			Y = trainingSet[0:length, 784]
			
			#print('array: ',array)
			X = [[float(x) for x in rec]for rec in X]
			X = np.array(X)
			#print('array:',array)
			knn.fit(X,Y)
			#print('shape of X: ',X.shape)
			#print('shape of arr:',array.shape)
			print('predicted: ',knn.predict(array))
			g=knn.predict(array)
			print('Value:',g[0])
			
			with open('dataaa.csv') as csvfile:
				readCSV = csv.reader(csvfile, delimiter=',')
				filee= open("file.txt","a")
				for row in readCSV:
					if row[0]==g[0]:
							nee=row[1]
							filee.write(nee)
							print('UNICODE Value:',nee)
						

			
				filee.close()
				

		webbrowser.open('http://127.0.0.1/FINALS/final.html')
		

main()
c = input('Press any key to quit: ')
