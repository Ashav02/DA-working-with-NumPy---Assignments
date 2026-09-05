#Simulate a Flipkart-style 'Add to Cart' button counter by creating a NumPy array of 10 zeros using np.zeros(),
#then update the 3rd and 7th items to 1 (representing items added to cart), and print the updated array.


import numpy as np

cart = np.zeros(10,dtype=int)

#3rd item added to cart
cart[2] = 1 
print(cart)

#7th item added to cart
cart[6] = 1
print(cart)
