#Create a NumPy array of 10 random float ratings (between 1 and 5) for a new movie on BookMyShow,
#then use np.round(), np.floor(), and np.ceil() 
#to show how the rating would appear if rounded to the nearest whole number, always rounded down, and always rounded up.

import numpy as np

ratings = np.array([3.5, 4.5, 4.7, 5, 4, 4.2,
                   3.7, 2.7, 3, 3.9, 4.2])

#np.round() use to rounded to the nearest whole number

round_ratings = np.round(ratings)
print("Round ratings: ",round_ratings)

#np.floor() use to always rounded down

floor_ratings = np.floor(ratings)
print("Floor ratings: ",floor_ratings)

#np.ceil()use for always rounded up.

ceil_ratings = np.ceil(ratings)
print("Ceil ratings: ",ceil_ratings)
