#Use ChatGPT to generate Python code that calculates the percentage of songs
#you skipped in your last 20 Spotify plays using NumPy arrays and np.percentile(),
#then run the code and paste your output.

import numpy as np

#1 = skipped, 0 = played
skips = np.array([
    0, 1, 0, 0, 1,
    0, 1, 0, 0, 0,
    1, 0, 0, 1, 0,
    0, 1, 0, 0, 0
])

# Percentage of songs skipped
skip_percentage = np.mean(skips) * 100

# 75th percentile of skips
percentile_75 = np.percentile(skips, 75)

print("Percentage of songs skipped:", skip_percentage, "%")
print("75th percentile of skips:", percentile_75)
