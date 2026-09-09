#Take a NumPy array of daily step counts for the last 30 days (you can make up the numbers),
#and use np.mean(), np.median(), np.std(), and np.max() to analyze your fitness stats like a health app would.


import numpy as np

daily_step_count = np.array([1751, 1961, 1958, 2748, 5141,
                             4021, 4623, 3281, 1407, 4341,
                             4317, 4745, 4520, 4025, 1975,
                             6180, 3604, 4202, 4550, 3601,
                             3759, 4335, 2517, 1958, 4022,
                             6085, 5337, 3956, 4291, 1404])


#np.mean() use for count average steps.
mean_steps = np.mean(daily_step_count)
print("Average steps: ",mean_steps)

#np.median() use for see median number of array.
median_steps = np.median(daily_step_count)
print("Median steps: ",median_steps)

#np.std() use for see how much your daily steps vary.
std_steps = np.std(daily_step_count)
print("Standard deviation: ",std_steps)

#np.max() use for see max steps in month.
max_steps = np.max(daily_step_count)
print("Maximun steps: ",max_steps)
