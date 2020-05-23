import numpy as np
file1 = open("Graph1.txt","r")
file2 = open("Graph2.txt","r")
h1,h2 = file1.readline(),file2.readline()
data1,data2 = file1.readlines(),file2.readlines()
array1=[]
array2=[]
for a in data1:
	a=a.strip()
	a=a.split(",")[1]
	array1.append(float(a))
for a in data2:
	a=a.strip()
	a=a.split(",")[1]
	array2.append(float(a))
array1 = np.array(array1)
array2 = np.array(array2)
std1,std2 = array1.std(),array2.std()
print("GPS standard deviation:",std1)
print("Accelerometer standard deviation:",std2)
