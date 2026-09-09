#Given an array of Flipkart product prices, use np.clip() to limit all prices between 100 and 1000, and print the resulting array.<br><br><em><strong>Hint:</strong> Use np.clip(array, 100, 1000).</em>


import numpy as np

prices = np.array([100, 150, 300, 500, 1200, 1300, 1000, 1100, 700, 900, 1001, 600])

result = np.clip(prices, 100, 1000)
print(result)