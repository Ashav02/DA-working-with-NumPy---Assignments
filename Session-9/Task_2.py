#Some entries in the prices array are invalid (0 or negative).
#Replace all values less than or equal to zero with the average of the remaining positive prices.

import numpy as np

prices = np.array([299, 499, 799, 0, 1599, -1, 899])

average_prices = prices[prices>0].mean()
print("Average prices: ",average_prices)

prices[prices <= 0] = average_prices

print("updated prices: ",prices)

