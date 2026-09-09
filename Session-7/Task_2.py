#Given three arrays representing the number of likes on three different Instagram posts over 7 days,
#stack them vertically using np.vstack() so that each row represents one post's weekly likes, and print the stacked array.


import numpy as np

post_1 = np.array([150, 250, 300, 350, 500, 600, 700])
post_2 = np.array([250, 300, 350, 345, 360, 450, 450])
post_3 = np.array([175, 200, 250, 275, 325, 350, 345])

weekly_likes = np.vstack((post_1, post_2, post_3))
print(weekly_likes)
