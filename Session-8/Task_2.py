#Create a NumPy array of Zomato order ratings (with some NaN values), then use np.isnan() to count how many ratings are missing.


import numpy as np

ratings = np.array([4.5, 5.0, np.nan, 3.5, np.nan, 4.0, 2.5, np.nan])


missing_ratings = np.isnan(ratings)

print("Ratings: ", ratings)
print("Missing ratings: ",missing_ratings)
print("Missing ratings count: ",np.sum(missing_ratings))