#pip install numpy
import numpy as np

list = np.array([[5,6,7],[1,3,2],[5,6,6]])

print(list.ndim) #dimantion of array
print(list.dtype) #type of variable
print(list.itemsize) #size of eatch elements
print(list.shape) #safe of array
print(np.zeros(3,4))

# for i in list:
#     print(list[i])