#Create two NumPy arrays: one showing whether a user paid via Paytm (1 for paid, 0 for not)
#and another for PhonePe for 6 transactions. Use np.logical_or() to find out which transactions were paid by either app and print the result.


import numpy as np

paytm = np.array([0,1,0,0,1])
phonepay = np.array([1,1,0,0,1])

result = np.logical_or(paytm,phonepay)
print(result)