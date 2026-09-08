#Given a NumPy array of item prices from your last Zomato order, use np.multiply() to apply a 10% discount on each item,
#then use np.sum() to calculate the final bill amount after discount.

import numpy as np

zomato_prices = np.array([250,300,350,400,450,500])

discounted_prices = zpmato_prices*0.09

final_bill = sum(discounted_prices)