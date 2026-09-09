#Given a 2D NumPy array representing cricket scores for 3 players across 5 matches,
#use slicing to extract the scores of all players for matches 2 to 4 (index 1 to 3).


import numpy as np

scores = np.array([[35, 45, 50, 60, 41],
                   [17, 10, 65, 98, 55],
                   [77, 60, 55, 42, 50]])

## Matches 2 to 4 → index 1 to 3
result = scores[:,1:4]
print(result)