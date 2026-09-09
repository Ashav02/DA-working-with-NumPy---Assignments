#Create two NumPy arrays representing the ratings of 5 restaurants on Zomato and Swiggy,
#then use np.concatenate() to combine them into a single array of 10 ratings and print the result.


import numpy as np

zomato_ratings = np.array([4.7, 4.3, 4, 4.1, 3.9])
swiggy_ratings = np.array([4.2, 4.8, 4.4, 3, 3.5])


#use np.concatenate() to combine them into a single array of 10 ratings
array = np.concatenate((zomato_ratings, swiggy_ratings))
print("Single array rating: ",array)