#Given a 2D NumPy array of daily step counts for 5 days (each row is a day, columns are morning and evening), use reshape() to convert it into a 1D array, then back to a 2D array with 5 rows and 2 columns.

import numpy as np

steps = np.array([[6000,4000],[5000,5000],[4500,5500],[6000,6500],[3500,4500]])

#1D Array

steps_1D = steps.reshape(10)
print("1D array: ",steps_1D)
print("1D shape: ",steps_1D)

#2D Array 
steps_2D = steps_1D.reshape(5,2)
print("2D Array: ",steps_2D)
print("2D Shape: ",steps_2D)
