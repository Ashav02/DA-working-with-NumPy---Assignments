#Use ChatGPT or Copilot to suggest a NumPy function or method
#that can help you find out how many unique price values are present in your cleaned prices array.
#Try the suggested method and print the result.

import numpy as np

value = np.array([299, 399, 150, 1599, 6700, 640, 999, 1299, 777, 888])

unique_value = np.unique(value)

print("Value: ",value)
print("Unique Value: ",unique_value)
