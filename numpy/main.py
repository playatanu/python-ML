#pip install numpy
import numpy as np

list = np.array([[5,6,7],[1,3,12],[5,6,6]])

print(list.ndim) #dimantion of array
print(list.dtype) #type of variable
print(list.itemsize) #size of eatch elements
print(list.shape) #safe of array

zeroList = np.zeros((3,4)); #create zero list of array
print(zeroList)

oneList = np.ones((2,2)); #create ones list of array
print(oneList)

arrayRange = np.arange(1,5) #create array with range
print(arrayRange)

linearSpace = np.linspace(1,5, 10)
print(linearSpace)


print(list.min()) #minum number of an array
print(list.max()) #maximum number of an array
print(list.sum()) #sum array

print(list.sum(axis=0)) #sum of row
print(list.sum(axis=1)) #sum of column

print(np.sqrt(25)); #sqre root 

np.vsplit() #vartical partition
np.hsplit() #horizontal partition

# for i in list:
#     print(list[i])