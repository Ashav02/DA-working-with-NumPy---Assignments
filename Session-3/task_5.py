#Given a 1D NumPy array of 15 Flipkart product ratings,
#use reshape() to convert it into a 3x5 array, then use flatten() to return it to a 1D array.
#Explain in a comment when you would use flatten() versus ravel() in real projects.


import numpy as np

ratings = np.array([4, 5, 3, 4, 2, 5, 4, 3, 5, 4, 2, 3, 4, 5, 4])


#convert in 3 x 5 array

new_array = ratings.reshape(3, 5)
print("3x5 array: ",new_array)

#using flatten for convert in 1D array

array_1D = new_array.flatten()
print("flatten array: ",array_1D)

# flatten() creates a COPY of the data, so use it when you want to
# modify the flattened array without affecting the original array.
# ravel() usually returns a VIEW, so use it when you want better
# memory efficiency and don't need an independent copy.

