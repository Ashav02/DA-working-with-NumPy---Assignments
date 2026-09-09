#You have an array of 12 Flipkart product IDs. Use np.array_split() to divide this array into 5 nearly equal parts,
#and display each part.<br><br><em><strong>Hint:</strong> Check the shape of each split to confirm the division.</em>


import numpy as np

products_id = np.array([201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212])

parts = np.array_split(products_id, 5)

for part in parts:
    print(part)

    print("Shape: ",part.shape)
