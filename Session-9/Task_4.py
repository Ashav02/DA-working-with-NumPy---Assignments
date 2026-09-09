#Generate and print a summary report: show the minimum, maximum, average, and total
#of the cleaned prices array, and also the total bill for all items combined.


import numpy as np

prices = np.array([299, 499, 799, 809, 1599, 809, 899])
qty = np.array([2, 1, 3, 4, 2, 1, 5])

total_bill = prices * qty

print("Minimum price: ",prices.min())
print("Maximum price: ",prices.max())
print("Average price: ",prices.mean())
print("Total price: ",prices.sum())
print("Total bil amount: ",total_bill.sum())