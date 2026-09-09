#Given a NumPy array of YouTube video view counts, use .view() to create a view and .copy() to create a copy.
#Modify the first element in each and print all arrays to demonstrate the difference between view and copy.<br><br><em><strong>Hint:</strong> Observe which changes affect the original array.</em>


import numpy as np

views = np.array([3994, 1826, 7306, 2112, 2709, 2111])

#create view & copy 
view_array = views.view()
copy_array = views.copy()

#modify first element 
view_array[0] = 1165
copy_array[0] = 7777

print("Orignal array: ",views)
print("View array: ",view_array)
print("Copy array: ",copy_array)

