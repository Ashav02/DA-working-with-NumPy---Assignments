#Build a NumPy array representing the prices of 12 food items from a Zomato order,
#then use ravel(), flatten(), and resize() to create different shaped versions of the data and print each result.

import numpy as np

zomato_order_prices = np.array([[250,300,275,325],[450,500,455,550],[600,750,800,825]])
print("Orignal Price: ",zomato_order_prices)
print("Orignal Shape: ",zomato_order_prices.shape)

#Ravel()
ravel_1 = zomato_order_prices.ravel()
print("Using Ravel: ",ravel_1)
print("Ravel Shape: ",ravel_1.shape)

#Flatten()
flatten_price = zomato_order_prices.flatten()
print("Flatten: ",flatten_price)
print("Shape: ",flatten_price.shape)

#Resize()
resize_price = zomato_order_prices.copy()
resize_price.resize(4, 3)
print("Resize: ",resize_price)
print("Sahpe: ",resize_price.shape)