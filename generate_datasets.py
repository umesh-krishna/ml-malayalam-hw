# This program read training images and after skeletonizing, the pixel values(0 or 255) are stored in the datasets

import segmentation as s
import numpy as np
import cv2
import sys
import csv
from scipy import ndimage
import skeletonize as ske


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
	sys.setrecursionlimit(99999)
	img_name = input('Input the image name containing training characters: ')
	img = openImage(img_name)
	showImage(img)
	
	#.....preprocessing....
	img = ndimage.median_filter(img, 3)
	#img = cv2.GaussianBlur(img,(5,5),0)
	#img = ske.skeleton(img)
	#print('after skeletonizing..')
	showImage(img)
	
	#.....segmentation.....
	list_img = s._main(img)
	
	label_name = input('Input the label of the segmented characters: ')
	csv_file_name1 = input('Dataset(without skeletonizing)PATH: ')
	csv_file_name2 = input('Dataset(with skeletonizing)PATH: ')
	#csv_file_name3 = input('Dataset(with zoning)PATH: ')
	
	#.....writing to csv.....
	csv_file_1 = open(csv_file_name1, 'a', newline = '')
	csv_file_2 = open(csv_file_name2, 'a', newline = '')
	#csv_file_3 = open(csv_file_name3, 'a', newline = '')
	with csv_file_1:
		with csv_file_2:
			writer1 = csv.writer(csv_file_1)
			writer2 = csv.writer(csv_file_2)
			for i in range(len(list_img)):
				try:
					w,h = list_img[i].shape
				except:
					continue
				if w+h <= 5:#to avoid very small segments
					continue
				#showImage(list_img[i])
				
				if True:
					try:
						list_img[i] = resize(list_img[i],28,28)
					except:
						continue
					#print('after resizing: ')
					#showImage(list_img[i])
					ret,skeleton = cv2.threshold(list_img[i],40,255,cv2.THRESH_BINARY_INV)
					#print('binarization: ')
					#showImage(list_img[i])
					skeleton = ske.skeleton(skeleton)
					print('after skeletonizing: ')
					showImage(skeleton)
					t = input('Want to store the feature values of this image? (Y / N)')
					if t not in ['Y','y']:
						continue
					#label_name = input('Input the label of the segmented characters: ')

					array1 = np.array(list_img[i])
					array1 = np.append(array1, [[label_name]])
					array1 = np.reshape(array1, (1,np.product(array1.shape)))
					
					array2 = np.array(skeleton)
					array2 = np.append(array2, [[label_name]])
					array2 = np.reshape(array2, (1,np.product(array2.shape)))
					
					writer1.writerows(array1)
					writer2.writerows(array2)
					print(((i+1)/len(list_img))*100, '% done...')
main()			

	
		
			
			
			
			
			
			
			