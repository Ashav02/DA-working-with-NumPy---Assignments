#Create a NumPy array of the first 20 natural numbers.
#Use step slicing to print every 3rd number starting from the second element.


import numpy as np

numbers = np.arange(1,21)
print(numbers)

print(numbers[1::3])