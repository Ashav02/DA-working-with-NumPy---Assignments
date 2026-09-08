#Write a function compare_addition_speed() 
#that adds 5 to every element in both a Python list and a NumPy array of 10,000 integers, and prints the time taken for each.

import numpy as np
import time

size = 10000


#pythone list
list_1 = range(size)
list_2 = range(size)

#array list
arr_1 = np.arange(size)
arr_2 = np.arange(size)

#time taken for python list addition
start = time.time()
result_list = [list_1[i] + list_2[i] for i in range(len(list_1))]
print(f"List addition time: {time.time() - start:.6f} seconds")

#time taken for numpy array addition
start = time.time()
result_array = arr_1 + arr_2
print(f"Array addition time: {time.time() - start:.6f} seconds")