#You have a NumPy array called ratings = np.array([4.5, 3.8, 4.2, 2.9, 5.0, 3.5]).
#Use negative indexing to print the last three ratings.


import numpy as np

ratings = np.array([4.5, 3.8, 4.2, 2.9, 5.0, 3.5])

#negative indexing to print the last three ratings.

last_ratings = ratings[-3:]
print(last_ratings)