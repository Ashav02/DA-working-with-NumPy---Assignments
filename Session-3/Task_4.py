#Take a 3x3 NumPy array representing a mini Spotify playlist grid (rows: playlists, columns: song counts in categories like Pop, Rock, Indie).
#Use both T and np.transpose() to swap rows and columns, then print the transposed array.

import numpy as np

#3x3 array

playlist = np.array([[10,5,9],[7,8,5],[3,6,4]])
print(playlist)

print("using T: ",playlist.T)
print("using np.transpose(): ",playlist.transpose())