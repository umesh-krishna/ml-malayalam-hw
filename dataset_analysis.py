import csv
import random
import numpy as np
from pandas import DataFrame#for printing list as matrix

def loadDataset(filename, split, trainingSet =[], testSet = []):
	with open(filename,'r') as csvfile:
		lines = csv.reader(csvfile)
		dataset = list(lines)
		for x in range(len(dataset)-1):
			for y in range(28*28):
				dataset[x][y] = float(dataset[x][y])
			if random.random()<split:
				trainingSet.append(dataset[x])
			else:
				testSet.append(dataset[x])

def main():
	dataset=[]
	nullset=[]
	path = input('Input dataset file name: ')
	loadDataset(path,1,dataset,nullset)
	data = np.array(dataset)
	Y = data[:,-1]
	labels=[]
	output=[]
	new=[]
	new.append('label')
	new.append('count')
	output.append(new)
	for i in range(len(data)):
		if Y[i] not in labels:
			labels.append(Y[i])
			new=[]
			new.append(Y[i])
			new.append(1)
			output.append(new)
		else:
			index = labels.index(Y[i])
			output[index+1][1]=output[index+1][1]+1
	new=[]
	new.append('Total')
	new.append(len(data))
	output.append(new)
	output=np.array(output)
	print(DataFrame(output))
main()
input('Press any key to quit: ')