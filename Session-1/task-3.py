#Write a function compare_addition_speed() 
#that adds 5 to every element in both a Python list and a NumPy array of 10,000 integers, and prints the time taken for each.

import numpy as np.
import time

size = 10000

list_1 = list(size)
list_2 = list(size)
array_1 = np.arange(size)
array_2 = np.arange(size)

start = time.time()