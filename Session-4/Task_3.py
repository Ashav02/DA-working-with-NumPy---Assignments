#Suppose you have a NumPy array of IPL team scores for 5 matches.
#Use comparison operators to create a boolean array indicating which matches had scores greater than 180, then print the boolean array.


import numpy as np

ipl_scores = np.array([186,178,150,209,250])

new_1 = ipl_scores > 180
print(new_1)