#Explain with code how vectorized operations in NumPy can replace for-loops when multiplying all elements of an array by 2.
#Show both the loop and the vectorized version using a Zomato-style example:
#multiplying all restaurant ratings by 2.

import numpy as np

#using a foor loop to multiply ratings by 2 

ratings1 = [4.3, 4, 4.1, 3.5, 2, 2.5]

doubled_ratings = []

for rating in ratings1:
    doubled_ratings.append(rating * 2)
print("doubled ratings using for loop: ",doubled_ratings)

#using vectorized operations to multiply ratings by 2

ratings = np.array([4.3,4,4.1,3.5,2,2.5])

doubled_ratings_vec = ratings * 2
print("doubled ratings using vectorized opration: ",doubled_ratings_vec)