#Use np.random.randint() to create an array of 6 random integers between 1000 and 9999 (representing random OTP codes like Paytm),
#and print the array.
#Set the random seed to 42 using np.random.seed(42) before generating the array so your results are reproducible.

import numpy as np

np.random.seed(42)

code = np.random.randint(1000,9999,size=6)

print(code)
