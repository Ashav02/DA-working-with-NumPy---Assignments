#Suppose you have a NumPy array quantities = [2, 1, 3, 4, 2, 1, 5].
#Calculate the total bill for each item by multiplying the cleaned prices array with quantities, and print the resulting array.

import numpy as np

prices = np.array([199, 249, 299, 349, 399, 449, 499])
quantities = np.array([2, 1, 3, 4, 2, 1, 5])

total_bill_amt = prices*quantities


print("Price: ",prices)
print("Quantiies: ",quantities)
print("Total Bill Amount: ",total_bill_amt)