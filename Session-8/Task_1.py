#Given a NumPy array of IPL team names with some duplicates,
#use np.unique() to print a sorted list of all unique team names.


import numpy as np

teams = np.array(["CSK", "MI", "RCB", "KKR", "CSK",
    "GT", "MI", "RR", "RCB", "SRH"])


unique_teams = np.unique(teams)

print(unique_teams)