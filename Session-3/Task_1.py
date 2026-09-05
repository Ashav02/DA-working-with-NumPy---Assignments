#Create a NumPy array representing the number of likes on 7 Instagram posts 
#and print its ndim, shape, size, dtype, itemsize, and nbytes properties.

import numpy as np

likes_array = np.array([111,222,333,444,555,666,777,888,999])
print(likes_array)

#ndim
ndim = likes_array.ndim
print("ndim: ",ndim)

#Shape
shape = likes_array.shape
print("Shape: ",shape)

#Size
size = likes_array.size
print("Size: ",size)

#Dtype
dtype = likes_array.dtype
print("Dtype: ",dtype)

#Itemsize
itemsize = likes_array.itemsize
print("Itemsize: ",itemsize)

#Nbyte
nbytes = likes_array.nbytes
print("Nbytes: ",nbytes)
