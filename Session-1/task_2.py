#In your script, measure and print the memory usage (in bytes) of both the Python list and the NumPy array containing 1000 integers.

import numpy as np
import sys

#list
listnumbers = list(range(1,1001))
list_memory = sys.getsizeof(listnumbers)
print("List: ",listnumbers)
print("Memory usage of list: ", list_memory, "bytes")

#Array
array_number = np.array(range(1,1001))
array_memory = array_number.nbytes
print("Array: ",array_number)
print("Memory usage of array: ", array_memory, "bytes")

