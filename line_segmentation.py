import cv2
import numpy as np

def openImage(path):
	img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
	ret,img = cv2.threshold(img,130,255,cv2.THRESH_BINARY)
	return img

def showImage(img1):
	cv2.imshow('image',img1)
	cv2.waitKey()
	cv2.destroyAllWindows()

def segment(img):#input: binary image, BG: white
	#showImage(img)
	height,width=img.shape
	lines=[]
	i=j=0
	a=b=0
	p = False
	start = 0
	for i in range(height):
		f = True
		for j in range(width):
			if img[i,j] == 0:#foreground pixel
				#print('non blank line')
				f=False
				p=True
				break
		if f == True:
			#print('blank line')
			if p == True:
				img1 = img[ start:i , 0:width]
				lines.append(img1)
				start=i
				p = False
	
	#for i in range(len(lines)):
		#showImage(lines[i])
	return lines		
	
	
#path = input('image path: ')
#img = openImage(path)
#segment(img)