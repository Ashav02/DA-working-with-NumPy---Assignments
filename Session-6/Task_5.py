#Given a NumPy array of Flipkart product prices,
#use boolean indexing to extract all prices greater than 500. Print the resulting array.


import numpy as np

prices = np.array([150, 300, 450, 600, 700, 980])


result = prices[prices>500]
print(result)
