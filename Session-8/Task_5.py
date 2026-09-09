

import numpy as np

numbers = np.array([ 21, 2, 27, 5, 58, 9, 73, 6, 50, 12, 26, 30, 35])

#find indices of even numbers

even = np.where(numbers % 2 == 0)

print("Array: ",numbers)
print("Even indices: ",even)
