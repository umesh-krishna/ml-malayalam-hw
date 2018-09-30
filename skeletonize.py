import sys
from scipy import ndimage
import cv2
from skimage.morphology import skeletonize
import numpy as np

def img_to_bin(img):
	try:
		h,w = img.shape
	except:
		print('exception in skeletonize.py -> img_to_bin()')
		return img
	for i in range (h):
		for j in range (w):
			if img[i,j] >=150:
				img[i,j]=0;
			else:
				img[i,j]=1;
	return img

def bin_to_img(img):
	h,w = img.shape
	skeleton = np.zeros((h,w))
	for i in range(h):
		for j in range(w):
			if img[i,j] == True:
				skeleton[i,j]=255
			else:
				skeleton[i,j]=0
	#print('image::::',skeleton)
	return skeleton
	
def showImage(img1):
	cv2.imshow('image',img1)
	cv2.waitKey()
	cv2.destroyAllWindows()

def skeleton(img):
	img = img_to_bin(img)
	try:
		img=skeletonize(img)
	except:
		print('Exception in skeleton(), cant skeletonize!!!!')
		return np.zeros((10,10))
	img = bin_to_img(img)
	return img




