#You have an array of IPL team scores: np.array([210, 180, 195, 220, 205, 175]).
#Use np.where() to find the indices of all scores above 200 and print these indices.


import numpy as np

scores = np.array([210, 180, 195, 220, 205, 175])

result = np.where(scores>200)
print(result)
