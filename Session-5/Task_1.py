#Create two NumPy arrays representing the number of likes on your last 7 Instagram posts
# and your friend's last 7 posts, then use np.add() and np.subtract() to calculate both the combined and difference arrays.


import numpy as np

my_likes = np.array([35,40,50,33,30,29,25])
friends_likes = np.array([30,45,40,22,20,19,30])

# Calculate combined likes using np.add()
combian_like = np.add(my_likes,friends_likes)
print(combian_like)

# Calculate difference in likes using np.subtract()
diff_likes = np.subtract(my_likes,friends_likes)
print(diff_likes)




