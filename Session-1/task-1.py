#Install NumPy using pip and write a Python script list_vs_array.py that creates a list and a NumPy array, each containing the numbers from 1 to 1000.


import numpy as np

#list
listnumbers = list(range(1,1001))
print("List: ",listnumbers)

#Array
array_number = np.array(range(1,1001))
print("Array: ",array_number)