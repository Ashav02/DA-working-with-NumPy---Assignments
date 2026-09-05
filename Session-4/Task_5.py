#Given a NumPy array of the number of steps you walked each day for a week,
# use broadcasting to add a bonus of 500 steps to each day's count, then calculate and print the total steps for the week using an aggregate operation.



import numpy as np

steps= np.array([6000,5000,4000,5500,6600,7000,6500])

# Broadcasting: add 500 bonus steps to every day
bounus_steps = steps + 500

# Aggregate operation: calculate total steps for the week
total_steps = np.sum(bounus_steps)

print("Steps after bonus: ",bounus_steps)
print("Total steps for the week: ",total_steps)